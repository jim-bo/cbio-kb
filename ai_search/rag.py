"""RAG retrieval + single-shot LLM answering mode.

Loads a pre-built FAISS index of paper-markdown chunks (from
``cbio-kb index build-papers``) and answers a user query by:

1. Embedding the query via Vertex AI (gemini-embedding-001).
2. Retrieving top-k passages by cosine similarity.
3. Packing them into a single prompt alongside a system instruction.
4. Making one LLM call (same model as the agentic agent) and streaming
   the response.

The module exposes two entry points consumed by ``app.py``:

- ``retrieve(query, max_context_tokens)`` → list of passage dicts
- ``rag_event_generator(query, session_id, history, ...)`` → async SSE
  generator that mirrors the agentic envelope (``context_system``,
  ``context_user``, ``tool_use``, ``text``, ``done``).
"""
from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path

import anthropic
import numpy as np

_INDEX_DIR = Path(os.environ.get(
    "RAG_INDEX_DIR",
    Path(__file__).resolve().parent.parent / "data" / "paper_index",
))

_DEFAULT_TOP_K = 40
_DEFAULT_MAX_CONTEXT_CHARS = 60_000  # ~15k tokens

RAG_SYSTEM_PROMPT = """\
You are a research assistant answering questions about cBioPortal cancer
genomics publications. You have been given a set of retrieved passages
from the source papers. Answer the user's question using ONLY these
passages.

## Rules

- Cite sources inline using the PMID, e.g. (PMID:39506116).
- If the passages do not contain enough information, say so explicitly
  rather than guessing.
- Be concise: 2–4 sentences or a tight bullet list unless the user
  asks for depth.
- Do not invent facts not present in the passages.
"""


def _embed_query(text: str) -> np.ndarray:
    """Embed a single query string via Vertex AI, returns (1, dim) float32."""
    from cbio_kb.index.papers import embed_texts
    return embed_texts([text], task_type="RETRIEVAL_QUERY", batch_size=1)


class RAGIndex:
    """Lazy-loaded singleton for the FAISS index."""

    _instance: RAGIndex | None = None

    def __init__(self, index_dir: Path) -> None:
        import faiss

        idx_path = index_dir / "faiss.index"
        meta_path = index_dir / "meta.jsonl"
        if not idx_path.exists() or not meta_path.exists():
            raise FileNotFoundError(
                f"RAG index not found at {index_dir}. "
                "Run: uv run cbio-kb index build-papers"
            )
        self.index = faiss.read_index(str(idx_path))
        self.meta: list[dict] = []
        with meta_path.open() as fh:
            for line in fh:
                self.meta.append(json.loads(line))

    @classmethod
    def get(cls, index_dir: Path | None = None) -> RAGIndex:
        if cls._instance is None:
            cls._instance = cls(index_dir or _INDEX_DIR)
        return cls._instance

    def search(self, query: str, top_k: int = _DEFAULT_TOP_K) -> list[dict]:
        qvec = _embed_query(query)
        D, I = self.index.search(qvec, top_k)
        results = []
        for j, idx in enumerate(I[0]):
            if idx == -1:
                continue
            rec = dict(self.meta[idx])
            rec["score"] = float(D[0][j])
            results.append(rec)
        return results


def retrieve(
    query: str,
    max_context_chars: int = _DEFAULT_MAX_CONTEXT_CHARS,
    top_k: int = _DEFAULT_TOP_K,
) -> list[dict]:
    """Retrieve passages that fit within ``max_context_chars``."""
    rag = RAGIndex.get()
    candidates = rag.search(query, top_k=top_k)
    passages: list[dict] = []
    budget = max_context_chars
    for c in candidates:
        text_len = len(c["text"])
        if text_len > budget:
            break
        passages.append(c)
        budget -= text_len
    return passages


