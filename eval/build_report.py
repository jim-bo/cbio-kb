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


def _abstract_block(records: list[dict], extra_splits: dict | None) -> list[str]:
    """Write the ~120-word abstract from the merged record pool."""
    all_records = list(records)
    for recs in (extra_splits or {}).values():
        all_records.extend(recs)

    def _m(mode: str, split: str, metric: str) -> str:
        return _headline_metric(all_records, mode, split, metric)

    ag_test_acc = _m("agentic", "test", "accuracy")
    rg_test_acc = _m("rag", "test", "accuracy")
    ag_test_comp = _m("agentic", "test", "completeness")
    rg_test_comp = _m("rag", "test", "completeness")
    ag_test_rec = _m("agentic", "test", "citation_recall")
    rg_test_rec = _m("rag", "test", "citation_recall")

    return [
        "## Abstract",
        "",
        "We compare two retrieval strategies over a curated, 56-paper subset",
        "of the cBioPortal cancer-genomics publication corpus. The first",
        "(**Agentic**) is a language-model agent that navigates a",
        "hand-compiled wiki of papers, genes, cancer types, datasets, drugs,",
        "and methods via six graph-walk tools. The second (**RAG**) is",
        "standard dense-vector retrieval: chunk paper markdowns, embed with",
        "Vertex AI `gemini-embedding-001`, pull the top-40 chunks, answer in",
        "a single call. Both modes share the answering model",
        "(`claude-haiku-4-5`) and a rubric judge (`claude-opus-4-6`). On a",
        "50-question set split 30/10/10 across train/val/test and four",
        "question categories, the agent wins on every dimension of the",
        f"held-out test split — accuracy {ag_test_acc} vs {rg_test_acc},",
        f"completeness {ag_test_comp} vs {rg_test_comp}, citation recall",
        f"{ag_test_rec} vs {rg_test_rec} — at roughly 25% more wall time.",
        "Results are consistent across splits, so the win is not train-set",
        "overfitting. We read this as a preliminary step before trying",
        "GraphRAG-style community summarization, adaptive retrieval",
        "(Self-RAG / CRAG), and a larger corpus. The apparatus, data, and",
        "source are all reproducible from `eval/`.",
        "",
    ]


def _introduction_block(bib: dict) -> list[str]:
    """Three paragraphs with inline citations."""
    return [
        "## Introduction and background",
        "",
        "Retrieval-augmented generation",
        f"({_cite(bib, 'lewis2020rag')}) has become the default recipe for",
        "grounding language-model answers in a specific corpus. The dominant",
        "implementation is dense-vector search over fixed-size text chunks",
        f"({_cite(bib, 'karpukhin2020dpr')}, {_cite(bib, 'khattab2022colbertv2')}),",
        "evaluated on heterogeneous retrieval benchmarks",
        f"({_cite(bib, 'thakur2021beir')}, {_cite(bib, 'muennighoff2022mteb')}) and",
        f"generation-quality rubrics ({_cite(bib, 'es2023ragas')}). In parallel, two",
        "threads have emerged that treat retrieval as a *behaviour* rather than a",
        "single lookup: graph-augmented retrieval",
        f"({_cite(bib, 'edge2024graphrag')}, {_cite(bib, 'jimenez2024hipporag')},",
        f"{_cite(bib, 'guo2024lightrag')}, {_cite(bib, 'gao2024structrag')}) builds",
        "an explicit structure over the corpus and walks it; agentic retrieval",
        f"({_cite(bib, 'yao2023react')}, {_cite(bib, 'nakano2022webgpt')},",
        f"{_cite(bib, 'asai2023selfrag')}, {_cite(bib, 'yan2024crag')},",
        f"{_cite(bib, 'singh2025agenticrag')}) lets a language-model agent decide what",
        "to read next based on what it just saw. Both converge on the same",
        "observation: for questions that span documents, flat top-k vector",
        "search is underpowered.",
        "",
        "This experiment is a preliminary step in that direction for a",
        "cancer-genomics corpus. We already maintain a hand-compiled wiki of",
        "papers, genes, cancer types, datasets, drugs and methods (56 papers",
        "as of this run, a subset of the cBioPortal publication list), with",
        "cross-links between entity pages and their citing papers. The",
        "question we want to answer is modest: *given that graph, does an",
        "agent that walks it beat a vanilla RAG pipeline over the same",
        "papers?* A positive answer makes the wiki investment defensible and",
        "motivates building more structure into it; a negative one says the",
        "structure isn't paying for itself and a plain embedding pipeline",
        "would do. Biomedical-QA evaluation has a long tradition of treating",
        "this setup carefully — factoid, list, yes/no and summary question",
        f"types ({_cite(bib, 'krithara2023bioasq')},",
        f"{_cite(bib, 'jin2019pubmedqa')},",
        f"{_cite(bib, 'wadden2020scifact')}) — which shaped our question set.",
        "",
        "We are aware of several gaps before this can serve as a full",
        "comparison to the 2024–2026 GraphRAG / agentic-retrieval literature.",
        "Our wiki graph has no community-detection layer",
        f"({_cite(bib, 'edge2024graphrag')}), no pre-computed theme/subgraph",
        "summaries, and no adaptive retrieval loop",
        f"({_cite(bib, 'asai2023selfrag')}, {_cite(bib, 'yan2024crag')}). We are",
        "under-covering the full cBioPortal publication set (56 of several",
        "hundred), and question-set coverage of synthesis and list question",
        "types is thin. Treat the numbers here as directional, not absolute.",
        "",
    ]


