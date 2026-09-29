"""Markdown-paper indexer for the RAG-vs-agentic comparison.

Walks ``data/raw/papers/{pmid}.md`` for a restricted PMID set, splits each
paper into anchored passages (sections, paragraphs and character offsets; see
``cbio_kb.index.passages``), embeds the passages (a local
sentence-transformers model by default, see ``cbio_kb.index.embed``), and
writes ``faiss.index`` + ``meta.jsonl`` + ``index_config.json`` so the RAG
runner can query over the same corpus the agentic runner walks. The config
records the model, and queries are always embedded with that model.

Usage (direct)::

    uv run python -m cbio_kb.index.papers build \\
        --papers-dir data/raw/papers \\
        --pmid-list  eval/corpus_pmids.txt \\
        --index-dir  data/paper_index

Usage (wired via cli)::

    uv run cbio-kb index build-papers \\
        --papers-dir data/raw/papers \\
        --pmid-list  eval/corpus_pmids.txt \\
        --index-dir  data/paper_index
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Iterable

import numpy as np

from cbio_kb.index import embed as _embed
from cbio_kb.index import passages as _passages

# Model for new builds (override with --embed-model or CBIO_EMBED_MODEL).
EMBED_MODEL = _embed.DEFAULT_MODEL
_BATCH_SIZE = 25  # also stays under Vertex's per-minute quota for Gemini builds


def _read_pmid_list(path: Path) -> list[str]:
    return [ln.strip() for ln in path.read_text().splitlines() if ln.strip()]


def embed_texts(
    texts: list[str],
    *,
    task_type: str = "RETRIEVAL_DOCUMENT",
    batch_size: int = _BATCH_SIZE,
    model: str | None = None,
) -> np.ndarray:
    """Embed texts as documents (``RETRIEVAL_DOCUMENT``) or queries
    (``RETRIEVAL_QUERY``) with ``model`` (default ``EMBED_MODEL``).

    Returns an (N, dim) float32 array; see ``cbio_kb.index.embed.embed``.
    """
    kind = "query" if task_type == "RETRIEVAL_QUERY" else "document"
    return _embed.embed(texts, kind=kind, model=model or EMBED_MODEL, batch_size=batch_size)


def iter_chunks(
    papers_dir: Path,
    pmids: Iterable[str],
    nlp,
    chunk_chars: int,
    overlap: int,
) -> list[dict]:
    """Anchored passages for each paper (see ``cbio_kb.index.passages``)."""
    records: list[dict] = []
    for pmid in pmids:
        fpath = papers_dir / f"{pmid}.md"
        if not fpath.exists():
            print(f"[!] missing raw paper: {fpath}", file=sys.stderr)
            continue
        _, found = _passages.passages(nlp, fpath.read_text(), target_chars=chunk_chars, overlap=overlap)
        for idx, p in enumerate(found):
            records.append({
                "pmid": pmid,
                "chunk_id": idx,
                "text": p.text,
                "section": p.section,
                "subsection": p.subsection,
                "paragraph": p.paragraph,
                "char_start": p.char_start,
                "char_end": p.char_end,
            })
    return records


def _load_existing(out_dir: Path, args: argparse.Namespace):
    """Return (records, vectors) from a published index built with the same
    model and chunking as *args*, or None (with a message) if it can't be reused."""
    import faiss  # type: ignore

    meta_path, index_path = out_dir / "meta.jsonl", out_dir / "faiss.index"
    config = json.loads((out_dir / "index_config.json").read_text()) \
        if (out_dir / "index_config.json").exists() else {}
    if not (meta_path.exists() and index_path.exists()):
        print(f"[!] --incremental: no index in {out_dir}; run a full build", file=sys.stderr)
        return None
    expected = {"embed_model": args.embed_model, "chunker": _passages.CHUNKER_VERSION,
                "chunk_chars": args.chunk_chars, "overlap": args.overlap}
    mismatched = {k: config.get(k) for k, v in expected.items() if config.get(k) != v}
    if mismatched:
        print(f"[!] --incremental: existing index differs {mismatched} from {expected}; "
              "run a full build", file=sys.stderr)
        return None
    with meta_path.open(encoding="utf-8") as fh:
        records = [json.loads(line) for line in fh]
    index = faiss.read_index(str(index_path))
    if index.ntotal != len(records):
        print(f"[!] --incremental: faiss.index has {index.ntotal} vectors but meta.jsonl "
              f"{len(records)} rows; run a full build", file=sys.stderr)
        return None
    return records, index.reconstruct_n(0, index.ntotal)


