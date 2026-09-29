#!/usr/bin/env python3
"""cbio-kb MCP server: the cBioPortal literature knowledge base as MCP tools.

A companion to the published cBioPortal MCP servers (``cbioportal-mcp`` for
the ClickHouse database, ``cbioportal-navigator`` for portal URLs). It speaks
the same identifiers (cBioPortal study IDs, OncoTree codes, HUGO symbols) and
follows the same conventions: stdio by default, streamable HTTP at ``/mcp``
with a ``/health`` route, env-var configuration, a server-level
``instructions`` prompt, and ``{"error_message": ...}`` on failure.

Tools
-----
Corpus / identifier bridge (deterministic; need only ``wiki/``):

- ``get_study_papers``  cBioPortal study ID -> the paper(s) behind it + the
  corpus papers that analyzed the cohort.
- ``get_paper``         PMID -> metadata, study IDs, and selected sections.
- ``list_papers``       filter / keyword-rank papers by gene, cancer type, …
- ``get_entity``        gene / cancer_type / dataset / drug / method / theme page
  plus the papers citing it.
- ``read_wiki_page``    any wiki page (or one section) by vault path.
- ``corpus_info``       coverage and freshness.

Retrieval (need the ``data/paper_index`` FAISS + BM25 index):

- ``search_hybrid``  dense + BM25 + wiki-graph, RRF-fused and reranked. Queries
  are embedded locally with the model that built the index; only an index built
  with ``gemini-embedding-001`` needs Vertex (``GCP_PROJECT``), and without it
  runs as BM25 + graph.
- ``search_dense``   dense only.
- ``route_query`` / ``search_auto``  the eval-driven router.
- ``search_agentic`` graph-walking agent run server-side; registered only when
  ``ANTHROPIC_API_KEY`` is set (or ``CBIO_KB_MCP_ENABLE_AGENTIC=1``), since it
  spends LLM tokens on the server's account.

Paper text (need only the index's ``meta.jsonl``):

- ``get_passage``   a passage of a paper's full text, verbatim, with neighbours.
- ``verify_quote``  checks a quotation against the paper before it's presented
  as one; returns the paper's wording and a PMC link to the sentence.

Results carry ``text_source``: verbatim paper text, or a wiki summary written
by an LLM from the papers.

Configuration (CLI flags override env)::

    CBIO_KB_MCP_SERVER_TRANSPORT  stdio | http | sse   (default stdio)
    CBIO_KB_MCP_BIND_HOST         default 127.0.0.1
    CBIO_KB_MCP_BIND_PORT         default 8124
    CBIO_KB_MCP_HTTP_PATH         default /mcp (set e.g. /lit/mcp behind a proxy)
    CBIO_KB_MCP_FORWARDED_ALLOW_IPS  trust X-Forwarded-* from these IPs
    CBIO_WIKI_DIR / CBIO_KB_SEED_CSV / CBIO_KB_ONTOLOGY_DIR / RAG_INDEX_DIR
    CBIOPORTAL_BASE_URL           default https://www.cbioportal.org

Run::

    uv run cbio-kb serve                                  # stdio
    uv run cbio-kb serve --transport http --port 8124     # http://127.0.0.1:8124/mcp
"""
from __future__ import annotations

import argparse
import asyncio
import bisect
import csv
import difflib
import json
import os
import re
import sys
import unicodedata
from collections import defaultdict
from dataclasses import dataclass, field
from functools import cached_property, lru_cache
from pathlib import Path
from typing import Annotated, Any, Literal
from urllib.parse import quote as _urlquote

from fastmcp import FastMCP
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse

from cbio_kb.wiki.vault import _parse_frontmatter

_REPO_ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = Path(os.environ.get("CBIO_WIKI_DIR", _REPO_ROOT / "wiki"))
SEED_CSV = Path(os.environ.get(
    "CBIO_KB_SEED_CSV", _REPO_ROOT / "data" / "seed" / "cbioportal_study_pmids.csv",
))
ONTOLOGY_DIR = Path(os.environ.get("CBIO_KB_ONTOLOGY_DIR", _REPO_ROOT / "schema" / "ontology"))
INDEX_DIR = Path(os.environ.get("RAG_INDEX_DIR", _REPO_ROOT / "data" / "paper_index"))
CBIOPORTAL_URL = os.environ.get("CBIOPORTAL_BASE_URL", "https://www.cbioportal.org").rstrip("/")
SERVER_VERSION = "0.2.0"

_ENTITY_DIRS = {
    "gene": "genes", "cancer_type": "cancer_types", "dataset": "datasets",
    "drug": "drugs", "method": "methods", "theme": "themes",
}
_ENTITY_LINK_RE = re.compile(
    r"\]\((?:\.\./)?(genes|cancer_types|datasets|drugs|methods|themes)/([^)#\s/]+)\.(?:md|html)\)"
)
_MD_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_DEFAULT_PAPER_SECTIONS = ["TL;DR", "Cohort & data", "Key findings"]
MAX_LIST_LIMIT = 100


# --------------------------------------------------------------------------
# Catalog: everything the deterministic tools need, built once from disk
# --------------------------------------------------------------------------


@dataclass
class Paper:
    pmid: str
    title: str
    journal: str
    year: str
    doi: str
    authors: list[str]
    cancer_types: list[str]
    genes: list[str]
    datasets: list[str]
    drugs: list[str]
    methods: list[str]
    study_ids: list[str]
    tldr: str
    tags: list[str] = field(default_factory=list)
    entity_links: set[str] = field(default_factory=set)  # "genes/EGFR", ...
    pmcid: str = ""

    @property
    def retracted(self) -> bool:
        return "retracted" in self.tags

    def brief(self) -> dict[str, Any]:
        out = {"pmid": self.pmid, "title": self.title, "year": self.year, "journal": self.journal}
        if self.retracted:
            out["retracted"] = True
        return out


@dataclass
class Catalog:
    papers: dict[str, Paper]
    study_pmids: dict[str, list[str]]           # seed: studyId -> PMIDs behind it
    studies: dict[str, dict]                     # ontology: studyId -> cBioPortal record
    cited_by: dict[str, list[str]]               # "genes/EGFR" -> citing PMIDs
    entity_stems: dict[str, dict[str, str]]      # folder -> {lower stem: stem}
    gene_aliases: dict[str, str]                 # lower alias -> gene stem
    oncotree_names: dict[str, str]               # lower name -> OncoTree code
    synced_at: str | None


def _as_list(v: Any) -> list[str]:
    if isinstance(v, list):
        return [str(x) for x in v if str(x).strip()]
    return [v] if isinstance(v, str) and v.strip() else []


def _plain(md: str) -> str:
    """Markdown -> one line of plain text (links reduced to their labels)."""
    return re.sub(r"\s+", " ", _MD_LINK_RE.sub(r"\1", md)).replace("**", "").strip()


def _split_sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    """Return (frontmatter-stripped body, [(h2 heading, section text), ...])."""
    body = text.split("\n---\n", 1)[1] if text.startswith("---\n") and "\n---\n" in text else text
    sections: list[tuple[str, str]] = []
    for chunk in re.split(r"(?m)^## ", body)[1:]:
        heading, _, rest = chunk.partition("\n")
        sections.append((heading.strip(), rest.strip()))
    return body, sections


