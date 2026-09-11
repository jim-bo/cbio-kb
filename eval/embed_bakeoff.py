"""Embedding-model bake-off for the passage index. No LLM calls, no cloud.

Every model embeds the same chunks (an existing index's ``meta.jsonl``), so
only the embeddings differ. For each of the eval's labeled questions we
check whether retrieval surfaces its gold papers (``gold_pmids`` in
eval/questions/v1.yaml):

- dense recall@8 / @40: share of gold papers among the papers of the top 8
  / top 40 chunks from dense search alone (40 is what the dense leg hands to
  hybrid fusion);
- dense MRR: reciprocal rank of the first gold paper;
- hybrid recall@8: the full hybrid pipeline (dense + BM25 + wiki graph,
  RRF-fused, cross-encoder reranked, max 2 passages per paper), i.e. what
  the MCP server's search_hybrid returns by default;
- router accuracy: leave-one-out kNN category accuracy over the labeled
  questions with the router's k and vote (the router embeds with the same
  model).

The Gemini baseline needs no Vertex call: chunk vectors come from a
Gemini-built FAISS index and question vectors from the router's cached Gemini
bank (``data/router_qbank.gemini.npz``, else ``router_qbank.npz``; same
questions, checked by fingerprint).
"no-dense" is hybrid with the dense leg off, i.e. the server's degraded mode.

    uv run --extra chat --extra server python eval/embed_bakeoff.py
    uv run ... python eval/embed_bakeoff.py --models BAAI/bge-base-en-v1.5
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from collections import defaultdict
from datetime import date
from pathlib import Path

import numpy as np
import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))

GEMINI = "gemini-embedding-001"
NO_DENSE = "no-dense (BM25 + graph)"
DEFAULT_MODELS = [
    "BAAI/bge-base-en-v1.5",
    "Snowflake/snowflake-arctic-embed-m-v1.5",
    "intfloat/e5-base-v2",
    "ncbi/MedCPT",
    "Qwen/Qwen3-Embedding-0.6B",
]
FINAL_K, MAX_PER_PAPER = 8, 2  # search_hybrid defaults


def load_questions() -> tuple[list[dict], str]:
    from ai_search import router

    qs = router._load_questions()
    raw = yaml.safe_load((REPO / "eval/questions/v1.yaml").read_text())["questions"]
    gold = {q["id"]: {str(p) for p in q.get("gold_pmids", [])} for q in raw}
    for q in qs:
        q["gold"] = gold[q["id"]]
    return qs, router._fingerprint(qs)


def top_pmids(chunk_idx, meta: list[dict], k: int) -> set[str]:
    return {meta[i]["pmid"] for i in chunk_idx[:k]}


def recall(found: set[str], gold: set[str]) -> float:
    return len(found & gold) / len(gold) if gold else 0.0


def mrr(chunk_idx, meta: list[dict], gold: set[str]) -> float:
    seen: list[str] = []
    for i in chunk_idx:
        p = meta[i]["pmid"]
        if p not in seen:
            seen.append(p)
            if p in gold:
                return 1.0 / len(seen)
    return 0.0


def capped_pmids(passages: list[dict]) -> set[str]:
    per: dict[str, int] = defaultdict(int)
    out: list[str] = []
    for p in passages:
        if per[p["pmid"]] < MAX_PER_PAPER:
            per[p["pmid"]] += 1
            out.append(p["pmid"])
        if len(out) == FINAL_K:
            break
    return set(out)


def router_loo_accuracy(queries: np.ndarray, qs: list[dict]) -> float:
    """Leave-one-out accuracy of the router's similarity-weighted kNN vote."""
    from ai_search.router import _DEFAULT_K

    cats = [q["category"] for q in qs]
    q = queries / np.linalg.norm(queries, axis=1, keepdims=True)
    sims = q @ q.T
    np.fill_diagonal(sims, -np.inf)
    hits = 0
    for i in range(len(qs)):
        votes: dict[str, float] = defaultdict(float)
        for j in np.argsort(-sims[i])[:_DEFAULT_K]:
            votes[cats[j]] += max(float(sims[i, j]), 0.0)
        hits += max(votes, key=votes.get) == cats[i]
    return round(hits / len(qs), 3)


