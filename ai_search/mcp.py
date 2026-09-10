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

- ``search_hybrid``  dense + BM25 + wiki-graph, RRF-fused and reranked. Runs as
  BM25 + graph when Vertex credentials are absent.
- ``search_dense``   dense only (needs ``GCP_PROJECT`` + Vertex ADC).
- ``route_query`` / ``search_auto``  the eval-driven router.
- ``search_agentic`` graph-walking agent run server-side; registered only when
  ``ANTHROPIC_API_KEY`` is set (or ``CBIO_KB_MCP_ENABLE_AGENTIC=1``), since it
  spends LLM tokens on the server's account.

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
import csv
import difflib
import json
import os
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Annotated, Any, Literal

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
        "retracted": p.retracted,
    }


def _passage_view(chunks: list[dict], top_k: int, max_per_paper: int = 0) -> list[dict]:
    """Trim retrieval chunks to a stable, JSON-friendly shape for the client.

    ``max_per_paper`` > 0 keeps at most that many passages per PMID so one
    long paper can't fill every slot.
    """
    papers = catalog().papers
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
        out.append({
            "pmid": pmid,
            "title": paper.title if paper else None,
            "year": paper.year if paper else None,
            "study_ids": paper.study_ids if paper else [],
            **({"retracted": True} if paper and paper.retracted else {}),
            "chunk_id": c.get("chunk_id"),
            "score": round(float(score), 4) if score is not None else None,
            "path": f"papers/{pmid}.md",
            "text": c.get("text", ""),
        })
    return out


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


def _dense_available() -> bool:
    return bool(os.environ.get("GCP_PROJECT"))


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
    """A corpus paper's metadata, the cBioPortal studies it backs, and chosen sections."""
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
    plus the papers that cite it (the entry point for cross-paper questions)."""
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
    return {"path": rel, "content": content, "truncated": truncated, "links": links}


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
        "passages": _passage_view(legs["final"], top_k, max_per_paper),
    }
    if legs.get("dense_error"):
        out["degraded"] = {"dense": "skipped: Vertex embeddings unavailable "
                                    "(set GCP_PROJECT with Application Default Credentials)"}
    return out


def _dense_sync(query: str, top_k: int) -> dict[str, Any]:
    from . import rag

    return {"mode": "dense", "query": query,
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
        return _err("search_dense needs Vertex embeddings: set GCP_PROJECT (with Application "
                    "Default Credentials) on the server. search_hybrid works without them.")
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
    its PMID, title, and the cBioPortal study_ids that paper backs. Runs as
    BM25 + graph (flagged under `degraded`) when the server has no Vertex
    credentials.
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
        if hybrid._RERANK_ENABLED_DEFAULT:
            hybrid._Reranker.get()
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