def _read_seed() -> dict[str, list[str]]:
    out: dict[str, list[str]] = defaultdict(list)
    if SEED_CSV.exists():
        with SEED_CSV.open(encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                sid, pmid = row["studyId"].strip(), row["pmid"].strip()
                if sid and pmid and pmid not in out[sid]:
                    out[sid].append(pmid)
    return dict(out)


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


@lru_cache(maxsize=1)
def catalog() -> Catalog:
    study_pmids = _read_seed()
    pmid_studies: dict[str, list[str]] = defaultdict(list)
    for sid, pmids in sorted(study_pmids.items()):
        for p in pmids:
            pmid_studies[p].append(sid)

    papers: dict[str, Paper] = {}
    cited_by: dict[str, list[str]] = defaultdict(list)
    for f in sorted((WIKI_DIR / "papers").glob("*.md")):
        if not f.stem.isdigit():
            continue
        text = f.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text)
        _, sections = _split_sections(text)
        tldr = next((s for h, s in sections if h.lower().startswith("tl;dr")), "")
        links = {f"{d}/{s}" for d, s in _ENTITY_LINK_RE.findall(text)}
        pmcid = str(fm.get("pmcid") or "").strip()
        paper = Paper(
            pmid=f.stem,
            title=str(fm.get("title") or ""),
            journal=str(fm.get("journal") or ""),
            year=str(fm.get("year") or ""),
            doi=str(fm.get("doi") or ""),
            authors=_as_list(fm.get("authors")),
            cancer_types=_as_list(fm.get("cancer_types")),
            genes=_as_list(fm.get("genes")),
            datasets=_as_list(fm.get("datasets")),
            drugs=_as_list(fm.get("drugs")),
            methods=_as_list(fm.get("methods")),
            study_ids=pmid_studies.get(f.stem, []),
            tldr=_plain(tldr)[:600],
            tags=_as_list(fm.get("tags")),
            entity_links=links,
            pmcid=pmcid if re.fullmatch(r"PMC\d+", pmcid) else "",
        )
        papers[paper.pmid] = paper
        for key in links | {f"datasets/{d}" for d in paper.datasets}:
            if paper.pmid not in cited_by[key]:
                cited_by[key].append(paper.pmid)

    entity_stems: dict[str, dict[str, str]] = {}
    gene_aliases: dict[str, str] = {}
    for folder in _ENTITY_DIRS.values():
        stems = {p.stem for p in (WIKI_DIR / folder).glob("*.md")}
        entity_stems[folder] = {s.lower(): s for s in stems}
    for f in (WIKI_DIR / "genes").glob("*.md"):
        head = f.read_text(encoding="utf-8")[:1500]
        for alias in _as_list(_parse_frontmatter(head).get("aliases")):
            gene_aliases.setdefault(alias.lower(), f.stem)

    studies = {s["studyId"]: s for s in (_read_json(ONTOLOGY_DIR / "studies.json") or [])}
    oncotree_names: dict[str, str] = {}
    for t in _read_json(ONTOLOGY_DIR / "oncotree.json") or []:
        if t.get("code") and t.get("name"):
            oncotree_names.setdefault(t["name"].lower(), t["code"])
    synced = (_read_json(ONTOLOGY_DIR / "sync_log.json") or {}).get("synced_at")
    return Catalog(papers, study_pmids, studies, dict(cited_by), entity_stems,
                   gene_aliases, oncotree_names, synced)


# --------------------------------------------------------------------------
# Shaping helpers
# --------------------------------------------------------------------------


def _err(message: str, **extra: Any) -> dict[str, Any]:
    return {"error_message": message, **extra}


def _pubmed(pmid: str) -> str:
    return f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"


def _pmc_url(pmcid: str) -> str | None:
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/" if pmcid else None


def _study_url(study_id: str) -> str:
    return f"{CBIOPORTAL_URL}/study/summary?id={study_id}"


def _norm_pmid(pmid: str) -> str:
    return re.sub(r"\D", "", str(pmid))


def _paper_meta(p: Paper) -> dict[str, Any]:
    authors = p.authors[:3] + (["et al."] if len(p.authors) > 3 else [])
    return {
        "pmid": p.pmid, "title": p.title, "journal": p.journal, "year": p.year,
        "doi": p.doi, "authors": authors,
        "study_ids": p.study_ids, "datasets_used": p.datasets,
        "cancer_types": p.cancer_types, "genes": p.genes[:40],
        "drugs": p.drugs, "methods": p.methods,
        "path": f"papers/{p.pmid}.md", "pubmed_url": _pubmed(p.pmid),
        "pmc_url": _pmc_url(p.pmcid),
        "retracted": p.retracted,
    }


def _passage_view(chunks: list[dict], top_k: int, max_per_paper: int = 0) -> list[dict]:
    """Trim retrieval chunks to a stable, JSON-friendly shape for the client.

    ``max_per_paper`` > 0 keeps at most that many passages per PMID so one
    long paper can't fill every slot.
    """
    papers = catalog().papers
    try:
        texts = _paper_texts()
    except FileNotFoundError:
        texts = {}
    out: list[dict] = []
    per_paper: dict[str, int] = defaultdict(int)
    for c in chunks:
        if len(out) >= top_k:
            break
        pmid = str(c.get("pmid"))
        if max_per_paper and per_paper[pmid] >= max_per_paper:
            continue
        per_paper[pmid] += 1
        score = c.get("rerank_score", c.get("fused_score", c.get("score")))
        paper = papers.get(pmid)
        text = texts.get(pmid)
        out.append({
            "pmid": pmid,
            "title": paper.title if paper else None,
            "year": paper.year if paper else None,
            "study_ids": paper.study_ids if paper else [],
            **({"retracted": True} if paper and paper.retracted else {}),
            **({"text_quality": "garbled: paraphrase, don't quote"} if text and text.garbled else {}),
            "chunk_id": c.get("chunk_id"),
            **({"anchor": a} if text and (a := _chunk_anchor(text, c.get("chunk_id"))) else {}),
            "score": round(float(score), 4) if score is not None else None,
            "path": f"papers/{pmid}.md",
            "text": c.get("text", ""),
        })
    return out


def _chunk_anchor(pt: "PaperText", chunk_id: Any) -> str | None:
    try:
        return pt.anchor_at(pt.starts[pt.chunk_ids.index(int(chunk_id))])
    except (TypeError, ValueError):
        return None


def _resolve_study(study_id: str) -> str | None:
    cat = catalog()
    wanted = study_id.strip().lower()
    for sid in list(cat.study_pmids) + list(cat.studies):
        if sid.lower() == wanted:
            return sid
    return None


def _similar_studies(study_id: str, limit: int = 8) -> list[dict]:
    cat = catalog()
    ids = sorted(set(cat.studies) | set(cat.study_pmids))
    tokens = [t for t in re.split(r"[_\-\s]+", study_id.lower()) if len(t) >= 3]
    scored = []
    for sid in ids:
        name = (cat.studies.get(sid) or {}).get("name", "")
        hay = f"{sid} {name}".lower()
        hits = sum(t in hay for t in tokens)
        ratio = difflib.SequenceMatcher(None, study_id.lower(), sid.lower()).ratio()
        if hits or ratio > 0.6:
            scored.append((hits + ratio, sid, name))
    scored.sort(reverse=True)
    return [{"study_id": s, "name": n} for _, s, n in scored[:limit]]


def _resolve_entity(kind: str, ident: str) -> str | None:
    cat = catalog()
    folder = _ENTITY_DIRS[kind]
    stems = cat.entity_stems.get(folder, {})
    key = ident.strip().lower()
    candidates = [key, key.replace(" ", "-"), key.replace("_", "-"), key.replace(" ", "_")]
    for c in candidates:
        if c in stems:
            return stems[c]
    if kind == "gene" and key in cat.gene_aliases:
        return cat.gene_aliases[key]
    if kind == "cancer_type" and key in cat.oncotree_names:
        code = cat.oncotree_names[key].lower()
        return stems.get(code)
    return None


def _section_lookup(sections: list[tuple[str, str]], wanted: str) -> tuple[str, str] | None:
    w = wanted.strip().lower()
    for h, s in sections:
        if h.lower() == w:
            return h, s
    for h, s in sections:
        if h.lower().startswith(w) or w in h.lower():
            return h, s
    return None


