"""PMC full text via NCBI BioC -> raw/papers/{pmid}.md, for papers with no PDF.

Europe PMC's PDF render only covers the open-access subset and PMC itself
gates PDFs behind a JS challenge, so author manuscripts and some OA papers
never arrive as PDFs. NCBI's BioC API serves the same full text as JSON
passages; this converts them to the Markdown shape ``extract`` produces.

Every record is checked against the PMID we expect (BioC reports the article's
own ``article-id_pmid``), so a PMCID that resolves to a different paper is
refused rather than filed under the wrong PMID.
"""
from __future__ import annotations

import csv
import json
import re
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

from cbio_kb.ingest.extract import _frontmatter

BIOC_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{pmcid}/unicode"
EXTRACTOR_VERSION = "bioc-1"

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_FIELD_RE = re.compile(r"^(\w+):[ \t]*(\S.*)$", re.MULTILINE)

_SECTION_TITLES = {
    "ABSTRACT": "Abstract", "INTRO": "Introduction", "METHODS": "Methods",
    "RESULTS": "Results", "DISCUSS": "Discussion", "CONCL": "Conclusions",
    "CASE": "Case report", "FIG": "Figures", "TABLE": "Tables",
    "SUPPL": "Supplementary material", "REF": "References",
}


def fetch(pmcid: str, session: requests.Session, retries: int = 4) -> dict | None:
    """Return the BioC document for *pmcid*, or None if NCBI has no full text."""
    delay = 2.0
    for _ in range(retries):
        r = session.get(BIOC_URL.format(pmcid=pmcid), timeout=60)
        if r.status_code == 429:
            time.sleep(delay)
            delay *= 2
            continue
        r.raise_for_status()
        if r.text.startswith("[Error]"):
            return None
        return r.json()[0]["documents"][0]
    raise RuntimeError(f"BioC rate-limited for {pmcid}")


def to_markdown(doc: dict) -> tuple[str, str]:
    """Return (pmid, markdown body) for a BioC document."""
    passages = doc.get("passages", [])
    pmid = str(passages[0]["infons"].get("article-id_pmid", "")) if passages else ""
    lines: list[str] = []
    section = None
    for p in passages:
        text = (p.get("text") or "").strip()
        if not text:
            continue
        stype = p["infons"].get("section_type", "")
        ptype = p["infons"].get("type", "")
        if stype == "TITLE" and ptype == "front":
            lines += [f"# {text}", ""]
            continue
        if stype != section:
            section = stype
            lines += [f"## {_SECTION_TITLES.get(stype, stype.title() or 'Body')}", ""]
        if ptype.startswith("title") or ptype.endswith("_title_1"):
            lines += [f"### {text}", ""]
        else:
            lines += [text, ""]
    return pmid, "\n".join(lines).strip() + "\n"


def _doi_matches(doc: dict, doi: str) -> bool:
    """For BioC records with no PMID: the article's DOI equals the one we expect."""
    passages = doc.get("passages", [])
    got = str(passages[0]["infons"].get("article-id_doi", "")) if passages else ""
    return bool(doi) and got.strip().lower() == doi.strip().lower()


def _existing_meta(path: Path) -> dict[str, str]:
    """Scalar frontmatter fields of an existing raw paper."""
    if not path.exists():
        return {}
    m = _FRONTMATTER_RE.match(path.read_text(encoding="utf-8"))
    if not m:
        return {}
    return {k: v.strip() for k, v in _FIELD_RE.findall(m.group(1))}


def run(mapping_csv: Path, out_dir: Path, pdf_dir: Path,
        replace: bool = False, backup_dir: Path | None = None, wiki_dir: Path = Path("wiki")) -> int:
    """Write BioC full text for mapped papers that have neither a raw file nor a PDF.

    With ``replace``, also re-fetch every existing raw paper that didn't come
    from BioC (PDF or web extractions), using the PMCID in its frontmatter. The
    old file is moved to ``backup_dir`` first; papers BioC doesn't serve keep
    their current text. A raw file with no DOI borrows its wiki page's, which
    confirms BioC records that lack a PMID.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    fetch_log_path = out_dir.parent / "fetch_log.json"
    log = json.loads(fetch_log_path.read_text()) if fetch_log_path.exists() else {}

    todo: dict[str, dict] = {}
    with mapping_csv.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            pmid, pmcid = row["pmid"].strip(), row["pmcid"].strip()
            if not pmcid or (out_dir / f"{pmid}.md").exists() or (pdf_dir / f"{pmcid}.pdf").exists():
                continue
            todo.setdefault(pmid, {"pmcid": pmcid, "study_id": row.get("studyId", ""), "doi": row.get("doi", "")})
    if replace:
        backup_dir = backup_dir or out_dir.parent / "papers_pre_bioc"
        for path in sorted(out_dir.glob("*.md")):
            meta = _existing_meta(path)
            if meta.get("extractor_version") == EXTRACTOR_VERSION or not meta.get("pmcid"):
                continue
            doi = meta.get("doi") or _existing_meta(wiki_dir / "papers" / path.name).get("doi", "")
            todo[path.stem] = {"pmcid": meta["pmcid"], "study_id": meta.get("study_id", ""),
                               "doi": doi.strip("\"'"), "replaces": path}

    written = missing = refused = replaced = 0
    with requests.Session() as s:
        s.headers["User-Agent"] = "cbio-kb/0.1 (bioc fallback)"
        for pmid, meta in sorted(todo.items()):
            doc = fetch(meta["pmcid"], s)
            time.sleep(0.4)
            if doc is None:
                print(f"[miss] {pmid} {meta['pmcid']}: no BioC full text")
                missing += 1
                continue
            got, body = to_markdown(doc)
            if got != pmid and not (not got and _doi_matches(doc, meta.get("doi", ""))):
                print(f"[refuse] {pmid} {meta['pmcid']}: BioC article PMID is {got or 'absent'}"
                      + ("" if got else " and its DOI doesn't match"))
                refused += 1
                continue
            fm = {
                "pmid": pmid, "pmcid": meta["pmcid"], "study_id": meta["study_id"], "doi": meta["doi"],
                "extractor_version": EXTRACTOR_VERSION,
                "extracted_at": datetime.now(timezone.utc).isoformat(),
                "source_pdf": f"bioc:{meta['pmcid']}", "char_count": len(body),
            }
            if old := meta.get("replaces"):
                backup_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(old, backup_dir / old.name)
                replaced += 1
            (out_dir / f"{pmid}.md").write_text(f"{_frontmatter(fm)}\n\n## Full Text\n\n{body}")
            log[pmid] = {k: fm[k] for k in ("pmcid", "extractor_version", "extracted_at", "char_count")}
            log[pmid] |= {"source_pdf": fm["source_pdf"], "warnings": []}
            print(f"[ok] {pmid} {meta['pmcid']}: {len(body):,} chars")
            written += 1

    fetch_log_path.write_text(json.dumps(log, indent=2, sort_keys=True))
    print(f"[done] written={written} (replaced={replaced}) missing={missing} "
          f"refused={refused} candidates={len(todo)}")
    return 0
