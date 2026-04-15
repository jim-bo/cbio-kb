"""Reprocess wiki pages after ontology or template changes.

Two tiers:

Tier 1 — ``frontmatter``: deterministic.  Reads each wiki page and its
matching template, adds missing frontmatter keys with empty defaults,
removes keys not in the template, and reorders to match the template.
No LLM needed.

Tier 2 — ``extract``: generates a delta-extraction report.  Compares each
paper page's frontmatter against the current template and the raw paper,
identifies gaps (empty entity lists, missing fields that the raw text
could fill), and emits a JSON manifest the orchestrator can feed to a
sonnet-level agent for targeted re-extraction — much cheaper than a full
recompile.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from cbio_kb.wiki.vault import _parse_frontmatter, _FRONTMATTER_RE

# Section → template file mapping
_SECTION_TEMPLATE = {
    "papers": "paper.md",
    "genes": "gene.md",
    "cancer_types": "cancer_type.md",
    "datasets": "dataset.md",
    "drugs": "drug.md",
    "methods": "method.md",
    "themes": "theme.md",
}

# Frontmatter key renames applied during reprocessing (old → new).
# If both keys coexist, the new-key value wins when it is non-empty,
# otherwise the old-key value migrates over. The old key is dropped.
_KEY_RENAMES = {
    "slug": "studyId",
}


def _apply_key_renames(existing: dict) -> list[str]:
    """Rename legacy keys in-place per ``_KEY_RENAMES``. Returns the list of
    old-key names that were present (useful to signal that a page needs patching
    even when the template-ordered key set looks unchanged)."""
    renamed: list[str] = []
    for old_k, new_k in _KEY_RENAMES.items():
        if old_k not in existing:
            continue
        old_val = existing.pop(old_k)
        if not existing.get(new_k):
            existing[new_k] = old_val
        renamed.append(old_k)
    return renamed


def _template_keys(template_path: Path) -> list[str]:
    """Return the ordered list of frontmatter keys from a template."""
    text = template_path.read_text()
    fm = _parse_frontmatter(text)
    # Preserve insertion order from the raw YAML to maintain template ordering
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return list(fm.keys())
    keys: list[str] = []
    for line in m.group(1).splitlines():
        if ":" in line:
            key = line.partition(":")[0].strip()
            if key and not line.startswith(" ") and not line.startswith("\t"):
                keys.append(key)
    return keys


def _serialize_value(val) -> str:
    """Serialize a frontmatter value back to YAML-ish text."""
    if isinstance(val, list):
        if not val:
            return "[]"
        # Short lists inline, long lists block
        if all(isinstance(v, str) and len(v) < 40 for v in val) and len(val) <= 5:
            items = ", ".join(f'"{v}"' if " " in v else v for v in val)
            return f"[{items}]"
        lines = [f"  - {v}" for v in val]
        return "\n" + "\n".join(lines)
    if val == "":
        return ""
    return str(val)


def _rebuild_frontmatter(
    existing: dict, template_keys: list[str], *, keep_extra: bool = False
) -> str:
    """Rebuild frontmatter YAML with template key order, adding missing keys."""
    lines: list[str] = []
    seen: set[str] = set()
    for key in template_keys:
        seen.add(key)
        val = existing.get(key, "" if key not in ("tags", "aliases", "cancer_types",
                                                    "genes", "datasets", "drugs",
                                                    "methods", "authors", "targets",
                                                    "assays", "panels") else [])
        if isinstance(val, list) and not val:
            # Check if the template default is a list
            val = existing.get(key, [])
            if not isinstance(val, list):
                val = [val] if val else []
        serialized = _serialize_value(val)
        if "\n" in serialized:
            lines.append(f"{key}:{serialized}")
        else:
            lines.append(f"{key}: {serialized}")

    if keep_extra:
        for key, val in existing.items():
            if key not in seen:
                serialized = _serialize_value(val)
                if "\n" in serialized:
                    lines.append(f"{key}:{serialized}")
                else:
                    lines.append(f"{key}: {serialized}")

    return "---\n" + "\n".join(lines) + "\n---"


def patch_frontmatter(
    wiki_dir: Path,
    template_dir: Path,
    *,
    sections: list[str] | None = None,
    dry_run: bool = False,
) -> list[dict]:
    """Tier 1: deterministic frontmatter patching.

    For each wiki page, ensure its frontmatter has exactly the keys from the
    matching template, in template order, with missing keys added (empty default)
    and extra keys preserved at the end.

    Returns a list of ``{path, action, keys_added, keys_reordered}`` dicts.
    """
    target_sections = sections or list(_SECTION_TEMPLATE.keys())
    results: list[dict] = []

    for section in target_sections:
        tmpl_name = _SECTION_TEMPLATE.get(section)
        if not tmpl_name:
            continue
        tmpl_path = template_dir / tmpl_name
        if not tmpl_path.exists():
            continue

        tmpl_keys = _template_keys(tmpl_path)
        folder = wiki_dir / section
        if not folder.is_dir():
            continue

        for page in sorted(folder.glob("*.md")):
            if page.name == "index.md":
                continue
            text = page.read_text()
            existing = _parse_frontmatter(text)
            if not existing and not text.startswith("---"):
                continue  # skip non-frontmatter files

            keys_renamed = _apply_key_renames(existing)

            # Detect changes needed
            existing_keys = list(existing.keys())
            keys_added = [k for k in tmpl_keys if k not in existing]
            needs_reorder = existing_keys != [k for k in tmpl_keys if k in existing_keys]

            if not keys_added and not needs_reorder and not keys_renamed:
                continue

            new_fm = _rebuild_frontmatter(existing, tmpl_keys, keep_extra=True)

            # Replace old frontmatter with new
            m = _FRONTMATTER_RE.match(text)
            if m:
                body = text[m.end():]
            else:
                body = "\n" + text
            new_text = new_fm + body

            result = {
                "path": str(page.relative_to(wiki_dir.parent)),
                "keys_added": keys_added,
                "keys_renamed": keys_renamed,
                "reordered": needs_reorder,
            }
            results.append(result)

            if not dry_run:
                page.write_text(new_text)

    return results


def find_extraction_gaps(
    wiki_dir: Path,
    raw_dir: Path,
    template_dir: Path,
) -> list[dict]:
    """Tier 2: identify papers that need delta extraction.

    Compares each paper page's frontmatter against the template to find
    empty entity-list fields that the raw paper text likely contains data for.

    Returns a manifest: ``[{pmid, path, raw_path, gaps: [{field, reason}]}]``.
    """
    tmpl_path = template_dir / "paper.md"
    if not tmpl_path.exists():
        return []
    tmpl_keys = _template_keys(tmpl_path)

    # Entity list fields that could be populated from raw text
    entity_fields = {"genes", "cancer_types", "datasets", "drugs", "methods", "tags"}

    papers_dir = wiki_dir / "papers"
    if not papers_dir.is_dir():
        return []

    results: list[dict] = []
    for page in sorted(papers_dir.glob("*.md")):
        if page.name == "index.md":
            continue
        pmid = page.stem
        raw_path = raw_dir / f"{pmid}.md"

        fm = _parse_frontmatter(page.read_text())
        gaps: list[dict] = []

        # Check for missing template keys
        for key in tmpl_keys:
            if key not in fm:
                gaps.append({"field": key, "reason": "missing_field"})

        # Check for empty entity lists that might have data in raw
        for field in entity_fields:
            val = fm.get(field, [])
            if isinstance(val, str):
                val = [v.strip() for v in val.split(",") if v.strip()] if val else []
            if not val:
                gaps.append({"field": field, "reason": "empty_list"})

        if gaps:
            entry: dict = {
                "pmid": pmid,
                "path": str(page.relative_to(wiki_dir.parent)),
                "gaps": gaps,
            }
            if raw_path.exists():
                entry["raw_path"] = str(raw_path)
                entry["has_raw"] = True
            else:
                entry["has_raw"] = False
            results.append(entry)

    return results


def generate_extract_prompt(gap_entry: dict) -> str:
    """Generate a focused prompt for a sonnet-level agent to fill gaps.

    Given one entry from ``find_extraction_gaps()``, produce a prompt that
    asks the agent to read the raw paper + existing wiki page and fill in
    only the missing fields — not rewrite the whole page.
    """
    pmid = gap_entry["pmid"]
    gaps = gap_entry["gaps"]
    gap_fields = sorted(set(g["field"] for g in gaps))

    prompt = f"""You are doing a targeted re-extraction on PMID {pmid}.