def _truncate(text: str, max_chars: int) -> tuple[str, bool]:
    max_chars = max(500, int(max_chars))
    return (text, False) if len(text) <= max_chars else (text[:max_chars] + " …", True)


def _safe_wiki_path(path: str) -> Path | None:
    """Resolve a vault path (tolerating ../, wiki/, .html) inside WIKI_DIR."""
    if not isinstance(path, str) or not path.strip():
        return None
    p = path.strip().split("#", 1)[0]
    p = re.sub(r"^(?:\.\./)+", "", p)
    p = re.sub(r"^wiki/", "", p)
    if p.endswith(".html"):
        p = p[:-5] + ".md"
    if not p.endswith(".md"):
        p += ".md"
    root = WIKI_DIR.resolve()
    try:
        candidate = (root / p).resolve()
        candidate.relative_to(root)
    except (OSError, ValueError):
        return None
    return candidate if candidate.is_file() else None


_VERTEX_HINT = ("the passage index was built with gemini-embedding-001, which runs on Vertex "
                "AI: set GCP_PROJECT (with Application Default Credentials) on the server, or "
                "rebuild the index with a local model (`cbio-kb index build-papers`)")


def _dense_available() -> bool:
    """Dense search works if the index's model runs locally, or it's a Vertex
    model and the server has GCP_PROJECT (Vertex bills the operator)."""
    from cbio_kb.index.embed import index_model, is_vertex

    return not is_vertex(index_model(INDEX_DIR)) or bool(os.environ.get("GCP_PROJECT"))


def _index_available() -> bool:
    return (INDEX_DIR / "meta.jsonl").exists() and (INDEX_DIR / "bm25.pkl").exists()


def _agentic_enabled() -> bool:
    flag = os.environ.get("CBIO_KB_MCP_ENABLE_AGENTIC")
    if flag is not None:
        return flag.strip().lower() in ("1", "true", "yes")
    return bool(os.environ.get("ANTHROPIC_API_KEY"))


# --------------------------------------------------------------------------
# Server
# --------------------------------------------------------------------------

mcp = FastMCP(
    name="cbio-kb",
    instructions=(Path(__file__).with_name("mcp_instructions.md")).read_text(encoding="utf-8"),
    version=SERVER_VERSION,
    website_url="https://jim-bo.github.io/cbio-kb/",
)

_RO = {"readOnlyHint": True, "idempotentHint": True, "openWorldHint": False}

# Every text-bearing result says which kind of text it carries (`text_source`),
# so clients can tell quotable paper text from the LLM-written wiki.
_PAPER_TEXT = ("paper_text: verbatim from the paper's full text. Quote it only after "
               "verify_quote confirms the wording.")
_WIKI_TEXT = ("wiki_summary: written by an LLM from the papers. Don't quote it, and confirm "
              "any number it gives in paper text (search_hybrid, get_passage) before reporting it.")

StudyId = Annotated[str, Field(description="cBioPortal study identifier (cancer_study_identifier), e.g. 'msk_chord_2024'.")]
Pmid = Annotated[str, Field(description="PubMed ID, e.g. '39506116'.")]
Query = Annotated[str, Field(description="Natural-language question about the cBioPortal paper corpus.")]
TopK = Annotated[int, Field(description="Number of passages to return (1-30).", ge=1, le=30)]


@mcp.tool(annotations=_RO)
def get_study_papers(study_id: StudyId) -> dict:
    """Papers behind a cBioPortal study, and corpus papers that analyzed its cohort.

    Accepts the same study IDs as cbioportal-mcp (list_studies / get_study_guide)
    and cbioportal-navigator. `papers` are the study's own publications
    (`in_corpus: false` means the paper is not open access, so it has no wiki
    page); `used_by` are other corpus papers that analyzed the cohort.
    """
    cat = catalog()
    sid = _resolve_study(study_id)
    if sid is None:
        return _err(
            f"'{study_id}' is not a study in the cBioPortal snapshot this server uses "
            f"(synced {cat.synced_at or 'unknown'}). That does not prove it doesn't exist: "
            "it may be spelled differently, be newer than the snapshot, or live on another "
            "cBioPortal instance. Check list_studies on cbioportal-mcp.",
            similar_studies=_similar_studies(study_id),
        )
    rec = cat.studies.get(sid, {})
    backing = cat.study_pmids.get(sid, [])
    papers = []
    for pmid in backing:
        p = cat.papers.get(pmid)
        if p:
            papers.append({**p.brief(), "in_corpus": True, "tldr": p.tldr,
                           "path": f"papers/{pmid}.md", "pubmed_url": _pubmed(pmid)})
        else:
            papers.append({"pmid": pmid, "in_corpus": False, "citation": rec.get("citation"),
                           "pubmed_url": _pubmed(pmid),
                           "note": "Not in the corpus: no open-access full text in PMC."})
    used_by = [
        cat.papers[p].brief() for p in cat.cited_by.get(f"datasets/{sid}", [])
        if p in cat.papers and p not in backing
    ]
    used_by.sort(key=lambda b: b["year"], reverse=True)
    out: dict[str, Any] = {
        "study_id": sid,
        "name": rec.get("name"),
        "cancer_type_id": rec.get("cancerTypeId"),
        "citation": rec.get("citation"),
        "cbioportal_url": _study_url(sid),
        "papers": papers,
        "used_by": used_by[:50],
        "used_by_total": len(used_by),
        "dataset_page": f"datasets/{sid}.md" if (WIKI_DIR / "datasets" / f"{sid}.md").exists() else None,
    }
    if not backing:
        out["note"] = ("cBioPortal lists no publication for this study (often a study "
                       "released before its paper).")
    return out


@mcp.tool(annotations=_RO)
def get_paper(
    pmid: Pmid,
    sections: Annotated[
        list[str] | None,
        Field(description="Section headings to return (prefix match, case-insensitive), e.g. "
                          "['Key findings', 'Limitations']. Default: TL;DR, Cohort & data, Key "
                          "findings. Use ['all'] for the whole page."),
    ] = None,
    max_chars: Annotated[int, Field(description="Cap on returned section text.", ge=500, le=60000)] = 12000,
) -> dict:
    """A corpus paper's metadata, the cBioPortal studies it backs, and chosen sections
    of its wiki summary.

    The summary is written by an LLM, not the paper's words: use it to orient,
    confirm any number in the paper's own text (search_hybrid, get_passage)
    before reporting it, and quote only what verify_quote confirms.
    """
    cat = catalog()
    pid = _norm_pmid(pmid)
    paper = cat.papers.get(pid)
    if paper is None:
        backs = sorted(s for s, ps in cat.study_pmids.items() if pid in ps)
        if backs:
            return _err(f"PMID {pid} is the publication for {backs}, but it is not in the corpus "
                        "(no open-access full text in PMC).", study_ids=backs, pubmed_url=_pubmed(pid))
        return _err(f"PMID {pid} is not in the corpus. Use list_papers or search_hybrid to find papers.")
    text = (WIKI_DIR / "papers" / f"{pid}.md").read_text(encoding="utf-8")
    body, secs = _split_sections(text)
    wanted = sections or _DEFAULT_PAPER_SECTIONS
    if any(w.strip().lower() == "all" for w in wanted):
        content, truncated = _truncate(body.strip(), max_chars)
        chosen = {"all": content}
    else:
        chosen, total = {}, 0
        for w in wanted:
            hit = _section_lookup(secs, w)
            if hit:
                chosen[hit[0]] = hit[1]
                total += len(hit[1])
        joined = json.dumps(chosen)
        truncated = len(joined) > max_chars
        if truncated:
            budget = max_chars // max(1, len(chosen))
            chosen = {h: _truncate(s, budget)[0] for h, s in chosen.items()}
    return {
        **_paper_meta(paper),
        "text_source": _WIKI_TEXT,
        "sections": chosen,
        "available_sections": [h for h, _ in secs],
        "truncated": truncated,
    }


