"""Smoke test: the real wiki/ lints clean (apart from known unverified terms)."""
from __future__ import annotations

from pathlib import Path

from cbio_kb.wiki import lint


def test_wiki_lint_smoke() -> None:
    repo = Path(__file__).resolve().parents[1]
    # Returns 0 on structural success; unverified terms are warnings, not errors.
    rc = lint.run(wiki_dir=repo / "wiki")
    assert rc == 0
