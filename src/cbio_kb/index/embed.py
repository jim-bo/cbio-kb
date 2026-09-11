"""Embedding backends for the passage index.

An index records the model that built it (``embed_model`` in
``index_config.json``), and queries must be embedded with that same model;
``index_model()`` reads it back. ``gemini-embedding-001`` runs on Vertex AI
(needs GCP_PROJECT + Application Default Credentials, and is billed); any
other name is a Hugging Face model run locally with sentence-transformers,
so it needs no cloud account at all.

Local models are loaded once per process and use the query/document
prompts from their model cards (``_LOCAL``). A model not listed there is
run with no prompts.
"""
from __future__ import annotations

import json
import os
import sys
import time
from functools import lru_cache
from pathlib import Path

import numpy as np

#: Model for new index builds and for the router's question bank.
DEFAULT_MODEL = os.environ.get("CBIO_EMBED_MODEL", "Snowflake/snowflake-arctic-embed-m-v1.5")
VERTEX_MODELS = {"gemini-embedding-001"}
GCP_LOCATION = os.environ.get("GCP_LOCATION", "us-central1")
_VERTEX_BATCH_SIZE = 25  # keep well under the per-minute token quota

_BGE_QUERY = "Represent this sentence for searching relevant passages: "

# Per-model settings from each model card. "query"/"document" are literal
# prefixes; "query_prompt_name" uses a prompt stored in the model's own
# sentence-transformers config. MedCPT is two encoders (short queries,
# long articles) trained for raw dot product, so it isn't normalized.
_LOCAL: dict[str, dict] = {
    "BAAI/bge-base-en-v1.5": {"query": _BGE_QUERY},
    "Snowflake/snowflake-arctic-embed-m-v1.5": {"query": _BGE_QUERY},
    "intfloat/e5-base-v2": {"query": "query: ", "document": "passage: "},
    "Qwen/Qwen3-Embedding-0.6B": {"query_prompt_name": "query"},
    "ncbi/MedCPT": {
        "query_model": "ncbi/MedCPT-Query-Encoder", "query_max_len": 64,
        "document_model": "ncbi/MedCPT-Article-Encoder", "document_max_len": 512,
        "pooling": "cls", "normalize": False,
    },
}


def is_vertex(model: str) -> bool:
    return model in VERTEX_MODELS


def index_model(index_dir: Path, default: str = "gemini-embedding-001") -> str:
    """The embedding model recorded in an index's ``index_config.json``.

    Indexes built before the model was recorded were all Gemini, hence the
    default.
    """
    cfg = Path(index_dir) / "index_config.json"
    if cfg.exists():
        return json.loads(cfg.read_text()).get("embed_model", default)
    return default


def _device() -> str:
    import torch

    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"


@lru_cache(maxsize=4)
def _st_model(name: str, max_len: int | None = None, pooling: str | None = None):
    from sentence_transformers import SentenceTransformer, models

    if pooling:  # plain transformers checkpoint (MedCPT): build the pipeline
        word = models.Transformer(name, max_seq_length=max_len or 512)
        pool = models.Pooling(word.get_word_embedding_dimension(), pooling_mode=pooling)
        return SentenceTransformer(modules=[word, pool], device=_device())
    model = SentenceTransformer(name, device=_device())
    if max_len:
        model.max_seq_length = max_len
    return model


def _embed_local(texts: list[str], kind: str, model: str, batch_size: int) -> np.ndarray:
    cfg = _LOCAL.get(model, {})
    st = _st_model(cfg.get(f"{kind}_model", model), cfg.get(f"{kind}_max_len"), cfg.get("pooling"))
    kwargs: dict = {}
    if kind == "query" and cfg.get("query_prompt_name"):
        kwargs["prompt_name"] = cfg["query_prompt_name"]
    elif cfg.get(kind):
        kwargs["prompt"] = cfg[kind]
    vecs = st.encode(
        texts, batch_size=batch_size, normalize_embeddings=cfg.get("normalize", True),
        convert_to_numpy=True, show_progress_bar=len(texts) > 1000, **kwargs,
    )
    return np.asarray(vecs, dtype="float32")


def _embed_vertex(texts: list[str], kind: str, model: str, batch_size: int) -> np.ndarray:
    from google import genai
    from google.genai import types

    project = os.environ.get("GCP_PROJECT")
    if not project:
        raise RuntimeError(
            f"{model} runs on Vertex AI, a paid service: export GCP_PROJECT "
            "(with Application Default Credentials) or use a local model."
        )
    client = genai.Client(vertexai=True, project=project, location=GCP_LOCATION)
    task_type = "RETRIEVAL_QUERY" if kind == "query" else "RETRIEVAL_DOCUMENT"
    all_vecs: list[list[float]] = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        for attempt in range(5):
            try:
                resp = client.models.embed_content(
                    model=model, contents=batch,
                    config=types.EmbedContentConfig(task_type=task_type),
                )
                break
            except Exception as e:
                if "429" in str(e) and attempt < 4:
                    wait = 30 * (attempt + 1)
                    print(f"  rate limited, waiting {wait}s…", file=sys.stderr)
                    time.sleep(wait)
                else:
                    raise
        all_vecs.extend(emb.values for emb in resp.embeddings)
        done = min(i + batch_size, len(texts))
        if len(texts) > batch_size:
            print(f"  embedded {done}/{len(texts)}", file=sys.stderr)
        if done < len(texts):
            time.sleep(2)
    arr = np.array(all_vecs, dtype="float32")
    norms = np.linalg.norm(arr, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return arr / norms


def embed(texts: list[str], *, kind: str, model: str, batch_size: int | None = None) -> np.ndarray:
    """Embed ``texts`` as ``kind`` ("query" or "document") with ``model``.

    Returns an (N, dim) float32 array, L2-normalized except for models
    trained for raw dot product (MedCPT).
    """
    if kind not in ("query", "document"):
        raise ValueError(f"kind must be 'query' or 'document', not {kind!r}")
    if is_vertex(model):
        return _embed_vertex(texts, kind, model, batch_size or _VERTEX_BATCH_SIZE)
    return _embed_local(texts, kind, model, batch_size or 32)
