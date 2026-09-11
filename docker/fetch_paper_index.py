"""Fetch a packaged passage index and unpack it as <dest>/paper_index/.

    python fetch_paper_index.py DEST [URL] [SHA256]

The tarball is the one scripts/package_index.sh produces: a single top-level
``paper_index/`` directory holding faiss.index, meta.jsonl, bm25.pkl and
index_config.json. With no URL this only creates an empty
``DEST/paper_index`` and exits 0, which leaves the servers in wiki-only mode:
the search tools report the missing index and everything else works.

Used in two places, both standard library only:
  - docker/{mcp,chat}.Dockerfile, to bake an index into an image at build
    time (build args PAPER_INDEX_URL / PAPER_INDEX_SHA256);
  - the optional initContainer in deploy/k8s/mcp.yaml, to fetch one into an
    emptyDir when the pod starts.
"""
from __future__ import annotations

import hashlib
import shutil
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path

REQUIRED = ("meta.jsonl", "bm25.pkl")  # what the servers check for


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0 if argv else 2
    dest = Path(argv[0])
    url = argv[1].strip() if len(argv) > 1 else ""
    want = argv[2].strip().lower() if len(argv) > 2 else ""
    target = dest / "paper_index"
    target.mkdir(parents=True, exist_ok=True)
    if not url:
        print("[paper-index] no URL given; leaving the passage index empty")
        return 0

    with tempfile.TemporaryDirectory() as tmp:
        archive = Path(tmp) / "paper-index.tar.gz"
        digest = hashlib.sha256()
        print(f"[paper-index] downloading {url}")
        with urllib.request.urlopen(url, timeout=600) as resp, archive.open("wb") as out:
            while chunk := resp.read(1 << 20):
                digest.update(chunk)
                out.write(chunk)
        got = digest.hexdigest()
        if want and got != want:
            print(f"[paper-index] sha256 mismatch: expected {want}, got {got}", file=sys.stderr)
            return 1
        print(f"[paper-index] sha256 {got}" + ("" if want else " (not verified)"))

        staging = Path(tmp) / "unpacked"
        with tarfile.open(archive) as tf:
            tf.extractall(staging, filter="data")
        src = staging / "paper_index"
        missing = [f for f in REQUIRED if not (src / f).is_file()]
        if missing:
            print(f"[paper-index] archive has no paper_index/{', paper_index/'.join(missing)}",
                  file=sys.stderr)
            return 1
        for item in src.iterdir():
            if item.name.startswith("._"):  # macOS AppleDouble metadata
                continue
            dst = target / item.name
            if dst.is_dir():
                shutil.rmtree(dst)
            shutil.move(str(item), str(dst))

    print(f"[paper-index] unpacked into {target}: {sorted(p.name for p in target.iterdir())}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