def _score(paper: Paper, terms: list[str]) -> float:
    title = paper.title.lower()
    ents = " ".join(paper.genes + paper.cancer_types + paper.datasets + paper.drugs + paper.methods).lower()
    tldr = paper.tldr.lower()
    s = 0.0
    for t in terms:
        s += 3 * (t in title) + 2 * (t in ents) + (t in tldr)
    return s


@mcp.tool(annotations=_RO)
def list_papers(
    search: Annotated[str | None, Field(description="Keywords ranked against title, entities, and TL;DR.")] = None,
    study_id: Annotated[str | None, Field(description="Only papers backing or analyzing this cBioPortal study.")] = None,
    gene: Annotated[str | None, Field(description="HUGO symbol.")] = None,
    cancer_type: Annotated[str | None, Field(description="OncoTree code.")] = None,
    drug: Annotated[str | None, Field(description="Drug name as used in the wiki, e.g. 'osimertinib'.")] = None,
    year_from: Annotated[int | None, Field(description="Earliest publication year.")] = None,
    year_to: Annotated[int | None, Field(description="Latest publication year.")] = None,
    limit: Annotated[int, Field(description="Max rows (1-100).", ge=1, le=MAX_LIST_LIMIT)] = 20,
) -> dict:
    """List corpus papers, filtered by metadata and optionally keyword-ranked.

    Works without the passage index, so it is also the fallback when
    search_hybrid is unavailable. Returns brief rows; call get_paper for detail.
    """
    cat = catalog()
    rows = list(cat.papers.values())
    if study_id:
        sid = (_resolve_study(study_id) or study_id).lower()
        rows = [p for p in rows if sid in {s.lower() for s in p.study_ids + p.datasets}]
    if gene:
        g = gene.lower()
        rows = [p for p in rows if g in {x.lower() for x in p.genes}]
    if cancer_type:
        c = cancer_type.lower()
        rows = [p for p in rows if c in {x.lower() for x in p.cancer_types}]
    if drug:
        d = drug.lower().replace(" ", "-")
        rows = [p for p in rows if d in {x.lower() for x in p.drugs}]
    if year_from:
        rows = [p for p in rows if p.year.isdigit() and int(p.year) >= year_from]
    if year_to:
        rows = [p for p in rows if p.year.isdigit() and int(p.year) <= year_to]
    scored: list[tuple[float, Paper]]
    if search:
        terms = [t for t in re.findall(r"[a-z0-9][a-z0-9\-\.]+", search.lower()) if len(t) > 2]
        scored = [(s, p) for p in rows if (s := _score(p, terms)) > 0]
    else:
        scored = [(0.0, p) for p in rows]
    scored.sort(key=lambda sp: (-sp[0], -int(sp[1].year) if sp[1].year.isdigit() else 0))
    limit = max(1, min(int(limit), MAX_LIST_LIMIT))
    out = []
    for s, p in scored[:limit]:
        row = {**p.brief(), "study_ids": p.study_ids, "cancer_types": p.cancer_types}
        if search:
            row["score"] = s
        out.append(row)
    return {"total_matches": len(scored), "papers": out}


@mcp.tool(annotations=_RO)
def get_entity(
    kind: Annotated[
        Literal["gene", "cancer_type", "dataset", "drug", "method", "theme"],
        Field(description="Entity type. dataset ids are cBioPortal study IDs; cancer_type ids "
                          "are OncoTree codes (names also accepted); genes accept aliases."),
    ],
    id: Annotated[str, Field(description="Entity identifier, e.g. 'EGFR', 'LUAD', 'msk_chord_2024', 'osimertinib'.")],
    section: Annotated[str | None, Field(description="Return only this section (prefix match).")] = None,
    max_chars: Annotated[int, Field(description="Cap on returned page text.", ge=500, le=60000)] = 12000,
) -> dict:
    """What the corpus says about a gene, cancer type, dataset, drug, method, or theme,
    plus the papers that cite it (the entry point for cross-paper questions).

    The page is an LLM-written summary across papers: use it to find papers,
    confirm any number in paper text (search_hybrid, get_passage) before
    reporting it, and quote only what verify_quote confirms.
    """
    cat = catalog()
    folder = _ENTITY_DIRS[kind]
    stem = _resolve_entity(kind, id)
    if stem is None:
        pool = list(cat.entity_stems.get(folder, {}).values())
        close = difflib.get_close_matches(id, pool, n=8, cutoff=0.6)
        close += [s for s in pool if id.lower() in s.lower() and s not in close][:8 - len(close)]
        return _err(f"No {kind} page for '{id}'. The corpus may simply not discuss it.",
                    did_you_mean=close)
    path = WIKI_DIR / folder / f"{stem}.md"
    text = path.read_text(encoding="utf-8")
    fm = _parse_frontmatter(text)
    body, secs = _split_sections(text)
    if section:
        hit = _section_lookup(secs, section)
        if hit is None:
            return _err(f"No section '{section}' on {folder}/{stem}.md.",
                        available_sections=[h for h, _ in secs])
        content, truncated = _truncate(f"## {hit[0]}\n{hit[1]}", max_chars)
    else:
        content, truncated = _truncate(body.strip(), max_chars)
    citing = [cat.papers[p] for p in cat.cited_by.get(f"{folder}/{stem}", []) if p in cat.papers]
    citing.sort(key=lambda p: p.year, reverse=True)
    out: dict[str, Any] = {
        "kind": kind, "id": stem, "path": f"{folder}/{stem}.md",
        "properties": {k: v for k, v in fm.items() if k not in ("processed_by", "processed_at")},
        "text_source": _WIKI_TEXT,
        "content": content, "truncated": truncated,
        "available_sections": [h for h, _ in secs],
        "cited_by": [p.brief() for p in citing[:50]],
        "cited_by_total": len(citing),
    }
    if kind == "dataset":
        out["cbioportal_url"] = _study_url(stem)
        out["study_papers"] = cat.study_pmids.get(stem, [])
    return out


@mcp.tool(annotations=_RO)
def read_wiki_page(
    path: Annotated[str, Field(description="Vault-relative path, e.g. 'papers/39506116.md' or "
                                           "'genes/EGFR.md'. Relative links from page content "
                                           "('../genes/EGFR.md') are accepted as-is.")],
    heading: Annotated[str | None, Field(description="Return only this H2 section (prefix match).")] = None,
    max_chars: Annotated[int, Field(description="Cap on returned text.", ge=500, le=60000)] = 20000,
) -> dict:
    """Read any wiki page (or one section) and list the wiki pages it links to."""
    fpath = _safe_wiki_path(path)
    if fpath is None:
        return _err(f"No wiki page at '{path}'.")
    rel = str(fpath.relative_to(WIKI_DIR.resolve()))
    text = fpath.read_text(encoding="utf-8")
    body, secs = _split_sections(text)
    if heading:
        hit = _section_lookup(secs, heading)
        if hit is None:
            return _err(f"No section '{heading}' on {rel}.", available_sections=[h for h, _ in secs])
        text = f"## {hit[0]}\n{hit[1]}"
    content, truncated = _truncate(text, max_chars)
    links = sorted({f"{d}/{s}.md" for d, s in _ENTITY_LINK_RE.findall(text)}
                   | {f"papers/{p}.md" for p in re.findall(r"papers/(\d+)\.(?:md|html)", text)})
    return {"path": rel, "text_source": _WIKI_TEXT, "content": content, "truncated": truncated,
            "links": links}


