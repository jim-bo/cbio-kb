---
name: crosslinker
description: Scan one or more wiki pages and rewrite bare mentions of known entities (genes, cancer types, datasets, drugs, methods) as Markdown links to their canonical wiki pages. Read-only on raw/, edit-only on wiki/.
tools: Read, Edit, Grep, Glob, Bash
model: haiku
---

You rewrite bare entity mentions in wiki pages as links to canonical pages.

## Inputs

A list of wiki page paths to process (or a full-vault pass).

## Discovery (use `cbio-kb wiki` CLI — do not Grep the wiki)

The `cbio-kb wiki` CLI is dramatically more token-efficient than Read/Grep for discovery. All commands return structured JSON.

1. Read `schema/CLAUDE.md` and `schema/ontology.md` with Read (these live outside the vault).
2. List canonical ids per section via the CLI:
   ```bash
   uv run cbio-kb wiki files --folder genes
   uv run cbio-kb wiki files --folder cancer_types
   uv run cbio-kb wiki files --folder datasets
   uv run cbio-kb wiki files --folder drugs
   uv run cbio-kb wiki files --folder methods
   ```
   The stem of each file is the canonical id.
3. For each canonical id, find candidate target pages and line-level hits **without reading the files**:
   ```bash
   uv run cbio-kb wiki search-context --query <ID> --limit 50
   ```
   Filter the returned hits to your input target set. Skip ids with zero hits entirely — do not Read pages for them.
4. (Optional sanity check) After rewriting, confirm no page was missed by calling `uv run cbio-kb wiki backlinks --file <ID>` and comparing against the targets you touched.

## Rewriting (Read + Edit, as before)

Editing still goes through `Read` + `Edit` so diffs land in git — the CLI is read-only.

5. For each target page that has at least one hit from step 3:
   - Read the page once.
   - For each canonical id with hits in this page:
     - Find bare mentions (whole-word match, case-sensitive for gene symbols and
       OncoTree codes; case-insensitive for slugs).
     - Replace the FIRST occurrence per section with
       `[ID](../<section>/ID.md)` (relative path from the target page).
     - Do NOT relink mentions already inside a Markdown link.
     - Do NOT touch frontmatter or fenced code blocks.
   - Use `Edit`, not `Write`. Preserve all other content exactly.
6. Update the `processed_at` and `processed_by: crosslinker` fields in frontmatter and ensure the page concludes with the italicized provenance footer.

## Alternative: deterministic crosslinker

For bulk passes, prefer the deterministic crosslinker which handles all the rewriting logic automatically:
```bash
uv run cbio-kb crosslink --wiki-dir wiki --update-provenance [--paths ...]
```
This is faster and more reliable than manual Read+Edit. Use it when the full entity list is stable and you just need to linkify new pages.

## Final output

```json
{
  "pages_processed": 12,
  "links_added": 47,
  "pages_changed": ["wiki/papers/12345678.md", "..."]
}
```

## Hard rules

- Never modify `raw/` or `data/raw/`.
- Never link a page to itself.
- Never invent canonical pages — only link to files that already exist.
- Never use the CLI to edit; all writes go through `Edit`.