def cmd_build(args: argparse.Namespace) -> int:
    import shutil
    import tempfile
    import faiss  # type: ignore
    import spacy  # type: ignore

    papers_dir = Path(args.papers_dir)
    pmid_list = _read_pmid_list(Path(args.pmid_list))
    out_dir = Path(args.index_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[*] corpus: {len(pmid_list)} PMIDs from {args.pmid_list}")
    print("[*] loading spaCy (en_core_web_sm) for sentence splitting")
    try:
        # Only sentence boundaries (from the parser) are needed.
        nlp = spacy.load("en_core_web_sm", disable=["ner", "lemmatizer"])
    except OSError:
        print(
            "[!] spaCy model en_core_web_sm not installed. Run:\n"
            "    uv run python -m spacy download en_core_web_sm",
            file=sys.stderr,
        )
        return 2

    kept_records: list[dict] = []
    kept_vecs = None
    todo = pmid_list
    if args.incremental:
        existing = _load_existing(out_dir, args)
        if existing is None:
            return 1
        old_records, old_vecs = existing
        wanted = set(pmid_list)
        keep = [i for i, r in enumerate(old_records) if str(r["pmid"]) in wanted]
        have = {str(old_records[i]["pmid"]) for i in keep}
        todo = [p for p in pmid_list if p not in have]
        kept_records = [old_records[i] for i in keep]
        kept_vecs = old_vecs[keep]
        print(f"[*] incremental: keeping {len(keep)} chunks from {len(have)} papers, "
              f"dropping {len(old_records) - len(keep)}, embedding {len(todo)} new papers")

    print("[*] chunking papers…")
    new_records = iter_chunks(
        papers_dir=papers_dir,
        pmids=todo,
        nlp=nlp,
        chunk_chars=args.chunk_chars,
        overlap=args.overlap,
    )
    records = kept_records + new_records
    if not records:
        print("[!] no chunks produced — aborting", file=sys.stderr)
        return 1
    print(f"[*] {len(new_records)} new chunks; {len(records)} total across {len(pmid_list)} papers")

    # Stage all artifacts in a sibling temp dir and swap them in only
    # after the embedding + FAISS write succeed. Avoids leaving a fresh
    # meta.jsonl next to a stale faiss.index when the build dies
    # mid-embedding (which would mis-map retrieval).
    staging = Path(tempfile.mkdtemp(prefix=".staging-", dir=out_dir.parent))
    try:
        meta_path = staging / "meta.jsonl"
        with meta_path.open("w", encoding="utf-8") as fh:
            for rec in records:
                fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"[*] wrote metadata to {meta_path}")

        texts = [r["text"] for r in new_records]
        print(f"[*] embedding {len(texts)} chunks with {args.embed_model}…")
        embeddings = (
            embed_texts(texts, task_type="RETRIEVAL_DOCUMENT", batch_size=args.batch_size,
                        model=args.embed_model)
            if texts else np.zeros((0, kept_vecs.shape[1]), dtype="float32")
        )
        if kept_vecs is not None:
            embeddings = np.vstack([kept_vecs, embeddings])

        index = faiss.IndexFlatIP(embeddings.shape[1])
        index.add(embeddings)
        index_path = staging / "faiss.index"
        faiss.write_index(index, str(index_path))
        print(f"[*] wrote FAISS index to {index_path}")

        config_path = staging / "index_config.json"
        config_path.write_text(json.dumps({
            "embed_model": args.embed_model,
            "embed_dim": int(embeddings.shape[1]),
            "chunker": _passages.CHUNKER_VERSION,
            "chunk_chars": args.chunk_chars,
            "overlap": args.overlap,
            "n_papers": len(pmid_list),
            "n_chunks": len(records),
            "papers_dir": str(papers_dir),
            "pmid_list": str(args.pmid_list),
        }, indent=2))
        print(f"[*] wrote index config to {config_path}")

        for name in ("meta.jsonl", "faiss.index", "index_config.json"):
            shutil.move(str(staging / name), str(out_dir / name))
    finally:
        shutil.rmtree(staging, ignore_errors=True)

    print(f"[*] published artifacts to {out_dir}")

    # Build the BM25 sidecar from the freshly-published meta.jsonl. Kept
    # coupled to FAISS publication so the two retrievers can't drift —
    # any rebuild of the dense index implies a rebuild of the sparse one.
    print("[*] building BM25 sidecar…")
    from cbio_kb.index import bm25 as _bm25
    _bm25.build_bm25(out_dir)

    print("[✓] done")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build a FAISS index over raw paper markdowns")
    sub = p.add_subparsers(dest="cmd", required=True)

    pb = sub.add_parser("build", help="Build the index")
    pb.add_argument("--papers-dir", default="data/raw/papers")
    pb.add_argument("--pmid-list", default="eval/corpus_pmids.txt")
    pb.add_argument("--index-dir", default="data/paper_index")
    pb.add_argument("--chunk-chars", type=int, default=900)
    pb.add_argument("--overlap", type=int, default=250,
                    help="Max characters of whole trailing sentences each passage repeats")
    pb.add_argument("--batch-size", type=int, default=_BATCH_SIZE)
    pb.add_argument("--embed-model", default=EMBED_MODEL,
                    help="Hugging Face model id (runs locally) or gemini-embedding-001 (Vertex AI)")
    pb.add_argument("--incremental", action="store_true",
                    help="Reuse vectors from the existing index; embed only PMIDs it lacks "
                         "and drop PMIDs no longer in --pmid-list")
    pb.set_defaults(func=cmd_build)

    args = p.parse_args(argv)
    if getattr(args, "batch_size", 1) <= 0:
        p.error("--batch-size must be > 0")
    if getattr(args, "chunk_chars", 1) <= 0:
        p.error("--chunk-chars must be > 0")
    if not 0 <= getattr(args, "overlap", 0) < getattr(args, "chunk_chars", 1):
        p.error("--overlap must be >= 0 and smaller than --chunk-chars")
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
