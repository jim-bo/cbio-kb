"""Tests for the wiki vault CLI (pure-Python Obsidian CLI replacement)."""
from __future__ import annotations

from pathlib import Path

from cbio_kb.wiki import vault


def _build_wiki(root: Path) -> None:
    """Minimal wiki fixture."""
    for kind in ("genes", "cancer_types", "datasets", "drugs", "methods", "papers"):
        (root / kind).mkdir(parents=True, exist_ok=True)

    (root / "genes" / "EGFR.md").write_text(
        "---\nsymbol: EGFR\naliases: []\n"
        "cancer_types:\n  - LUAD\n  - NSCLC\n"
        "tags:\n  - oncogene\n  - targeted-therapy\n"
        "processed_by: crosslinker\nprocessed_at: 2026-04-09\n---\n\n"
        "# EGFR\n\n"
        "## Alterations observed in the corpus\n\n"
        "- L858R activating mutation [PMID:12345678](../papers/12345678.md)\n\n"
        "## Cancer types (linked)\n\n"
        "- [LUAD](../cancer_types/LUAD.md)\n\n"
        "## Sources\n\n"
        "- [PMID:12345678](../papers/12345678.md)\n\n"
        "*This page was processed by **crosslinker** on **2026-04-09**.*\n"
    )
    (root / "genes" / "KRAS.md").write_text(
        "---\nsymbol: KRAS\ntags: [oncogene]\n---\n\n# KRAS\n"
    )
    (root / "cancer_types" / "LUAD.md").write_text(
        "---\nname: Lung Adenocarcinoma\ntags: [nsclc]\n---\n\n"
        "# LUAD\n\n"
        "Mentions [EGFR](../genes/EGFR.md) and [KRAS](../genes/KRAS.md).\n"
    )
    (root / "papers" / "12345678.md").write_text(
        "---\npmid: \"12345678\"\ntitle: Test paper\n"
        "genes: [EGFR, KRAS]\ncancer_types: [LUAD]\n"
        "tags: [genomics]\n---\n\n"
        "# Test paper\n\n## TL;DR\n\nA test.\n\n"
        "## Key findings\n\nEGFR L858R is common.\n"
    )
    (root / "index.md").write_text(
        "# Index\n\n## Papers\n\n- [12345678](papers/12345678.md)\n\n"
        "## Genes\n\n- [EGFR](genes/EGFR.md)\n- [KRAS](genes/KRAS.md)\n\n"
        "## Cancer types\n\n- [LUAD](cancer_types/LUAD.md)\n"
    )


# --- list_files ---

