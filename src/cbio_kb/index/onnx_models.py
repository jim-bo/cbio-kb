"""ONNX Runtime inference for the search models, without PyTorch.

At query time, search runs two small transformer models: the embedding model
the passage index was built with, and the cross-encoder that reranks hybrid
results. Both publish ONNX exports on Hugging Face (``onnx/model.onnx``).
Running them on onnxruntime + tokenizers gives the same numbers as
sentence-transformers on PyTorch (checked for arctic-embed-m-v1.5 and
ms-marco-MiniLM-L-6-v2 with ``eval/onnx_parity.py``). That lets the server
images leave PyTorch out.

Pooling, prompts, and the reranker's output activation come from the model
repo's own sentence-transformers config files, so a model behaves the same
here as it does under sentence-transformers.

This module imports nothing from cbio_kb, so the Dockerfiles can run it on
its own to download model files before the package is installed::

    python onnx_models.py --embed <hf model id> --rerank <hf model id>
"""
from __future__ import annotations

import argparse
import json
import math
import os
from functools import lru_cache

import numpy as np

ONNX_FILE = "onnx/model.onnx"
_OPTIONAL = ("config.json", "1_Pooling/config.json", "config_sentence_transformers.json",
             "sentence_bert_config.json")
_DEFAULT_MAX_LEN = 512


def _download(model: str, filename: str, required: bool = True) -> str | None:
    from huggingface_hub import hf_hub_download
    from huggingface_hub.errors import EntryNotFoundError, LocalEntryNotFoundError

    try:
        return hf_hub_download(model, filename)
    except (EntryNotFoundError, LocalEntryNotFoundError):
        if required:
            raise
        return None


def _json(model: str, filename: str) -> dict:
    path = _download(model, filename, required=False)
    if not path:
        return {}
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def prefetch(model: str) -> None:
    """Download everything this module reads for ``model`` into the HF cache."""
    for name in (ONNX_FILE, "tokenizer.json"):
        _download(model, name)
    for name in _OPTIONAL:
        _download(model, name, required=False)


def _threads() -> int | None:
    """ONNX Runtime threads per inference: CBIO_ONNX_THREADS, else the
    container's CPU limit (cgroup v2 ``cpu.max``), else None for every core.

    A container sees all of the host's cores, and ONNX Runtime starts one
    thread per core. Under a 1-CPU limit on a 14-core host that made a hybrid
    search take ~32 s instead of ~2 s with one thread.
    """
    if os.environ.get("CBIO_ONNX_THREADS"):
        return max(1, int(os.environ["CBIO_ONNX_THREADS"]))
    try:
        with open("/sys/fs/cgroup/cpu.max", encoding="ascii") as fh:
            quota, period = fh.read().split()[:2]
        if quota != "max":
            return max(1, math.ceil(int(quota) / int(period)))
    except (OSError, ValueError):
        pass
    return None


@lru_cache(maxsize=4)
def _session(model: str):
    import onnxruntime as ort

    try:
        path = _download(model, ONNX_FILE)
    except Exception as e:
        raise RuntimeError(
            f"{model} has no {ONNX_FILE} on Hugging Face, so it can't run without "
            "PyTorch; install the `index` extra (sentence-transformers) to use it"
        ) from e
    opts = ort.SessionOptions()
    if threads := _threads():
        opts.intra_op_num_threads = threads
    return ort.InferenceSession(path, opts, providers=["CPUExecutionProvider"])


@lru_cache(maxsize=4)
def _tokenizer(model: str):
    from tokenizers import Tokenizer

    tok = Tokenizer.from_file(_download(model, "tokenizer.json"))
    max_len = _json(model, "sentence_bert_config.json").get("max_seq_length") or _DEFAULT_MAX_LEN
    tok.enable_truncation(max_len)
    pad_id = tok.token_to_id("[PAD]")
    tok.enable_padding(pad_id=pad_id if pad_id is not None else 0,
                       pad_token="[PAD]" if pad_id is not None else "<pad>")
    return tok


def _feed(session, encodings) -> dict[str, np.ndarray]:
    arrays = {
        "input_ids": [e.ids for e in encodings],
        "attention_mask": [e.attention_mask for e in encodings],
        "token_type_ids": [e.type_ids for e in encodings],
    }
    return {i.name: np.asarray(arrays[i.name], dtype="int64") for i in session.get_inputs()}