The existing wiki page at wiki/papers/{pmid}.md is mostly complete, but the
following frontmatter fields are empty or missing and need to be filled:

{chr(10).join(f'- {f}' for f in gap_fields)}

## Steps

1. Read `schema/CLAUDE.md` for hard rules.
2. Read the raw paper at data/raw/papers/{pmid}.md for source text.
3. Read the existing wiki page at wiki/papers/{pmid}.md.
4. For each gap field listed above:
   - Extract the relevant values from the raw paper text.
   - Validate entity slugs with `uv run cbio-kb ontology lookup "<slug>"`.
   - Update ONLY the frontmatter of the wiki page via Edit — do not rewrite body sections.
5. Update `processed_at` to today's date.

## Hard rules

- Do NOT rewrite body sections. Only update frontmatter fields.
- Do NOT remove existing values. Only add missing ones.
- Validate all entity slugs against the ontology before adding.

## Final output

```json
{{
  "pmid": "{pmid}",
  "fields_updated": ["..."],
  "values_added": {{"field": ["values"]}}
}}
```"""
    return prompt


def run_patch(
    wiki_dir: Path,
    template_dir: Path,
    *,
    sections: list[str] | None = None,
    dry_run: bool = False,
) -> int:
    results = patch_frontmatter(wiki_dir, template_dir, sections=sections, dry_run=dry_run)
    for r in results:
        action = "would patch" if dry_run else "patched"
        added = f", added: {r['keys_added']}" if r["keys_added"] else ""
        renamed = f", renamed: {r['keys_renamed']}" if r.get("keys_renamed") else ""
        reord = ", reordered" if r["reordered"] else ""
        print(f"  {action} {r['path']}{added}{renamed}{reord}")
    suffix = " (dry run)" if dry_run else ""
    print(f"[reprocess:frontmatter] {len(results)} page(s){suffix}")
    return 0


def run_extract(
    wiki_dir: Path,
    raw_dir: Path,
    template_dir: Path,
    *,
    emit_prompts: bool = False,
) -> int:
    gaps = find_extraction_gaps(wiki_dir, raw_dir, template_dir)
    if emit_prompts:
        for g in gaps:
            if g.get("has_raw"):
                print(f"--- PMID {g['pmid']} ---")
                print(generate_extract_prompt(g))
                print()
    else:
        print(json.dumps(gaps, indent=2))
    print(f"[reprocess:extract] {len(gaps)} paper(s) with gaps", flush=True)
    return 0
