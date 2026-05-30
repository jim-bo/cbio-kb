"""BM25 sparse-retrieval index built from the same chunk corpus as the FAISS index.

The dense FAISS index produced by ``cbio_kb.index.papers`` already persists
every chunk's text in ``meta.jsonl``. BM25 reuses that corpus verbatim: no
re-chunking, so the two retrievers stay in lock-step by construction.

Artifacts written alongside ``faiss.index``:

- ``bm25.pkl``      — pickled ``(BM25Okapi, list[chunk_record])``
- ``bm25_meta.json`` — small stats blob (vocab size, avg doc length, n_chunks)
"""
from __future__ import annotations

import json
import pickle
import re
import sys
from pathlib import Path
from typing import Iterable

# Pure-Python tokenizer. Splits on non-word chars, lowercases, drops 1-char
# tokens (BM25 weighs them as noise) and a small stopword list. Kept inline
# so neither nltk nor sklearn becomes a runtime dep.
_TOKEN_RE = re.compile(r"[a-zA-Z0-9]+")

_STOPWORDS = frozenset({
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "from",
    "has", "have", "he", "her", "his", "i", "in", "is", "it", "its", "of",
    "on", "or", "she", "such", "than", "that", "the", "their", "them", "then",
    "there", "these", "they", "this", "those", "to", "was", "we", "were",
    "what", "when", "which", "who", "will", "with", "would", "you", "your",
    "if", "no", "not", "do", "does", "did", "been", "being", "into", "than",
    "also", "can", "could", "may", "might", "should", "shall",
})


def tokenize(text: str) -> list[str]:
    """Lowercase, regex-tokenize, drop 1-char tokens + stopwords."""
    out: list[str] = []
    for tok in _TOKEN_RE.findall(text.lower()):
        if len(tok) <= 1:
            continue
        if tok in _STOPWORDS:
            continue
        out.append(tok)
    return out


def _read_meta(meta_path: Path) -> list[dict]:
    records: list[dict] = []
    with meta_path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                records.append(json.loads(line))
    return records


def build_bm25(index_dir: Path) -> dict:
    """Build a BM25 index over the chunks in ``{index_dir}/meta.jsonl``.

    Returns the stats dict written to ``bm25_meta.json``. Raises
    ``FileNotFoundError`` if ``meta.jsonl`` is absent.
    """
    from rank_bm25 import BM25Okapi  # local import — chat-only dep

    meta_path = index_dir / "meta.jsonl"
    if not meta_path.exists():
        raise FileNotFoundError(
            f"BM25 build requires {meta_path}; run `cbio-kb index build-papers` first."
        )

    records = _read_meta(meta_path)
    if not records:
        raise ValueError(f"{meta_path} is empty — nothing to index.")

    tokenized: list[list[str]] = [tokenize(r["text"]) for r in records]
    bm25 = BM25Okapi(tokenized)

    out_path = index_dir / "bm25.pkl"
    with out_path.open("wb") as fh:
        pickle.dump({"bm25": bm25, "records": records}, fh, protocol=pickle.HIGHEST_PROTOCOL)

    vocab = {tok for doc in tokenized for tok in doc}
    avg_dl = sum(len(d) for d in tokenized) / max(1, len(tokenized))
    stats = {
        "n_chunks": len(records),
        "vocab_size": len(vocab),
        "avg_doc_length": round(avg_dl, 2),
        "tokenizer": "lower+regex+stopwords",
    }
    (index_dir / "bm25_meta.json").write_text(json.dumps(stats, indent=2))
    print(
        f"[bm25] wrote {out_path} "
        f"({stats['n_chunks']} chunks, vocab={stats['vocab_size']}, "
        f"avg_dl={stats['avg_doc_length']})",
        file=sys.stderr,
    )
    return stats


def load_bm25(index_dir: Path) -> tuple[object, list[dict]]:
    """Load (BM25Okapi, records) from a prior ``build_bm25`` call."""
    path = index_dir / "bm25.pkl"
    if not path.exists():
        raise FileNotFoundError(
            f"BM25 index not found at {path}. Run `cbio-kb index build-bm25`."
        )
    with path.open("rb") as fh:
        obj = pickle.load(fh)
    return obj["bm25"], obj["records"]


def main(argv: Iterable[str] | None = None) -> int:
    import argparse

    p = argparse.ArgumentParser(description="Build a BM25 index from meta.jsonl")
    p.add_argument("--index-dir", default="data/paper_index")
    args = p.parse_args(list(argv) if argv is not None else None)

    build_bm25(Path(args.index_dir))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
