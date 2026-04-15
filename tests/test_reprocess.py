"""Tests for wiki reprocess (frontmatter patching + extraction gap analysis)."""
from __future__ import annotations

from pathlib import Path

from cbio_kb.wiki.reprocess import (
    patch_frontmatter,
    find_extraction_gaps,
    generate_extract_prompt,
    _template_keys,
)


def _build_fixtures(root: Path) -> tuple[Path, Path, Path]:
    """Build minimal wiki + templates + raw dirs. Returns (wiki, templates, raw)."""
    wiki = root / "wiki"
    templates = root / "templates"
    raw = root / "raw"
    for d in (wiki, templates, raw):
        d.mkdir()

    # Template
    templates_paper = templates / "paper.md"
    templates_paper.write_text(
        "---\npmid:\ntitle:\nauthors: []\nyear:\n"
        "cancer_types: []\ngenes: []\ndatasets: []\n"
        "drugs: []\nmethods: []\ntags: []\n"
        "processed_by:\nprocessed_at:\n---\n\n# {{title}}\n"
    )
    templates_gene = templates / "gene.md"
    templates_gene.write_text(
        "---\nsymbol:\naliases: []\ncancer_types: []\n"
        "tags: []\nprocessed_by:\nprocessed_at:\n---\n\n# {{symbol}}\n"
    )

    # Wiki pages
    (wiki / "papers").mkdir()
    (wiki / "genes").mkdir()

    (wiki / "papers" / "111.md").write_text(
        "---\npmid: \"111\"\ntitle: Test Paper\nauthors: [Alice]\n"
        "year: \"2024\"\ncancer_types: [LUAD]\ngenes: [EGFR]\n"
        "datasets: []\ndrugs: []\nmethods: []\ntags: [genomics]\n"
        "processed_by: paper-compiler\nprocessed_at: 2024-01-01\n---\n\n"
        "# Test Paper\n\nBody text.\n"
    )
    # Gene page missing aliases and cancer_types (added by template)
    (wiki / "genes" / "EGFR.md").write_text(
        "---\nsymbol: EGFR\ntags: [oncogene]\n"
        "processed_by: entity-page-writer\nprocessed_at: 2024-01-01\n---\n\n"
        "# EGFR\n"
    )
    # Raw paper
    (raw / "111.md").write_text(
        "---\npmid: 111\n---\n\n## Full Text\n\nSome raw content about EGFR and osimertinib.\n"
    )

    return wiki, templates, raw


# --- _template_keys ---

def test_template_keys(tmp_path: Path) -> None:
    tmpl = tmp_path / "gene.md"
    tmpl.write_text(
        "---\nsymbol:\naliases: []\ncancer_types: []\ntags: []\n"
        "processed_by:\nprocessed_at:\n---\n"
    )
    keys = _template_keys(tmpl)
    assert keys == ["symbol", "aliases", "cancer_types", "tags", "processed_by", "processed_at"]


# --- Tier 1: patch_frontmatter ---

def test_patch_adds_missing_keys(tmp_path: Path) -> None:
    wiki, templates, _ = _build_fixtures(tmp_path)
    results = patch_frontmatter(wiki, templates, sections=["genes"], dry_run=True)
    assert len(results) == 1
    r = results[0]
    assert "aliases" in r["keys_added"]
    assert "cancer_types" in r["keys_added"]


def test_patch_writes_when_not_dry(tmp_path: Path) -> None:
    wiki, templates, _ = _build_fixtures(tmp_path)
    results = patch_frontmatter(wiki, templates, sections=["genes"])
    assert len(results) == 1
    # Verify the file was actually updated
    text = (wiki / "genes" / "EGFR.md").read_text()
    assert "aliases:" in text
    assert "cancer_types:" in text
    # Body preserved
    assert "# EGFR" in text


def test_patch_no_change_when_complete(tmp_path: Path) -> None:
    wiki, templates, _ = _build_fixtures(tmp_path)
    results = patch_frontmatter(wiki, templates, sections=["papers"])
    assert len(results) == 0  # paper already has all template keys


def test_patch_preserves_extra_keys(tmp_path: Path) -> None:
    wiki, templates, _ = _build_fixtures(tmp_path)
    # Add an extra key not in template
    gene = wiki / "genes" / "EGFR.md"
    text = gene.read_text()
    text = text.replace("tags: [oncogene]", "tags: [oncogene]\ncustom_field: hello")
    gene.write_text(text)

    patch_frontmatter(wiki, templates, sections=["genes"])
    new_text = gene.read_text()
    assert "custom_field: hello" in new_text


# --- _KEY_RENAMES (slug → studyId) ---

def _write_dataset_template(templates: Path) -> None:
    (templates / "dataset.md").write_text(
        "---\nname:\nstudyId:\nsize:\n"
        "processed_by:\nprocessed_at:\n---\n\n# {{name}}\n"
    )


