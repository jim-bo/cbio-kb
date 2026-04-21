"""Render the visualization plots from an eval run.

Writes PNGs and an HTML snippet to ``wiki/experiments/plots/`` so the
Quarto report can embed them via plain markdown image references (plus
one raw-HTML fence for the interactive scatter).

Plots:

1. ``per_question_scatter.png`` / ``.html`` — agentic total-score vs
   RAG total-score per question; bubble size = max wall time; color =
   category. The HTML version is an interactive Plotly scatter whose
   hover tooltip carries the full question and both answers.
2. ``category_bars.png`` — grouped bar chart of metric × category × mode.
3. ``cost_quality.png`` — total judge score vs (tokens, wall time),
   both modes overlaid.

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

# Shared styling knobs. The plots are rendered at reduced width on the
# Quarto page; the sizes below are chosen to stay readable even when
# the PNG is scaled down to ~60% of its native width.
_TITLE_SIZE = 18
_LABEL_SIZE = 15
_TICK_SIZE = 13
_LEGEND_SIZE = 13
_ANNOT_SIZE = 12


def _apply_style(fig, *, title_size: int = _TITLE_SIZE,
                 label_size: int = _LABEL_SIZE,
                 tick_size: int = _TICK_SIZE) -> None:
    """Apply a consistent axis style across every axes in ``fig``.

    Bumps the text size hierarchy and drops the top/right spines so the
    plots read like a light-weight publication style rather than a
    debug dump.
    """
    for ax in fig.axes:
        if ax.get_title():
            ax.title.set_size(title_size)
            ax.title.set_weight("medium")
        if ax.get_xlabel():
            ax.xaxis.label.set_size(label_size)
        if ax.get_ylabel():
            ax.yaxis.label.set_size(label_size)
        ax.tick_params(axis="both", labelsize=tick_size)
        for side in ("top", "right"):
            if side in ax.spines:
                ax.spines[side].set_visible(False)
    # Make suptitles a touch bigger than panel titles.
    if fig._suptitle is not None:
        fig._suptitle.set_size(title_size + 1)
        fig._suptitle.set_weight("semibold")


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
    """Static scatter — per-question agentic vs RAG totals.

    The upper-right corner (easy lookup/definition questions) tends to
    pile up at (15, 15) because both modes ace those. A literal label
    there produces a ball of overlapping text. Instead we group every
    question stacked at a single integer grid cell and replace its
    per-dot labels with a single corner annotation like
    ``L01 L02 L03 D05 D06 (5)``.
    """
    by_id: dict[str, dict[str, dict]] = {}
    for r in records:
        by_id.setdefault(r["id"], {})[r["mode"]] = r

    points: list[dict] = []
    for qid, modes in sorted(by_id.items()):
        ag = modes.get("agentic", {})
        rg = modes.get("rag", {})
        ag_total = _total_score(ag)
        rg_total = _total_score(rg)
        if ag_total is None or rg_total is None:
            continue
        cat = (ag or rg).get("category", "unknown")
        wall = max(ag.get("wall_time_s", 0) or 0, rg.get("wall_time_s", 0) or 0)
        points.append({
            "qid": qid, "cat": cat, "ag": ag_total, "rg": rg_total, "wall": wall,
        })

    # Group labels by (rg, ag) grid cell so overlapping corner pileups
    # get a single compact annotation instead of N overlapping ones.
    by_cell: dict[tuple[int, int], list[str]] = defaultdict(list)
    for p in points:
        by_cell[(int(p["rg"]), int(p["ag"]))].append(p["qid"])

    fig, ax = plt.subplots(figsize=(11, 8.5))

    jitter_seed = 0
    for p in points:
        color = _CATEGORY_COLORS.get(p["cat"], "#888")
        size = 60 + (p["wall"] * 6)
        # Deterministic jitter so points at the same integer coords don't
        # hide each other.
        jitter_seed += 1
        jx = ((jitter_seed * 17) % 7 - 3) * 0.06
        jy = ((jitter_seed * 23) % 7 - 3) * 0.06
        ax.scatter(
            p["rg"] + jx, p["ag"] + jy,
            s=size, c=color, alpha=0.78, edgecolors="white", linewidths=1.0,
        )

    # Annotate each grid cell exactly once, avoiding text pileups. Near
    # the right/top edge of the plot we push labels left/down so they
    # don't run off; at large pileups we show a compact "n=K" badge
    # rather than listing every ID (hover on the interactive version
    # has the full detail).
    for (rg, ag), qids in by_cell.items():
        near_right = rg >= 14
        near_top = ag >= 14
        dx = -6 if near_right else 6
        dy = -10 if near_top else 4
        ha = "right" if near_right else "left"
        va = "top" if near_top else "bottom"
        if len(qids) == 1:
            ax.annotate(qids[0], (rg, ag),
                        xytext=(dx, dy), textcoords="offset points",
                        fontsize=_ANNOT_SIZE, color="#333", ha=ha, va=va)
        elif len(qids) <= 3:
            label = ", ".join(qids)
            ax.annotate(label, (rg, ag),
                        xytext=(dx, dy), textcoords="offset points",
                        fontsize=_ANNOT_SIZE, color="#333", ha=ha, va=va,
                        bbox=dict(boxstyle="round,pad=0.2",
                                  fc="#fff", ec="#ddd", alpha=0.85))
        else:
            # Compact pileup badge — avoids smearing 10 IDs across the corner.
            ax.annotate(f"n={len(qids)}", (rg, ag),
                        xytext=(dx, dy), textcoords="offset points",
                        fontsize=_ANNOT_SIZE + 1, color="#222",
                        ha=ha, va=va, weight="semibold",
                        bbox=dict(boxstyle="round,pad=0.25",
                                  fc="#f5f5f7", ec="#bbb", alpha=0.95))

    lo, hi = 2, 16
    ax.plot([lo, hi], [lo, hi], "--", color="#999", linewidth=1.1, zorder=0)
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_xlabel("RAG judge score (accuracy + completeness + citation)")
    ax.set_ylabel("Agentic judge score")
    ax.set_title("Per-question judge score, agentic vs RAG\n(bubble size ∝ max wall time)")

    legend_handles = [
        plt.Line2D([0], [0], marker="o", color="w", label=cat,
                   markerfacecolor=c, markersize=10)
        for cat, c in _CATEGORY_COLORS.items()
    ]
    ax.legend(handles=legend_handles, loc="lower right", frameon=True,
              framealpha=0.9, title="category", fontsize=_LEGEND_SIZE,
              title_fontsize=_LEGEND_SIZE)
    ax.grid(True, alpha=0.2)
    _apply_style(fig)
    fig.tight_layout()
    fig.savefig(out, dpi=150)
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
    """Grouped bar chart — mean judge score per (mode × category × metric).

    Value labels sit *above* each bar, with left/right horizontal
    alignment keyed to the mode so adjacent labels don't overlap when
    both bars are near the ceiling.
    """
    categories = ["lookup", "list", "synthesis", "definition"]
    metrics = [("accuracy", "Accuracy"), ("completeness", "Completeness"),
               ("citation_correctness", "Citation")]
    modes = ["agentic", "rag"]
    ha_by_mode = {"agentic": "right", "rag": "left"}

    by_mode_cat: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in records:
        if r.get("mode") in modes and r.get("category") in categories:
            by_mode_cat[(r["mode"], r["category"])].append(r)

    fig, axes = plt.subplots(1, 3, figsize=(14, 5.4), sharey=True)
    width = 0.38
    x = list(range(len(categories)))

    legend_handles: list = []
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
                          label=mode.title(), color=_MODE_COLORS[mode],
                          alpha=0.9, edgecolor="white", linewidth=0.8)
            if not legend_handles and ax is axes[0]:
                # Capture handle on first axis; reuse as figure-level legend.
                pass
            for bar, v in zip(bars, vals):
                if v > 0:
                    # Lean the label left (agentic) or right (rag) so two
                    # near-equal bars don't collide in the centre.
                    label_x = bar.get_x() + (bar.get_width() * 0.85
                                             if ha_by_mode[mode] == "right"
                                             else bar.get_width() * 0.15)
                    ax.text(label_x, v + 0.12, f"{v:.1f}",
                            ha=ha_by_mode[mode], va="bottom",
                            fontsize=_ANNOT_SIZE, color="#222")

        ax.set_xticks(x)
        ax.set_xticklabels(categories, rotation=0)
        ax.set_title(metric_label)
        ax.set_ylim(0, 5.8)
        ax.grid(True, alpha=0.25, axis="y")

    axes[0].set_ylabel("Mean judge score (1–5)")
    # Legend as a figure-level strip, above the panels — never overlaps
    # the bars regardless of how tall the tallest bar is.
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(
        handles, labels,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.93),
        ncol=len(labels),
        frameon=False,
        fontsize=_LEGEND_SIZE,
    )
    fig.suptitle("Mean judge score by question category", y=0.995)
    _apply_style(fig)
    # Reserve the top ~14% of the figure for suptitle + legend.
    fig.tight_layout(rect=[0, 0, 1, 0.88])
    fig.savefig(out, dpi=150)
    plt.close(fig)


def plot_cost_quality(records: list[dict], out: Path) -> None:
    """Total judge score as a function of input tokens (left) and wall
    time (right). Both modes overlaid so the frontier is visible.
    """
    fig, axes = plt.subplots(1, 2, figsize=(15, 6), sharey=True)

    panels = [
        ("input_tokens", "Input tokens per query (log scale)", True,
         "Input cost"),
        ("wall_time_s", "Wall time per query (s)", False,
         "Latency"),
    ]

    for ax, (xkey, xlabel, xlog, panel_title) in zip(axes, panels):
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
                ax.scatter(xs, ys, c=color, alpha=0.7, s=80,
                           edgecolors="white", linewidths=0.8,
                           label=mode.title())
        ax.set_xlabel(xlabel)
        ax.set_title(panel_title)
        if xlog:
            ax.set_xscale("log")
        ax.grid(True, alpha=0.25)

    axes[0].set_ylabel("Total judge score (3–15)")
    # Figure-level legend above the panels, same pattern as category_bars.
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(
        handles, labels,
        loc="upper center",
        bbox_to_anchor=(0.5, 0.93),
        ncol=len(labels),
        frameon=False,
        fontsize=_LEGEND_SIZE,
    )
    fig.suptitle("Cost vs quality: what does each mode buy you?", y=0.995)
    _apply_style(fig)
    fig.tight_layout(rect=[0, 0, 1, 0.88])
    fig.savefig(out, dpi=150)
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
