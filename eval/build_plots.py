"""Render the four visualization plots from an eval run.

Writes PNGs to ``wiki/experiments/plots/{plot_name}.png`` so the Quarto
site can embed them via plain markdown image references.

Plots:

1. ``per_question_scatter.png`` — agentic total-score vs RAG total-score
   per question; bubble size = max wall time; color = category.
2. ``category_bars.png`` — grouped bar chart of metric × category × mode.
3. ``cost_quality.png`` — accuracy vs (tokens, wall time), both modes
   overlaid.
4. ``strategy_strip.png`` — side-by-side "what did each mode look at" for
   one sample question: agentic tool-call gantt vs RAG top-k chunks bar.

Usage:

    uv run python -m eval.build_plots
    uv run python -m eval.build_plots --run-dir eval/results/2026-04-19-1757
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import html

import matplotlib.pyplot as plt
import plotly.graph_objects as go

_EVAL_DIR = Path(__file__).resolve().parent
_RESULTS_DIR = _EVAL_DIR / "results"
_PLOTS_DIR = _EVAL_DIR.parent / "wiki" / "experiments" / "plots"

_CATEGORY_COLORS = {
    "lookup": "#4C78A8",
    "list": "#F58518",
    "synthesis": "#E45756",
    "definition": "#54A24B",
}
_MODE_COLORS = {"agentic": "#4C78A8", "rag": "#E45756"}


def _latest_run_dir() -> Path:
    dirs = sorted(p for p in _RESULTS_DIR.iterdir() if p.is_dir() and (p / "runs.jsonl").exists())
    if not dirs:
        print(f"[!] no eval runs found in {_RESULTS_DIR}", file=sys.stderr)
        sys.exit(1)
    return dirs[-1]


def _load_runs(run_dir: Path) -> list[dict]:
    return [json.loads(line) for line in (run_dir / "runs.jsonl").read_text().splitlines() if line.strip()]


def _total_score(rec: dict) -> int | None:
    s = rec.get("scores") or {}
    keys = ("accuracy", "completeness", "citation_correctness")
    if not all(k in s for k in keys):
        return None
    return sum(s[k] for k in keys)


def plot_per_question_scatter(records: list[dict], out: Path) -> None:
    by_id: dict[str, dict[str, dict]] = {}
    for r in records:
        by_id.setdefault(r["id"], {})[r["mode"]] = r

    fig, ax = plt.subplots(figsize=(8.5, 7))
    jitter_seed = 0

    for qid, modes in sorted(by_id.items()):
        ag = modes.get("agentic", {})
        rg = modes.get("rag", {})
        ag_total = _total_score(ag)
        rg_total = _total_score(rg)
        if ag_total is None or rg_total is None:
            continue
        cat = (ag or rg).get("category", "unknown")
        color = _CATEGORY_COLORS.get(cat, "#888")
        wall = max(ag.get("wall_time_s", 0) or 0, rg.get("wall_time_s", 0) or 0)
        size = 40 + (wall * 6)

        # Nudge overlapping points apart with deterministic per-id jitter.
        jitter_seed += 1
        jx = ((jitter_seed * 17) % 7 - 3) * 0.04
        jy = ((jitter_seed * 23) % 7 - 3) * 0.04

        ax.scatter(
            rg_total + jx, ag_total + jy,
            s=size, c=color, alpha=0.75, edgecolors="white", linewidths=0.8,
        )
        ax.annotate(qid, (rg_total + jx, ag_total + jy),
                    xytext=(5, 3), textcoords="offset points",
                    fontsize=7, color="#333")

    lo, hi = 2, 16
    ax.plot([lo, hi], [lo, hi], "--", color="#999", linewidth=1, zorder=0)
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_xlabel("RAG total score  (accuracy + completeness + citation)")
    ax.set_ylabel("Agentic total score")
    ax.set_title("Per-question scores: agentic vs RAG\n(bubble size ∝ wall time)")

    legend_handles = [
        plt.Line2D([0], [0], marker="o", color="w", label=cat,
                   markerfacecolor=c, markersize=8)
        for cat, c in _CATEGORY_COLORS.items()
    ]
    ax.legend(handles=legend_handles, loc="lower right", frameon=False, title="category")
    ax.grid(True, alpha=0.2)
    fig.tight_layout()
    fig.savefig(out, dpi=140)
    plt.close(fig)


def _wrap(text: str, width: int = 90, limit: int = 900) -> str:
    """Escape + soft-wrap for Plotly hover tooltips (they honor <br>)."""
    text = (text or "").strip().replace("\r", "")
    if len(text) > limit:
        text = text[:limit].rstrip() + "…"
    text = html.escape(text)
    out: list[str] = []
    for para in text.split("\n"):
        while len(para) > width:
            cut = para.rfind(" ", 0, width)
            if cut == -1:
                cut = width
            out.append(para[:cut])
            para = para[cut:].lstrip()
        out.append(para)
    return "<br>".join(out)


def plot_per_question_scatter_interactive(records: list[dict], out: Path) -> None:
    """Interactive scatter — hover reveals question, both answers, and scores."""
    by_id: dict[str, dict[str, dict]] = {}
    for r in records:
        by_id.setdefault(r["id"], {})[r["mode"]] = r

    categories = list(_CATEGORY_COLORS.keys())
    per_cat: dict[str, dict[str, list]] = {
        cat: {"x": [], "y": [], "size": [], "ids": [], "hover": []}
        for cat in categories
    }

    for qid, modes in sorted(by_id.items()):
        ag = modes.get("agentic", {})
        rg = modes.get("rag", {})
        ag_total = _total_score(ag)
        rg_total = _total_score(rg)
        if ag_total is None or rg_total is None:
            continue
        cat = (ag or rg).get("category", "unknown")
        if cat not in per_cat:
            continue

        ag_scores = ag.get("scores", {})
        rg_scores = rg.get("scores", {})
        ag_wall = ag.get("wall_time_s") or 0
        rg_wall = rg.get("wall_time_s") or 0
        question = (ag.get("question") or rg.get("question") or "").strip()
        ag_answer = (ag.get("answer") or "").strip()
        rg_answer = (rg.get("answer") or "").strip()

        hover = (
            f"<b>{qid} · {cat}</b>"
            f"<br><b>Q:</b> {_wrap(question, limit=400)}"
            f"<br><br><b>Agentic</b> "
            f"acc={ag_scores.get('accuracy', '—')} "
            f"comp={ag_scores.get('completeness', '—')} "
            f"cite={ag_scores.get('citation_correctness', '—')} "
            f"· {ag_wall:.1f}s"
            f"<br>{_wrap(ag_answer)}"
            f"<br><br><b>RAG</b> "
            f"acc={rg_scores.get('accuracy', '—')} "
            f"comp={rg_scores.get('completeness', '—')} "
            f"cite={rg_scores.get('citation_correctness', '—')} "
            f"· {rg_wall:.1f}s"
            f"<br>{_wrap(rg_answer)}"
        )

        wall = max(ag_wall, rg_wall)
        per_cat[cat]["x"].append(rg_total)
        per_cat[cat]["y"].append(ag_total)
        per_cat[cat]["size"].append(10 + wall * 0.7)
        per_cat[cat]["ids"].append(qid)
        per_cat[cat]["hover"].append(hover)

    fig = go.Figure()
    for cat in categories:
        d = per_cat[cat]
        if not d["x"]:
            continue
        fig.add_trace(go.Scatter(
            x=d["x"], y=d["y"],
            mode="markers+text",
            text=d["ids"],
            textposition="top center",
            textfont=dict(size=9, color="#444"),
            marker=dict(
                size=d["size"],
                color=_CATEGORY_COLORS[cat],
                opacity=0.75,
                line=dict(color="white", width=1),
            ),
            name=cat,
            hovertext=d["hover"],
            hoverinfo="text",
            hoverlabel=dict(bgcolor="white", font_size=11, align="left"),
        ))

    # y = x reference line
    fig.add_shape(
        type="line", x0=2, y0=2, x1=16, y1=16,
        line=dict(color="#999", width=1, dash="dash"),
        layer="below",
    )

    fig.update_layout(
        title="Per-question scores: agentic vs RAG<br><sup>bubble size ∝ max wall time · hover for question + answers</sup>",
        xaxis=dict(title="RAG total score (accuracy + completeness + citation)", range=[2, 16], gridcolor="#eee"),
        yaxis=dict(title="Agentic total score", range=[2, 16], gridcolor="#eee"),
        plot_bgcolor="white",
        height=620,
        legend=dict(title="category", yanchor="bottom", y=0.02, xanchor="right", x=0.98, bgcolor="rgba(255,255,255,0.8)"),
        margin=dict(l=60, r=30, t=80, b=60),
    )

    snippet = fig.to_html(
        include_plotlyjs="cdn",
        full_html=False,
        div_id="per-question-scatter",
        config={"displaylogo": False, "responsive": True},
    )
    out.write_text(snippet)


def plot_category_bars(records: list[dict], out: Path) -> None:
    categories = ["lookup", "list", "synthesis", "definition"]
    metrics = [("accuracy", "Accuracy"), ("completeness", "Completeness"),
               ("citation_correctness", "Citation")]
    modes = ["agentic", "rag"]

    by_mode_cat: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in records:
        if r.get("mode") in modes and r.get("category") in categories:
            by_mode_cat[(r["mode"], r["category"])].append(r)

    fig, axes = plt.subplots(1, 3, figsize=(13, 4.2), sharey=True)
    width = 0.38
    x = list(range(len(categories)))

    for ax, (metric_key, metric_label) in zip(axes, metrics):
        for j, mode in enumerate(modes):
            vals = []
            for cat in categories:
                recs = by_mode_cat.get((mode, cat), [])
                scored = [r["scores"][metric_key] for r in recs
                          if r.get("scores") and metric_key in r["scores"]]
                vals.append(sum(scored) / len(scored) if scored else 0)
            offset = (j - 0.5) * width
            bars = ax.bar([xi + offset for xi in x], vals, width,
                          label=mode, color=_MODE_COLORS[mode], alpha=0.85)
            for bar, v in zip(bars, vals):
                if v > 0:
                    ax.text(bar.get_x() + bar.get_width() / 2, v + 0.08,
                            f"{v:.1f}", ha="center", fontsize=7, color="#333")

        ax.set_xticks(x)
        ax.set_xticklabels(categories, rotation=20)
        ax.set_title(metric_label)
        ax.set_ylim(0, 5.5)
        ax.grid(True, alpha=0.2, axis="y")

    axes[0].set_ylabel("mean score (1–5)")
    axes[0].legend(loc="upper right", frameon=False)
    fig.suptitle("Per-category scores by mode", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(out, dpi=140)
    plt.close(fig)


def plot_cost_quality(records: list[dict], out: Path) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))

    for ax, (xkey, xlabel, xlog) in zip(
        axes,
        [("input_tokens", "Input tokens", True),
         ("wall_time_s", "Wall time (s)", False)],
    ):
        for mode, color in _MODE_COLORS.items():
            xs, ys = [], []
            for r in records:
                if r.get("mode") != mode:
                    continue
                total = _total_score(r)
                xv = r.get(xkey)
                if total is None or xv is None or xv <= 0:
                    continue
                xs.append(xv)
                ys.append(total)
            if xs:
                ax.scatter(xs, ys, c=color, alpha=0.65, s=50,
                           edgecolors="white", linewidths=0.6, label=mode)
        ax.set_xlabel(xlabel)
        ax.set_ylabel("Total score (3–15)")
        if xlog:
            ax.set_xscale("log")
        ax.grid(True, alpha=0.2)
        ax.legend(loc="lower right", frameon=False)

    fig.suptitle("Cost vs quality", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(out, dpi=140)
    plt.close(fig)


def _pick_sample_question(records: list[dict]) -> str | None:
    """Prefer a list question with both modes and a tool_timeline on the agentic record."""
    by_id: dict[str, dict[str, dict]] = {}
    for r in records:
        by_id.setdefault(r["id"], {})[r["mode"]] = r

    def has_data(rec: dict) -> bool:
        return bool(rec.get("tool_timeline") or rec.get("retrieval"))

    candidates = [
        qid for qid, modes in by_id.items()
        if "agentic" in modes and "rag" in modes
        and has_data(modes["agentic"]) and has_data(modes["rag"])
    ]
    if not candidates:
        return None
    # Prefer list / synthesis (more interesting traversals)
    def prio(qid: str) -> tuple[int, str]:
        cat = by_id[qid]["agentic"].get("category", "")
        order = {"list": 0, "synthesis": 1, "lookup": 2, "definition": 3}
        return (order.get(cat, 9), qid)
    return sorted(candidates, key=prio)[0]


def plot_strategy_strip(records: list[dict], out: Path) -> None:
    qid = _pick_sample_question(records)
    fig, axes = plt.subplots(2, 1, figsize=(12, 6.8),
                             gridspec_kw={"height_ratios": [1, 1]})
    if qid is None:
        for ax in axes:
            ax.text(0.5, 0.5,
                    "No run has both a tool_timeline (agentic) and retrieval (rag).\n"
                    "Re-run the eval after enabling the capture to populate this chart.",
                    ha="center", va="center", fontsize=11, color="#666")
            ax.axis("off")
        fig.tight_layout()
        fig.savefig(out, dpi=140)
        plt.close(fig)
        return

    by_id: dict[str, dict[str, dict]] = {}
    for r in records:
        by_id.setdefault(r["id"], {})[r["mode"]] = r
    ag = by_id[qid]["agentic"]
    rg = by_id[qid]["rag"]
    question = (ag.get("question") or rg.get("question") or "").strip().splitlines()[0][:110]

    def _short_detail(args: dict) -> str:
        val = args.get("path") or args.get("folder") or args.get("entity") or args.get("heading") or ""
        if val.startswith("papers/"):
            val = val[len("papers/"):]
        if val.endswith(".md"):
            val = val[:-3]
        return val

    # --- Top: agentic tool gantt ---
    ax = axes[0]
    timeline = ag.get("tool_timeline") or []
    y_labels = []
    for i, ev in enumerate(timeline):
        t0 = float(ev.get("t_start", 0) or 0)
        t1 = float(ev.get("t_end", 0) or 0)
        if t1 <= t0:
            t1 = t0 + 0.08  # zero-width → sliver for visibility
        name = ev.get("name", "?")
        detail = _short_detail(ev.get("args") or {})
        ax.barh(i, t1 - t0, left=t0, height=0.65,
                color=_MODE_COLORS["agentic"], alpha=0.85, edgecolor="white")
        y_labels.append(f"{name}({detail})" if detail else name)

    ax.set_yticks(list(range(len(timeline))))
    ax.set_yticklabels(y_labels, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("seconds since turn start")
    if timeline:
        ax.set_xlim(left=0)
    wall = ag.get("wall_time_s") or 0
    ax.set_title(f"Agentic — {qid} ({len(timeline)} tool calls, {wall:.1f}s total)")
    ax.grid(True, alpha=0.2, axis="x")

    # --- Bottom: RAG top-k bar ---
    ax = axes[1]
    retrieval = (rg.get("retrieval") or [])[:15]
    scores = [float(r.get("score", 0)) for r in retrieval]
    labels = [f"PMID:{r.get('pmid', '?')}  (chunk {r.get('chunk_id', '?')})"
              for r in retrieval]
    y_pos = list(range(len(retrieval)))
    ax.barh(y_pos, scores, color=_MODE_COLORS["rag"], alpha=0.85, edgecolor="white")
    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=8)
    ax.invert_yaxis()
    ax.set_xlabel("cosine similarity")
    if scores:
        ax.set_xlim(0, max(scores) * 1.05)
    ax.set_title(f"RAG — {qid} (top {len(retrieval)} chunks)")
    ax.grid(True, alpha=0.2, axis="x")

    fig.suptitle(f"Strategy side-by-side — “{question}”", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(out, dpi=140)
    plt.close(fig)


def render_all(run_dir: Path, out_dir: Path) -> list[Path]:
    records = _load_runs(run_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    outputs = []
    targets = [
        ("per_question_scatter", plot_per_question_scatter, "png"),
        ("per_question_scatter", plot_per_question_scatter_interactive, "html"),
        ("category_bars", plot_category_bars, "png"),
        ("cost_quality", plot_cost_quality, "png"),
        ("strategy_strip", plot_strategy_strip, "png"),
    ]
    for name, fn, ext in targets:
        path = out_dir / f"{name}.{ext}"
        fn(records, path)
        outputs.append(path)
        print(f"[*] wrote {path}")
    return outputs


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build plots for the rag-vs-agentic experiment")
    p.add_argument("--run-dir", type=Path, default=None, help="Path to eval/results/{ts}/")
    p.add_argument("--out-dir", type=Path, default=_PLOTS_DIR, help="Where to save PNGs")
    args = p.parse_args(argv)
    run_dir = args.run_dir or _latest_run_dir()
    render_all(run_dir, args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
