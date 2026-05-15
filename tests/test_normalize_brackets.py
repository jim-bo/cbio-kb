"""Tests for the deterministic bracket normalizer."""
from __future__ import annotations

from pathlib import Path

from cbio_kb.wiki.normalize_brackets import (
    _existing_pages_per_kind,
    normalize_text,
    run,
)


def _build_wiki(root: Path) -> None:
    for kind in ("genes", "cancer_types", "datasets", "drugs", "methods", "papers"):
        (root / kind).mkdir(parents=True, exist_ok=True)
    (root / "genes" / "TP53.md").write_text("---\nsymbol: TP53\n---\n")
    (root / "genes" / "NFIB.md").write_text("---\nsymbol: NFIB\n---\n")
    (root / "cancer_types" / "GBM.md").write_text("---\nname: GBM\n---\n")
    (root / "datasets" / "difg_glass.md").write_text("---\nname: glass\n---\n")


def test_repairs_unbalanced_double_open(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    pages = _existing_pages_per_kind(tmp_path)
    text = "see [[TP53](../genes/TP53.md) signalling axis"
    out, counts = normalize_text(text, pages)
    assert out == "see [TP53](../genes/TP53.md) signalling axis"
    assert counts == {"dangerous": 1, "bare": 0}


def test_repairs_triple_bracket(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    pages = _existing_pages_per_kind(tmp_path)
    text = "**[[[TP53](../genes/TP53.md)]]** mutated"
    out, counts = normalize_text(text, pages)
    assert out == "**[TP53](../genes/TP53.md)** mutated"
    assert counts["dangerous"] == 1


def test_repairs_pipe_alias(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    pages = _existing_pages_per_kind(tmp_path)
    text = "[[[TP53](../genes/TP53.md)|p53]] mutation"
    out, counts = normalize_text(text, pages)
    assert out == "[p53](../genes/TP53.md) mutation"
    assert counts["dangerous"] == 1


def test_repairs_target_pipe_with_inner_link(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    pages = _existing_pages_per_kind(tmp_path)
    text = "Dataset: [[../datasets/difg_glass.md|[difg_glass](../datasets/difg_glass.md)]] used"
    out, counts = normalize_text(text, pages)
    assert out == "Dataset: [difg_glass](../datasets/difg_glass.md) used"
    assert counts["dangerous"] == 1


def test_repairs_double_close(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    pages = _existing_pages_per_kind(tmp_path)
    text = "[[KRAS](../genes/KRAS.md)] / [[TP53](../genes/TP53.md)]"
    out, counts = normalize_text(text, pages)
    # KRAS doesn't exist in our test wiki; dangerous-pattern fix only cares
    # about the bracket shape, not whether the target page exists.
    assert "[KRAS](../genes/KRAS.md)" in out
    assert "[TP53](../genes/TP53.md)" in out
    assert "[[" not in out
    assert counts["dangerous"] == 2


def test_resolves_bare_with_section(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    pages = _existing_pages_per_kind(tmp_path)
    text = "Cancer: [[cancer_types/GBM]] is common"
    out, counts = normalize_text(text, pages)
    assert out == "Cancer: [GBM](../cancer_types/GBM.md) is common"
    assert counts == {"dangerous": 0, "bare": 1}


def test_resolves_bare_unqualified_when_page_exists(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    pages = _existing_pages_per_kind(tmp_path)
    text = "[[NFIB]] amplifications co-occurred"
    out, counts = normalize_text(text, pages)
    assert out == "[NFIB](../genes/NFIB.md) amplifications co-occurred"
    assert counts == {"dangerous": 0, "bare": 1}


def test_leaves_bare_alone_when_page_missing(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    pages = _existing_pages_per_kind(tmp_path)
    text = "[[NOTAREALGENE]] mentioned"
    out, counts = normalize_text(text, pages)
    assert out == text  # untouched
    assert counts == {"dangerous": 0, "bare": 0}


def test_idempotent(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    pages = _existing_pages_per_kind(tmp_path)
    text = "**[[[TP53](../genes/TP53.md)]]** and bare [[NFIB]] and [[cancer_types/GBM]]"
    once, _ = normalize_text(text, pages)
    twice, counts = normalize_text(once, pages)
    assert once == twice
    assert counts == {"dangerous": 0, "bare": 0}


def test_run_writes_in_place(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    paper = tmp_path / "papers" / "1.md"
    paper.write_text(
        "---\npmid: 1\n---\n\n"
        "**[[[TP53](../genes/TP53.md)]]** in [[NFIB]]-rearranged tumors.\n"
    )
    rc = run(tmp_path, paths=[paper])
    assert rc == 0
    new = paper.read_text()
    assert "**[TP53](../genes/TP53.md)** in [NFIB](../genes/NFIB.md)" in new
    assert "[[" not in new
