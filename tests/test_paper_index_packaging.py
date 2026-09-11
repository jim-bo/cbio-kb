"""scripts/package_index.sh -> docker/fetch_paper_index.py round trip.

The pair is how the passage index reaches a container without GCP: package it
as a tarball, then unpack it at image build time or in a k8s initContainer.
"""
import hashlib
import importlib.util
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("fetch_paper_index", ROOT / "docker" / "fetch_paper_index.py")
fetch = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fetch)


@pytest.fixture
def tarball(tmp_path: Path) -> Path:
    if shutil.which("bash") is None or shutil.which("tar") is None:
        pytest.skip("needs bash and tar")
    idx = tmp_path / "some_index_dir"
    idx.mkdir()
    (idx / "meta.jsonl").write_text('{"pmid": "1"}\n')
    (idx / "bm25.pkl").write_bytes(b"bm25")
    (idx / "faiss.index").write_bytes(b"faiss")
    (idx / "index_config.json").write_text('{"embed_model": "BAAI/bge-base-en-v1.5"}')
    out = tmp_path / "dist"
    res = subprocess.run(["bash", str(ROOT / "scripts" / "package_index.sh"), str(idx), str(out)],
                         capture_output=True, text=True)
    assert res.returncode == 0, res.stderr
    assert "EMBED_MODEL=BAAI/bge-base-en-v1.5" in res.stdout
    [archive] = out.glob("paper-index-*.tar.gz")
    sha_line = (out / f"{archive.name}.sha256").read_text().split()
    assert sha_line == [hashlib.sha256(archive.read_bytes()).hexdigest(), archive.name]
    return archive


def _sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def test_round_trip_with_checksum(tarball: Path, tmp_path: Path):
    dest = tmp_path / "out"
    assert fetch.main([str(dest), tarball.as_uri(), _sha(tarball)]) == 0
    got = sorted(p.name for p in (dest / "paper_index").iterdir())
    assert got == ["bm25.pkl", "faiss.index", "index_config.json", "meta.jsonl"]
    # Re-running over an existing index (a restarted initContainer) is fine.
    assert fetch.main([str(dest), tarball.as_uri(), _sha(tarball)]) == 0


def test_checksum_mismatch_fails(tarball: Path, tmp_path: Path):
    dest = tmp_path / "out"
    assert fetch.main([str(dest), tarball.as_uri(), "0" * 64]) == 1
    assert not any((dest / "paper_index").iterdir())


def test_no_url_leaves_an_empty_index_dir(tmp_path: Path):
    assert fetch.main([str(tmp_path / "out")]) == 0
    assert (tmp_path / "out" / "paper_index").is_dir()
    assert not any((tmp_path / "out" / "paper_index").iterdir())


def test_package_refuses_an_incomplete_index(tmp_path: Path):
    (tmp_path / "idx").mkdir()
    (tmp_path / "idx" / "meta.jsonl").write_text("{}\n")
    res = subprocess.run(["bash", str(ROOT / "scripts" / "package_index.sh"),
                          str(tmp_path / "idx"), str(tmp_path / "dist")],
                         capture_output=True, text=True)
    assert res.returncode == 1
    assert "bm25.pkl not found" in res.stderr
