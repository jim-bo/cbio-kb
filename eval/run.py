"""End-to-end eval runner: questions → runners → judge → results/.

Usage:
    uv run python -m eval.run --split train --mode both
    uv run python -m eval.run --split val --mode rag --no-judge
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from statistics import mean

import yaml

from .judge import judge
from .runners import agentic, rag

_EVAL_DIR = Path(__file__).resolve().parent
_QUESTIONS_PATH = _EVAL_DIR / "questions" / "v1.yaml"

RUNNERS = {
    "agentic": agentic.run,
    "rag": rag.run,
}


def load_questions(split: str | None = None) -> list[dict]:
    data = yaml.safe_load(_QUESTIONS_PATH.read_text())
    qs = data["questions"]
    if split:
        qs = [q for q in qs if q["split"] == split]
    return qs


def run_eval(
    split: str,
    modes: list[str],
    do_judge: bool = True,
    api_base: str = "http://localhost:8080",
    ids: list[str] | None = None,
) -> Path:
    questions = load_questions(split)
    if ids:
        wanted = {i.strip() for i in ids}
        questions = [q for q in questions if q["id"] in wanted]
    if not questions:
        print(f"[!] no questions for split={split} ids={ids}", file=sys.stderr)
        sys.exit(1)

    ts = datetime.now().strftime("%Y-%m-%d-%H%M")
    out_dir = _EVAL_DIR / "results" / ts
    out_dir.mkdir(parents=True, exist_ok=True)

    runs_path = out_dir / "runs.jsonl"
    all_records: list[dict] = []

    total = len(questions) * len(modes)
    idx = 0

    for q in questions:
        for mode in modes:
            idx += 1
            qid = q["id"]
            print(f"[{idx}/{total}] {qid} ({mode})… ", end="", flush=True)

            try:
                result = RUNNERS[mode](q["question"], api_base=api_base)
            except Exception as e:
                print(f"ERROR: {e}")
                result = {
                    "mode": mode,
                    "question": q["question"],
                    "answer": "",
                    "cited_pmids": [],
                    "error": str(e),
                }

            record = {
                "id": qid,
                "category": q["category"],
                "split": q["split"],
                **result,
            }

            if do_judge and result.get("answer"):
                print("judging… ", end="", flush=True)
                try:
                    scores = judge(q, result)
                    record["scores"] = scores
                except Exception as e:
                    print(f"judge error: {e}")
                    record["scores"] = {"error": str(e)}

            # citation recall vs gold
            gold = set(str(p) for p in q.get("gold_pmids", []))
            cited = set(result.get("cited_pmids", []))
            if gold:
                record["citation_recall"] = round(len(cited & gold) / len(gold), 3)
                record["citation_precision"] = round(
                    len(cited & gold) / len(cited), 3
                ) if cited else 0.0

            all_records.append(record)
            with runs_path.open("a") as fh:
                fh.write(json.dumps(record, ensure_ascii=False) + "\n")

            score_str = ""
            if "scores" in record and "accuracy" in record.get("scores", {}):
                s = record["scores"]
                score_str = f" acc={s['accuracy']} comp={s['completeness']} cite={s['citation_correctness']}"
            print(f"done ({result.get('wall_time_s', '?')}s){score_str}")

    print(f"\n[*] wrote {len(all_records)} records to {runs_path}")

    if do_judge:
        report_path = out_dir / "report.md"
        _write_report(all_records, modes, report_path)
        print(f"[*] wrote report to {report_path}")

    return out_dir


def _write_report(records: list[dict], modes: list[str], path: Path) -> None:
    lines = ["# Eval Report\n"]

    for mode in modes:
        mode_recs = [r for r in records if r.get("mode") == mode and "scores" in r]
        if not mode_recs:
            continue
        lines.append(f"\n## {mode.title()} mode ({len(mode_recs)} questions)\n")

        for dim in ("accuracy", "completeness", "citation_correctness"):
            vals = [r["scores"][dim] for r in mode_recs if dim in r.get("scores", {})]
            if vals:
                lines.append(f"- **{dim}**: {mean(vals):.2f} (min={min(vals)}, max={max(vals)})")

        recalls = [r["citation_recall"] for r in mode_recs if "citation_recall" in r]
        if recalls:
            lines.append(f"- **citation_recall**: {mean(recalls):.3f}")

        def _nums(key: str) -> list[float]:
            return [r[key] for r in mode_recs
                    if isinstance(r.get(key), (int, float))]

        tokens_in = _nums("input_tokens")
        tokens_out = _nums("output_tokens")
        times = _nums("wall_time_s")
        if tokens_in:
            lines.append(f"- **avg input_tokens**: {mean(tokens_in):.0f}")
        if tokens_out:
            lines.append(f"- **avg output_tokens**: {mean(tokens_out):.0f}")
        if times:
            lines.append(f"- **avg wall_time_s**: {mean(times):.1f}")

        lines.append("\n### Per-category breakdown\n")
        lines.append("| category | n | accuracy | completeness | cite_correct | recall |")
        lines.append("|----------|---|----------|--------------|--------------|--------|")
        for cat in ("lookup", "list", "synthesis", "definition"):
            cat_recs = [r for r in mode_recs if r.get("category") == cat]
            if not cat_recs:
                continue
            acc_vals = [r["scores"]["accuracy"] for r in cat_recs
                        if isinstance(r.get("scores"), dict) and "accuracy" in r["scores"]]
            comp_vals = [r["scores"]["completeness"] for r in cat_recs
                         if isinstance(r.get("scores"), dict) and "completeness" in r["scores"]]
            cite_vals = [r["scores"]["citation_correctness"] for r in cat_recs
                         if isinstance(r.get("scores"), dict) and "citation_correctness" in r["scores"]]
            rec_vals = [r["citation_recall"] for r in cat_recs
                        if isinstance(r.get("citation_recall"), (int, float))]
            if not (acc_vals and comp_vals and cite_vals):
                continue
            n = len(cat_recs)
            acc = mean(acc_vals)
            comp = mean(comp_vals)
            cite = mean(cite_vals)
            rec = mean(rec_vals) if rec_vals else 0.0
            lines.append(f"| {cat} | {n} | {acc:.2f} | {comp:.2f} | {cite:.2f} | {rec:.3f} |")

    path.write_text("\n".join(lines) + "\n")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Run RAG-vs-agentic evaluation")
    p.add_argument("--split", default="train", choices=["train", "val", "test", "all"])
    p.add_argument("--mode", default="both", choices=["agentic", "rag", "both"])
    p.add_argument("--no-judge", action="store_true")
    p.add_argument("--api-base", default="http://localhost:8080")
    p.add_argument("--ids", default=None, help="Comma-separated question IDs to run (overrides split filter)")
    args = p.parse_args(argv)

    modes = ["agentic", "rag"] if args.mode == "both" else [args.mode]
    ids = [i for i in args.ids.split(",") if i.strip()] if args.ids else None
    # --ids searches across all splits; --split is ignored when ids are given
    split = None if (args.split == "all" or ids) else args.split

    run_eval(
        split=split,
        modes=modes,
        do_judge=not args.no_judge,
        api_base=args.api_base,
        ids=ids,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
