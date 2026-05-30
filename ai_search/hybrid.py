"""Hybrid 3-leg retrieval + single-shot LLM answering mode.

Runs three retrievers concurrently against the same chunk corpus that
:mod:`ai_search.rag` indexes:

1. **Dense** — Vertex ``gemini-embedding-001`` + FAISS ``IndexFlatIP``
   (reuses :class:`ai_search.rag.RAGIndex`).
2. **BM25** — pickled ``rank_bm25.BM25Okapi`` built by
   ``cbio_kb.index.bm25`` from the same ``meta.jsonl``.
3. **Graph 1-hop** — :func:`ai_search.anchors.extract_anchors` finds
   entity mentions, then ``wiki/graph.json`` cross-edges expand to citing
   papers, whose chunks become candidates.

Results are fused with Reciprocal Rank Fusion (k=60) and optionally
reranked by a cross-encoder before being packed into a single LLM call
with the same prompt template as RAG mode. The SSE envelope matches
:func:`ai_search.rag.rag_event_generator` so the frontend doesn't need
mode-specific rendering.
"""
from __future__ import annotations

import asyncio
import json
import os
import pickle
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

import anthropic
import numpy as np

from . import anchors as _anchors
from .rag import (
    RAG_SYSTEM_PROMPT,
    RAGIndex,
    _build_rag_prompt,
)

_INDEX_DIR = Path(os.environ.get(
    "RAG_INDEX_DIR",
    Path(__file__).resolve().parent.parent / "data" / "paper_index",
))
_WIKI_DIR = Path(os.environ.get(
    "CBIO_WIKI_DIR",
    Path(__file__).resolve().parent.parent / "wiki",
))

K_DENSE = 40
K_BM25 = 40
K_GRAPH = 40
K_FUSED = 30
K_FINAL = 12
RRF_K = 60

_RERANKER_MODEL = os.environ.get(
    "CBIO_RERANKER_MODEL", "cross-encoder/ms-marco-MiniLM-L-6-v2",
)
_RERANK_ENABLED_DEFAULT = os.environ.get("CBIO_HYBRID_RERANK", "1") not in (
    "0", "false", "False", "",
)


# ---------------------------------------------------------------------------
# Index loaders (lazy singletons)
# ---------------------------------------------------------------------------


class BM25Index:
    """Lazy-loaded singleton holding the pickled BM25 model + chunk records."""

    _instance: "BM25Index | None" = None

    def __init__(self, index_dir: Path) -> None:
        path = index_dir / "bm25.pkl"
        if not path.exists():
            raise FileNotFoundError(
                f"BM25 index not found at {path}. "
                "Run: uv run cbio-kb index build-bm25"
            )
        with path.open("rb") as fh:
            obj = pickle.load(fh)
        self.bm25 = obj["bm25"]
        self.records: list[dict] = obj["records"]
        self.by_pmid: dict[str, list[dict]] = defaultdict(list)
        for r in self.records:
            self.by_pmid[str(r["pmid"])].append(r)

    @classmethod
    def get(cls, index_dir: Path | None = None) -> "BM25Index":
        if cls._instance is None:
            cls._instance = cls(index_dir or _INDEX_DIR)
        return cls._instance

    def search(self, query: str, top_k: int = K_BM25) -> list[dict]:
        from cbio_kb.index.bm25 import tokenize
        tokens = tokenize(query)
        if not tokens:
            return []
        scores = np.asarray(self.bm25.get_scores(tokens))
        if scores.size == 0:
            return []
        # Cheap partial sort: argpartition for top-K then sort that slice.
        k = min(top_k, scores.size)
        idx_part = np.argpartition(-scores, k - 1)[:k]
        idx_sorted = idx_part[np.argsort(-scores[idx_part])]
        out: list[dict] = []
        for i in idx_sorted:
            s = float(scores[i])
            if s <= 0.0:
                continue
            rec = dict(self.records[int(i)])
            rec["score"] = s
            out.append(rec)
        return out


class GraphIndex:
    """Lazy-loaded backlinks index: ``target_path -> [source_pmid, ...]``."""

    _instance: "GraphIndex | None" = None

    def __init__(self, wiki_dir: Path) -> None:
        graph_path = wiki_dir / "graph.json"
        if not graph_path.exists():
            raise FileNotFoundError(
                f"wiki graph not found at {graph_path}. "
                "Run: uv run cbio-kb wiki build-graph"
            )
        graph = json.loads(graph_path.read_text())
        # Map every cross-edge target to the set of source pmids that cite it.
        self.backlinks: dict[str, set[str]] = defaultdict(set)
        for e in graph.get("cross_edges", []):
            src = e.get("from", "")
            tgt = e.get("to", "")
            if not src.startswith("papers/"):
                continue
            pmid = Path(src).stem
            self.backlinks[tgt].add(pmid)

    @classmethod
    def get(cls, wiki_dir: Path | None = None) -> "GraphIndex":
        if cls._instance is None:
            cls._instance = cls(wiki_dir or _WIKI_DIR)
        return cls._instance

    def papers_citing(self, anchor_path: str) -> list[str]:
        return sorted(self.backlinks.get(anchor_path, ()))


