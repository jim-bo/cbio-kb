"""Check that the ONNX Runtime backend reproduces PyTorch for the search models.

The server images run the embedding model and the reranker on ONNX Runtime
(``cbio_kb.index.onnx_models``), while indexes are usually built with
sentence-transformers on PyTorch. The two must agree, or queries embedded in
production won't match the index. Run this after changing either model:

    uv run --extra chat --extra server python eval/onnx_parity.py
    uv run ... python eval/onnx_parity.py --embed-model BAAI/bge-base-en-v1.5

It embeds the eval questions (as queries) and a sample of passage-index chunks
(as documents) on both backends and compares cosine similarity, then scores
question/chunk pairs with the reranker on both and compares the scores.
Exits non-zero if they disagree beyond the tolerances.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))


def main(argv: list[str] | None = None) -> int:
    from ai_search import hybrid, router
    from cbio_kb.index import embed, onnx_models

    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--embed-model", default=embed.index_model(REPO / "data/paper_index",
                                                               default=embed.DEFAULT_MODEL))
    ap.add_argument("--rerank-model", default=hybrid._RERANKER_MODEL)
    ap.add_argument("--index-dir", default=str(REPO / "data/paper_index"))
    ap.add_argument("--min-cosine", type=float, default=0.9999)
    ap.add_argument("--max-score-diff", type=float, default=1e-3)
    args = ap.parse_args(argv)

    questions = [q["question"] for q in router._load_questions()]
    meta_path = Path(args.index_dir) / "meta.jsonl"
    with meta_path.open(encoding="utf-8") as fh:
        chunks = [json.loads(line)["text"] for line in fh]
    docs = chunks[:: max(1, len(chunks) // 50)][:50]

    def both(kind: str, texts: list[str]) -> tuple[np.ndarray, np.ndarray]:
        os.environ["CBIO_EMBED_BACKEND"] = "torch"
        t = embed.embed(texts, kind=kind, model=args.embed_model)
        os.environ["CBIO_EMBED_BACKEND"] = "onnx"
        return t, embed.embed(texts, kind=kind, model=args.embed_model)

    ok = True
    for kind, texts in (("query", questions), ("document", docs)):
        t, o = both(kind, texts)
        cos = (t * o).sum(axis=1) / (np.linalg.norm(t, axis=1) * np.linalg.norm(o, axis=1))
        ok &= bool(cos.min() >= args.min_cosine)
        print(f"{args.embed_model} {kind:8} n={len(texts):3}  min cosine {cos.min():.6f}")

    from sentence_transformers import CrossEncoder

    pairs = [(q, d) for q in questions[:10] for d in docs[:10]]
    torch_scores = np.asarray(CrossEncoder(args.rerank_model).predict(pairs), dtype="float32")
    onnx_scores = np.concatenate([
        onnx_models.rerank(args.rerank_model, q, [d for qq, d in pairs if qq == q])
        for q in questions[:10]
    ])
    diff = float(np.abs(torch_scores - onnx_scores).max())
    ok &= diff <= args.max_score_diff
    print(f"{args.rerank_model} rerank  n={len(pairs)}  max |score diff| {diff:.6f}")
    print("parity OK" if ok else "PARITY FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
