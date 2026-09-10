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
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

from cbio_kb.ingest.extract import _frontmatter

BIOC_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/{pmcid}/unicode"
EXTRACTOR_VERSION = "bioc-1"

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


def run(mapping_csv: Path, out_dir: Path, pdf_dir: Path) -> int:
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

    written = missing = refused = 0
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
            if got != pmid:
                print(f"[refuse] {pmid} {meta['pmcid']}: BioC article PMID is {got or 'absent'}")
                refused += 1
                continue
            fm = {
                "pmid": pmid, "pmcid": meta["pmcid"], "study_id": meta["study_id"], "doi": meta["doi"],
                "extractor_version": EXTRACTOR_VERSION,
                "extracted_at": datetime.now(timezone.utc).isoformat(),
                "source_pdf": f"bioc:{meta['pmcid']}", "char_count": len(body),
            }
            (out_dir / f"{pmid}.md").write_text(f"{_frontmatter(fm)}\n\n## Full Text\n\n{body}")
            log[pmid] = {k: fm[k] for k in ("pmcid", "extractor_version", "extracted_at", "char_count")}
            log[pmid] |= {"source_pdf": fm["source_pdf"], "warnings": []}
            print(f"[ok] {pmid} {meta['pmcid']}: {len(body):,} chars")
            written += 1

    fetch_log_path.write_text(json.dumps(log, indent=2, sort_keys=True))
    print(f"[done] written={written} missing={missing} refused={refused} candidates={len(todo)}")
    return 0