@mcp.tool(annotations=_RO)
def corpus_info() -> dict:
    """Corpus coverage and freshness: paper and entity counts, how many public
    cBioPortal studies have their paper in the corpus, snapshot date, and which
    retrieval tools are available on this server."""
    cat = catalog()
    seed_pmids = {p for ps in cat.study_pmids.values() for p in ps}
    backing = [p for p in cat.papers.values() if p.study_ids]
    studies_covered = [s for s, ps in cat.study_pmids.items() if any(p in cat.papers for p in ps)]
    index_cfg = _read_json(INDEX_DIR / "index_config.json") or {}
    index_pmids = None
    if (INDEX_DIR / "meta.jsonl").exists():
        with (INDEX_DIR / "meta.jsonl").open(encoding="utf-8") as fh:
            index_pmids = len({json.loads(line)["pmid"] for line in fh})
    return {
        "papers": len(cat.papers),
        "papers_backing_cbioportal_studies": len(backing),
        "papers_not_backing_a_study": len(cat.papers) - len(backing),
        "entity_pages": {k: len(cat.entity_stems.get(v, {})) for k, v in _ENTITY_DIRS.items()},
        "cbioportal_studies_with_publication": len(cat.study_pmids),
        "cbioportal_studies_with_corpus_paper": len(studies_covered),
        "cbioportal_publications": len(seed_pmids),
        "cbioportal_publications_in_corpus": len(seed_pmids & set(cat.papers)),
        "cbioportal_snapshot_synced_at": cat.synced_at,
        "retrieval": {
            "passage_index_papers": index_pmids,
            "passage_index_model": index_cfg.get("embed_model"),
            "search_hybrid": "dense+bm25+graph" if _index_available() and _dense_available()
                             else ("bm25+graph" if _index_available() else "unavailable"),
            "search_dense": _index_available() and _dense_available(),
            "search_agentic": _agentic_enabled(),
        },
    }


# ---- retrieval -----------------------------------------------------------


def _hybrid_sync(query: str, top_k: int, max_per_paper: int) -> dict[str, Any]:
    from . import hybrid  # local import: pulls in BM25/graph/reranker

    legs = hybrid.retrieve_hybrid(query, top_k_final=hybrid.K_FUSED,
                                  use_dense=_dense_available(), allow_dense_failure=True)
    out: dict[str, Any] = {
        "mode": "hybrid",
        "query": query,
        "leg_counts": {
            "dense": len(legs["dense"][0]), "bm25": len(legs["bm25"][0]),
            "graph": len(legs["graph"][0]), "fused": len(legs["fused"]),
        },
        "anchors": legs.get("anchors", []),
        "text_source": _PAPER_TEXT,
        "passages": _passage_view(legs["final"], top_k, max_per_paper),
    }
    if legs.get("dense_error"):
        reason = _VERTEX_HINT if legs["dense_error"] == "disabled" else legs["dense_error"]
        out["degraded"] = {"dense": f"skipped: {reason}"}
    return out


def _dense_sync(query: str, top_k: int) -> dict[str, Any]:
    from . import rag

    return {"mode": "dense", "query": query, "text_source": _PAPER_TEXT,
            "passages": _passage_view(rag.retrieve(query, top_k=max(top_k, 8)), top_k)}


async def _do_hybrid(query: str, top_k: int, max_per_paper: int = 2) -> dict[str, Any]:
    if not _index_available():
        return _err(f"Passage index not found at {INDEX_DIR}. Use list_papers(search=...) "
                    "and get_paper instead, or build it with `cbio-kb index build-papers`.")
    try:
        return await asyncio.to_thread(_hybrid_sync, query, top_k, max_per_paper)
    except Exception as e:  # surface, don't crash the session
        return _err(f"search_hybrid failed: {type(e).__name__}: {e}")


async def _do_dense(query: str, top_k: int) -> dict[str, Any]:
    if not _index_available():
        return _err(f"Passage index not found at {INDEX_DIR}.")
    if not _dense_available():
        return _err(f"search_dense unavailable: {_VERTEX_HINT}. search_hybrid works without it.")
    try:
        return await asyncio.to_thread(_dense_sync, query, top_k)
    except Exception as e:
        return _err(f"search_dense failed: {type(e).__name__}: {e}")


async def _do_agentic(query: str) -> dict[str, Any]:
    from pydantic_ai.usage import UsageLimits

    from .agent import Deps, agent

    result = await agent.run(query, deps=Deps(wiki_dir=WIKI_DIR),
                             usage_limits=UsageLimits(tool_calls_limit=20))
    answer = str(result.output)
    cited = list(dict.fromkeys(re.findall(r"(?:PMID[:\s]?|papers/)(\d{5,9})", answer)))
    papers = catalog().papers
    studies = list(dict.fromkeys(s for p in cited if p in papers for s in papers[p].study_ids))
    payload: dict[str, Any] = {"mode": "agentic", "query": query, "answer": answer,
                               "cited_pmids": cited, "cited_study_ids": studies}
    usage = result.usage()
    if usage is not None:
        payload["usage"] = {"input_tokens": usage.input_tokens,
                            "output_tokens": usage.output_tokens, "llm_calls": usage.requests}
    return payload


@mcp.tool(annotations=_RO)
async def search_hybrid(
    query: Query,
    top_k: TopK = 8,
    max_per_paper: Annotated[int, Field(description="Cap passages per paper (0 = no cap).", ge=0, le=30)] = 2,
) -> dict:
    """Passage search: dense + BM25 + wiki-graph 1-hop, RRF-fused and cross-encoder reranked.

    Best first call for factual and definitional questions. Each passage carries
    its PMID, title, and the cBioPortal study_ids that paper backs. Passages are
    the paper's own words: read around one with get_passage, and confirm a quote
    with verify_quote, which also returns a link to the sentence. Runs as BM25 +
    graph (flagged under `degraded`) when the server has no Vertex credentials.
    """
    return await _do_hybrid(query, top_k, max_per_paper)


@mcp.tool(annotations=_RO)
async def search_dense(query: Query, top_k: TopK = 8) -> dict:
    """Dense-vector passage search (gemini-embedding-001). Needs Vertex credentials
    on the server; prefer search_hybrid, which also works without them."""
    return await _do_dense(query, top_k)


@mcp.tool(annotations=_RO)
def route_query(query: Query) -> dict:
    """Classify a question and return the recommended retrieval strategy
    (hybrid / rag / agentic) with category, confidence, and rationale, without running it."""
    from . import router

    return router.route(query).to_dict()


@mcp.tool(annotations=_RO)
async def search_auto(query: Query, top_k: TopK = 8) -> dict:
    """Classify the question, then run the strategy the eval found best:
    lookup/definition -> hybrid; list/synthesis -> agentic (when enabled on this
    server; otherwise hybrid plus a hint to walk get_entity -> get_paper).
    The routing decision is returned under `route`."""
    from . import router

    decision = await asyncio.to_thread(router.route, query)
    if decision.mode == "agentic" and _agentic_enabled():
        result = await _do_agentic(query)
    elif decision.mode in ("dense", "rag") and _dense_available():
        result = await _do_dense(query, top_k)
    else:
        result = await _do_hybrid(query, top_k)
        if decision.mode == "agentic":
            result["hint"] = ("Routed as list/synthesis. For full coverage, open the relevant "
                              "entity with get_entity (its cited_by lists every paper) and read "
                              "those papers with get_paper.")
    result["route"] = decision.to_dict()
    return result


if _agentic_enabled():
    @mcp.tool(annotations={**_RO, "openWorldHint": True})
    async def search_agentic(query: Query) -> dict:
        """A server-side agent walks the cross-linked wiki and returns a synthesized,
        PMID-cited answer. Best for enumeration and cross-paper synthesis; slower and
        token-heavy (spends LLM tokens on the server's account)."""
        try:
            return await _do_agentic(query)
        except Exception as e:
            return _err(f"search_agentic failed: {type(e).__name__}: {e}")


# ---- paper text: get_passage / verify_quote ---------------------------------
#
# Both read the passage index's copy of each paper's full text, which ships
# with the server (the raw papers in data/raw/ don't).