def prompt(model: str, name: str) -> str:
    """A named prompt from the model's sentence-transformers config (e.g. "query")."""
    prompts = _json(model, "config_sentence_transformers.json").get("prompts") or {}
    if name not in prompts:
        raise KeyError(f"{model} defines no prompt named {name!r}")
    return prompts[name]


def _pool(token_embeddings: np.ndarray, attention_mask: np.ndarray, pooling: dict) -> np.ndarray:
    if pooling.get("pooling_mode_cls_token"):
        return token_embeddings[:, 0]
    if pooling.get("pooling_mode_lasttoken"):
        last = attention_mask.sum(axis=1) - 1
        return token_embeddings[np.arange(len(last)), last]
    mask = attention_mask[..., None].astype(token_embeddings.dtype)  # mean pooling
    return (token_embeddings * mask).sum(axis=1) / np.clip(mask.sum(axis=1), 1e-9, None)


def embed(model: str, texts: list[str], *, prefix: str = "", normalize: bool = True,
          batch_size: int = 32) -> np.ndarray:
    """Embed ``texts`` (with ``prefix`` prepended) like SentenceTransformer.encode."""
    session, tok = _session(model), _tokenizer(model)
    outputs = [o.name for o in session.get_outputs()]
    pooling = {} if "sentence_embedding" in outputs else _json(model, "1_Pooling/config.json")
    chunks = []
    for i in range(0, len(texts), batch_size):
        enc = tok.encode_batch([prefix + t for t in texts[i : i + batch_size]])
        feed = _feed(session, enc)
        if "sentence_embedding" in outputs:
            vecs = session.run(["sentence_embedding"], feed)[0]
        else:
            tokens = session.run([outputs[0]], feed)[0]
            vecs = _pool(tokens, np.asarray([e.attention_mask for e in enc]), pooling)
        chunks.append(vecs.astype("float32"))
    vecs = np.concatenate(chunks) if chunks else np.zeros((0, 0), dtype="float32")
    if normalize and len(vecs):
        vecs /= np.clip(np.linalg.norm(vecs, axis=1, keepdims=True), 1e-12, None)
    return vecs


def _activation(model: str, num_labels: int):
    """The output activation sentence-transformers' CrossEncoder applies."""
    cfg = _json(model, "config.json")
    path = (cfg.get("sentence_transformers") or {}).get("activation_fn") \
        or cfg.get("sbert_ce_default_activation_function")
    if path:
        name = path.rsplit(".", 1)[-1]
    else:
        name = "Sigmoid" if num_labels == 1 else "Identity"
    if name == "Sigmoid":
        return lambda x: 1.0 / (1.0 + np.exp(-x))
    if name == "Identity":
        return lambda x: x
    raise ValueError(f"{model}: unsupported cross-encoder activation {path!r}")


def rerank(model: str, query: str, texts: list[str], *, batch_size: int = 4) -> np.ndarray:
    """Score (query, text) pairs like CrossEncoder.predict for a 1-label model.

    Small batches keep memory down: hybrid search reranks 30 passages of up to
    512 tokens, and in one batch ONNX Runtime's attention buffers took peak
    memory to ~2.9 GB; in batches of 4 it's ~1.1 GB, and no slower on CPU.
    """
    if not texts:
        return np.zeros(0, dtype="float32")
    session, tok = _session(model), _tokenizer(model)
    logits = []
    for i in range(0, len(texts), batch_size):
        enc = tok.encode_batch([(query, t) for t in texts[i : i + batch_size]])
        logits.append(session.run(None, _feed(session, enc))[0])
    out = np.concatenate(logits)
    if out.ndim == 2 and out.shape[1] != 1:
        raise ValueError(f"{model}: expected one logit per pair, got shape {out.shape}")
    return _activation(model, 1)(out.reshape(-1)).astype("float32")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Download ONNX search models into the HF cache")
    ap.add_argument("--embed", action="append", default=[], help="embedding model id")
    ap.add_argument("--rerank", action="append", default=[], help="cross-encoder model id")
    args = ap.parse_args(argv)
    for model in filter(None, args.embed + args.rerank):  # "" skips a model
        prefetch(model)
        print(f"[onnx_models] cached {model}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