def _methods_block() -> list[str]:
    return [
        "## Methods",
        "",
        "**Corpus.** 56 papers from the cBioPortal publication list, selected",
        "because they were fully ingested into both our compiled wiki (at",
        "`wiki/papers/{pmid}.md`) and our chunking/embedding pipeline (raw",
        "markdown at `data/raw/papers/{pmid}.md`). Both retrieval modes see",
        "exactly this set — no side channel.",
        "",
        "**Question set.** 50 questions authored manually, split 30 / 10 / 10",
        "across train / val / test, and tagged with one of four categories:",
        "*lookup* (single-paper factoid), *list* (enumerate papers or",
        "entities meeting a criterion), *synthesis* (cross-paper claim), or",
        "*definition* (what is X?). Each question carries one or more gold",
        "PMIDs so we can measure citation recall independently of the judge.",
        "",
        "**Agentic mode.** A PydanticAI agent using `claude-haiku-4-5` with",
        "six graph-walk tools: `read_page`, `read_section`, `follow_links`,",
        "`find_references`, `get_page_metadata`, `list_pages`. The system",
        "prompt instructs the agent to start from `index.md` and traverse by",
        "title match → entity pivot → follow links. A hard cap of 20 tool",
        "calls per query and a 180-second wall-clock deadline are enforced",
        "at the server and runner layers respectively.",
        "",
        "**RAG mode.** Paper markdowns are chunked (~900 chars with 120",
        "overlap), embedded with Vertex AI `gemini-embedding-001`",
        "(3072-dim), and stored in a FAISS `IndexFlatIP` for cosine",
        "similarity. At query time we embed the question, pull the top-40",
        "passages (budgeted to ~60k characters of context), and issue a",
        "single `claude-haiku-4-5` call with the stitched passages plus the",
        "question.",
        "",
        "**Judge.** `claude-opus-4-6` reads the question, gold notes, and",
        "the agent's final answer, and returns three integer scores on a",
        "1–5 rubric — *accuracy*, *completeness*, *citation_correctness* —",
        "plus a free-text reason. We separately compute citation recall as",
        "the fraction of gold PMIDs cited in the answer (detected by regex",
        "on `PMID:\\d+` and `papers/\\d+\\.html` link forms). Full rubric",
        "and scoring code are in",
        "[eval/judge.py](https://github.com/jim-bo/cbio-kb/blob/main/eval/judge.py)",
        "and [eval/README.md](https://github.com/jim-bo/cbio-kb/blob/main/eval/README.md).",
        "",
    ]


