"""Markdown-paper indexer for the RAG-vs-agentic comparison.

Walks ``data/raw/papers/{pmid}.md`` for a restricted PMID set, strips YAML
frontmatter, chunks by sentence windows, embeds via Google Vertex AI
(``gemini-embedding-001``), and writes ``faiss.index`` + ``meta.jsonl``
so the RAG runner can query over the same corpus the agentic runner walks.

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
import os
import re
import sys
import time
from pathlib import Path
from typing import Iterable

import numpy as np

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

EMBED_MODEL = "gemini-embedding-001"
# GCP_PROJECT is required — embedding runs are billed, so we refuse to
# silently fall back to whatever project happened to be cached locally.
# Resolved at call time inside embed_texts so the import path stays cheap.
GCP_LOCATION = os.environ.get("GCP_LOCATION", "us-central1")
_VERTEX_BATCH_SIZE = 25  # keep well under per-minute token quota


def _require_gcp_project() -> str:
    project = os.environ.get("GCP_PROJECT")
    if not project:
        raise RuntimeError(
            "GCP_PROJECT is not set. Embedding via Vertex AI is a paid "
            "operation; export GCP_PROJECT explicitly before running."
        )
    return project


def _strip_frontmatter(text: str) -> str:
    m = _FRONTMATTER_RE.match(text)
    return text[m.end():] if m else text


def _read_pmid_list(path: Path) -> list[str]:
    return [ln.strip() for ln in path.read_text().splitlines() if ln.strip()]


def _chunk_sentences(nlp, text: str, target_chars: int, overlap: int) -> list[str]:
    doc = nlp(text)
    sents = [s.text.strip() for s in doc.sents if s.text.strip()]
    chunks: list[str] = []
    cur: list[str] = []
    cur_len = 0
    for s in sents:
        if cur and cur_len + len(s) > target_chars:
            chunk = " ".join(cur)
            chunks.append(chunk)
            tail = chunk[-overlap:] if overlap > 0 else ""
            cur = [tail, s] if tail else [s]
            cur_len = len(" ".join(cur))
        else:
            cur.append(s)
            cur_len += len(s)
    if cur:
        chunks.append(" ".join(cur))
    if not chunks and text.strip():
        chunks = [text[:target_chars]]
    return chunks


def embed_texts(
    texts: list[str],
    *,
    task_type: str = "RETRIEVAL_DOCUMENT",
    batch_size: int = _VERTEX_BATCH_SIZE,
) -> np.ndarray:
    """Embed a list of texts via Vertex AI gemini-embedding-001.

    Returns an (N, dim) float32 array, L2-normalized for cosine/IP search.
    """
    from google import genai
    from google.genai import types

    client = genai.Client(vertexai=True, project=_require_gcp_project(), location=GCP_LOCATION)
    all_vecs: list[list[float]] = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        for attempt in range(5):
            try:
                resp = client.models.embed_content(
                    model=EMBED_MODEL,
                    contents=batch,
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
        for emb in resp.embeddings:
            all_vecs.append(emb.values)
        done = min(i + batch_size, len(texts))
        print(f"  embedded {done}/{len(texts)}", file=sys.stderr)
        if done < len(texts):
            time.sleep(2)

    arr = np.array(all_vecs, dtype="float32")
    norms = np.linalg.norm(arr, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return arr / norms


def iter_chunks(
    papers_dir: Path,
    pmids: Iterable[str],
    nlp,
    chunk_chars: int,
    overlap: int,
) -> list[dict]:
    records: list[dict] = []
    for pmid in pmids:
        fpath = papers_dir / f"{pmid}.md"
        if not fpath.exists():
            print(f"[!] missing raw paper: {fpath}", file=sys.stderr)
            continue
        body = _strip_frontmatter(fpath.read_text())
        for idx, chunk in enumerate(
            _chunk_sentences(nlp, body, target_chars=chunk_chars, overlap=overlap)
        ):
            records.append({
                "pmid": pmid,
                "chunk_id": idx,
                "text": chunk,
            })
    return records


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
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        print(
            "[!] spaCy model en_core_web_sm not installed. Run:\n"
            "    uv run python -m spacy download en_core_web_sm",
            file=sys.stderr,
        )
        return 2

    print("[*] chunking papers…")
    records = iter_chunks(
        papers_dir=papers_dir,
        pmids=pmid_list,
        nlp=nlp,
        chunk_chars=args.chunk_chars,
        overlap=args.overlap,
    )
    if not records:
        print("[!] no chunks produced — aborting", file=sys.stderr)
        return 1
    print(f"[*] produced {len(records)} chunks across {len(pmid_list)} papers")

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

        texts = [r["text"] for r in records]
        print(f"[*] embedding {len(texts)} chunks via Vertex AI ({EMBED_MODEL})…")
        embeddings = embed_texts(texts, task_type="RETRIEVAL_DOCUMENT", batch_size=args.batch_size)

        index = faiss.IndexFlatIP(embeddings.shape[1])
        index.add(embeddings)
        index_path = staging / "faiss.index"
        faiss.write_index(index, str(index_path))
        print(f"[*] wrote FAISS index to {index_path}")

        config_path = staging / "index_config.json"
        config_path.write_text(json.dumps({
            "embed_model": EMBED_MODEL,
            "embed_dim": int(embeddings.shape[1]),
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
    pb.add_argument("--overlap", type=int, default=120)
    pb.add_argument("--batch-size", type=int, default=_VERTEX_BATCH_SIZE)
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
