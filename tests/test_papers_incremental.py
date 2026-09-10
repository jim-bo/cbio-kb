"""`index build-papers --incremental` keeps existing vectors and embeds only new PMIDs."""
import json

import numpy as np
import pytest

faiss = pytest.importorskip("faiss")
spacy = pytest.importorskip("spacy")

from cbio_kb.index import papers  # noqa: E402

DIM = 4


def _unit(v):
    v = np.asarray(v, dtype="float32")
    return v / np.linalg.norm(v)


def test_incremental_build(tmp_path, monkeypatch):
    index_dir, raw = tmp_path / "idx", tmp_path / "raw"
    index_dir.mkdir()
    raw.mkdir()
    old = [{"pmid": "111", "chunk_id": 0, "text": "dropped paper"},
           {"pmid": "222", "chunk_id": 0, "text": "kept paper"}]
    old_vecs = np.stack([_unit([1, 0, 0, 0]), _unit([0, 1, 0, 0])])
    (index_dir / "meta.jsonl").write_text("".join(json.dumps(r) + "\n" for r in old))
    idx = faiss.IndexFlatIP(DIM)
    idx.add(old_vecs)
    faiss.write_index(idx, str(index_dir / "faiss.index"))
    (index_dir / "index_config.json").write_text(json.dumps(
        {"embed_model": papers.EMBED_MODEL, "chunk_chars": 900, "overlap": 120}))
    (raw / "333.md").write_text("---\npmid: 333\n---\nA new paper. It has two sentences.\n")
    pmid_list = tmp_path / "pmids.txt"
    pmid_list.write_text("222\n333\n")

    def fake_load(_name):
        nlp = spacy.blank("en")
        nlp.add_pipe("sentencizer")
        return nlp

    embedded: list[str] = []

    def fake_embed(texts, **_):
        embedded.extend(texts)
        return np.stack([_unit([0, 0, 1, 0])] * len(texts))

    monkeypatch.setattr(spacy, "load", fake_load)
    monkeypatch.setattr(papers, "embed_texts", fake_embed)
    monkeypatch.setattr("cbio_kb.index.bm25.build_bm25", lambda _d: None)

    rc = papers.main(["build", "--papers-dir", str(raw), "--pmid-list", str(pmid_list),
                      "--index-dir", str(index_dir), "--incremental"])
    assert rc == 0
    meta = [json.loads(line) for line in (index_dir / "meta.jsonl").read_text().splitlines()]
    assert [r["pmid"] for r in meta] == ["222", "333"]
    assert embedded == ["A new paper. It has two sentences."]  # only the new paper
    out = faiss.read_index(str(index_dir / "faiss.index"))
    assert out.ntotal == 2
    np.testing.assert_allclose(out.reconstruct(0), old_vecs[1])  # kept vector reused


def test_incremental_refuses_mismatched_chunking(tmp_path, capsys):
    (tmp_path / "meta.jsonl").write_text("")
    faiss.write_index(faiss.IndexFlatIP(DIM), str(tmp_path / "faiss.index"))
    (tmp_path / "index_config.json").write_text(json.dumps(
        {"embed_model": papers.EMBED_MODEL, "chunk_chars": 500, "overlap": 120}))

    class Args:
        chunk_chars, overlap = 900, 120

    assert papers._load_existing(tmp_path, Args) is None
    assert "run a full build" in capsys.readouterr().err
