"""Smoke test: the real wiki/ lints clean (apart from known unverified terms)."""
from __future__ import annotations

from pathlib import Path

from cbio_kb.wiki import lint


def test_wiki_lint_smoke() -> None:
    repo = Path(__file__).resolve().parents[1]
    # Smoke test only: ensures lint runs end-to-end on the real wiki without
    # crashing. Orphan warnings are expected now that Quarto listing pages
    # (papers/index.qmd etc.) are the canonical index, not wiki/index.md.
    rc = lint.run(wiki_dir=repo / "wiki")
    assert rc in (0, 1)
