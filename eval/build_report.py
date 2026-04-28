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
_BIBLIOGRAPHY_PATH = _EVAL_DIR / "bibliography.yaml"
_NARRATIVE_PATH = _EVAL_DIR / "narrative.md"


def _load_narrative() -> dict[str, str]:
    """Parse ``eval/narrative.md`` into a dict keyed by section id.

    Sections are delimited by a top-level heading of the form
    ``## section:<id>``; everything until the next such heading (or
    EOF) is the body. HTML comments at the top of the file are ignored.
    Returns an empty dict if the file is missing.
    """
    import re

    if not _NARRATIVE_PATH.exists():
        return {}
    text = _NARRATIVE_PATH.read_text()
    parts = re.split(r"(?m)^## section:([a-z0-9_]+)\s*$", text)
    # parts layout after split: [preamble, id1, body1, id2, body2, ...]
    sections: dict[str, str] = {}
    for i in range(1, len(parts), 2):
        sid = parts[i].strip()
        body = parts[i + 1].strip() if i + 1 < len(parts) else ""
        sections[sid] = body
    return sections


def _compute_stats(records: list[dict], extra_splits: dict | None) -> dict[str, str]:
    """Pre-compute the handful of numeric values that narrative.md may
    reference via ``{stat:<name>}`` placeholders.

    Keep this list small — only stats that should stay live when new
    runs land. Commentary numbers ("roughly 25% more wall time") stay
    as plain text in narrative.md.
    """
    all_records = list(records)
    for recs in (extra_splits or {}).values():
        all_records.extend(recs)

    def _m(mode: str, split: str, metric: str) -> str:
        return _headline_metric(all_records, mode, split, metric)

    return {
        "ag_test_acc":  _m("agentic", "test", "accuracy"),
        "rg_test_acc":  _m("rag",     "test", "accuracy"),
        "ag_test_comp": _m("agentic", "test", "completeness"),
        "rg_test_comp": _m("rag",     "test", "completeness"),
        "ag_test_rec":  _m("agentic", "test", "citation_recall"),
        "rg_test_rec":  _m("rag",     "test", "citation_recall"),
    }


def _expand_placeholders(text: str, bib: dict, stats: dict[str, str]) -> str:
    """Replace ``{cite:key}`` and ``{stat:name}`` placeholders.

    Unknown citation keys expand to ``[key]`` (visible typo), unknown
    stats to ``{stat:name}`` (left untouched so the placeholder is
    clearly still there and the author can fix it).
    """
    import re

    def _sub_cite(match: re.Match) -> str:
        return _cite(bib, match.group(1))

    def _sub_stat(match: re.Match) -> str:
        key = match.group(1)
        return stats.get(key, match.group(0))

    text = re.sub(r"\{cite:([A-Za-z0-9_]+)\}", _sub_cite, text)
    text = re.sub(r"\{stat:([A-Za-z0-9_]+)\}", _sub_stat, text)
    return text


def _load_bibliography() -> tuple[dict, list]:
    """Load ``eval/bibliography.yaml``.

    Returns ``(entries_by_key, group_order)`` where ``entries_by_key``
    maps bibliography keys to full entry dicts and ``group_order`` is
    the list of ``{id, label}`` group descriptors in the order the YAML
    file declared them.
    """
    import yaml  # local import — yaml isn't always installed at import time

    if not _BIBLIOGRAPHY_PATH.exists():
        return {}, []
    data = yaml.safe_load(_BIBLIOGRAPHY_PATH.read_text()) or {}
    groups = data.get("groups", [])
    entries = data.get("entries", [])
    by_key = {e["key"]: e for e in entries}
    return by_key, groups


