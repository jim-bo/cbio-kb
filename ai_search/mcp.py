#!/usr/bin/env python3
"""MCP server exposing the three cbio-kb retrieval strategies as tools.

Unlike ``cbio_kb.server.mcp`` (a single dense ``search_pdf_corpus`` tool over
the e5 PDF index), this server fronts the *eval* retrieval stack in
``ai_search/`` over the gemini-embedding ``data/paper_index`` and the wiki
graph. It gives an LLM client four search tools plus a routing helper:

- ``search_dense``  — pure dense FAISS retrieval (``ai_search.rag``).
- ``search_hybrid`` — dense + BM25 + graph 1-hop, RRF-fused + reranked
  (``ai_search.hybrid``). Cheapest competitive option for factual questions.
- ``search_agentic``— the PydanticAI wiki graph-walk agent, run to completion;
  returns a synthesized answer + cited PMIDs. Best for list/synthesis.
- ``search_auto``   — classify the question and dispatch to the strategy the
  eval found best on the cost/quality frontier (see ``ai_search.router``).
- ``route_query``   — return the routing decision *without* executing, so a
  client can inspect or override the choice.

Run (needs ``server`` for fastmcp + ``chat`` for pydantic-ai/anthropic)::

    GCP_PROJECT=… uv run --extra chat --extra server \
        python -m ai_search.mcp --host 0.0.0.0 --port 8124

``GCP_PROJECT`` must be set for the Vertex embeddings the dense/hybrid/auto
tools depend on.
"""
from __future__ import annotations

import argparse
import re
from typing import Annotated, Any

from fastmcp import FastMCP

from . import rag, router
from .agent import Deps, agent

mcp = FastMCP(name="cbio-kb Retrieval Strategies")

# --------------------------------------------------------------------------
# Shared shaping helpers
# --------------------------------------------------------------------------

_PMID_RE = re.compile(r"(?:PMID[:\s]?|papers/)(\d{5,9})")


def _passage_view(chunks: list[dict], top_k: int) -> list[dict]:
    """Trim retrieval chunks to a stable, JSON-friendly shape for the client."""
    out: list[dict] = []
    for c in chunks[:top_k]:
        score = c.get("rerank_score", c.get("fused_score", c.get("score")))
        out.append(
            {
                "pmid": c.get("pmid"),
                "chunk_id": c.get("chunk_id"),
                "score": round(float(score), 4) if score is not None else None,
                "path": f"papers/{c.get('pmid')}.md",
                "text": c.get("text", ""),
            }
        )
    return out


def _cited_pmids(text: str) -> list[str]:
    """Extract unique PMIDs cited in an agent answer (PMID:… or papers/….html)."""
    seen: dict[str, None] = {}
    for m in _PMID_RE.finditer(text):
        seen.setdefault(m.group(1), None)
    return list(seen)


# --------------------------------------------------------------------------
# Strategy implementations (thin wrappers around ai_search/*)
# --------------------------------------------------------------------------


def _do_dense(query: str, top_k: int) -> dict[str, Any]:
    passages = rag.retrieve(query, top_k=max(top_k, 8))
    return {
        "mode": "dense",
        "query": query,
        "passages": _passage_view(passages, top_k),
    }


def _do_hybrid(query: str, top_k: int) -> dict[str, Any]:
    from . import hybrid  # local import: pulls in BM25/graph/reranker

    legs = hybrid.retrieve_hybrid(query, top_k_final=max(top_k, 8))
    return {
        "mode": "hybrid",
        "query": query,
        "leg_counts": {
            "dense": len(legs["dense"][0]),
            "bm25": len(legs["bm25"][0]),
            "graph": len(legs["graph"][0]),
            "fused": len(legs["fused"]),
            "final": len(legs["final"]),
        },
        "anchors": legs.get("anchors", []),
        "passages": _passage_view(legs["final"], top_k),
    }