def model_vectors(model: str, texts: list[str], qtexts: list[str], index_dir: Path,
                  cache: Path, fingerprint: str) -> tuple[np.ndarray, np.ndarray, dict]:
    """(doc_vecs, query_vecs, timing) for one model, caching doc vectors."""
    if model == GEMINI:
        import faiss

        idx = faiss.read_index(str(index_dir / "faiss.index"))
        docs = idx.reconstruct_n(0, idx.ntotal)
        # The router's Gemini question vectors; router_qbank.gemini.npz keeps a
        # copy once the router has switched to a local model.
        qb_path = REPO / "data/router_qbank.gemini.npz"
        qb = np.load(qb_path if qb_path.exists() else REPO / "data/router_qbank.npz", allow_pickle=False)
        if str(qb["fingerprint"]) != fingerprint:
            raise SystemExit("router_qbank.npz is stale for the current questions; can't score Gemini offline")
        return docs, qb["embeddings"].astype("float32"), {}
    from cbio_kb.index import embed

    slug = model.replace("/", "__")
    doc_path = cache / f"{slug}.docs.npy"
    timing: dict = {}
    if doc_path.exists():
        docs = np.load(doc_path)
    else:
        t0 = time.perf_counter()
        docs = embed.embed(texts, kind="document", model=model)
        timing["doc_chunks_per_s"] = round(len(texts) / (time.perf_counter() - t0), 1)
        np.save(doc_path, docs)
    t0 = time.perf_counter()
    queries = embed.embed(qtexts, kind="query", model=model, batch_size=1)
    timing["query_ms"] = round(1000 * (time.perf_counter() - t0) / len(qtexts), 1)
    return docs, queries, timing


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--index-dir", default=str(REPO / "data/paper_index"))
    ap.add_argument("--models", nargs="*", default=[GEMINI, *DEFAULT_MODELS])
    ap.add_argument("--cache-dir", default=str(REPO / "data/tmp/bakeoff"))
    ap.add_argument("--out-dir", default=str(REPO / "eval/results/embed_bakeoff"))
    ap.add_argument("--no-hybrid", action="store_true")
    args = ap.parse_args(argv)

    index_dir, cache = Path(args.index_dir), Path(args.cache_dir)
    cache.mkdir(parents=True, exist_ok=True)
    meta = [json.loads(line) for line in open(index_dir / "meta.jsonl", encoding="utf-8")]
    texts = [m["text"] for m in meta]
    qs, fingerprint = load_questions()
    qtexts = [q["question"] for q in qs]
    print(f"[bakeoff] {len(meta)} chunks from {len({m['pmid'] for m in meta})} papers; {len(qs)} questions")

    import ai_search.hybrid as hybrid

    results: dict[str, dict] = {}
    variants = list(args.models) + ([] if args.no_hybrid else [NO_DENSE])
    for model in variants:
        print(f"[bakeoff] {model}", flush=True)
        row: dict = {"per_q": {}}
        ranked: dict[str, list[int]] = {}
        if model != NO_DENSE:
            docs, queries, timing = model_vectors(model, texts, qtexts, index_dir, cache, fingerprint)
            row.update(timing, dim=int(docs.shape[1]), router_acc=router_loo_accuracy(queries, qs))
            order = np.argsort(-(queries @ docs.T), axis=1)[:, :100]
            for q, idx in zip(qs, order):
                ranked[q["question"]] = idx.tolist()
                row["per_q"][q["id"]] = {
                    "dense_r8": recall(top_pmids(idx, meta, 8), q["gold"]),
                    "dense_r40": recall(top_pmids(idx, meta, 40), q["gold"]),
                    "dense_mrr": mrr(idx, meta, q["gold"]),
                }
            hybrid._dense_search = lambda query, top_k: [
                dict(meta[i], score=0.0) for i in ranked[query][:top_k]
            ]
        if not args.no_hybrid:
            for q in qs:
                legs = hybrid.retrieve_hybrid(q["question"], top_k_final=hybrid.K_FUSED,
                                              use_dense=model != NO_DENSE)
                row["per_q"].setdefault(q["id"], {})["hybrid_r8"] = recall(capped_pmids(legs["final"]), q["gold"])
        results[model] = row

    cats = sorted({q["category"] for q in qs})
    metrics = ["dense_r8", "dense_r40", "dense_mrr", "hybrid_r8"]
    for row in results.values():
        for m in metrics:
            vals = [v[m] for v in row["per_q"].values() if m in v]
            row[m] = round(float(np.mean(vals)), 3) if vals else None
            for c in cats:
                cv = [row["per_q"][q["id"]][m] for q in qs if q["category"] == c and m in row["per_q"].get(q["id"], {})]
                row.setdefault("by_category", {}).setdefault(c, {})[m] = round(float(np.mean(cv)), 3) if cv else None

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = out_dir / f"{date.today().isoformat()}"
    stem.with_suffix(".json").write_text(json.dumps(
        {"chunks": len(meta), "questions": len(qs), "results": results}, indent=1))
    lines = [f"# Embedding bake-off ({date.today().isoformat()})", "",
             f"{len(meta)} chunks from {len({m['pmid'] for m in meta})} papers; {len(qs)} labeled questions; "
             "recall = share of each question's gold papers retrieved, averaged.", "",
             "| model | dim | dense R@8 | dense R@40 | dense MRR | hybrid R@8 | "
             + " | ".join(f"hybrid R@8 {c}" for c in cats) + " | router acc | chunks/s | query ms |",
             "|---|---|---|---|---|---|" + "---|" * len(cats) + "---|---|---|"]
    for model, r in results.items():
        cells = [r.get(m) for m in metrics]
        lines.append(f"| {model} | {r.get('dim', '')} | " + " | ".join("" if v is None else f"{v:.3f}" for v in cells)
                     + " | " + " | ".join(f"{r['by_category'][c]['hybrid_r8']:.3f}" if r['by_category'][c].get('hybrid_r8') is not None else "" for c in cats)
                     + f" | {r.get('router_acc', '')} | {r.get('doc_chunks_per_s', '')} | {r.get('query_ms', '')} |")
    stem.with_suffix(".md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