def _cite(bib: dict, key: str) -> str:
    """Render an inline citation as a markdown link.

    ``[Lewis 2020](https://arxiv.org/abs/2005.11401)``. Falls back to
    the bare key if the bibliography doesn't carry that entry (so a
    typo surfaces loudly rather than silently eats the citation).
    """
    entry = bib.get(key)
    if not entry:
        return f"[{key}]"
    # Author-year style short form: "Lewis 2020", "Edge et al. 2024".
    authors = entry.get("authors", "").strip()
    # Trim trailing "et al." to keep the short form compact.
    first = authors.split(",")[0].strip() if authors else key
    year = entry.get("year", "")
    label = f"{first} {year}".strip()
    url = entry.get("url", "")
    if url:
        return f"[{label}]({url})"
    return label


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

    # Caller owns the section heading (so this block can slot into
    # either the Results section or its own section). Emit only the
    # per-mode tables.
    lines: list[str] = []
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
        lines.append(f"#### {mode.title()}")
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


def _headline_metric(records: list[dict], mode: str, split: str, metric: str) -> str:
    """Mean of ``metric`` for the given mode/split, formatted to 2 dp."""
    recs = [r for r in records if r.get("mode") == mode and r.get("split") == split]
    if metric in ("accuracy", "completeness", "citation_correctness"):
        vals = [r["scores"][metric] for r in recs if metric in r.get("scores", {})]
    else:
        vals = [r[metric] for r in recs if metric in r]
    return _avg(vals, ".2f" if metric != "citation_recall" else ".3f")


def _abstract_block(narrative: dict, bib: dict, stats: dict) -> list[str]:
    body = _expand_placeholders(narrative.get("abstract", ""), bib, stats)
    return ["## Abstract", "", body, ""]


def _introduction_block(narrative: dict, bib: dict, stats: dict) -> list[str]:
    body = _expand_placeholders(narrative.get("intro", ""), bib, stats)
    return ["## Introduction and background", "", body, ""]


def _methods_block(narrative: dict, bib: dict, stats: dict) -> list[str]:
    body = _expand_placeholders(narrative.get("methods", ""), bib, stats)
    return ["## Methods", "", body, ""]