# ---------------------------------------------------------------------------
# Reranker
# ---------------------------------------------------------------------------


class _Reranker:
    _instance: "_Reranker | None" = None

    def __init__(self, model_name: str) -> None:
        from sentence_transformers import CrossEncoder  # local import
        self.model = CrossEncoder(model_name)

    @classmethod
    def get(cls) -> "_Reranker":
        if cls._instance is None:
            cls._instance = cls(_RERANKER_MODEL)
        return cls._instance

    def score(self, query: str, passages: list[dict]) -> list[dict]:
        if not passages:
            return []
        pairs = [(query, p["text"]) for p in passages]
        scores = self.model.predict(pairs)
        for p, s in zip(passages, scores):
            p["rerank_score"] = float(s)
        passages.sort(key=lambda p: p["rerank_score"], reverse=True)
        return passages


# ---------------------------------------------------------------------------
# Retrievers
# ---------------------------------------------------------------------------


def _dense_search(query: str, top_k: int) -> list[dict]:
    return RAGIndex.get(_INDEX_DIR).search(query, top_k=top_k)


def _bm25_search(query: str, top_k: int) -> list[dict]:
    return BM25Index.get(_INDEX_DIR).search(query, top_k=top_k)


def _graph_search(query: str, top_k: int) -> tuple[list[dict], list[dict]]:
    """Return (chunks, anchors_meta).

    ``anchors_meta`` is a small list of ``{stem, kind, path, matched_text}``
    suitable for the tool_use preview.
    """
    found = _anchors.extract_anchors(query, _WIKI_DIR)
    anchors_meta = [
        {"stem": a.stem, "kind": a.kind, "path": a.path,
         "matched_text": a.matched_text}
        for a in found
    ]
    if not found:
        return [], anchors_meta

    graph = GraphIndex.get(_WIKI_DIR)
    bm25 = BM25Index.get(_INDEX_DIR)  # reused for its by_pmid index

    # anchor-coverage scoring: a paper cited by more anchors ranks higher.
    pmid_coverage: dict[str, int] = defaultdict(int)
    for a in found:
        for pmid in graph.papers_citing(a.path):
            pmid_coverage[pmid] += 1
    if not pmid_coverage:
        return [], anchors_meta

    # Materialize chunks for the top-covered pmids; cap by top_k chunks total
    # to avoid swamping the fuser when a popular paper has 40 chunks.
    ordered_pmids = sorted(pmid_coverage.items(), key=lambda kv: (-kv[1], kv[0]))
    out: list[dict] = []
    for pmid, cov in ordered_pmids:
        for rec in bm25.by_pmid.get(pmid, []):
            rec = dict(rec)
            rec["score"] = float(cov)
            out.append(rec)
            if len(out) >= top_k:
                return out, anchors_meta
    return out, anchors_meta


# ---------------------------------------------------------------------------
# Fusion
# ---------------------------------------------------------------------------


def rrf_fuse(
    rankings: Iterable[list[dict]],
    k: int = RRF_K,
    top_k: int = K_FUSED,
) -> list[dict]:
    """Reciprocal Rank Fusion across N ranked lists.

    Chunks are identified by ``(pmid, chunk_id)``. Each occurrence at rank
    *r* contributes ``1 / (k + r)`` to the chunk's fused score. Scale-agnostic
    by construction — no normalization needed across legs.
    """
    scores: dict[tuple[str, int], float] = {}
    by_key: dict[tuple[str, int], dict] = {}
    for ranking in rankings:
        for rank, c in enumerate(ranking, start=1):
            key = (str(c["pmid"]), int(c["chunk_id"]))
            scores[key] = scores.get(key, 0.0) + 1.0 / (k + rank)
            by_key.setdefault(key, c)
    ordered = sorted(
        by_key.values(),
        key=lambda c: scores[(str(c["pmid"]), int(c["chunk_id"]))],
        reverse=True,
    )
    out: list[dict] = []
    for c in ordered[:top_k]:
        c = dict(c)
        c["fused_score"] = scores[(str(c["pmid"]), int(c["chunk_id"]))]
        out.append(c)
    return out


# ---------------------------------------------------------------------------
# SSE event helpers
# ---------------------------------------------------------------------------


