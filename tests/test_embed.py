"""Tests for cbio_kb.index.embed and the places that pick a model from the index."""
from __future__ import annotations

import json

import numpy as np
import pytest

from cbio_kb.index import embed


class _FakeST:
    """Stands in for a SentenceTransformer; records how encode() was called."""

    def __init__(self, name):
        self.name, self.calls = name, []

    def encode(self, texts, **kw):
        self.calls.append((list(texts), kw))
        return np.ones((len(texts), 3), dtype="float32")


@pytest.fixture
def fake_models(monkeypatch):
    made: dict[str, _FakeST] = {}

    def _st_model(name, max_len=None, pooling=None):
        made.setdefault(name, _FakeST(name))
        made[name].max_len, made[name].pooling = max_len, pooling
        return made[name]

    monkeypatch.setattr(embed, "_st_model", _st_model)
    return made


def test_index_model_reads_config_and_defaults_to_gemini(tmp_path):
    assert embed.index_model(tmp_path) == "gemini-embedding-001"  # pre-config indexes
    (tmp_path / "index_config.json").write_text(json.dumps({"embed_model": "BAAI/bge-base-en-v1.5"}))
    assert embed.index_model(tmp_path) == "BAAI/bge-base-en-v1.5"


def test_bge_prefixes_queries_only(fake_models):
    embed.embed(["q"], kind="query", model="BAAI/bge-base-en-v1.5")
    embed.embed(["d"], kind="document", model="BAAI/bge-base-en-v1.5")
    (_, q_kw), (_, d_kw) = fake_models["BAAI/bge-base-en-v1.5"].calls
    assert q_kw["prompt"].startswith("Represent this sentence")
    assert "prompt" not in d_kw and q_kw["normalize_embeddings"]


def test_prompt_name_models_and_unknown_models(fake_models):
    embed.embed(["q"], kind="query", model="Qwen/Qwen3-Embedding-0.6B")
    assert fake_models["Qwen/Qwen3-Embedding-0.6B"].calls[0][1]["prompt_name"] == "query"
    embed.embed(["q"], kind="query", model="some/other-model")
    kw = fake_models["some/other-model"].calls[0][1]
    assert "prompt" not in kw and "prompt_name" not in kw


def test_medcpt_uses_two_unnormalized_cls_encoders(fake_models):
    embed.embed(["q"], kind="query", model="ncbi/MedCPT")
    embed.embed(["d"], kind="document", model="ncbi/MedCPT")
    q, d = fake_models["ncbi/MedCPT-Query-Encoder"], fake_models["ncbi/MedCPT-Article-Encoder"]
    assert (q.max_len, d.max_len, q.pooling) == (64, 512, "cls")
    assert q.calls[0][1]["normalize_embeddings"] is False


def test_bad_kind_and_vertex_without_project(monkeypatch):
    with pytest.raises(ValueError):
        embed.embed(["x"], kind="passage", model="BAAI/bge-base-en-v1.5")
    monkeypatch.delenv("GCP_PROJECT", raising=False)
    pytest.importorskip("google.genai")
    with pytest.raises(RuntimeError, match="GCP_PROJECT"):
        embed.embed(["x"], kind="query", model="gemini-embedding-001")


def test_rag_embeds_queries_with_the_index_model(tmp_path, monkeypatch):
    faiss = pytest.importorskip("faiss")
    rag = pytest.importorskip("ai_search.rag")
    idx = faiss.IndexFlatIP(3)
    idx.add(np.eye(3, dtype="float32"))
    faiss.write_index(idx, str(tmp_path / "faiss.index"))
    (tmp_path / "meta.jsonl").write_text(
        "".join(json.dumps({"pmid": str(i), "chunk_id": 0, "text": "t"}) + "\n" for i in range(3)))
    (tmp_path / "index_config.json").write_text(json.dumps({"embed_model": "local/model"}))
    seen = []
    monkeypatch.setattr(rag, "_embed_query",
                        lambda text, model: seen.append(model) or np.eye(3, dtype="float32")[:1])
    index = rag.RAGIndex(tmp_path)

    # Stub the FAISS search: on macOS, faiss's OpenMP aborts if spaCy has run
    # earlier in the same process (test_papers_incremental does), and this
    # test is about which model embeds the query, not about FAISS.
    class _Search:
        def search(self, qvec, k):
            return np.array([[1.0]], dtype="float32"), np.array([[0]])

    index.index = _Search()
    hits = index.search("anything", top_k=1)
    assert seen == ["local/model"] and hits[0]["pmid"] == "0"


def test_mcp_dense_needs_gcp_only_for_vertex_indexes(tmp_path, monkeypatch):
    mcp = pytest.importorskip("ai_search.mcp")
    monkeypatch.setattr(mcp, "INDEX_DIR", tmp_path)
    monkeypatch.delenv("GCP_PROJECT", raising=False)
    (tmp_path / "index_config.json").write_text(json.dumps({"embed_model": "gemini-embedding-001"}))
    assert not mcp._dense_available()
    monkeypatch.setenv("GCP_PROJECT", "p")
    assert mcp._dense_available()
    monkeypatch.delenv("GCP_PROJECT")
    (tmp_path / "index_config.json").write_text(json.dumps({"embed_model": "BAAI/bge-base-en-v1.5"}))
    assert mcp._dense_available()
