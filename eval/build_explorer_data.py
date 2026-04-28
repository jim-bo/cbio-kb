"""Emit per-question JSON for the traversal explorer.

For every question that has both agentic and RAG records in the run, write
``wiki/experiments/explorer/{qid}.json`` with a compact summary: the
question text, gold PMIDs, per-mode scores, and the behavior shape each
mode produced (agentic timeline, RAG retrieval). A sibling
``index.json`` lists the available questions so the explorer page can
populate its picker without scanning.

Usage:

    uv run python -m eval.build_explorer_data
    uv run python -m eval.build_explorer_data --run-dir eval/results/2026-04-19-1757
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

_EVAL_DIR = Path(__file__).resolve().parent
_RESULTS_DIR = _EVAL_DIR / "results"
_QUESTIONS_PATH = _EVAL_DIR / "questions" / "v1.yaml"
_OUT_DIR = _EVAL_DIR.parent / "wiki" / "experiments" / "explorer"


def _latest_run_dir() -> Path:
    dirs = sorted(p for p in _RESULTS_DIR.iterdir() if p.is_dir() and (p / "runs.jsonl").exists())
    if not dirs:
        print(f"[!] no eval runs in {_RESULTS_DIR}", file=sys.stderr)
        sys.exit(1)
    return dirs[-1]


def _load_runs(run_dir: Path) -> list[dict]:
    return [json.loads(line) for line in (run_dir / "runs.jsonl").read_text().splitlines() if line.strip()]


def _load_questions() -> dict[str, dict]:
    data = yaml.safe_load(_QUESTIONS_PATH.read_text())
    return {q["id"]: q for q in data["questions"]}


def _answer_preview(text: str, limit: int = 1200) -> str:
    text = (text or "").strip()
    return text if len(text) <= limit else text[:limit].rstrip() + "…"


def _agentic_summary(rec: dict) -> dict:
    timeline = []
    for ev in rec.get("tool_timeline") or []:
        timeline.append({
            "name": ev.get("name"),
            "args": ev.get("args") or {},
            "t_start": round(float(ev.get("t_start") or 0), 3),
            "t_end": round(float(ev.get("t_end") or 0), 3),
            "chars": int(ev.get("chars") or 0),
            "summary": ev.get("summary"),
        })
    answer = (rec.get("answer") or "").strip()
    return {
        "answer": answer,
        "answer_preview": _answer_preview(answer),
        "cited_pmids": list(rec.get("cited_pmids") or []),
        "scores": rec.get("scores") or {},
        "wall_time_s": rec.get("wall_time_s"),
        "input_tokens": rec.get("input_tokens"),
        "output_tokens": rec.get("output_tokens"),
        "tool_uses": rec.get("tool_uses", 0),
        "timed_out": bool(rec.get("timed_out")),
        "tool_limit_reached": bool(rec.get("tool_limit_reached")),
        "timeline": timeline,
    }


def _rag_summary(rec: dict) -> dict:
    retrieval = []
    for r in rec.get("retrieval") or []:
        retrieval.append({
            "pmid": str(r.get("pmid", "")),
            "chunk_id": r.get("chunk_id"),
            "score": round(float(r.get("score") or 0), 4),
            "path": r.get("path") or (f"papers/{r.get('pmid')}.md" if r.get("pmid") else None),
            "chars": r.get("chars"),
        })
    answer = (rec.get("answer") or "").strip()
    return {
        "answer": answer,
        "answer_preview": _answer_preview(answer),
        "cited_pmids": list(rec.get("cited_pmids") or []),
        "scores": rec.get("scores") or {},
        "wall_time_s": rec.get("wall_time_s"),
        "input_tokens": rec.get("input_tokens"),
        "output_tokens": rec.get("output_tokens"),
        "retrieval": retrieval,
    }


def build(run_dir: Path, out_dir: Path) -> list[dict]:
    records = _load_runs(run_dir)
    questions = _load_questions()

    by_id: dict[str, dict[str, dict]] = {}
    for r in records:
        by_id.setdefault(r["id"], {})[r["mode"]] = r

    out_dir.mkdir(parents=True, exist_ok=True)
    index: list[dict] = []

    for qid in sorted(by_id.keys()):
        modes = by_id[qid]
        q = questions.get(qid, {})
        # Prefer the canonical question text from questions/v1.yaml so
        # editing the source picks up on the next regenerate even when
        # the underlying run records still have the old text baked in.
        run_question = (modes.get("agentic") or modes.get("rag") or {}).get("question", "").strip()
        canonical = (q.get("question") or "").strip()
        payload = {
            "id": qid,
            "category": (modes.get("agentic") or modes.get("rag") or {}).get("category", "—"),
            "split": (modes.get("agentic") or modes.get("rag") or {}).get("split", "—"),
            "question": canonical or run_question,
            "gold_pmids": [str(p) for p in (q.get("gold_pmids") or [])],
            "gold_notes": q.get("notes", ""),
            "run_id": run_dir.name,
            "agentic": _agentic_summary(modes["agentic"]) if "agentic" in modes else None,
            "rag": _rag_summary(modes["rag"]) if "rag" in modes else None,
        }
        (out_dir / f"{qid}.json").write_text(json.dumps(payload))

        index.append({
            "id": qid,
            "category": payload["category"],
            "question": payload["question"],
            "has_agentic": payload["agentic"] is not None,
            "has_rag": payload["rag"] is not None,
            "agentic_total": _total(modes.get("agentic")),
            "rag_total": _total(modes.get("rag")),
        })

    (out_dir / "index.json").write_text(json.dumps({
        "run_id": run_dir.name,
        "questions": index,
    }, indent=2))

    print(f"[*] wrote {len(index)} questions to {out_dir}")
    return index


def _total(rec: dict | None) -> int | None:
    if not rec:
        return None
    s = rec.get("scores") or {}
    keys = ("accuracy", "completeness", "citation_correctness")
    if not all(k in s for k in keys):
        return None
    return sum(s[k] for k in keys)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build per-question explorer data")
    p.add_argument("--run-dir", type=Path, default=None, help="Path to eval/results/{ts}/")
    p.add_argument("--out-dir", type=Path, default=_OUT_DIR, help="Where to write JSON files")
    args = p.parse_args(argv)
    build(args.run_dir or _latest_run_dir(), args.out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
