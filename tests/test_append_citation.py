"""Tests for cbio_kb.wiki.append_citation."""
from pathlib import Path
from textwrap import dedent

import pytest

from cbio_kb.wiki.append_citation import run


@pytest.fixture
def wiki_dir(tmp_path):
    """Create a minimal wiki with one gene page."""
    genes = tmp_path / "genes"
    genes.mkdir()
    (genes / "TP53.md").write_text(dedent("""\
        ---
        symbol: TP53
        aliases: []
        cancer_types: [LUAD]
        tags: []
        processed_by: entity-page-writer
        processed_at: 2026-01-01
        ---

        # TP53

        ## Overview

        Tumor suppressor.

        ## Alterations observed in the corpus

        - Missense mutations (R175H, R248W) in lung adenocarcinoma [PMID:11111111](../papers/11111111.md)

        ## Sources

        - [PMID:11111111](../papers/11111111.md)

        *This page was processed by **entity-page-writer** on **2026-01-01**.*
    """))
    return tmp_path


def test_append_new_pmid(wiki_dir):
    result = run(
        wiki_dir=wiki_dir,
        kind="gene",
        entity_id="TP53",
        pmid="22222222",
        bullet="Truncating mutations in BRCA1 co-occur with TP53 loss [PMID:22222222](../papers/22222222.md)",
    )
    assert result["action"] == "appended"
    assert result["exit_code"] == 0

    text = (wiki_dir / "genes" / "TP53.md").read_text()
    assert "PMID:22222222" in text
    assert "Truncating mutations" in text
    assert "processed_by: wiki-cli" in text
    assert "**wiki-cli**" in text


def test_idempotent_skip(wiki_dir):
    result = run(
        wiki_dir=wiki_dir,
        kind="gene",
        entity_id="TP53",
        pmid="11111111",
        bullet="duplicate",
    )
    assert result["action"] == "skipped"
    assert result["reason"] == "pmid_present"
    assert result["exit_code"] == 0


def test_missing_page(wiki_dir):
    result = run(
        wiki_dir=wiki_dir,
        kind="gene",
        entity_id="NONEXISTENT",
        pmid="33333333",
        bullet="test",
    )
    assert result["action"] == "error"
    assert result["reason"] == "page_not_found"
    assert result["exit_code"] == 1


def test_missing_section(wiki_dir):
    result = run(
        wiki_dir=wiki_dir,
        kind="gene",
        entity_id="TP53",
        pmid="44444444",
        bullet="test",
        section="Nonexistent Section",
    )
    assert result["action"] == "error"
    assert "section_not_found" in result["reason"]
    assert result["exit_code"] == 1


def test_sources_entry_added(wiki_dir):
    run(
        wiki_dir=wiki_dir,
        kind="gene",
        entity_id="TP53",
        pmid="55555555",
        bullet="GOF p53 in PDAC [PMID:55555555](../papers/55555555.md)",
    )
    text = (wiki_dir / "genes" / "TP53.md").read_text()
    assert "- [PMID:55555555](../papers/55555555.md)" in text