_MIN_SEGMENT_CHARS = 8  # letters and digits per quoted segment; shorter matches anywhere
_ELLIPSIS_RE = re.compile(r"\s*(?:\[\s*(?:\.\.\.|…)\s*\]|\.\.\.|…)\s*")
_SENTENCE_END_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9(\[])")
_TRANSLATE = {
    **dict.fromkeys(map(ord, "‐‑‒–—―−﹣－"), "-"),
    **dict.fromkeys(map(ord, "‘’‚‛′"), "'"),
    **dict.fromkeys(map(ord, "“”„‟″"), '"'),
}
# A reference number glued to the end of a lowercase word ("hotspot24"), left by
# PDF extraction. Uppercase stems are left alone, so gene symbols (STK11, RRAS2)
# keep their digits.
_REF_MARKER_RE = re.compile(r"(?<=[a-z]{3})\d{1,3}(?=[\s,.;:)\]]|$)")
# Text with this many run-together words (25+ letters) per 1,000 is garbled:
# PDF columns lost their spaces and may be interleaved (83 papers in 2026-09).
_GARBLED_PER_1K = 10
_GARBLED_NOTE = ("garbled: this paper's extracted text has words run together and may "
                 "interleave page columns, so quotes from it can't be checked. Paraphrase it "
                 "with the PMID instead of quoting it.")


@dataclass
class PaperText:
    """A paper's full text rebuilt from the passage index, and where each chunk
    starts. Indexes from the anchored chunker also give each chunk's end,
    heading (subsection, else section) and first paragraph, so a text offset
    maps to ``§Heading ¶N``."""

    text: str
    chunk_ids: list[int]
    starts: list[int]
    ends: list[int] = field(default_factory=list)
    sections: list[str] = field(default_factory=list)
    paragraphs: list[int] = field(default_factory=list)

    @cached_property
    def garbled(self) -> bool:
        words = re.findall(r"[A-Za-z]+", self.text)
        run_together = sum(len(w) >= 25 for w in words)
        return bool(words) and run_together * 1000 >= _GARBLED_PER_1K * len(words)

    def chunk_at(self, offset: int) -> int:
        return self.chunk_ids[max(0, bisect.bisect_right(self.starts, offset) - 1)]

    def chunk_text(self, chunk_id: int) -> str:
        i = self.chunk_ids.index(chunk_id)
        if self.ends:
            return self.text[self.starts[i]:self.ends[i]]
        end = self.starts[i + 1] if i + 1 < len(self.starts) else len(self.text)
        return self.text[self.starts[i]:end].strip()

    def anchor_at(self, offset: int) -> str | None:
        """``§Section ¶N`` of the paragraph containing ``offset``."""
        if not self.sections:
            return None
        i = max(0, bisect.bisect_right(self.starts, offset) - 1)
        # a chunk's text holds its later paragraphs' breaks ("\n\n")
        extra = self.text.count("\n\n", self.starts[i], max(self.starts[i], offset))
        return _anchor(self.sections[i], self.paragraphs[i] + extra)

    def chunk_for_anchor(self, section: str, paragraph: int) -> int | None:
        """The chunk holding paragraph ``paragraph`` of ``section`` (case-insensitive)."""
        want = section.strip().lower()
        best = None
        for i, sec in enumerate(self.sections):
            if sec.lower() != want:
                continue
            last = self.paragraphs[i] + self.text.count("\n\n", self.starts[i], self.ends[i])
            if self.paragraphs[i] <= paragraph <= last:
                return self.chunk_ids[i]
            if self.paragraphs[i] <= paragraph:
                best = self.chunk_ids[i]
        return best


def _anchor(section: str, paragraph: int) -> str:
    return f"§{section} ¶{paragraph}"


_ANCHOR_RE = re.compile(r"^\s*(?:PMID:?\s*\d+\s*)?§?\s*(.+?)\s*¶\s*(\d+)\s*$")


@lru_cache(maxsize=1)
def _paper_texts() -> dict[str, PaperText]:
    """Every indexed paper's continuous text, rebuilt from ``meta.jsonl``.

    Anchored indexes (``cbio_kb.index.passages``) give each chunk's offsets in
    the paper's clean text, so chunks are laid back at their offsets; the gaps
    between them are whitespace. Older indexes repeat the last ``overlap``
    characters of the previous chunk, and dropping that prefix restores the
    text. Either way a quote that crosses a chunk boundary still matches.
    """
    overlap = int((_read_json(INDEX_DIR / "index_config.json") or {}).get("overlap") or 0)
    chunks: dict[str, list[dict]] = defaultdict(list)
    with (INDEX_DIR / "meta.jsonl").open(encoding="utf-8") as fh:
        for line in fh:
            rec = json.loads(line)
            chunks[str(rec["pmid"])].append(rec)
    out: dict[str, PaperText] = {}
    for pmid, recs in chunks.items():
        recs.sort(key=lambda r: int(r["chunk_id"]))
        if all("char_start" in r for r in recs):
            buf = [" "] * max(int(r["char_end"]) for r in recs)
            for r in recs:
                buf[int(r["char_start"]):int(r["char_end"])] = r["text"]
            out[pmid] = PaperText(
                "".join(buf), [int(r["chunk_id"]) for r in recs],
                [int(r["char_start"]) for r in recs], [int(r["char_end"]) for r in recs],
                [r.get("subsection") or r.get("section") or "Text" for r in recs], [int(r.get("paragraph") or 1) for r in recs])
            continue
        parts: list[str] = []
        ids: list[int] = []
        starts: list[int] = []
        pos, prev = 0, ""
        for r in recs:
            cid, raw = int(r["chunk_id"]), r["text"]
            tail = prev[-overlap:] if overlap else ""
            body = raw[len(tail):].lstrip() if tail and raw.startswith(tail) else raw
            sep = " " if parts else ""
            ids.append(cid)
            starts.append(pos + len(sep))
            parts.append(sep + body)
            pos += len(sep) + len(body)
            prev = raw
        out[pmid] = PaperText("".join(parts), ids, starts)
    return out


def _normalize(text: str, loose: bool = False, drop: set[int] | None = None) -> tuple[str, list[int]]:
    """``text`` normalized for quote matching, plus the offset in ``text`` of
    each normalized character.

    Applies NFKC (so ``10⁻⁷`` reads ``10-7``), one style of dash and quote
    mark, case folding, collapsed whitespace, and rejoined line-break
    hyphenation (``non- synonymous``). ``loose`` keeps only letters and digits.
    Characters at the offsets in ``drop`` are skipped.
    """
    out: list[str] = []
    pos: list[int] = []
    for i, ch in enumerate(text):
        if drop and i in drop:
            continue
        norm = ch.lower() if ch.isascii() else (
            unicodedata.normalize("NFKC", ch).translate(_TRANSLATE).casefold())
        for c in norm:
            if loose:
                if c.isalnum():
                    out.append(c)
                    pos.append(i)
            elif c.isspace():
                if out and out[-1] != " " and not (
                        out[-1] == "-" and len(out) > 1 and out[-2].isalpha()):
                    out.append(" ")
                    pos.append(i)
            else:
                out.append(c)
                pos.append(i)
    return "".join(out), pos


def _loose(text: str) -> str:
    """Letters and digits only, case-folded: the fast form of ``_normalize(loose=True)``."""
    return re.sub(r"[\W_]+", "", unicodedata.normalize("NFKC", text).casefold())


def _quote_segments(quote: str) -> list[str]:
    """Split a quotation at its ellipses; strip surrounding quotation marks."""
    q = quote.strip().strip("\"'“”‘’«»").strip()
    return [s for s in _ELLIPSIS_RE.split(q) if s.strip()]


