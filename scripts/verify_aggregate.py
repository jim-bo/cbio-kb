"""Aggregate per-paper verification JSON into a corpus-wide report.

Walks `eval/verify/{pmid}.json` (produced by `verify_paper.py --all --out-dir
eval/verify`) and emits:
  - eval/verify/summary.json   — machine-readable rollup
  - eval/verify/REPORT.md      — human-readable, grouped by finding type

Usage:
    uv run python scripts/verify_aggregate.py
    uv run python scripts/verify_aggregate.py --in-dir eval/verify
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IN_DIR = REPO_ROOT / "eval" / "verify"

SEVERITY = ("pass", "info", "warn", "fail")
SYMBOL = {"pass": "✓", "info": "•", "warn": "⚠", "fail": "✗"}


def load_reports(in_dir: Path) -> list[dict]:
    reports = []
    for p in sorted(in_dir.glob("*.json")):
        if p.name in {"summary.json"}:
            continue
        try:
            reports.append(json.loads(p.read_text()))
        except json.JSONDecodeError:
            continue
    return reports


def build_summary(reports: list[dict]) -> dict:
    corpus = {s: 0 for s in SEVERITY}
    by_code: Counter = Counter()
    by_code_severity: dict[str, str] = {}
    for r in reports:
        for s in SEVERITY:
            corpus[s] += r["tallies"].get(s, 0)
        for f in r["findings"]:
            by_code[f["code"]] += 1
            by_code_severity.setdefault(f["code"], f["severity"])
    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "n_papers": len(reports),
        "corpus_tallies": corpus,
        "findings_by_code": [
            {"code": code, "severity": by_code_severity[code], "count": n}
            for code, n in by_code.most_common()
        ],
        "papers": [
            {"pmid": r["pmid"], "title": r["title"],
             "study_id": r.get("study_id"), "tallies": r["tallies"]}
            for r in sorted(reports, key=lambda r: r["pmid"])
        ],
    }


def _findings_with_code(reports: list[dict], code: str) -> list[tuple[dict, dict]]:
    """Return [(report, finding)] pairs for all findings matching `code`."""
    out = []
    for r in reports:
        for f in r["findings"]:
            if f["code"] == code:
                out.append((r, f))
    return out


def _section_table(out: list[str], heading: str, rows: list[tuple[dict, dict]],
                   columns: list[tuple[str, callable]]) -> None:
    if not rows:
        return
    out.append(f"\n## {heading} ({len(rows)})\n")
    header = "| " + " | ".join(c[0] for c in columns) + " |"
    sep = "| " + " | ".join("---" for _ in columns) + " |"
    out.append(header)
    out.append(sep)
    for r, f in rows:
        cells = [str(extractor(r, f)) for _, extractor in columns]
        out.append("| " + " | ".join(cells) + " |")


def build_report(reports: list[dict], summary: dict) -> str:
    out: list[str] = []
    out.append("# Paper-compiler fact verification — corpus report\n")
    out.append(f"_Generated {summary['generated_at']}; "
               f"{summary['n_papers']} papers._\n")
    ct = summary["corpus_tallies"]
    out.append(f"**Corpus tallies:** "
               f"{SYMBOL['pass']} {ct['pass']} pass · "
               f"{SYMBOL['info']} {ct['info']} info · "
               f"{SYMBOL['warn']} {ct['warn']} warn · "
               f"{SYMBOL['fail']} {ct['fail']} fail\n")

    out.append("## Findings by code\n")
    out.append("| severity | code | count |")
    out.append("| --- | --- | --- |")
    for row in summary["findings_by_code"]:
        out.append(f"| {SYMBOL[row['severity']]} {row['severity']} "
                   f"| `{row['code']}` | {row['count']} |")

    # Per-section drilldowns by finding code.
    _section_table(out, "Studies not found on cBioPortal",
                   _findings_with_code(reports, "study.missing"),
                   [("PMID", lambda r, f: r["pmid"]),
                    ("scope", lambda r, f: f"`{f['scope']}`"),
                    ("message", lambda r, f: f["message"])])

    _section_table(out, "PMID mismatch on primary study_id (likely wrong study)",
                   _findings_with_code(reports, "study.pmid_differs"),
                   [("PMID", lambda r, f: r["pmid"]),
                    ("study_id", lambda r, f: f"`{f['scope'].split(':',1)[1]}`"),
                    ("API pmids", lambda r, f: ", ".join(f["evidence"].get("api_pmids", [])) or
                                                f["evidence"].get("api_pmid", "")),
                    ("title", lambda r, f: r["title"][:60])])

    _section_table(out, "Cancer-type mismatches (frontmatter vs API)",
                   _findings_with_code(reports, "study.cancer_type_mismatch"),
                   [("PMID", lambda r, f: r["pmid"]),
                    ("scope", lambda r, f: f"`{f['scope']}`"),
                    ("API cancerTypeId", lambda r, f: f"`{f['evidence'].get('api_cancer_type_id','')}`"),
                    ("frontmatter cancer_types", lambda r, f: ", ".join(f["evidence"].get("frontmatter", [])))])

    _section_table(out, "Frontmatter panel ID claimed but not in study profiles",
                   _findings_with_code(reports, "method.panel_missing"),
                   [("PMID", lambda r, f: r["pmid"]),
                    ("scope", lambda r, f: f"`{f['scope']}`"),
                    ("panel", lambda r, f: f"`{f['evidence'].get('method','')}`")])

    _section_table(out, "Panel id has fuzzy family match only",
                   _findings_with_code(reports, "method.panel_family_only"),
                   [("PMID", lambda r, f: r["pmid"]),
                    ("scope", lambda r, f: f"`{f['scope']}`"),
                    ("panel", lambda r, f: f"`{f['evidence'].get('method','')}`"),
                    ("family", lambda r, f: f"`{f['evidence'].get('stem','')}`")])

    _section_table(out, "HUGO symbols that did not resolve",
                   [(r, f) for r, f in _findings_with_code(reports, "ontology.genes")
                    if f["severity"] != "pass"],
                   [("PMID", lambda r, f: r["pmid"]),
                    ("missing", lambda r, f: ", ".join(f["evidence"].get("missing", [])))])

    _section_table(out, "Cancer types that did not resolve",
                   [(r, f) for r, f in _findings_with_code(reports, "ontology.cancer_types")
                    if f["severity"] != "pass"],
                   [("PMID", lambda r, f: r["pmid"]),
                    ("missing", lambda r, f: ", ".join(f["evidence"].get("missing", [])))])

    # Per-paper scoreboard at the end.
    out.append("\n## Per-paper scoreboard\n")
    out.append("| PMID | study_id | ✓ | • | ⚠ | ✗ | title |")
    out.append("| --- | --- | --- | --- | --- | --- | --- |")
    for p in sorted(summary["papers"],
                    key=lambda p: (-p["tallies"].get("fail", 0),
                                   -p["tallies"].get("warn", 0),
                                   p["pmid"])):
        t = p["tallies"]
        out.append(f"| {p['pmid']} | `{p.get('study_id') or ''}` "
                   f"| {t['pass']} | {t['info']} | {t['warn']} | {t['fail']} "
                   f"| {p['title'][:60]} |")

    return "\n".join(out) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--in-dir", type=Path, default=DEFAULT_IN_DIR,
                    help=f"Directory of per-paper JSON (default: {DEFAULT_IN_DIR})")
    args = ap.parse_args()

    if not args.in_dir.exists():
        raise SystemExit(f"no such dir: {args.in_dir}")
    reports = load_reports(args.in_dir)
    if not reports:
        raise SystemExit(f"no *.json reports in {args.in_dir}")

    summary = build_summary(reports)
    (args.in_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    (args.in_dir / "REPORT.md").write_text(build_report(reports, summary))
    print(f"wrote {args.in_dir / 'summary.json'} and {args.in_dir / 'REPORT.md'} "
          f"({summary['n_papers']} papers)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