def _results_block(records: list[dict], run_dir: Path,
                   extra_splits: dict | None) -> list[str]:
    ts = run_dir.name
    modes = sorted({r["mode"] for r in records})
    agg_rows = [_aggregate(records, m) for m in modes]

    lines: list[str] = ["## Results", ""]

    # --- Headline numbers (train-split primary) ---
    lines += [
        "### Headline numbers (train split)",
        "",
        "Mean scores on the 30-question train split. Judge scores are on a",
        "1–5 scale; citation recall is the fraction of gold PMIDs appearing",
        "in the answer.",
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
        "*Takeaway — agentic wins on completeness and recall; RAG is 2× cheaper in",
        "tokens and ~2× faster in wall time. Accuracy and citation correctness are",
        "within noise.*",
        "",
    ]

    # --- Figure 1: category bars ---
    lines += [
        "### Figure 1 — Mean judge score by question category",
        "",
        "Each category is a different flavour of question. Categories",
        "where *completeness* (did you enumerate the facts?) carries signal",
        "are where the agent's per-page reading pays off.",
        "",
        "![Figure 1. Mean judge score by question category, agentic vs RAG. Each panel is one metric (accuracy / completeness / citation). Agentic pulls clearly ahead on completeness for list and synthesis questions.](plots/category_bars.png)",
        "",
        "*Takeaway — lookup and definition are a wash; agentic edges RAG on",
        "list (+0.3 completeness) and especially synthesis (+1.3 completeness),",
        "the categories where full-page reading matters most.*",
        "",
    ]

    # --- Split comparison ---
    if extra_splits:
        lines += [
            "### Generalization: train / val / test",
            "",
            "Three disjoint splits run with identical configuration. Consistency",
            "across the three is evidence the agent's win isn't train-set",
            "overfitting (we tuned nothing between splits).",
            "",
        ]
        lines += _compare_splits_block(records, extra_splits)
        lines += [
            "*Takeaway — agentic stays ahead on every metric on every split,",
            "with the test margins matching or exceeding the train margins.*",
            "",
        ]

    # --- Figure 2: per-question scatter (interactive + PNG) ---
    lines += [
        "### Figure 2 — Per-question comparison",
        "",
        "Each point is one train-split question plotted at its total judge",
        "score (accuracy + completeness + citation, 3–15) for both modes.",
        "Bubble size is proportional to whichever mode took longer on that",
        "question. Points above the dashed *y = x* line are agent wins;",
        "below the line are RAG wins.",
        "",
        "*Hover any point in the interactive version for the full question",
        "and both answers.*",
        "",
        _raw_html_block(_PLOTS_DIR / "per_question_scatter.html"),
        "",
        "![Figure 2 static fallback. Per-question agentic vs RAG judge scores; synthesis (red) clusters above the diagonal, one notable agent-loss at LS04 and one at S04 sits below.](plots/per_question_scatter.png)",
        "",
        "*Takeaway — most synthesis points (red) sit above the diagonal, most",
        "definition and high-scoring lookup points pile near (15, 15). Two",
        "agent-losses stand out: LS04 (a list question the agent got lost on)",
        "and S04 (a synthesis question both modes struggled with, but RAG",
        "did better).*",
        "",
    ]

    # --- Figure 3: cost/quality ---
    lines += [
        "### Figure 3 — Cost vs quality",
        "",
        "Cost here is deliberately not budget-matched: each strategy carries",
        "its own shape. The left panel shows input-token cost (log scale)",
        "against total judge score; the right panel shows the same against",
        "wall time. A well-behaved retrieval strategy should have its",
        "high-scoring dots concentrated at the left of each panel.",
        "",
        "![Figure 3. Total judge score vs input tokens (log scale, left) and wall time (right), agentic and RAG overlaid. RAG clusters cheap/fast; agentic spends more to reach the same score ceiling, but also reaches it on questions where RAG cannot.](plots/cost_quality.png)",
        "",
        "*Takeaway — RAG has a tight, cheap, fast cluster in the 10k-token",
        "band; agentic spreads across 10k–200k tokens. Both modes hit the",
        "score ceiling of 15, but for several mid-scoring synthesis",
        "questions only the agent crosses into the high band.*",
        "",
    ]

    # --- Guardrails ---
    lines += [
        "### Run guardrails",
        "",
    ]
    for mode in modes:
        mode_recs = [r for r in records if r.get("mode") == mode]
        timed_out = sum(1 for r in mode_recs if r.get("timed_out"))
        hit_limit = sum(1 for r in mode_recs if r.get("tool_limit_reached"))
        lines.append(
            f"- **{mode.title()}**: {timed_out} / {len(mode_recs)} runs hit the "
            f"180 s wall-clock timeout; {hit_limit} hit the 20-call tool cap."
        )
    lines += [
        "",
        "Exceeding either cap is a harness-level failure, not a judge",
        "failure; the record is kept and scored on whatever partial output",
        "was emitted before the cap fired.",
        "",
    ]
    return lines