def _build_rag_prompt(passages: list[dict], user_message: str) -> str:
    parts: list[str] = []
    for i, p in enumerate(passages, 1):
        parts.append(
            f"[Passage {i} — PMID:{p['pmid']}, chunk {p['chunk_id']}, "
            f"score {p['score']:.3f}]\n{p['text']}"
        )
    context_block = "\n\n---\n\n".join(parts)
    return (
        f"## Retrieved passages\n\n{context_block}\n\n"
        f"---\n\n## User question\n\n{user_message}"
    )


async def rag_event_generator(
    user_message: str,
    session_id: str,
    max_context_chars: int = _DEFAULT_MAX_CONTEXT_CHARS,
    top_k: int = _DEFAULT_TOP_K,
):
    """Async generator that yields SSE-shaped ``(event_type, data_json)``
    tuples, matching the agentic envelope in ``app.py``.
    """
    # Emit system context
    sys_chars = len(RAG_SYSTEM_PROMPT)
    yield (
        "context_system",
        json.dumps({
            "content": RAG_SYSTEM_PROMPT,
            "chars": sys_chars,
            "tokens": max(1, sys_chars // 4),
        }),
    )

    # Emit turn start (always turn 0 for RAG — stateless)
    yield (
        "turn_start",
        json.dumps({"turn_index": 0, "keep_recent": 1}),
    )

    # Emit user message context
    yield (
        "context_user",
        json.dumps({
            "content": user_message,
            "chars": len(user_message),
            "tokens": max(1, len(user_message) // 4),
            "turn_index": 0,
        }),
    )

    # Retrieval (blocking but fast — run in executor to not block event loop)
    loop = asyncio.get_event_loop()
    passages = await loop.run_in_executor(
        None, retrieve, user_message, max_context_chars, top_k
    )

    # Emit one synthetic tool_use event for the retrieval step
    retrieved_pmids = list(dict.fromkeys(p["pmid"] for p in passages))
    total_chars = sum(len(p["text"]) for p in passages)
    results_payload = [
        {
            "pmid": p["pmid"],
            "chunk_id": p.get("chunk_id"),
            "score": round(float(p["score"]), 4),
            "path": f"papers/{p['pmid']}.md",
            "chars": len(p["text"]),
        }
        for p in passages
    ]
    yield (
        "tool_use",
        json.dumps({
            "name": "vector_search",
            "args": {
                "query": user_message,
                "top_k": top_k,
                "max_context_chars": max_context_chars,
            },
            "preview": json.dumps(
                [{"pmid": p["pmid"], "score": round(p["score"], 3)}
                 for p in passages[:10]]
            ),
            "summary": f"{len(passages)} passages from {len(retrieved_pmids)} papers",
            "chars": total_chars,
            "tokens": max(1, total_chars // 4),
            "turn_index": 0,
            "result_paths": [f"papers/{pmid}.md" for pmid in retrieved_pmids],
            "results": results_payload,
            "t_start": 0.0,
            "t_end": 0.0,
        }),
    )

    # Build the prompt and stream from Anthropic
    from .agent import MODEL

    model_id = MODEL.replace("anthropic:", "") if MODEL.startswith("anthropic:") else MODEL
    user_prompt = _build_rag_prompt(passages, user_message)

    try:
        client = anthropic.AsyncAnthropic()
        async with client.messages.stream(
            model=model_id,
            max_tokens=2048,
            system=RAG_SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        ) as stream:
            async for text in stream.text_stream:
                yield ("text", json.dumps({"delta": text}))

        # Capture usage from the final message
        final = await stream.get_final_message()
        usage_data = {}
        if final.usage:
            usage_data["input_tokens"] = final.usage.input_tokens
            usage_data["output_tokens"] = final.usage.output_tokens
        yield (
            "done",
            json.dumps({
                "session_id": session_id,
                "mode": "rag",
                **usage_data,
            }),
        )
    except Exception as e:
        yield ("error", json.dumps({"error": str(e)}))
        yield ("done", json.dumps({"session_id": session_id, "mode": "rag"}))