def test_rename_slug_to_studyid_when_only_slug(tmp_path: Path) -> None:
    wiki = tmp_path / "wiki"
    templates = tmp_path / "templates"
    (wiki / "datasets").mkdir(parents=True)
    templates.mkdir()
    _write_dataset_template(templates)
    (wiki / "datasets" / "foo.md").write_text(
        "---\nname: Foo Cohort\nslug: foo_cohort\nsize: 42\n"
        "processed_by: x\nprocessed_at: 2024-01-01\n---\n\n# Foo Cohort\n"
    )

    results = patch_frontmatter(wiki, templates, sections=["datasets"])
    assert len(results) == 1
    assert results[0]["keys_renamed"] == ["slug"]

    new_text = (wiki / "datasets" / "foo.md").read_text()
    assert "studyId: foo_cohort" in new_text
    assert "slug:" not in new_text


def test_rename_prefers_existing_studyid_over_empty_slug(tmp_path: Path) -> None:
    """When both slug and studyId exist and studyId is populated, studyId wins."""
    wiki = tmp_path / "wiki"
    templates = tmp_path / "templates"
    (wiki / "datasets").mkdir(parents=True)
    templates.mkdir()
    _write_dataset_template(templates)
    (wiki / "datasets" / "dual.md").write_text(
        "---\nname: Dual\nslug: \nsize: 1\n"
        "processed_by: x\nprocessed_at: 2024-01-01\n"
        "studyId: real_value\n---\n\n# Dual\n"
    )

    patch_frontmatter(wiki, templates, sections=["datasets"])
    new_text = (wiki / "datasets" / "dual.md").read_text()
    assert "studyId: real_value" in new_text
    assert "slug:" not in new_text


def test_rename_migrates_slug_when_studyid_empty(tmp_path: Path) -> None:
    """When both keys exist but studyId is empty, the slug value migrates."""
    wiki = tmp_path / "wiki"
    templates = tmp_path / "templates"
    (wiki / "datasets").mkdir(parents=True)
    templates.mkdir()
    _write_dataset_template(templates)
    (wiki / "datasets" / "partial.md").write_text(
        "---\nname: Partial\nslug: migrate_me\nsize: 1\n"
        "processed_by: x\nprocessed_at: 2024-01-01\n"
        "studyId: \n---\n\n# Partial\n"
    )

    patch_frontmatter(wiki, templates, sections=["datasets"])
    new_text = (wiki / "datasets" / "partial.md").read_text()
    assert "studyId: migrate_me" in new_text
    assert "slug:" not in new_text


# --- Tier 2: find_extraction_gaps ---

def test_find_gaps_detects_empty_lists(tmp_path: Path) -> None:
    wiki, templates, raw = _build_fixtures(tmp_path)
    gaps = find_extraction_gaps(wiki, raw, templates)
    assert len(gaps) == 1
    g = gaps[0]
    assert g["pmid"] == "111"
    assert g["has_raw"]
    gap_fields = [x["field"] for x in g["gaps"]]
    assert "drugs" in gap_fields
    assert "datasets" in gap_fields
    assert "methods" in gap_fields


def test_find_gaps_none_when_complete(tmp_path: Path) -> None:
    wiki, templates, raw = _build_fixtures(tmp_path)
    # Fill in all the empty lists
    paper = wiki / "papers" / "111.md"
    text = paper.read_text()
    text = text.replace("datasets: []", "datasets: [test-dataset]")
    text = text.replace("drugs: []", "drugs: [osimertinib]")
    text = text.replace("methods: []", "methods: [msk-impact-panel]")
    paper.write_text(text)

    gaps = find_extraction_gaps(wiki, raw, templates)
    assert len(gaps) == 0


def test_find_gaps_missing_raw(tmp_path: Path) -> None:
    wiki, templates, raw = _build_fixtures(tmp_path)
    # Add a paper with no raw file
    (wiki / "papers" / "999.md").write_text(
        "---\npmid: \"999\"\ntitle: No Raw\nauthors: []\nyear:\n"
        "cancer_types: []\ngenes: []\ndatasets: []\n"
        "drugs: []\nmethods: []\ntags: []\n"
        "processed_by:\nprocessed_at:\n---\n\n# No Raw\n"
    )
    gaps = find_extraction_gaps(wiki, raw, templates)
    no_raw = [g for g in gaps if g["pmid"] == "999"]
    assert len(no_raw) == 1
    assert not no_raw[0]["has_raw"]


# --- generate_extract_prompt ---

def test_generate_prompt(tmp_path: Path) -> None:
    wiki, templates, raw = _build_fixtures(tmp_path)
    gaps = find_extraction_gaps(wiki, raw, templates)
    prompt = generate_extract_prompt(gaps[0])
    assert "PMID 111" in prompt
    assert "drugs" in prompt
    assert "schema/CLAUDE.md" in prompt
    assert "ontology lookup" in prompt
