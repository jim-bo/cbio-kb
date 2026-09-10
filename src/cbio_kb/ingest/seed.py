"""Regenerate data/seed/cbioportal_study_pmids.csv from the live cBioPortal API.

The seed is the corpus definition: one ``studyId,pmid`` row per publication
backing a public cBioPortal study. A study's ``pmid`` field may list several
PMIDs (comma-separated, sometimes with repeats); each becomes its own row.
Studies without a PMID (typically pre-publication) are skipped.

Rows are sorted by (studyId, pmid) so reruns produce minimal diffs, and the
command prints which pairs were added/removed relative to the existing file.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

from cbio_kb.ontology.sync import fetch_studies


def build_rows(studies: list[dict]) -> list[tuple[str, str]]:
    """Return sorted unique (studyId, pmid) pairs from cBioPortal study records."""
    pairs: set[tuple[str, str]] = set()
    for s in studies:
        sid = (s.get("studyId") or "").strip()
        for pmid in re.split(r"[,;\s]+", str(s.get("pmid") or "")):
            if sid and pmid.isdigit():
                pairs.add((sid, pmid))
    return sorted(pairs)


def _read_pairs(path: Path) -> set[tuple[str, str]]:
    if not path.exists():
        return set()
    with path.open(encoding="utf-8") as f:
        return {(r["studyId"], r["pmid"]) for r in csv.DictReader(f)}


def run(out: Path) -> int:
    rows = build_rows(fetch_studies())
    before = _read_pairs(out)
    after = set(rows)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["studyId", "pmid"])
        w.writerows(rows)

    added, removed = sorted(after - before), sorted(before - after)
    new_pmids = sorted({p for _, p in after} - {p for _, p in before}, key=int)
    print(f"[seed] wrote {out}: {len(rows)} (studyId, pmid) pairs, "
          f"{len({p for _, p in rows})} unique PMIDs")
    print(f"[seed] +{len(added)} / -{len(removed)} pairs; {len(new_pmids)} PMIDs new to the seed")
    for sid, pmid in added:
        print(f"  + {sid},{pmid}")
    for sid, pmid in removed:
        print(f"  - {sid},{pmid}")
    return 0
