"""Tests for cbio_kb.index.onnx_models with fake ONNX sessions and tokenizers.

Nothing here downloads a model; eval/onnx_parity.py checks real models
against PyTorch.
"""
from __future__ import annotations

from types import SimpleNamespace

import numpy as np
import pytest

from cbio_kb.index import embed, onnx_models


class _Enc(SimpleNamespace):
    pass


class FakeTokenizer:
    def __init__(self):
        self.seen = []

    def encode_batch(self, inputs):
        self.seen.extend(inputs)
        # Two tokens each; the second is padding for odd batch positions.
        return [_Enc(ids=[1, 2], attention_mask=[1, 0 if i % 2 else 1], type_ids=[0, 1])
                for i, _ in enumerate(inputs)]


class FakeSession:
    def __init__(self, inputs, outputs, result):
        self._inputs, self._outputs, self.result, self.feeds = inputs, outputs, result, []

    def get_inputs(self):
        return [SimpleNamespace(name=n) for n in self._inputs]

    def get_outputs(self):
        return [SimpleNamespace(name=n) for n in self._outputs]

    def run(self, names, feed):
        self.feeds.append(feed)
        return [self.result(len(feed["input_ids"]))]


@pytest.fixture
def fake(monkeypatch):
    state = SimpleNamespace(tok=FakeTokenizer(), session=None, configs={})
    monkeypatch.setattr(onnx_models, "_tokenizer", lambda model: state.tok)
    monkeypatch.setattr(onnx_models, "_session", lambda model: state.session)
    monkeypatch.setattr(onnx_models, "_json", lambda model, name: state.configs.get(name, {}))
    return state


def test_embed_uses_sentence_embedding_output_and_normalizes(fake):
    fake.session = FakeSession(["input_ids", "attention_mask"], ["token_embeddings", "sentence_embedding"],
                               lambda n: np.tile([[3.0, 4.0]], (n, 1)))
    vecs = onnx_models.embed("m", ["a", "b", "c"], prefix="query: ", batch_size=2)
    assert vecs.shape == (3, 2) and np.allclose(vecs, [0.6, 0.8])
    assert fake.tok.seen == ["query: a", "query: b", "query: c"]
    assert set(fake.session.feeds[0]) == {"input_ids", "attention_mask"}  # only declared inputs


@pytest.mark.parametrize("pooling, expected", [
    ({"pooling_mode_cls_token": True}, [1.0, 0.0]),
    ({"pooling_mode_mean_tokens": True}, [1.0, 0.0]),   # first row: both tokens unmasked
])
def test_embed_pools_token_output_from_pooling_config(fake, pooling, expected):
    tokens = np.array([[[1.0, 0.0], [1.0, 0.0]], [[0.0, 1.0], [5.0, 5.0]]])
    fake.session = FakeSession(["input_ids", "attention_mask", "token_type_ids"],
                               ["last_hidden_state"], lambda n: tokens[:n])
    fake.configs["1_Pooling/config.json"] = pooling
    vecs = onnx_models.embed("m", ["x", "y"], normalize=False)
    assert np.allclose(vecs[0], expected)
    assert np.allclose(vecs[1], [0.0, 1.0])  # second row's token 2 is padding either way


@pytest.mark.parametrize("config, logit, expected", [
    ({"sbert_ce_default_activation_function": "torch.nn.modules.linear.Identity"}, 2.0, 2.0),
    ({"sentence_transformers": {"activation_fn": "torch.nn.modules.activation.Sigmoid"}}, 0.0, 0.5),
    ({}, 0.0, 0.5),  # sentence-transformers' default for a 1-label model
])
def test_rerank_applies_the_models_activation(fake, config, logit, expected):
    fake.session = FakeSession(["input_ids", "attention_mask", "token_type_ids"], ["logits"],
                               lambda n: np.full((n, 1), logit, dtype="float32"))
    fake.configs["config.json"] = config
    scores = onnx_models.rerank("ce", "q", ["p1", "p2"])
    assert np.allclose(scores, expected) and fake.tok.seen == [("q", "p1"), ("q", "p2")]
    assert onnx_models.rerank("ce", "q", []).shape == (0,)


def test_rerank_rejects_unknown_activation(fake):
    fake.session = FakeSession(["input_ids"], ["logits"], lambda n: np.zeros((n, 1)))
    fake.configs["config.json"] = {"sbert_ce_default_activation_function": "torch.nn.Tanh"}
    with pytest.raises(ValueError):
        onnx_models.rerank("ce", "q", ["p"])


def test_backend_selection(monkeypatch):
    monkeypatch.setenv("CBIO_EMBED_BACKEND", "onnx")
    assert embed.use_onnx()
    monkeypatch.setenv("CBIO_EMBED_BACKEND", "torch")
    assert not embed.use_onnx()
    monkeypatch.setenv("CBIO_EMBED_BACKEND", "gpu")
    with pytest.raises(ValueError):
        embed.use_onnx()
    monkeypatch.setenv("CBIO_EMBED_BACKEND", "auto")
    monkeypatch.setattr(embed.importlib.util, "find_spec", lambda name: None)
    assert embed.use_onnx()  # no sentence-transformers installed -> ONNX


def test_embed_routes_to_onnx_with_model_card_prompts(monkeypatch):
    monkeypatch.setenv("CBIO_EMBED_BACKEND", "onnx")
    calls = []
    monkeypatch.setattr(onnx_models, "embed", lambda model, texts, **kw: calls.append((model, kw))
                        or np.ones((len(texts), 2), dtype="float32"))
    embed.embed(["q"], kind="query", model="BAAI/bge-base-en-v1.5")
    embed.embed(["d"], kind="document", model="intfloat/e5-base-v2")
    assert calls[0][1]["prefix"].startswith("Represent this sentence")
    assert calls[1][1]["prefix"] == "passage: "
    with pytest.raises(RuntimeError, match="ONNX"):
        embed.embed(["q"], kind="query", model="ncbi/MedCPT")


def test_hybrid_reranker_uses_onnx_backend(monkeypatch):
    hybrid = pytest.importorskip("ai_search.hybrid")
    monkeypatch.setenv("CBIO_EMBED_BACKEND", "onnx")
    monkeypatch.setattr(onnx_models, "rerank",
                        lambda model, query, texts: np.array([len(t) for t in texts], dtype="float32"))
    reranker = hybrid._Reranker("ce")
    ranked = reranker.score("q", [{"text": "a"}, {"text": "ccc"}, {"text": "bb"}])
    assert [p["text"] for p in ranked] == ["ccc", "bb", "a"]
    assert ranked[0]["rerank_score"] == 3.0
