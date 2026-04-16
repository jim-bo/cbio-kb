"""Wiki linter: frontmatter, broken links, orphans, missing required sections,
and ontology validation against schema/ontology/*.json (cBioPortal + OncoTree).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from cbio_kb.ontology import lookup as ontology
from cbio_kb.wiki.vault import _parse_frontmatter, _LINK_RE as LINK_RE, _FRONTMATTER_RE as FRONTMATTER_RE

REQUIRED_FRONTMATTER = {
    "papers": {"pmid", "title"},
    "genes": {"symbol"},
    "cancer_types": {"name", "oncotree_code"},
    "datasets": {"name", "studyId"},
    "drugs": {"name"},
    "methods": {"name"},
    "themes": {"title"},
}


def _parse_list_field(text: str, field: str) -> list[str]:
    """Pull a YAML-ish list out of frontmatter. Handles inline `[a, b]` and
    block `- a\n- b` forms."""
    fm_match = FRONTMATTER_RE.match(text)
    if not fm_match:
        return []
    fm = fm_match.group(1)
    inline = re.search(rf"^{field}:\s*\[(.*?)\]\s*$", fm, re.MULTILINE)
    if inline:
        return [s.strip().strip('"\'') for s in inline.group(1).split(",") if s.strip()]
    block = re.search(rf"^{field}:\s*\n((?:\s+-\s+.*\n?)+)", fm, re.MULTILINE)
    if block:
        return [
            line.strip().lstrip("-").strip().strip('"\'')
            for line in block.group(1).splitlines()
            if line.strip().startswith("-")
        ]
    return []


def run(wiki_dir: Path, allow_orphans: bool = False) -> int:
    if not wiki_dir.exists():
        print(f"[!] wiki dir not found: {wiki_dir}")
        return 1

    repo_root = wiki_dir.parent
    canonical = ontology.load_canonical(repo_root / "schema" / "ontology")

    ENTITY_DIRS = {"genes", "cancer_types", "datasets", "drugs", "methods", "themes"}
    errors: list[str] = []
    warnings: list[str] = []
    stubs_needed: set[str] = set()
    unverified: list[str] = []
    all_pages = {p.relative_to(wiki_dir).as_posix(): p for p in wiki_dir.rglob("*.md")}

    for rel, path in sorted(all_pages.items()):
        text = path.read_text()
        fm = _parse_frontmatter(text)
        section = rel.split("/", 1)[0]
        if section in REQUIRED_FRONTMATTER:
            missing = REQUIRED_FRONTMATTER[section] - {k for k, v in fm.items() if v}
            if missing:
                errors.append(f"{rel}: missing frontmatter {sorted(missing)}")

        if section == "datasets":
            if "reference_genome" not in fm or not fm["reference_genome"]:
                warnings.append(f"{rel}: missing reference_genome")
        if section in {"datasets", "methods", "drugs"}:
            if "canonical_source" not in fm:
                warnings.append(f"{rel}: missing canonical_source")
            if "unverified" not in fm:
                warnings.append(f"{rel}: missing unverified flag")

        for href in LINK_RE.findall(text):
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = (path.parent / href).resolve()
            try:
                target_rel = target.relative_to(wiki_dir.resolve()).as_posix()
            except ValueError:
                continue
            if target_rel not in all_pages and not target.exists():
                first_seg = target_rel.split("/", 1)[0]
                if first_seg in ENTITY_DIRS:
                    stubs_needed.add(target_rel)
                else:
                    errors.append(f"{rel}: broken link -> {href}")

    index = wiki_dir / "index.md"
    if index.exists():
        index_text = index.read_text()
        # Sections whose per-section index.qmd uses a Quarto listing with
        # `contents: "*.md"` auto-include every page in the directory, so any
        # page under such a section is reachable from the site even if not
        # named in the top-level index.md.
        listed_sections: set[str] = set()
        for qmd in wiki_dir.glob("*/index.qmd"):
            qtext = qmd.read_text()
            if re.search(r"contents:\s*\"?\*\.md\"?", qtext):
                listed_sections.add(qmd.parent.name)
        for rel in all_pages:
            if rel == "index.md":
                continue
            section = rel.split("/", 1)[0]
            if section in listed_sections:
                continue
            stem = Path(rel).stem
            if stem not in index_text and rel not in index_text:
                msg = f"orphan (not in index.md): {rel}"
                if allow_orphans:
                    warnings.append(msg)
                else:
                    errors.append(msg)

    # Ontology validation against cBioPortal canonical lists
    field_to_canon = {
        "genes": "genes",
        "cancer_types": "cancer_types",
        "datasets": "datasets",
        "assays": "assays",
        "panels": "gene_panels",
        "clinical_fields": "clinical_attributes",
    }
    
    for rel, path in sorted(all_pages.items()):
        text = path.read_text()
        fm = _parse_frontmatter(text)
        
        section = rel.split("/", 1)[0]
        is_unverified = fm.get("unverified", "").lower() == "true"
        
        if section == "methods":
            kind = fm.get("kind")
            if kind and not is_unverified:
                known_kinds = canonical.get("molecular_profiles", set()) | canonical.get("gene_panels", set()) | canonical.get("assays", set())
                known_kinds.update({"method", "gene-panel", "sequencing"})
                if kind not in known_kinds:
                    warnings.append(f"{rel}: kind '{kind}' not canonical, but unverified is not true")

        if section == "datasets":
            for field in ["assays", "panels", "clinical_fields"]:
                canon = canonical.get(field_to_canon.get(field))
                if not canon:
                    continue
                for value in _parse_list_field(text, field):
                    if value not in canon and not is_unverified:
                         warnings.append(f"{rel}: {field}={value} not canonical, but unverified is not true")

        if not rel.startswith("papers/"):
            continue
            
        for field, canon_key in field_to_canon.items():
            if field in ["assays", "clinical_fields"]: continue
            canon = canonical.get(canon_key)
            if not canon:
                continue
            for value in _parse_list_field(text, field):
                if value not in canon:
                    unverified.append(f"{rel}: {field}={value} (not in cbioportal canonical)")

    for w in warnings:
        print(f"[warn] {w}")
    for e in errors:
        print(f"[err] {e}")
    if stubs_needed:
        print(f"\n[stubs] {len(stubs_needed)} entity page(s) referenced but not yet created:")
        for s in sorted(stubs_needed):
            print(f"  {s}")
    if unverified:
        print(f"\n[unverified] {len(unverified)} non-canonical term(s) — corpus-grown, promote via _observed.md:")
        for u in unverified:
            print(f"  {u}")

    if errors:
        print(
            f"\n[lint] {len(errors)} structural issue(s), {len(warnings)} warning(s), {len(stubs_needed)} stub(s), "
            f"{len(unverified)} unverified term(s)"
        )
        return 1
    print(
        f"[lint] ok ({len(warnings)} warning(s), {len(stubs_needed)} stub(s), {len(unverified)} unverified term(s))"
    )
    return 0