def _results_block(records: list[dict], run_dir: Path,
                   extra_splits: dict | None,
                   narrative: dict, bib: dict, stats: dict) -> list[str]:
    modes = sorted({r["mode"] for r in records})
    agg_rows = [_aggregate(records, m) for m in modes]

    def _prose(key: str) -> str:
        return _expand_placeholders(narrative.get(key, ""), bib, stats)

    lines: list[str] = ["## Results", ""]

    # --- Headline numbers (train-split primary) ---
    lines += [
        "### Headline numbers (train split)",
        "",
        _prose("headline_intro"),
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
    lines += ["", _prose("headline_takeaway"), ""]

    # --- Figure 1: category bars ---
    fig1_caption = _prose("figure1_caption") or "Figure 1."
    lines += [
        "### Figure 1 — Mean judge score by question category",
        "",
        _prose("figure1_intro"),
        "",
        f"![{fig1_caption}](plots/category_bars.png)",
        "",
        _prose("figure1_takeaway"),
        "",
    ]

    # --- Split comparison ---
    if extra_splits:
        lines += [
            "### Generalization: train / val / test",
            "",
            _prose("splits_intro"),
            "",
        ]
        lines += _compare_splits_block(records, extra_splits)
        lines += [_prose("splits_takeaway"), ""]

    # --- Figure 2: per-question scatter (interactive only on the web page) ---
    # The PNG twin is still rendered to disk by build_plots.render_all()
    # so downstream contexts (README embeds, exported static bundles)
    # can pick it up, but the web page shows the interactive version
    # only to avoid the same figure rendering twice in a row.
    lines += [
        "### Figure 2 — Per-question comparison",
        "",
        _prose("figure2_intro"),
        "",
        _raw_html_block(_PLOTS_DIR / "per_question_scatter.html"),
        "",
        _prose("figure2_takeaway"),
        "",
    ]

    # --- Figure 3: cost/quality ---
    fig3_caption = _prose("figure3_caption") or "Figure 3."
    lines += [
        "### Figure 3 — Cost vs quality",
        "",
        _prose("figure3_intro"),
        "",
        f"![{fig3_caption}](plots/cost_quality.png)",
        "",
        _prose("figure3_takeaway"),
        "",
    ]

    # --- Guardrails (numbers computed, commentary from narrative) ---
    lines += ["### Run guardrails", ""]
    for mode in modes:
        mode_recs = [r for r in records if r.get("mode") == mode]
        timed_out = sum(1 for r in mode_recs if r.get("timed_out"))
        hit_limit = sum(1 for r in mode_recs if r.get("tool_limit_reached"))
        lines.append(
            f"- **{mode.title()}**: {timed_out} / {len(mode_recs)} runs hit the "
            f"180 s wall-clock timeout; {hit_limit} hit the 20-call tool cap."
        )
    guardrails_note = _prose("guardrails_note")
    if guardrails_note:
        lines += ["", guardrails_note, ""]
    else:
        lines.append("")
    return lines


def _discussion_block(narrative: dict, bib: dict, stats: dict) -> list[str]:
    caveats = _expand_placeholders(narrative.get("discussion_caveats", ""), bib, stats)
    next_steps = _expand_placeholders(narrative.get("next_steps", ""), bib, stats)
    parts: list[str] = ["## Discussion and next steps", ""]
    if caveats:
        parts += [caveats, ""]
    if next_steps:
        parts += [next_steps, ""]
    return parts


def _references_block(bib: dict, groups: list) -> list[str]:
    if not bib:
        return []
    lines = ["## References", ""]
    for g in groups:
        gid, glabel = g["id"], g["label"]
        entries = [e for e in bib.values() if e.get("bucket") == gid]
        if not entries:
            continue
        lines.append(f"### {glabel}")
        lines.append("")
        # Sort by year then author surname.
        entries.sort(key=lambda e: (e.get("year", 0), e.get("authors", "")))
        for e in entries:
            authors = e.get("authors", "").strip()
            year = e.get("year", "")
            title = e.get("title", "").strip()
            venue = e.get("venue", "").strip()
            url = e.get("url", "").strip()
            one_liner = e.get("one_liner", "").strip()
            line = f"- {authors} ({year}). *{title}*. {venue}."
            if url:
                line += f" [{url}]({url})"
            if one_liner:
                line += f" — {one_liner}"
            lines.append(line)
        lines.append("")
    return lines


def _load_question_bank() -> list[dict]:
    """Load the v1 question set so the appendix can show what was asked.

    Returns a list of question dicts straight from ``eval/questions/v1.yaml``.
    Empty list if the file is missing or can't be parsed — a rendering
    concern, not a hard failure.
    """
    import yaml

    path = _EVAL_DIR / "questions" / "v1.yaml"
    if not path.exists():
        return []
    try:
        data = yaml.safe_load(path.read_text()) or {}
        return list(data.get("questions") or [])
    except Exception:
        return []


def _questions_table(records: list[dict]) -> list[str]:
    """Render the question bank as a markdown table, scoped to the ids
    that actually have records in this run.

    Columns: id · category · split · question · gold PMIDs.
    """
    questions = _load_question_bank()
    if not questions:
        return []

    seen_ids = {r["id"] for r in records}

    # Order: by split (train → val → test), then by id.
    split_rank = {"train": 0, "val": 1, "test": 2}

    def _sort_key(q: dict) -> tuple:
        return (split_rank.get(q.get("split", ""), 9), q.get("id", ""))

    ordered = sorted(
        [q for q in questions if q.get("id") in seen_ids],
        key=_sort_key,
    )
    if not ordered:
        return []

    lines = [
        "| ID | Split | Category | Question | Gold PMIDs |",
        "|----|-------|----------|----------|------------|",
    ]
    for q in ordered:
        qid = q.get("id", "—")
        split = q.get("split", "—")
        cat = q.get("category", "—")
        # Escape pipes and collapse whitespace so the table cell stays intact.
        text = " ".join(str(q.get("question", "")).split()).replace("|", "\\|")
        gold = q.get("gold_pmids") or []
        gold_str = ", ".join(f"`{p}`" for p in gold) if gold else "—"
        lines.append(f"| {qid} | {split} | {cat} | {text} | {gold_str} |")
    return lines


def _appendix_block(records: list[dict], run_dir: Path,
                    extra_splits: dict | None = None) -> list[str]:
    ts = run_dir.name
    modes = sorted({r["mode"] for r in records})

    # Merged record pool lets the Question Bank table include val/test
    # questions too, not just the train slice.
    all_records = list(records)
    for recs in (extra_splits or {}).values():
        all_records.extend(recs)

    lines = [
        "## Appendix",
        "",
        "### A. Question bank",
        "",
        "Every question that appears in this report, with its split,",
        "category, full text, and the gold PMIDs used to score citation",
        "recall. Scores for each question are in the *Per-question",
        "results* section below.",
        "",
    ]
    q_table = _questions_table(all_records)
    if q_table:
        lines += q_table
    else:
        lines.append("_Question bank not loadable from `eval/questions/v1.yaml`._")
    lines.append("")

    lines += [
        "### B. Per-category breakdown (train split)",
        "",
    ]
    for mode in modes:
        lines.append(f"#### {mode.title()} mode")
        lines.append("")
        lines.append("| category | n | accuracy | completeness | cite_correct | citation_recall | wall_time_s |")
        lines.append("|----------|---|----------|--------------|--------------|-----------------|-------------|")
        for row in _category_breakdown(records, mode):
            lines.append(
                f"| {row['category']} | {row['n']} | {row['accuracy']} | {row['completeness']} | "
                f"{row['citation_correctness']} | {row['citation_recall']} | {row['wall_time_s']} |"
            )
        lines.append("")

    lines += [
        "### C. Per-question results (train split)",
        "",
        "Scores shown as `accuracy / completeness / citation_correctness` (each 1–5).",
        "",
        _per_question_table(records),
        "",
        "### D. Notable failures",
        "",
        "Questions where either mode scored ≤ 2 on accuracy:",
        "",
        _low_scores_section(records, threshold=2),
        "",
        "### E. Source data",
        "",
        f"- Run directory: `eval/results/{ts}/`",
        f"- Raw records: `runs.jsonl` ({len(records)} rows)",
        "- Bibliography source: `eval/bibliography.yaml`",
        "- Narrative source: `eval/narrative.md`",
        "- Regenerate this page: `uv run python -m eval.build_report --run-dir … --val-dir … --test-dir …`",
        "",
    ]
    return lines


def _render(records: list[dict], run_dir: Path, extra_splits: dict[str, list[dict]] | None = None) -> str:
    ts = run_dir.name
    split = records[0].get("split", "unknown") if records else "unknown"
    modes = sorted({r["mode"] for r in records})
    bib, groups = _load_bibliography()
    narrative = _load_narrative()
    stats = _compute_stats(records, extra_splits)

    lines: list[str] = [
        "---",
        "title: \"Agentic graph-walk vs dense RAG on a cBioPortal paper wiki\"",
        f"subtitle: \"Run {ts} · primary split={split} · n={len(records)//len(modes)} questions × {len(modes)} modes\"",
        "format:",
        "  html:",
        "    toc: true",
        "    toc-depth: 3",
        "    number-sections: false",
        "---",
        "",
    ]

    lines += _abstract_block(narrative, bib, stats)
    lines += _introduction_block(narrative, bib, stats)
    lines += _methods_block(narrative, bib, stats)
    lines += _results_block(records, run_dir, extra_splits, narrative, bib, stats)
    lines += _discussion_block(narrative, bib, stats)
    lines += _references_block(bib, groups)
    lines += _appendix_block(records, run_dir, extra_splits)

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
        plot_extras = {}
        if args.val_dir:
            plot_extras["val"] = args.val_dir
        if args.test_dir:
            plot_extras["test"] = args.test_dir
        render_all(run_dir, _PLOTS_DIR, extra_dirs=plot_extras or None)
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
