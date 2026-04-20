"""Generate a static markdown report page for the wiki from eval runs.

Reads the most recent ``eval/results/{ts}/runs.jsonl`` (or a specific run
directory passed via ``--run-dir``) and writes
``wiki/experiments/rag-vs-agentic.md`` with aggregate tables, per-question
drill-down, and explicit placeholders for metrics not yet captured.

Usage:

    uv run python -m eval.build_report               # use latest run
    uv run python -m eval.build_report --run-dir eval/results/2026-04-16-1152
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from statistics import mean

_EVAL_DIR = Path(__file__).resolve().parent
_RESULTS_DIR = _EVAL_DIR / "results"
_WIKI_EXPERIMENTS_DIR = _EVAL_DIR.parent / "wiki" / "experiments"
_PLOTS_DIR = _WIKI_EXPERIMENTS_DIR / "plots"


def _raw_html_block(path: Path) -> str:
    """Wrap an HTML snippet in a Pandoc raw-HTML fence so Quarto passes it through."""
    if not path.exists():
        return f"<!-- missing: {path.name} -->"
    return "```{=html}\n" + path.read_text() + "\n```"


def _latest_run_dir() -> Path:
    dirs = sorted([p for p in _RESULTS_DIR.iterdir() if p.is_dir() and (p / "runs.jsonl").exists()])
    if not dirs:
        print(f"[!] no eval runs found in {_RESULTS_DIR}", file=sys.stderr)
        sys.exit(1)
    return dirs[-1]


def _load_runs(run_dir: Path) -> list[dict]:
    path = run_dir / "runs.jsonl"
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _fmt(value, spec: str = "", placeholder: str = "—") -> str:
    if value is None or value == [] or value == {}:
        return placeholder
    try:
        return format(value, spec) if spec else str(value)
    except (TypeError, ValueError):
        return str(value)


def _avg(vals: list, spec: str = ".2f") -> str:
    clean = [v for v in vals if isinstance(v, (int, float))]
    return format(mean(clean), spec) if clean else "—"


def _aggregate(records: list[dict], mode: str) -> dict:
    mode_recs = [r for r in records if r.get("mode") == mode]
    scored = [r for r in mode_recs if "accuracy" in r.get("scores", {})]
    return {
        "n": len(mode_recs),
        "n_scored": len(scored),
        "accuracy": _avg([r["scores"]["accuracy"] for r in scored]),
        "completeness": _avg([r["scores"]["completeness"] for r in scored]),
        "citation_correctness": _avg([r["scores"]["citation_correctness"] for r in scored]),
        "citation_recall": _avg([r["citation_recall"] for r in mode_recs if "citation_recall" in r], ".3f"),
        "wall_time_s": _avg([r["wall_time_s"] for r in mode_recs if "wall_time_s" in r], ".1f"),
        "input_tokens": _avg([r["input_tokens"] for r in mode_recs if "input_tokens" in r], ".0f"),
        "output_tokens": _avg([r["output_tokens"] for r in mode_recs if "output_tokens" in r], ".0f"),
    }


def _category_breakdown(records: list[dict], mode: str) -> list[dict]:
    rows = []
    for cat in ("lookup", "list", "synthesis", "definition"):
        cat_recs = [r for r in records if r.get("mode") == mode and r.get("category") == cat]
        scored = [r for r in cat_recs if "accuracy" in r.get("scores", {})]
        if not cat_recs:
            continue
        rows.append({
            "category": cat,
            "n": len(cat_recs),
            "accuracy": _avg([r["scores"]["accuracy"] for r in scored]),
            "completeness": _avg([r["scores"]["completeness"] for r in scored]),
            "citation_correctness": _avg([r["scores"]["citation_correctness"] for r in scored]),
            "citation_recall": _avg([r["citation_recall"] for r in cat_recs if "citation_recall" in r], ".3f"),
            "wall_time_s": _avg([r["wall_time_s"] for r in cat_recs if "wall_time_s" in r], ".1f"),
        })
    return rows


def _per_question_table(records: list[dict]) -> str:
    """Build a per-question comparison table, agentic vs RAG side-by-side."""
    by_id: dict[str, dict[str, dict]] = {}
    for r in records:
        by_id.setdefault(r["id"], {})[r["mode"]] = r

    lines = [
        "| ID | Category | Agentic acc/comp/cite | RAG acc/comp/cite | Agentic s | RAG s | Winner |",
        "|----|----------|----------------------|-------------------|-----------|-------|--------|",
    ]
    for qid in sorted(by_id.keys()):
        ag = by_id[qid].get("agentic", {})
        rg = by_id[qid].get("rag", {})
        cat = (ag or rg).get("category", "—")

        def _scores_str(r: dict) -> str:
            s = r.get("scores", {})
            if not all(k in s for k in ("accuracy", "completeness", "citation_correctness")):
                return "—"
            return f"{s['accuracy']}/{s['completeness']}/{s['citation_correctness']}"

        def _total(r: dict) -> int:
            s = r.get("scores", {})
            return sum(s.get(k, 0) for k in ("accuracy", "completeness", "citation_correctness"))

        ag_total = _total(ag)
        rg_total = _total(rg)
        winner = "tie"
        if ag_total > rg_total:
            winner = "**agentic**"
        elif rg_total > ag_total:
            winner = "**rag**"

        lines.append(
            f"| {qid} | {cat} | {_scores_str(ag)} | {_scores_str(rg)} | "
            f"{_fmt(ag.get('wall_time_s'), '.1f')} | {_fmt(rg.get('wall_time_s'), '.1f')} | {winner} |"
        )

    return "\n".join(lines)


def _low_scores_section(records: list[dict], threshold: int = 2) -> str:
    """Spotlight the worst failures (accuracy ≤ threshold)."""
    failures = [
        r for r in records
        if r.get("scores", {}).get("accuracy", 5) <= threshold
    ]
    if not failures:
        return "_No questions scored at or below accuracy {threshold}._".format(threshold=threshold)

    lines = []
    for r in sorted(failures, key=lambda r: (r["id"], r["mode"])):
        s = r.get("scores", {})
        lines.append(
            f"- **{r['id']}** ({r['mode']}, {r['category']}) — "
            f"acc={s.get('accuracy', '—')} comp={s.get('completeness', '—')} cite={s.get('citation_correctness', '—')}"
        )
        reasoning = s.get("reasoning", "")
        if reasoning:
            lines.append(f"  - _Judge:_ {reasoning}")
    return "\n".join(lines)


def _compare_splits_block(primary_records: list[dict], extra: dict[str, list[dict]]) -> list[str]:
    """Build a train/val/test side-by-side aggregate table.

    ``extra`` maps split label (e.g. "val", "test") to records from that
    split. The primary (train) records are always rendered as the first
    column so the page is stable when extras are missing.
    """
    if not extra:
        return []

    lines = ["## Train / val / test comparison", ""]
    all_cols: list[tuple[str, list[dict]]] = [("train", primary_records)]
    for k, recs in extra.items():
        all_cols.append((k, recs))

    modes = sorted({r["mode"] for r in primary_records})
    dims = [
        ("accuracy", "accuracy"),
        ("completeness", "completeness"),
        ("citation_correctness", "citation"),
        ("citation_recall", "citation recall"),
        ("wall_time_s", "wall time (s)"),
    ]

    for mode in modes:
        lines.append(f"### {mode.title()}")
        lines.append("")
        header = "| metric | " + " | ".join(f"{lbl} (n={len([r for r in recs if r.get('mode') == mode])})" for lbl, recs in all_cols) + " |"
        sep = "|---|" + "|".join(["---"] * len(all_cols)) + "|"
        lines.append(header)
        lines.append(sep)
        for dim, dim_lbl in dims:
            row = f"| {dim_lbl} |"
            for _lbl, recs in all_cols:
                mode_recs = [r for r in recs if r.get("mode") == mode]
                scored = [r for r in mode_recs if dim in r.get("scores", {})] if dim in ("accuracy", "completeness", "citation_correctness") else mode_recs
                if dim in ("accuracy", "completeness", "citation_correctness"):
                    vals = [r["scores"][dim] for r in scored]
                    row += f" {_avg(vals)} |"
                else:
                    vals = [r[dim] for r in scored if dim in r]
                    spec = ".3f" if dim == "citation_recall" else ".1f"
                    row += f" {_avg(vals, spec)} |"
            lines.append(row)
        lines.append("")

    return lines


def _render(records: list[dict], run_dir: Path, extra_splits: dict[str, list[dict]] | None = None) -> str:
    ts = run_dir.name
    split = records[0].get("split", "unknown") if records else "unknown"
    modes = sorted({r["mode"] for r in records})

    agg_rows = [_aggregate(records, m) for m in modes]

    lines = [
        "---",
        "title: \"RAG vs. Agentic: experimental comparison\"",
        f"subtitle: \"Run {ts} · split={split} · n={len(records)//len(modes)} questions × {len(modes)} modes\"",
        "format:",
        "  html:",
        "    toc: true",
        "---",
        "",
        "This page compares two retrieval strategies over the same 56-paper corpus:",
        "",
        "- **Agentic** — a PydanticAI agent that navigates the compiled `wiki/` vault",
        "  purely via graph-walk tools (`read_page`, `follow_links`, `find_references`,",
        "  etc.). No full-text search; the agent orients via `index.md` and entity pages.",
        "- **RAG** — pure vector retrieval over paper-markdown chunks embedded with",
        "  Google Vertex AI `gemini-embedding-001`, packed into a single-shot LLM call.",
        "",
        "Both modes use **`claude-haiku-4-5`** as the answering model. **`claude-opus-4-6`** is the judge.",
        "See [the experiment README](https://github.com/jim-bo/cbio-kb/blob/main/eval/README.md) for the full design.",
        "",
        "## Headline numbers",
        "",
        "| Metric | " + " | ".join(m.title() for m in modes) + " |",
        "|---|" + "|".join(["---"] * len(modes)) + "|",
    ]

    for dim, label in [
        ("accuracy", "accuracy (1–5)"),
        ("completeness", "completeness (1–5)"),
        ("citation_correctness", "citation correctness (1–5)"),
        ("citation_recall", "citation recall vs gold"),
        ("wall_time_s", "avg wall time (s)"),
        ("input_tokens", "avg input tokens"),
        ("output_tokens", "avg output tokens"),
    ]:
        row = f"| {label} |"
        for agg in agg_rows:
            row += f" {agg[dim]} |"
        lines.append(row)

    lines += [
        "",
        "## Run guardrails",
        "",
    ]

    for mode in modes:
        mode_recs = [r for r in records if r.get("mode") == mode]
        timed_out = sum(1 for r in mode_recs if r.get("timed_out"))
        hit_limit = sum(1 for r in mode_recs if r.get("tool_limit_reached"))
        lines.append(
            f"- **{mode.title()}**: {timed_out} / {len(mode_recs)} runs hit the wall-clock timeout; "
            f"{hit_limit} hit the tool-call cap."
        )

    lines += [
        "",
        "## Per-category breakdown",
        "",
    ]

    for mode, agg in zip(modes, agg_rows):
        lines.append(f"### {mode.title()} mode")
        lines.append("")
        lines.append("| category | n | accuracy | completeness | cite_correct | citation_recall | wall_time_s |")
        lines.append("|----------|---|----------|--------------|--------------|-----------------|-------------|")
        for row in _category_breakdown(records, mode):
            lines.append(
                f"| {row['category']} | {row['n']} | {row['accuracy']} | {row['completeness']} | "
                f"{row['citation_correctness']} | {row['citation_recall']} | {row['wall_time_s']} |"
            )
        lines.append("")

    if extra_splits:
        lines += _compare_splits_block(records, extra_splits)

    lines += [
        "## Visual comparison",
        "",
        _raw_html_block(_PLOTS_DIR / "per_question_scatter.html"),
        "",
        "![Per-category scores by mode](plots/category_bars.png)",
        "",
        "![Cost vs quality — tokens and wall time vs total score](plots/cost_quality.png)",
        "",
        "![Strategy side-by-side: agentic tool gantt vs RAG top-k chunks](plots/strategy_strip.png)",
        "",
        "## Per-question results",
        "",
        "Scores shown as `accuracy / completeness / citation_correctness` (each 1–5).",
        "",
        _per_question_table(records),
        "",
        "## Notable failures",
        "",
        "Questions where either mode scored ≤ 2 on accuracy:",
        "",
        _low_scores_section(records, threshold=2),
        "",
        "## Source data",
        "",
        f"- Run directory: `eval/results/{ts}/`",
        f"- Raw records: `runs.jsonl` ({len(records)} rows)",
        "- Regenerate this page: `uv run python -m eval.build_report`",
        "",
    ]

    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build the wiki experiments report from eval runs")
    p.add_argument("--run-dir", type=Path, default=None, help="Primary run dir (used for train split + plots).")
    p.add_argument("--val-dir", type=Path, default=None, help="Optional val-split run to include in the comparison table.")
    p.add_argument("--test-dir", type=Path, default=None, help="Optional test-split run to include in the comparison table.")
    p.add_argument(
        "--out",
        type=Path,
        default=_WIKI_EXPERIMENTS_DIR / "rag-vs-agentic.qmd",
        help="Output path for the rendered markdown",
    )
    args = p.parse_args(argv)

    run_dir = args.run_dir or _latest_run_dir()
    records = _load_runs(run_dir)
    if not records:
        print(f"[!] no records in {run_dir}", file=sys.stderr)
        return 1

    extra: dict[str, list[dict]] = {}
    if args.val_dir:
        extra["val"] = _load_runs(args.val_dir)
    if args.test_dir:
        extra["test"] = _load_runs(args.test_dir)

    # Render plots first — the markdown inlines the interactive scatter's
    # HTML snippet, so it needs to exist on disk before _render() reads it.
    try:
        from .build_plots import render_all
        render_all(run_dir, _PLOTS_DIR)
    except Exception as e:
        print(f"[!] plot rendering skipped: {e}", file=sys.stderr)

    rendered = _render(records, run_dir, extra_splits=extra or None)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(rendered)
    print(f"[*] wrote {args.out} from {run_dir}")
    if extra:
        print(f"[*] included extras: {', '.join(extra.keys())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