def _find_in_order(hay: str, segments: list[str], max_gap: int = 1500) -> tuple[int, int] | None:
    """Span of ``segments`` found in order in ``hay``, each within ``max_gap`` of the last."""
    start = 0
    while (first := hay.find(segments[0], start)) >= 0:
        end = first + len(segments[0])
        for seg in segments[1:]:
            nxt = hay.find(seg, end)
            if nxt < 0 or nxt - end > max_gap:
                break
            end = nxt + len(seg)
        else:
            return first, end
        start = first + 1
    return None


def _match_quote(pt: PaperText, segments: list[str]) -> tuple[str, int, int] | None:
    """(match level, start, end) of the quotation in the paper's text: exact up to
    whitespace, then ``normalized``, then ``loose``. The last two ignore
    reference numbers glued to words in the paper, which quotes usually drop."""
    pattern = r".{0,1500}?".join(r"\s+".join(map(re.escape, s.split())) for s in segments)
    if m := re.search(pattern, pt.text, flags=re.DOTALL):
        return "exact", m.start(), m.end()
    markers = {i for mk in _REF_MARKER_RE.finditer(pt.text) for i in range(mk.start(), mk.end())}
    for level, loose in (("normalized", False), ("loose", True)):
        segs = [_normalize(s, loose)[0].strip() for s in segments]
        hay, pos = _normalize(pt.text, loose, drop=markers)
        if all(segs) and (span := _find_in_order(hay, segs)):
            return level, pos[span[0]], pos[span[1] - 1] + 1
    return None


def _closest(pt: PaperText, quote: str, n: int = 3) -> list[dict]:
    """The paper's sentences (and adjacent pairs) most like ``quote``."""
    bounds = [0, *(m.end() for m in _SENTENCE_END_RE.finditer(pt.text)), len(pt.text)]
    spans = [(bounds[i], bounds[i + 1]) for i in range(len(bounds) - 1)]
    spans += [(bounds[i], bounds[i + 2]) for i in range(len(bounds) - 2)]
    words = set(re.findall(r"\w+", quote.lower()))
    if not words:
        return []
    overlap = sorted(spans, key=lambda s: -len(words & set(re.findall(r"\w+", pt.text[s[0]:s[1]].lower()))))
    target = _loose(quote)
    scored = []
    for a, b in overlap[:25]:
        ratio = difflib.SequenceMatcher(None, target, _loose(pt.text[a:b]), autojunk=False).ratio()
        scored.append((ratio, a, b))
    scored.sort(reverse=True)
    picked: list[tuple[float, int, int]] = []
    for r, a, b in scored:  # a sentence and a pair containing it are one candidate
        if r >= 0.3 and len(picked) < n and all(b <= pa or a >= pb for _, pa, pb in picked):
            picked.append((r, a, b))
    return [{"chunk_id": pt.chunk_at(a),
             **({"anchor": anc} if (anc := pt.anchor_at(a)) else {}),
             "text": " ".join(pt.text[a:b].split())[:700],
             "similarity": round(r, 2)} for r, a, b in picked]


@lru_cache(maxsize=1)
def _loose_corpus() -> tuple[str, list[int], list[str]]:
    """Every indexed paper's text in ``_loose`` form, joined with ``|``, with each
    paper's start offset: finds the paper a misattributed quote comes from."""
    parts, starts, pmids, pos = [], [], [], 0
    for pmid, pt in _paper_texts().items():
        s = _loose(pt.text)
        parts.append(s)
        starts.append(pos)
        pmids.append(pmid)
        pos += len(s) + 1
    return "|".join(parts), starts, pmids


def _found_elsewhere(segments: list[str], exclude: str, limit: int = 5) -> list[dict]:
    corpus, starts, pmids = _loose_corpus()
    needle = max((_loose(s) for s in segments), key=len)
    papers = catalog().papers
    found: list[dict] = []
    at = corpus.find(needle)
    while at >= 0 and len(found) < limit:
        pmid = pmids[bisect.bisect_right(starts, at) - 1]
        if pmid != exclude and all(f["pmid"] != pmid for f in found):
            found.append(papers[pmid].brief() if pmid in papers else {"pmid": pmid})
        at = corpus.find(needle, at + 1)
    return found


def _pmc_link(pmcid: str, passage: str) -> str | None:
    """PMC link that scrolls to ``passage`` (a text fragment, ``#:~:text=``).

    Uses the passage's longest run of plain words: numbers, symbols and
    hyphenation often read differently on PMC than in the extracted text. If
    PMC words the run differently, or the browser lacks text fragments, the
    link still opens the paper.
    """
    base = _pmc_url(pmcid)
    if base is None:
        return None
    best: list[str] = []
    run: list[str] = []
    for tok in passage.split():
        word = tok.rstrip(",;:.")
        if not re.fullmatch(r"[A-Za-z]+", word):
            run = []
            continue
        run.append(word)
        if len(run) > len(best):
            best = list(run)
        if word != tok:  # trailing punctuation ends the run
            run = []
    if len(best) < 3:
        return base
    return base + "#:~:text=" + _urlquote(" ".join(best[:10]), safe="").replace("-", "%2D")


def _text_for(pid: str) -> PaperText | dict[str, Any]:
    if not (INDEX_DIR / "meta.jsonl").exists():
        return _err(f"Passage index not found at {INDEX_DIR}, so paper text is unavailable. "
                    "get_paper returns the wiki summary.")
    pt = _paper_texts().get(pid)
    if pt is not None:
        return pt
    if pid in catalog().papers:
        return _err(f"PMID {pid} has a wiki page but isn't in the passage index yet.")
    return _err(f"PMID {pid} is not in the corpus.")


def _paper_brief(pid: str) -> dict[str, Any]:
    p = catalog().papers.get(pid)
    return {"pmid": pid, **({"title": p.title, "year": p.year} if p else {}),
            "pubmed_url": _pubmed(pid), "pmc_url": _pmc_url(p.pmcid) if p else None}


@mcp.tool(annotations=_RO)
def get_passage(
    pmid: Pmid,
    chunk_id: Annotated[int | None, Field(description="Passage number, from a search result's "
                                                      "chunk_id or verify_quote's.", ge=0)] = None,
    context: Annotated[int, Field(description="Neighbouring passages to include on each side.",
                                  ge=0, le=3)] = 1,
    anchor: Annotated[str | None, Field(description="Instead of chunk_id: a paragraph anchor "
                                                    "such as '§Results ¶4', from a search result "
                                                    "or verify_quote.")] = None,
) -> dict:
    """Read a passage of a paper's full text verbatim, with its neighbours.

    Use it to check the exact wording, the surrounding sentences, and what a
    statistic refers to before quoting or reporting a number from a search result.
    Give either `chunk_id` or `anchor`.
    """
    pid = _norm_pmid(pmid)
    pt = _text_for(pid)
    if isinstance(pt, dict):
        return pt
    if anchor is not None and chunk_id is None:
        m = _ANCHOR_RE.match(anchor)
        found = pt.chunk_for_anchor(m.group(1), int(m.group(2))) if m and pt.sections else None
        if found is None:
            sections = list(dict.fromkeys(pt.sections))
            return _err(f"No paragraph {anchor!r} in PMID {pid}"
                        + (f"; its sections are {', '.join(sections)}." if sections
                           else "; this index has no anchors, so use chunk_id."))
        chunk_id = found
    if chunk_id is None:
        return _err("Give chunk_id or anchor.")
    if chunk_id not in pt.chunk_ids:
        return _err(f"PMID {pid} has passages {pt.chunk_ids[0]}-{pt.chunk_ids[-1]}.")
    ids = [c for c in pt.chunk_ids if abs(c - chunk_id) <= context]
    return {
        **_paper_brief(pid),
        "text_source": _PAPER_TEXT,
        **({"text_quality": _GARBLED_NOTE} if pt.garbled else {}),
        "passages": [{"chunk_id": c, **({"anchor": anc} if (anc := _chunk_anchor(pt, c)) else {}),
                      "text": pt.chunk_text(c)} for c in ids],
        "n_passages": len(pt.chunk_ids),
    }