def test_list_files(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    stems = vault.list_files(tmp_path, "genes")
    assert stems == ["EGFR", "KRAS"]


def test_list_files_empty_folder(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    assert vault.list_files(tmp_path, "drugs") == []


def test_list_files_missing_folder(tmp_path: Path) -> None:
    assert vault.list_files(tmp_path, "nonexistent") == []


# --- get_properties ---

def test_properties_scalar_and_list(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    props = vault.get_properties(tmp_path, "genes/EGFR.md")
    assert props["symbol"] == "EGFR"
    assert props["cancer_types"] == ["LUAD", "NSCLC"]
    assert props["tags"] == ["oncogene", "targeted-therapy"]


def test_properties_inline_list(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    props = vault.get_properties(tmp_path, "papers/12345678.md")
    assert props["genes"] == ["EGFR", "KRAS"]
    assert props["pmid"] == "12345678"


def test_properties_file_not_found(tmp_path: Path) -> None:
    result = vault.get_properties(tmp_path, "genes/MISSING.md")
    assert "error" in result


# --- get_property ---

def test_property_single(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    assert vault.get_property(tmp_path, "genes/EGFR.md", "symbol") == "EGFR"
    assert vault.get_property(tmp_path, "genes/EGFR.md", "nonexistent") is None


# --- get_outline ---

def test_outline(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    outline = vault.get_outline(tmp_path, "genes/EGFR.md")
    headings = [h["heading"] for h in outline]
    assert "EGFR" in headings
    assert "Alterations observed in the corpus" in headings
    assert "Sources" in headings
    # Check line numbers are 1-indexed and levels correct
    h1 = [h for h in outline if h["heading"] == "EGFR"][0]
    assert h1["level"] == 1
    assert h1["line"] >= 1
    h2 = [h for h in outline if h["heading"] == "Sources"][0]
    assert h2["level"] == 2


def test_outline_file_not_found(tmp_path: Path) -> None:
    result = vault.get_outline(tmp_path, "genes/MISSING.md")
    assert len(result) == 1 and "error" in result[0]


# --- search_files ---

def test_search_files(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    results = vault.search_files(tmp_path, "L858R")
    assert any("EGFR" in r for r in results)


# --- search_context ---

def test_search_context(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    results = vault.search_context(tmp_path, "L858R", limit=10)
    assert len(results) >= 1
    hit = results[0]
    assert "file" in hit
    assert "line" in hit
    assert "text" in hit
    assert "L858R" in hit["text"]
    assert "before" in hit
    assert "after" in hit


def test_search_context_with_path(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    results = vault.search_context(tmp_path, "L858R", path="genes/EGFR.md")
    assert len(results) >= 1
    assert all(r["file"] == "genes/EGFR.md" for r in results)


def test_search_context_limit(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    results = vault.search_context(tmp_path, "EGFR", limit=2)
    assert len(results) <= 2


# --- find_backlinks ---

def test_backlinks(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    results = vault.find_backlinks(tmp_path, "EGFR")
    sources = [r["source"] for r in results]
    assert "cancer_types/LUAD.md" in sources
    assert "papers/12345678.md" not in sources  # paper links via ../papers/, not ../genes/EGFR.md


# --- find_links ---

def test_links(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    links = vault.find_links(tmp_path, "cancer_types/LUAD.md")
    assert "../genes/EGFR.md" in links
    assert "../genes/KRAS.md" in links


def test_links_file_not_found(tmp_path: Path) -> None:
    assert vault.find_links(tmp_path, "missing.md") == []


# --- find_by_tag ---

def test_find_by_tag(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    results = vault.find_by_tag(tmp_path, "oncogene")
    assert "genes/EGFR.md" in results
    assert "genes/KRAS.md" in results


def test_find_by_tag_no_matches(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    assert vault.find_by_tag(tmp_path, "nonexistent-tag") == []


# --- find_unresolved ---

def test_find_unresolved_none(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    results = vault.find_unresolved(tmp_path)
    # EGFR page links to papers/12345678.md which exists
    broken = [r for r in results if r["source"] == "genes/EGFR.md"]
    # The cancer_types/LUAD.md link is valid
    assert not any(r["target"] == "genes/EGFR.md" for r in results)


def test_find_unresolved_with_broken(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    # Add a broken link
    broken_page = tmp_path / "papers" / "99999999.md"
    broken_page.write_text(
        "---\npmid: \"99999999\"\ntitle: Broken\n---\n\n"
        "See [missing gene](../genes/MISSING.md)\n"
    )
    results = vault.find_unresolved(tmp_path)
    assert any(r["target"] == "genes/MISSING.md" for r in results)


# --- find_orphans ---

def test_find_orphans(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    # LUAD is in index.md, so not orphaned
    orphans = vault.find_orphans(tmp_path)
    assert "cancer_types/LUAD.md" not in orphans


def test_find_orphans_detects_unlisted(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    # Add a page not in index.md
    (tmp_path / "themes").mkdir(exist_ok=True)
    (tmp_path / "themes" / "test-theme.md").write_text(
        "---\ntitle: Test theme\n---\n\n# Test\n"
    )
    orphans = vault.find_orphans(tmp_path)
    assert "themes/test-theme.md" in orphans


# --- find_deadends ---

def test_find_deadends(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    deadends = vault.find_deadends(tmp_path)
    # KRAS.md has no outgoing links
    assert "genes/KRAS.md" in deadends
    # LUAD.md has outgoing links
    assert "cancer_types/LUAD.md" not in deadends


# --- reload ---

def test_reload() -> None:
    result = vault.reload()
    assert result == {"ok": True}


# --- build_index ---

def test_build_index_counts(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    template = tmp_path / "template.md"
    template.write_text(
        "# Index\n\n"
        "Papers: ${papers_count}, Genes: ${genes_count}, "
        "Cancer types: ${cancer_types_count}\n"
    )
    result = vault.build_index(tmp_path, template)
    assert "Papers: 1" in result
    assert "Genes: 2" in result
    assert "Cancer types: 1" in result


def test_build_index_entity_lists(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    template = tmp_path / "template.md"
    template.write_text("## Genes\n\n${genes_list}\n\n## Papers\n\n${papers_list}\n")
    result = vault.build_index(tmp_path, template)
    # Genes use compact inline format
    assert "[EGFR](genes/EGFR.md)" in result
    assert "[KRAS](genes/KRAS.md)" in result
    assert " · " in result  # separator
    # Paper links use bullet format with title
    assert "- [12345678](papers/12345678.md)" in result
    assert "Test paper" in result


def test_build_index_missing_section(tmp_path: Path) -> None:
    _build_wiki(tmp_path)
    template = tmp_path / "template.md"
    template.write_text("Themes: ${themes_count}\n${themes_list}\n")
    result = vault.build_index(tmp_path, template)
    # themes dir doesn't exist in fixture
    assert "Themes: 0" in result
