#!/usr/bin/env python3
"""
Minimal MCP server using fastmcp to expose the PDF search script as a tool.
Uses argparse to configure the server (host, port).
Uses environment variables for the index config (INDEX_DIR, etc.).
"""

import argparse  # <-- Added this import
import json
import csv
import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Annotated, Dict, List, Optional

# --- Vector index ---
import faiss

# --- NLP / embeddings ---
import numpy as np

# --- MCP Server ---
from fastmcp import Context, FastMCP
from sentence_transformers import CrossEncoder, SentenceTransformer

# ---------------------------
# Configuration (from Environment Variables)
# ---------------------------
INDEX_DIR = Path(os.environ.get("INDEX_DIR", "./data/index_dir"))
EMBED_MODEL = os.environ.get("EMBED_MODEL", "intfloat/e5-base-v2")
RERANKER_MODEL = os.environ.get("RERANKER_MODEL", "cross-encoder/ms-marco-MiniLM-L-6-v2")
FETCH_K = int(os.environ.get("FETCH_K", 40))

# ---------------------------
# Global state to hold models
# ---------------------------
models = {}

# ---------------------------
# Copied Utilities
# ---------------------------
def read_metadata(meta_path: str) -> List[Dict]:
    out = []
    with open(meta_path, "r", encoding="utf-8") as f:
        for line in f:
            out.append(json.loads(line))
    return out

def e5_prefix(text: str, is_query: bool, model_name: str) -> str:
    if "e5" in model_name.lower():
        return f"{'query' if is_query else 'passage'}: {text}"
    return text

def load_study_id_mapping(csv_path: str) -> Dict[str, str]:
    mapping = {}
    if not os.path.exists(csv_path):
        print(f"[!] WARNING: Mapping file not found: {csv_path}")
        return mapping
    
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pmcid = row.get("pmcid")
            study_id = row.get("studyId")
            if pmcid and study_id:
                mapping[pmcid.strip()] = study_id.strip()
    return mapping

# ---------------------------
# Server Startup & Shutdown
# ---------------------------
@asynccontextmanager
async def lifespan(mcp: FastMCP):
    """
    Handles loading the models on startup.
    """
    print("[*] Server starting... Loading models...")
    index_path = INDEX_DIR / "faiss.index"
    meta_path = INDEX_DIR / "meta.jsonl"

    if not index_path.exists() or not meta_path.exists():
        print(f"[!] ERROR: Index files not found in '{INDEX_DIR}'.")
    else:
        print(f"[*] Loading FAISS index: {index_path}")
        models["index"] = faiss.read_index(str(index_path))

        print(f"[*] Loading metadata: {meta_path}")
        models["meta"] = read_metadata(str(meta_path))

        print(f"[*] Loading embedding model: {EMBED_MODEL}")
        models["embedder"] = SentenceTransformer(EMBED_MODEL)

        print(f"[*] Loading reranker model: {RERANKER_MODEL}")
        models["reranker"] = CrossEncoder(RERANKER_MODEL)

        mapping_path = Path(os.environ.get("PMID_MAPPING_CSV", "data/pmid_to_pmcid.csv"))
        print(f"[*] Loading Study ID mapping: {mapping_path}")
        models["mapping"] = load_study_id_mapping(str(mapping_path))

        print("[✓] All models and index loaded. Server is ready.")

    yield

    print("[*] Server shutting down... Clearing models.")
    models.clear()

# ---------------------------
# Create the MCP Server
# ---------------------------
mcp = FastMCP(
    name="PDF Corpus Search Tool",
    lifespan=lifespan
)

# ---------------------------
# The MCP Tool
# ---------------------------
Query = Annotated[str, "The semantic search query to run against the documents."]
TopK = Annotated[int, "The final number of results to return.", "default: 5"]
Rerank = Annotated[bool, "Whether to use a cross-encoder to rerank results. Default: true.", "default: true"]

@mcp.tool()
def search_pdf_corpus(
    query: Query,
    top_k: TopK = 5,
    rerank: Rerank = True
) -> List[Dict]:
    """
    Searches a private corpus of PDF documents for relevant text chunks.
    Use this to answer questions about specific topics found in the user's files.
    """
    if "index" not in models:
        return [{"error": "Index is not loaded. Check server logs."}]

    # ... (search logic remains identical to before) ...
    # 1. Get pre-loaded assets
    index = models["index"]
    meta = models["meta"]
    embedder = models["embedder"]

    # 2. Embed Query
    query_text = e5_prefix(query, is_query=True, model_name=EMBED_MODEL)
    qvec = embedder.encode([query_text], normalize_embeddings=True).astype("float32")

    # 3. FAISS Search
    D, I = index.search(qvec, FETCH_K)

    # 4. Get Candidates
    candidates = []
    for j, idx in enumerate(I[0]):
        if idx == -1: continue
        rec = dict(meta[idx])
        rec["ann_score"] = float(D[0][j])
        candidates.append(rec)

    if not candidates:
        return []

    # 5. Optional Reranking
    if rerank:
        pairs = [(query, c["text"]) for c in candidates]
        scores = models["reranker"].predict(pairs)
        for c, s in zip(candidates, scores):
            c["rerank_score"] = float(s)
        candidates.sort(key=lambda x: x["rerank_score"], reverse=True)
    else:
        candidates.sort(key=lambda x: x["ann_score"], reverse=True)

    # 6. Format and return top_k results
    mapping = models.get("mapping", {})
    final_results = []
    for r in candidates[:top_k]:
        doc_path = r["doc_path"]
        pmcid = Path(doc_path).stem
        # If the stem is like "PMC12345", we use it. 
        # Note: Depending on file naming, might need adjustment, but assuming stem is PMCID per user context.
        study_id = mapping.get(pmcid, "Unknown")

        final_results.append({
            "study_id": study_id,
            "doc_path": doc_path,
            "page": r["page"],
            "score": r.get("rerank_score", r["ann_score"]),
            "text": r["text"]
        })

    return final_results

# ---------------------------
# Run the Server
# ---------------------------
def main(argv=None):
    parser = argparse.ArgumentParser(description="Run the PDF Search MCP Server")
    parser.add_argument("--host", type=str, default="localhost", help="Host to bind the server to")
    parser.add_argument("--port", type=int, default=8123, help="Port to run the server on")
    parser.add_argument("--transport", type=str, default="http", choices=["http"], help="Server transport protocol")
    args = parser.parse_args(argv)

    print(f"--- Starting PDF Search MCP Server on {args.transport}://{args.host}:{args.port} ---")
    print(f"--- Using INDEX_DIR: {INDEX_DIR.resolve()} ---")

    mcp.run(transport=args.transport, host=args.host, port=args.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