async def _do_agentic(query: str) -> dict[str, Any]:
    from pydantic_ai.usage import UsageLimits

    result = await agent.run(
        query,
        deps=Deps(),  # no tool_queue: tool events are no-ops headless
        usage_limits=UsageLimits(tool_calls_limit=20),
    )
    answer = str(result.output)
    payload: dict[str, Any] = {
        "mode": "agentic",
        "query": query,
        "answer": answer,
        "cited_pmids": _cited_pmids(answer),
    }
    try:
        usage = result.usage()
        if usage is not None:
            payload["usage"] = {
                "input_tokens": usage.input_tokens,
                "output_tokens": usage.output_tokens,
                "llm_calls": usage.requests,
            }
    except Exception:
        pass
    return payload


# --------------------------------------------------------------------------
# Tools
# --------------------------------------------------------------------------

Query = Annotated[str, "The natural-language question to answer from the cBioPortal paper corpus."]
TopK = Annotated[int, "Number of passages to return."]


@mcp.tool()
def search_dense(query: Query, top_k: TopK = 8) -> dict:
    """Dense-vector retrieval over the cBioPortal paper corpus.

    Embeds the query with gemini-embedding-001 and returns the top passages by
    cosine similarity. Fast, simple, no reranking. Good general-purpose
    retrieval; use search_hybrid for cheapest factual lookups or search_agentic
    for enumeration/synthesis.
    """
    return _do_dense(query, top_k)


@mcp.tool()
def search_hybrid(query: Query, top_k: TopK = 8) -> dict:
    """Hybrid retrieval: dense + BM25 + wiki-graph 1-hop, RRF-fused and
    cross-encoder reranked.

    Cheapest competitive option for single-fact (lookup) and definitional
    questions — near-parity accuracy and citations at a fraction of the tokens.
    Weaker than search_agentic for list/synthesis questions.
    """
    return _do_hybrid(query, top_k)


@mcp.tool()
async def search_agentic(query: Query) -> dict:
    """Agentic retrieval: a graph-walking agent reads the cross-linked wiki to
    completion and returns a synthesized answer with cited PMIDs.

    Best for list (enumeration) and synthesis (cross-paper reasoning)
    questions, where whole-page reading matters. Slower and more token-heavy
    than the single-shot retrievers.
    """
    return await _do_agentic(query)


@mcp.tool()
def route_query(query: Query) -> dict:
    """Classify a question and return which retrieval strategy is recommended,
    WITHOUT running it.

    Returns the chosen mode (hybrid/rag/agentic), the inferred question
    category, the classifier used (kNN over labeled eval questions, or a
    lexical-heuristic fallback), a confidence score, and a rationale. Use this
    to inspect or override the auto-router's choice.
    """
    return router.route(query).to_dict()


@mcp.tool()
async def search_auto(query: Query, top_k: TopK = 8) -> dict:
    """Auto mode: classify the question, then dispatch to the retrieval
    strategy the eval found best on the cost/quality frontier.

    lookup/definition -> hybrid (cheap, near-parity); list/synthesis ->
    agentic (whole-page reading). The routing decision is included in the
    response under "route".
    """
    decision = router.route(query)
    if decision.mode == "agentic":
        result = await _do_agentic(query)
    elif decision.mode == "dense" or decision.mode == "rag":
        result = _do_dense(query, top_k)
    else:  # hybrid (default)
        result = _do_hybrid(query, top_k)
    result["route"] = decision.to_dict()
    return result


# --------------------------------------------------------------------------
# Entry point
# --------------------------------------------------------------------------


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="cbio-kb retrieval-strategies MCP server")
    parser.add_argument("--host", default="localhost", help="Host to bind to")
    parser.add_argument("--port", type=int, default=8124, help="Port to run on")
    parser.add_argument(
        "--transport", default="http", choices=["http", "stdio"],
        help="Server transport protocol",
    )
    args = parser.parse_args(argv)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    else:
        print(f"--- cbio-kb retrieval MCP server on {args.transport}://{args.host}:{args.port} ---")
        mcp.run(transport=args.transport, host=args.host, port=args.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