def _disp_score(r: dict) -> float:
    """Best available score for display. Per-leg chunks carry ``score``;
    fused chunks carry ``fused_score``; reranked chunks carry ``rerank_score``.
    The fusion/rerank card would otherwise show 0.0 for every row."""
    for key in ("rerank_score", "fused_score", "score"):
        if key in r:
            return float(r[key])
    return 0.0


def _tool_event(
    *,
    name: str,
    args: dict[str, Any],
    summary: str,
    results: list[dict],
    t_start: float,
    t_end: float,
    turn_index: int = 0,
) -> tuple[str, str]:
    paths = list(dict.fromkeys(f"papers/{r['pmid']}.md" for r in results))
    preview = json.dumps(
        [
            {"pmid": r["pmid"], "chunk_id": r.get("chunk_id"),
             "score": round(_disp_score(r), 4)}
            for r in results[:10]
        ]
    )
    total_chars = sum(len(r.get("text", "")) for r in results)
    payload = {
        "name": name,
        "args": args,
        "preview": preview,
        "summary": summary,
        "chars": total_chars,
        "tokens": max(1, total_chars // 4),
        "turn_index": turn_index,
        "result_paths": paths,
        "results": [
            {
                "pmid": r["pmid"],
                "chunk_id": r.get("chunk_id"),
                "score": round(_disp_score(r), 4),
                "path": f"papers/{r['pmid']}.md",
                "chars": len(r.get("text", "")),
            }
            for r in results
        ],
        "t_start": round(t_start, 4),
        "t_end": round(t_end, 4),
    }
    return ("tool_use", json.dumps(payload))


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


async def _run_legs(
    query: str,
    top_k_dense: int,
    top_k_bm25: int,
    top_k_graph: int,
) -> dict[str, Any]:
    """Dispatch the three retrievers concurrently and return their results
    plus per-leg latency for the SSE tool_use cards."""
    loop = asyncio.get_event_loop()
    t0 = time.perf_counter()

    async def _leg_dense() -> tuple[list[dict], float, float]:
        s = time.perf_counter()
        out = await loop.run_in_executor(None, _dense_search, query, top_k_dense)
        return out, s - t0, time.perf_counter() - t0

    async def _leg_bm25() -> tuple[list[dict], float, float]:
        s = time.perf_counter()
        out = await loop.run_in_executor(None, _bm25_search, query, top_k_bm25)
        return out, s - t0, time.perf_counter() - t0

    async def _leg_graph() -> tuple[list[dict], list[dict], float, float]:
        s = time.perf_counter()
        chunks, anchors_meta = await loop.run_in_executor(
            None, _graph_search, query, top_k_graph,
        )
        return chunks, anchors_meta, s - t0, time.perf_counter() - t0

    dense_task = asyncio.create_task(_leg_dense())
    bm25_task = asyncio.create_task(_leg_bm25())
    graph_task = asyncio.create_task(_leg_graph())
    dense_out, bm25_out, graph_out = await asyncio.gather(
        dense_task, bm25_task, graph_task,
    )
    dense_chunks, dense_ts, dense_te = dense_out
    bm25_chunks, bm25_ts, bm25_te = bm25_out
    graph_chunks, anchors_meta, graph_ts, graph_te = graph_out
    return {
        "dense": (dense_chunks, dense_ts, dense_te),
        "bm25": (bm25_chunks, bm25_ts, bm25_te),
        "graph": (graph_chunks, graph_ts, graph_te),
        "anchors": anchors_meta,
    }


def retrieve_hybrid(
    query: str,
    *,
    top_k_dense: int = K_DENSE,
    top_k_bm25: int = K_BM25,
    top_k_graph: int = K_GRAPH,
    top_k_fused: int = K_FUSED,
    top_k_final: int = K_FINAL,
    rerank: bool = _RERANK_ENABLED_DEFAULT,
) -> dict[str, Any]:
    """Synchronous helper for tests / scripts. Returns the same dict shape
    as :func:`_run_legs` plus ``fused`` and ``final`` lists."""
    legs = asyncio.run(_run_legs(query, top_k_dense, top_k_bm25, top_k_graph))
    fused = rrf_fuse(
        [legs["dense"][0], legs["bm25"][0], legs["graph"][0]],
        k=RRF_K, top_k=top_k_fused,
    )
    final = list(fused)
    if rerank and final:
        final = _Reranker.get().score(query, final)
    final = final[:top_k_final]
    legs["fused"] = fused
    legs["final"] = final
    return legs


# ---------------------------------------------------------------------------
# Public SSE generator (mirrors ai_search.rag.rag_event_generator)
# ---------------------------------------------------------------------------


async def hybrid_event_generator(
    user_message: str,
    session_id: str,
    top_k_dense: int = K_DENSE,
    top_k_bm25: int = K_BM25,
    top_k_graph: int = K_GRAPH,
    top_k_fused: int = K_FUSED,
    top_k_final: int = K_FINAL,
    rerank: bool = _RERANK_ENABLED_DEFAULT,
    max_context_chars: int = 60_000,
):
    """Async generator that yields SSE-shaped ``(event_type, data_json)`` tuples."""
    sys_chars = len(RAG_SYSTEM_PROMPT)
    yield (
        "context_system",
        json.dumps({
            "content": RAG_SYSTEM_PROMPT,
            "chars": sys_chars,
            "tokens": max(1, sys_chars // 4),
        }),
    )
    yield ("turn_start", json.dumps({"turn_index": 0, "keep_recent": 1}))
    yield (
        "context_user",
        json.dumps({
            "content": user_message,
            "chars": len(user_message),
            "tokens": max(1, len(user_message) // 4),
            "turn_index": 0,
        }),
    )

    try:
        legs = await _run_legs(user_message, top_k_dense, top_k_bm25, top_k_graph)
        dense_chunks, dense_ts, dense_te = legs["dense"]
        bm25_chunks, bm25_ts, bm25_te = legs["bm25"]
        graph_chunks, graph_ts, graph_te = legs["graph"]
        anchors_meta = legs["anchors"]

        # Emit per-leg tool_use cards in a stable order.
        yield _tool_event(
            name="dense_search",
            args={"query": user_message, "top_k": top_k_dense},
            summary=f"{len(dense_chunks)} chunks via gemini-embedding-001",
            results=dense_chunks,
            t_start=dense_ts, t_end=dense_te,
        )
        yield _tool_event(
            name="bm25_search",
            args={"query": user_message, "top_k": top_k_bm25},
            summary=f"{len(bm25_chunks)} chunks via BM25Okapi",
            results=bm25_chunks,
            t_start=bm25_ts, t_end=bm25_te,
        )
        graph_summary = (
            f"{len(graph_chunks)} chunks from {len(anchors_meta)} anchor(s): "
            + ", ".join(a["matched_text"] for a in anchors_meta[:6])
            if anchors_meta else "no entity anchors matched"
        )
        yield _tool_event(
            name="graph_search",
            args={"query": user_message, "anchors": anchors_meta, "top_k": top_k_graph},
            summary=graph_summary,
            results=graph_chunks,
            t_start=graph_ts, t_end=graph_te,
        )

        fuse_start = time.perf_counter()
        fused = rrf_fuse(
            [dense_chunks, bm25_chunks, graph_chunks],
            k=RRF_K, top_k=top_k_fused,
        )

        loop = asyncio.get_event_loop()
        if rerank and fused:
            final = await loop.run_in_executor(
                None, _Reranker.get().score, user_message, list(fused),
            )
        else:
            final = list(fused)
        final = final[:top_k_final]
        fuse_end = time.perf_counter()

        yield _tool_event(
            name="rrf_fuse_rerank",
            args={
                "rrf_k": RRF_K, "top_k_fused": top_k_fused,
                "top_k_final": top_k_final, "rerank": rerank,
            },
            summary=(
                f"fused → {len(fused)} chunks; "
                f"reranked → top {len(final)}" if rerank
                else f"fused → top {len(final)} (no rerank)"
            ),
            results=final,
            t_start=fuse_start - fuse_start, t_end=fuse_end - fuse_start,
        )

        # Pack into the same prompt template as RAG mode, respecting the
        # max_context_chars budget (drops chunks that overflow).
        budget = max_context_chars
        passages: list[dict] = []
        for c in final:
            text_len = len(c.get("text", ""))
            if text_len > budget:
                continue
            passages.append(c)
            budget -= text_len

        from .agent import MODEL
        model_id = MODEL.replace("anthropic:", "") if MODEL.startswith("anthropic:") else MODEL
        user_prompt = _build_rag_prompt(passages, user_message)

        client = anthropic.AsyncAnthropic()
        async with client.messages.stream(
            model=model_id,
            max_tokens=2048,
            system=RAG_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        ) as stream:
            async for text in stream.text_stream:
                yield ("text", json.dumps({"delta": text}))

        final_msg = await stream.get_final_message()
        usage_data: dict[str, Any] = {}
        if final_msg.usage:
            usage_data["input_tokens"] = final_msg.usage.input_tokens
            usage_data["output_tokens"] = final_msg.usage.output_tokens
        yield (
            "done",
            json.dumps({
                "session_id": session_id,
                "mode": "hybrid",
                "leg_counts": {
                    "dense": len(dense_chunks),
                    "bm25": len(bm25_chunks),
                    "graph": len(graph_chunks),
                    "fused": len(fused),
                    "final": len(final),
                },
                **usage_data,
            }),
        )
    except Exception as e:
        yield ("error", json.dumps({"error": str(e)}))
        yield ("done", json.dumps({"session_id": session_id, "mode": "hybrid"}))