@mcp.tool(annotations=_RO)
def verify_quote(
    pmid: Pmid,
    quote: Annotated[str, Field(description="The exact words you intend to put in quotation marks. "
                                            "Mark omissions with '...'.")],
) -> dict:
    """Check that a quotation appears in a paper's full text before presenting it as a quote.

    Tries an exact match (ignoring whitespace), then `normalized` (also
    ignoring case, dash and quote-mark styles, superscripts, line-break
    hyphenation and reference numbers glued to words), then `loose` (letters
    and digits only). A match returns the paper's own wording to quote, the
    passage it's in, and `pmc_link`, which opens the paper at that sentence. No
    match returns the paper's closest sentences and any other corpus papers
    that contain the text; never put rejected text in quotation marks.
    """
    pid = _norm_pmid(pmid)
    segments = _quote_segments(quote)
    if not segments or any(len(_loose(s)) < _MIN_SEGMENT_CHARS for s in segments):
        return _err(f"Quote too short to verify: each part needs at least {_MIN_SEGMENT_CHARS} "
                    "letters or digits.")
    pt = _text_for(pid)
    if isinstance(pt, dict):
        return pt
    brief = _paper_brief(pid)
    hit = _match_quote(pt, segments)
    if hit is None:
        out = {
            **brief, "verified": False, "text_source": _PAPER_TEXT,
            "closest": [] if pt.garbled else _closest(pt, " ".join(segments)),
            "found_in_other_papers": _found_elsewhere(segments, pid),
            "note": ("Not in this paper's text. Don't put it in quotation marks, even if you "
                     "believe it's verbatim: paraphrase it with the PMID, quote one of "
                     "`closest` if it says the same thing, or cite the paper in "
                     "`found_in_other_papers` that contains it."),
        }
        if pt.garbled:
            out["text_quality"] = _GARBLED_NOTE
        return out
    level, a, b = hit
    wording = " ".join(pt.text[a:b].split())
    if level != "exact":
        wording = _REF_MARKER_RE.sub("", wording)
    lo, hi = max(0, a - 200), min(len(pt.text), b + 200)
    context = " ".join(pt.text[lo:hi].split())
    out: dict[str, Any] = {
        **brief, "verified": True, "match": level, "text_source": _PAPER_TEXT,
        "paper_wording": wording,
        "chunk_id": pt.chunk_at(a),
        **({"anchor": anc} if (anc := pt.anchor_at(a)) else {}),
        "context": ("…" if lo else "") + context + ("…" if hi < len(pt.text) else ""),
        "pmc_link": _pmc_link(catalog().papers[pid].pmcid, wording) if pid in catalog().papers else None,
    }
    notes = []
    if level != "exact":
        notes.append("Matched only after normalizing formatting: quote `paper_wording`, not your version.")
    if len(segments) > 1:
        notes.append("`paper_wording` includes the text your ellipses omit.")
    if notes:
        out["note"] = " ".join(notes)
    return out


# ---- resources + health ----------------------------------------------------


@mcp.resource("cbio-kb://guide", mime_type="text/markdown")
def guide() -> str:
    """How to use this server alongside cbioportal-mcp and cbioportal-navigator."""
    return mcp.instructions or ""


@mcp.resource("cbio-kb://paper/{pmid}", mime_type="text/markdown")
def paper_resource(pmid: str) -> str:
    """Full wiki page for a corpus paper."""
    f = WIKI_DIR / "papers" / f"{_norm_pmid(pmid)}.md"
    return f.read_text(encoding="utf-8") if f.exists() else f"PMID {pmid} is not in the corpus."


@mcp.resource("cbio-kb://study/{study_id}", mime_type="application/json")
def study_resource(study_id: str) -> str:
    """get_study_papers output for a cBioPortal study."""
    return json.dumps(get_study_papers(study_id), indent=2)


@mcp.custom_route("/health", methods=["GET"])
async def health(_: Request) -> JSONResponse:
    return JSONResponse({
        "status": "ok", "service": "cbio-kb", "version": SERVER_VERSION,
        "papers": len(catalog().papers), "passage_index": _index_available(),
    })


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------


def _env(name: str, default: str | None = None) -> str | None:
    return os.environ.get(f"CBIO_KB_MCP_{name}") or default


def _warm_retrieval() -> None:
    """Load BM25, the wiki graph, and the reranker so the first search_hybrid
    call doesn't pay ~30s of cold start. Best-effort, on a daemon thread."""
    try:
        from . import hybrid

        hybrid.BM25Index.get()
        hybrid.GraphIndex.get()
        _loose_corpus()  # also builds _paper_texts() for get_passage / verify_quote
        garbled = sum(pt.garbled for pt in _paper_texts().values())
        print(f"[cbio-kb] {garbled} indexed papers have garbled text (quotes unverifiable)",
              file=sys.stderr)
        if hybrid._RERANK_ENABLED_DEFAULT:
            hybrid._Reranker.get()
        if _dense_available():  # embeds the router's labeled questions once
            from . import router

            if router._QUESTIONS_PATH.exists():
                router.QuestionBank.get()
        print("[cbio-kb] retrieval indexes warm", file=sys.stderr)
    except Exception as e:  # never take the server down over a warm-up
        print(f"[cbio-kb] warm-up skipped: {type(e).__name__}: {e}", file=sys.stderr)


def _start_warmup() -> None:
    if _index_available() and _env("WARM", "1") not in ("0", "false", "no"):
        import threading

        threading.Thread(target=_warm_retrieval, daemon=True).start()


def run_config(argv: list[str] | None = None) -> dict[str, Any]:
    """Resolve CLI flags + CBIO_KB_MCP_* env into ``FastMCP.run`` kwargs."""
    ap = argparse.ArgumentParser(description="cbio-kb literature MCP server")
    ap.add_argument("--transport", choices=["stdio", "http", "sse"], default=None,
                    help="Default: $CBIO_KB_MCP_SERVER_TRANSPORT, else http if --host/--port "
                         "is given, else stdio")
    ap.add_argument("--host", default=None, help="Bind host (http/sse); default 127.0.0.1")
    ap.add_argument("--port", type=int, default=None, help="Bind port (http/sse); default 8124")
    ap.add_argument("--path", default=None, help="HTTP mount path; default /mcp")
    args = ap.parse_args(argv)

    transport = (args.transport or _env("SERVER_TRANSPORT")
                 or ("http" if args.host or args.port else "stdio")).lower()
    if transport not in ("stdio", "http", "sse"):
        ap.error(f"invalid transport {transport!r}")
    if transport == "stdio":
        return {"transport": "stdio"}

    kwargs: dict[str, Any] = {
        "transport": transport,
        "host": args.host or _env("BIND_HOST", "127.0.0.1"),
        "port": args.port or int(_env("BIND_PORT", "8124")),
    }
    path = args.path or _env("HTTP_PATH")
    if path:
        kwargs["path"] = path
    fwd = _env("FORWARDED_ALLOW_IPS")
    if fwd:
        kwargs["uvicorn_config"] = {"proxy_headers": True, "forwarded_allow_ips": fwd}
    return kwargs


def main(argv: list[str] | None = None) -> int:
    kwargs = run_config(argv)
    n = len(catalog().papers)  # warm the catalog (fast) and fail early on a bad WIKI_DIR
    _start_warmup()
    if kwargs["transport"] == "stdio":
        where = "stdio"
    else:
        where = f"{kwargs['transport']}://{kwargs['host']}:{kwargs['port']}{kwargs.get('path', '/mcp')}"
    print(f"[cbio-kb] MCP on {where} ({n} papers; passage index "
          f"{'on' if _index_available() else 'off'}; dense {'on' if _dense_available() else 'off'}; "
          f"agentic {'on' if _agentic_enabled() else 'off'})", file=sys.stderr)
    mcp.run(show_banner=False, **kwargs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