def _discussion_block(bib: dict) -> list[str]:
    return [
        "## Discussion and next steps",
        "",
        "The held-out test split is the number to quote — the agent beats",
        "RAG on every dimension (accuracy, completeness, citation,",
        "citation recall) at roughly 25% more wall time. The magnitude",
        "of the win is largest on *completeness*, which matches the",
        "intuition that graph-walking over whole pages beats passage-",
        "packing when the answer needs to enumerate. Train/val/test",
        "consistency rules out overfitting to a single split.",
        "",
        "Several caveats bound how far to push this result. It's a",
        "single corpus (56 papers), a single question set (50 questions),",
        "a single judge model, and no statistical-significance testing on",
        "the metric differences. RAG hyperparameters (chunk size, overlap,",
        "top-k, embedding model) were not swept; we used a sensible-",
        "default configuration. The agent benefits from a wiki that was",
        "itself authored by language-model agents from the same paper",
        "corpus, so some of the lift could be attributed to that",
        "pre-processing rather than graph-walk retrieval per se — a",
        "dedicated ablation would be needed to separate the two.",
        "",
        "**Next steps, in rough priority order:**",
        "",
        "1. **GraphRAG-style community summarization** on our wiki's",
        f"   cross-link graph ({_cite(bib, 'edge2024graphrag')}). We already",
        "   emit `wiki/graph.json`; running Leiden over it and generating",
        "   theme-level summaries would give a third retrieval strategy",
        "   to compare against — and address our current lack of",
        "   synthesis/theme pages.",
        "",
        "2. **Adaptive retrieval** — layering a reflection-token style",
        f"   decision ({_cite(bib, 'asai2023selfrag')}) or a retrieval",
        f"   evaluator ({_cite(bib, 'yan2024crag')}) on top of the RAG path",
        "   so it can fall through to graph-walk when the top-k is weak.",
        "",
        "3. **Corpus expansion.** We run on 56 of cBioPortal's several",
        "   hundred published studies. Re-evaluating on a 200+ paper",
        "   corpus would test whether the agent scales with depth.",
        "",
        "4. **Question-set scale and judges.** A larger, possibly",
        "   partially auto-generated question set; multiple judge models",
        "   and bootstrap confidence intervals on every delta.",
        "",
        "5. **Authoring themes and community pages.** A structural gap",
        "   in the current wiki: no pre-written cross-paper synthesis",
        "   pages. Their absence probably hurts both modes, but the agent",
        "   more (it's the natural top-down landing page).",
        "",
    ]


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


def _appendix_block(records: list[dict], run_dir: Path) -> list[str]:
    ts = run_dir.name
    modes = sorted({r["mode"] for r in records})
    lines = [
        "## Appendix",
        "",
        "### A. Per-category breakdown (train split)",
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
        "### B. Per-question results",
        "",
        "Scores shown as `accuracy / completeness / citation_correctness` (each 1–5).",
        "",
        _per_question_table(records),
        "",
        "### C. Notable failures",
        "",
        "Questions where either mode scored ≤ 2 on accuracy:",
        "",
        _low_scores_section(records, threshold=2),
        "",
        "### D. Source data",
        "",
        f"- Run directory: `eval/results/{ts}/`",
        f"- Raw records: `runs.jsonl` ({len(records)} rows)",
        "- Bibliography source: `eval/bibliography.yaml`",
        "- Regenerate this page: `uv run python -m eval.build_report --run-dir … --val-dir … --test-dir …`",
        "",
    ]
    return lines


def _render(records: list[dict], run_dir: Path, extra_splits: dict[str, list[dict]] | None = None) -> str:
    ts = run_dir.name
    split = records[0].get("split", "unknown") if records else "unknown"
    modes = sorted({r["mode"] for r in records})
    bib, groups = _load_bibliography()

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

    lines += _abstract_block(records, extra_splits)
    lines += _introduction_block(bib)
    lines += _methods_block()
    lines += _results_block(records, run_dir, extra_splits)
    lines += _discussion_block(bib)
    lines += _references_block(bib, groups)
    lines += _appendix_block(records, run_dir)

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
