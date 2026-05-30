"""Tests for the hybrid 3-leg retrieval pipeline.

Covers the pure-Python pieces (RRF fusion, anchor extraction, BM25 build
round-trip, orchestrator parallel dispatch). Vertex AI embedding and
Anthropic synthesis are not exercised here — those are integration concerns.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


# ---------------------------------------------------------------------------
# RRF fusion (pure function — no external deps)
# ---------------------------------------------------------------------------


def _chunk(pmid: str, chunk_id: int, text: str = "x") -> dict:
    return {"pmid": pmid, "chunk_id": chunk_id, "text": text, "score": 0.0}


def test_rrf_fuse_basic_order() -> None:
    pytest.importorskip("rank_bm25")  # hybrid imports it transitively
    from ai_search.hybrid import rrf_fuse

    a = [_chunk("p1", 0), _chunk("p2", 0), _chunk("p3", 0)]
    b = [_chunk("p2", 0), _chunk("p1", 0), _chunk("p4", 0)]
    out = rrf_fuse([a, b], k=60, top_k=10)
    keys = [(c["pmid"], c["chunk_id"]) for c in out]
    # p1 and p2 appear in both lists; p2 has higher combined RRF than p1
    # because it's rank-1 in b and rank-2 in a, vs p1 which is the reverse.
    # Actually both are symmetric — they tie. Tiebreak is dict insertion order
    # (first occurrence). a came first so p1 wins.
    assert keys[0] == ("p1", 0)
    assert keys[1] == ("p2", 0)
    # Singletons p3 (rank 3 in a) and p4 (rank 3 in b) come last, tied.
    assert {keys[2], keys[3]} == {("p3", 0), ("p4", 0)}


def test_rrf_fuse_empty_inputs() -> None:
    pytest.importorskip("rank_bm25")
    from ai_search.hybrid import rrf_fuse

    assert rrf_fuse([], k=60, top_k=5) == []
    assert rrf_fuse([[], [], []], k=60, top_k=5) == []


def test_rrf_fuse_dedupes_by_chunk_key() -> None:
    pytest.importorskip("rank_bm25")
    from ai_search.hybrid import rrf_fuse

    a = [_chunk("p1", 0), _chunk("p1", 1)]
    b = [_chunk("p1", 0), _chunk("p2", 0)]
    out = rrf_fuse([a, b], k=60, top_k=10)
    # (p1, 0) appears in both → highest. Then (p1, 1) and (p2, 0) tie.
    assert len(out) == 3
    assert out[0]["pmid"] == "p1" and out[0]["chunk_id"] == 0
    fused_top = out[0]["fused_score"]
    # Top score includes both lists' rank-1 contributions.
    assert fused_top == pytest.approx(2.0 / 61)


def test_rrf_fuse_carries_fused_score_field() -> None:
    pytest.importorskip("rank_bm25")
    from ai_search.hybrid import rrf_fuse

    out = rrf_fuse([[_chunk("p1", 0)]], k=60, top_k=10)
    assert out[0]["fused_score"] == pytest.approx(1.0 / 61)


# ---------------------------------------------------------------------------
# Anchor gazetteer extraction
# ---------------------------------------------------------------------------


def _build_wiki(root: Path) -> None:
    for kind in ("genes", "cancer_types", "datasets", "drugs", "methods", "papers"):
        (root / kind).mkdir(parents=True, exist_ok=True)
    (root / "genes" / "EGFR.md").write_text(
        "---\nsymbol: EGFR\naliases: [ERBB1, HER1]\n---\n\n# EGFR\n"
    )
    (root / "genes" / "TP53.md").write_text("---\nsymbol: TP53\n---\n\n# TP53\n")
    # A HUGO symbol that collides with an ordinary English word — must be
    # dropped from the gazetteer so it doesn't fire on prose like "we met".
    (root / "genes" / "MET.md").write_text("---\nsymbol: MET\n---\n\n# MET\n")
    (root / "cancer_types" / "NSCLC.md").write_text(
        "---\nname: Non-Small Cell Lung Cancer\n---\n\n# NSCLC\n"
    )
    (root / "drugs" / "sotorasib.md").write_text("---\nname: sotorasib\n---\n")
    # graph.json with minimal edges so GraphIndex can load (used in orchestrator
    # test below; harmless for the anchor-only tests).
    (root / "graph.json").write_text(json.dumps({
        "root": {"id": "index", "label": "Index"},
        "sections": [],
        "nodes": [],
        "tree_edges": [],
        "cross_edges": [
            {"from": "papers/111.md", "to": "genes/EGFR.md"},
            {"from": "papers/111.md", "to": "cancer_types/NSCLC.md"},
            {"from": "papers/222.md", "to": "genes/TP53.md"},
        ],
    }))


def test_extract_anchors_matches_stem(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    from ai_search import anchors

    anchors.build_gazetteer(tmp_path)
    found = anchors.extract_anchors("EGFR resistance in NSCLC patients", tmp_path)
    by_stem = {a.stem for a in found}
    assert "EGFR" in by_stem
    assert "NSCLC" in by_stem


def test_extract_anchors_case_insensitive(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    from ai_search import anchors

    anchors.build_gazetteer(tmp_path)
    found = anchors.extract_anchors("does tp53 status predict response?", tmp_path)
    assert any(a.stem == "TP53" for a in found)


def test_extract_anchors_aliases(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    from ai_search import anchors

    anchors.build_gazetteer(tmp_path)
    found = anchors.extract_anchors("ERBB1 inhibitor toxicity", tmp_path)
    # Alias 'ERBB1' should resolve to the canonical EGFR anchor.
    assert any(a.stem == "EGFR" for a in found)


def test_extract_anchors_word_boundary(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    from ai_search import anchors

    anchors.build_gazetteer(tmp_path)
    # 'TP53BP1' should NOT match 'TP53' because of word boundaries.
    found = anchors.extract_anchors("TP53BP1 is unrelated here", tmp_path)
    assert not any(a.stem == "TP53" for a in found)


def test_extract_anchors_no_match(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    from ai_search import anchors

    anchors.build_gazetteer(tmp_path)
    assert anchors.extract_anchors("how does the immune system work", tmp_path) == []


def test_extract_anchors_drops_common_word_symbols(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    from ai_search import anchors

    anchors.build_gazetteer(tmp_path)
    # "met" is a HUGO symbol (MET) but also a common verb — it must not fire
    # on ordinary prose, otherwise the graph leg fills with noise.
    found = anchors.extract_anchors("the rest of the set we met last time", tmp_path)
    assert found == []


# ---------------------------------------------------------------------------
# BM25 build round-trip
# ---------------------------------------------------------------------------


def _write_meta(index_dir: Path, records: list[dict]) -> None:
    index_dir.mkdir(parents=True, exist_ok=True)
    with (index_dir / "meta.jsonl").open("w") as fh:
        for r in records:
            fh.write(json.dumps(r) + "\n")


def test_bm25_build_writes_artifacts(tmp_path: Path) -> None:
    pytest.importorskip("rank_bm25")
    from cbio_kb.index import bm25

    _write_meta(tmp_path, [
        {"pmid": "1", "chunk_id": 0, "text": "KRAS G12C resistance in lung cancer"},
        {"pmid": "1", "chunk_id": 1, "text": "sotorasib clinical trial outcomes"},
        {"pmid": "2", "chunk_id": 0, "text": "immune checkpoint inhibitor response"},
    ])
    stats = bm25.build_bm25(tmp_path)
    assert (tmp_path / "bm25.pkl").exists()
    assert (tmp_path / "bm25_meta.json").exists()
    assert stats["n_chunks"] == 3
    assert stats["vocab_size"] > 0


def test_bm25_search_round_trip(tmp_path: Path) -> None:
    pytest.importorskip("rank_bm25")
    from cbio_kb.index import bm25
    from ai_search.hybrid import BM25Index

    _write_meta(tmp_path, [
        {"pmid": "1", "chunk_id": 0, "text": "KRAS G12C resistance in lung cancer"},
        {"pmid": "1", "chunk_id": 1, "text": "sotorasib clinical trial outcomes"},
        {"pmid": "2", "chunk_id": 0, "text": "immune checkpoint inhibitor response"},
    ])
    bm25.build_bm25(tmp_path)

    BM25Index._instance = None  # reset singleton between tests
    idx = BM25Index.get(tmp_path)
    hits = idx.search("sotorasib KRAS")
    assert hits, "expected at least one hit for in-corpus terms"
    # Top hit should be one of the KRAS/sotorasib chunks from PMID 1.
    assert hits[0]["pmid"] == "1"


def test_bm25_search_empty_query(tmp_path: Path) -> None:
    pytest.importorskip("rank_bm25")
    from cbio_kb.index import bm25
    from ai_search.hybrid import BM25Index

    _write_meta(tmp_path, [{"pmid": "1", "chunk_id": 0, "text": "lung cancer"}])
    bm25.build_bm25(tmp_path)
    BM25Index._instance = None
    idx = BM25Index.get(tmp_path)
    assert idx.search("") == []
    # All-stopwords query also returns empty.
    assert idx.search("the and of") == []


# ---------------------------------------------------------------------------
# Tokenizer (drops stopwords + 1-char tokens, lowercases)
# ---------------------------------------------------------------------------


def test_tokenize_drops_stopwords_and_lowercases() -> None:
    pytest.importorskip("rank_bm25")
    from cbio_kb.index.bm25 import tokenize

    toks = tokenize("The KRAS G12C is a mutation")
    assert "kras" in toks
    assert "g12c" in toks
    assert "the" not in toks
    assert "is" not in toks
    assert "a" not in toks  # 1-char drop


# ---------------------------------------------------------------------------
# Orchestrator: legs run in parallel, fused output shape is correct
# ---------------------------------------------------------------------------


def test_run_legs_invokes_all_three_in_parallel(monkeypatch, tmp_path: Path) -> None:
    pytest.importorskip("rank_bm25")
    import asyncio
    import threading
    import time as _time

    from ai_search import hybrid

    started: list[str] = []
    started_lock = threading.Lock()
    barrier = threading.Barrier(3, timeout=2.0)

    def _record_and_wait(name: str, ret):
        def _fn(query, top_k):
            with started_lock:
                started.append(name)
            barrier.wait()
            return ret
        return _fn

    monkeypatch.setattr(
        hybrid, "_dense_search",
        _record_and_wait("dense", [_chunk("d", 0)]),
    )
    monkeypatch.setattr(
        hybrid, "_bm25_search",
        _record_and_wait("bm25", [_chunk("b", 0)]),
    )
    def _graph(query, top_k):
        with started_lock:
            started.append("graph")
        barrier.wait()
        return [_chunk("g", 0)], []
    monkeypatch.setattr(hybrid, "_graph_search", _graph)

    legs = asyncio.run(hybrid._run_legs("any query", 10, 10, 10))
    # If they hadn't run in parallel, the barrier would have timed out.
    assert set(started) == {"dense", "bm25", "graph"}
    assert legs["dense"][0][0]["pmid"] == "d"
    assert legs["bm25"][0][0]["pmid"] == "b"
    assert legs["graph"][0][0]["pmid"] == "g"
    assert legs["anchors"] == []
