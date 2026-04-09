"""PDF -> raw/papers/{pmid}.md.

Idempotent: skips papers whose output already exists and whose source PDF
mtime hasn't changed since the last extraction (tracked in fetch_log.json).
"""
from __future__ import annotations

import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

EXTRACTOR_VERSION = "1"


def _load_pmcid_to_meta(mapping_csv: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    if not mapping_csv.exists():
        return out
    with mapping_csv.open() as f:
        for row in csv.DictReader(f):
            pmcid = (row.get("pmcid") or "").strip()
            if not pmcid:
                continue
            out[pmcid] = {
                "pmid": (row.get("pmid") or "").strip(),
                "study_id": (row.get("studyId") or "").strip(),
                "doi": (row.get("doi") or "").strip(),
            }
    return out


def _pmcid_from_filename(path: Path) -> str | None:
    m = re.match(r"(PMC\d+)", path.stem)
    return m.group(1) if m else None


def _extract_text(pdf_path: Path) -> tuple[str, list[str]]:
    """Return (text, warnings)."""
    warnings: list[str] = []
    try:
        import pdfplumber
    except Exception as e:
        return "", [f"pdfplumber import failed: {e}"]

    pages: list[str] = []
    try:
        with pdfplumber.open(str(pdf_path)) as pdf:
            for i, page in enumerate(pdf.pages):
                try:
                    pages.append(page.extract_text() or "")
                except Exception as e:
                    warnings.append(f"page {i}: {e}")
    except Exception as e:
        warnings.append(f"open failed: {e}")
    return "\n\n".join(pages).strip(), warnings


def _frontmatter(meta: dict) -> str:
    lines = ["---"]
    for k in ("pmid", "pmcid", "study_id", "doi", "extractor_version", "extracted_at", "source_pdf", "char_count"):
        v = meta.get(k)
        if v in (None, ""):
            continue
        lines.append(f"{k}: {v}")
    # placeholders for the compile agent to fill in later
    for k in ("title", "authors", "journal", "year"):
        lines.append(f"{k}:")
    for k in ("cancer_types", "genes", "datasets", "tags"):
        lines.append(f"{k}: []")
    lines.append("---")
    return "\n".join(lines)


def run(pdf_dir: Path, out_dir: Path, mapping_csv: Path, limit: int | None = None) -> int:
    if not pdf_dir.exists():
        print(f"[!] pdf-dir does not exist: {pdf_dir}")
        return 1
    out_dir.mkdir(parents=True, exist_ok=True)
    raw_root = out_dir.parent
    raw_root.mkdir(parents=True, exist_ok=True)
    fetch_log_path = raw_root / "fetch_log.json"

    pmcid_meta = _load_pmcid_to_meta(mapping_csv)
    log: dict[str, dict] = {}
    if fetch_log_path.exists():
        try:
            log = json.loads(fetch_log_path.read_text())
        except Exception:
            log = {}

    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if limit:
        pdfs = pdfs[:limit]

    written = skipped = unmapped = failed = 0
    for pdf in pdfs:
        pmcid = _pmcid_from_filename(pdf)
        if not pmcid:
            print(f"[skip] no PMCID in filename: {pdf.name}")
            unmapped += 1
            continue
        meta = pmcid_meta.get(pmcid)
        if not meta or not meta.get("pmid"):
            print(f"[skip] no PMID mapping for {pmcid}")
            unmapped += 1
            continue

        pmid = meta["pmid"]
        out_path = out_dir / f"{pmid}.md"
        mtime = pdf.stat().st_mtime
        prior = log.get(pmid)
        if (
            out_path.exists()
            and prior
            and prior.get("source_mtime") == mtime
            and prior.get("extractor_version") == EXTRACTOR_VERSION
        ):
            skipped += 1
            continue

        text, warnings = _extract_text(pdf)
        if not text:
            print(f"[fail] no text extracted: {pdf.name}")
            failed += 1
            log[pmid] = {
                "pmcid": pmcid,
                "source_pdf": str(pdf.relative_to(raw_root.parent)) if pdf.is_relative_to(raw_root.parent) else str(pdf),
                "source_mtime": mtime,
                "extractor_version": EXTRACTOR_VERSION,
                "extracted_at": datetime.now(timezone.utc).isoformat(),
                "char_count": 0,
                "warnings": warnings + ["empty extraction"],
            }
            continue

        fm_meta = {
            "pmid": pmid,
            "pmcid": pmcid,
            "study_id": meta.get("study_id"),
            "doi": meta.get("doi"),
            "extractor_version": EXTRACTOR_VERSION,
            "extracted_at": datetime.now(timezone.utc).isoformat(),
            "source_pdf": str(pdf.name),
            "char_count": len(text),
        }
        body = f"{_frontmatter(fm_meta)}\n\n## Full Text\n\n{text}\n"
        out_path.write_text(body)
        written += 1

        log[pmid] = {
            "pmcid": pmcid,
            "source_pdf": str(pdf.name),
            "source_mtime": mtime,
            "extractor_version": EXTRACTOR_VERSION,
            "extracted_at": fm_meta["extracted_at"],
            "char_count": len(text),
            "warnings": warnings,
        }

    fetch_log_path.write_text(json.dumps(log, indent=2, sort_keys=True))
    print(
        f"[done] written={written} skipped={skipped} unmapped={unmapped} failed={failed} "
        f"total_pdfs={len(pdfs)}"
    )
    return 0
