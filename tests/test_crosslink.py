"""Tests for the deterministic crosslinker."""
from __future__ import annotations

from pathlib import Path

from cbio_kb.wiki.crosslink import crosslink_file, _load_entities


def _build_wiki(root: Path) -> None:
    for kind in ("genes", "cancer_types", "datasets", "drugs", "methods", "papers"):
        (root / kind).mkdir(parents=True, exist_ok=True)
    (root / "genes" / "TP53.md").write_text("---\nsymbol: TP53\n---\n# TP53\n")
    (root / "genes" / "FGFR3.md").write_text("---\nsymbol: FGFR3\n---\n# FGFR3\n")
    (root / "cancer_types" / "BLCA.md").write_text("---\nname: Bladder\n---\n# BLCA\n")


def test_links_first_occurrence_and_skips_protected(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    paper = tmp_path / "papers" / "1.md"
    paper.write_text(
        "---\ngenes: [TP53]\n---\n\n"
        "# Heading with TP53 (should not link)\n\n"
        "Body mentions TP53 once and again TP53 and BLCA.\n"
        "Also `TP53` in code should not link.\n"
        "```\nTP53 in fenced block\n```\n"
    )
    entities = _load_entities(tmp_path)
    n, new = crosslink_file(paper, entities)
    assert n == 2  # TP53 + BLCA, each first-occurrence only
    # Heading TP53 untouched
    assert "# Heading with TP53 (should not link)" in new
    # Inline-code TP53 untouched
    assert "`TP53`" in new
    # First body TP53 linked
    assert "[TP53](../genes/TP53.md)" in new
    # Second plain TP53 still bare
    assert new.count("[TP53](../genes/TP53.md)") == 1
    assert "[BLCA](../cancer_types/BLCA.md)" in new


def test_family_completion_bug_regression(tmp_path: Path) -> None:
    """FGFR1.md does not exist → crosslinker must not invent a link to it
    even when the text mentions 'pan-FGFR' or 'FGFR1'."""
    _build_wiki(tmp_path)
    paper = tmp_path / "papers" / "2.md"
    paper.write_text(
        "---\n---\n\n"
        "The pan-FGFR inhibitor targets FGFR1, FGFR2, FGFR3, FGFR4.\n"
    )
    entities = _load_entities(tmp_path)
    n, new = crosslink_file(paper, entities)
    # Only FGFR3 exists on disk; nothing else should be linked.
    assert "[FGFR3](../genes/FGFR3.md)" in new
    assert "FGFR1.md" not in new
    assert "FGFR2.md" not in new
    assert "FGFR4.md" not in new
    assert n == 1
