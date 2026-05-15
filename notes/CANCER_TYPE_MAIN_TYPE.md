# Idea: Add `main_type` to cancer_type pages + require `oncotree_code`

Captured from the abandoned branch `feat/cancer-type-main-type`
(commit `1715d216`, 2026-04-15, deleted 2026-05-15). The branch had
drifted ~85 commits behind main and would have been a noisy rebase, but
the underlying change is small and worth re-doing cleanly when the moment
comes.

## What changes

1. **Template.** Add `main_type` to `schema/templates/cancer_type.md`,
   between `oncotree_code` and `parent`:

   ```yaml
   ---
   name:
   oncotree_code:
   main_type:
   parent:
   tags: []
   processed_by:
   processed_at:
   ---
   ```

2. **Backfill.** For every `wiki/cancer_types/*.md`, look up the OncoTree
   `mainType` field by the page's `oncotree_code` and write it to
   frontmatter. OncoTree groups specific codes into broad clinical
   buckets — examples:

   | code | name | main_type |
   |---|---|---|
   | STAD | Stomach Adenocarcinoma | Esophagogastric Cancer |
   | LUAD | Lung Adenocarcinoma | Non-Small Cell Lung Cancer |
   | BRCA | Invasive Breast Carcinoma | Breast Cancer |
   | GBM | Glioblastoma | Glioma |

3. **Lint tighten.** In `src/cbio_kb/wiki/lint.py`, the
   `REQUIRED_FRONTMATTER["cancer_types"]` set should add `oncotree_code`
   alongside `name`. The branch confirmed every page already had the
   field, so this wouldn't have produced new errors.

## Why it's useful

- Lets the `/ask` graph and search collapse on broader clinical groupings
  (e.g. "show me everything under Glioma" → GBM + DIFG + ASTR + ODG + PAST
  + LGG + PXA + ATRT + …) without each page hand-listing siblings.
- Mirrors OncoTree's own faceting, so future cBioPortal sync just maps
  fields rather than re-deriving groupings.
- Cheap analytic axis for theme synthesis ("how often does TP53 appear
  across `main_type=Lung Cancer` vs. `main_type=Glioma`").

## How to redo (it's mechanical)

1. Run `uv run cbio-kb ontology sync` (or read `schema/ontology/oncotree.json`
   directly) to grab the `mainType` for each code currently in
   `wiki/cancer_types/`.
2. Use the deterministic frontmatter reprocessor — exactly the use case
   it was built for:
   `uv run cbio-kb wiki reprocess-frontmatter --sections cancer_types`
   after the template change. It'll add the new field; you then fill it
   from the OncoTree lookup.
3. Update lint, run tests + `cbio-kb lint`, commit.

Estimated effort: under an hour for the script + a single batch commit
covering ~80 pages.

## Risks / open questions

- A handful of corpus-grown `cancer_types/*.md` pages (e.g. the `LAML`,
  `KIRC`, `KIRP`, `PANCAN`, `LGG`, `MESO`, `PCPG`, `SARC`, `TGCT`, `THCA`,
  `UVM` aliases the loop added during PMID 29617662) are TCGA cohort
  codes, *not* OncoTree codes — they won't have a `mainType` lookup.
  Two options:
  - Mark `main_type:` empty + `unverified: true` (matches their existing
    `canonical_source: corpus` posture).
  - Inherit from the OncoTree equivalent (e.g. LAML → AML's `Leukemia`).
  Latter is more useful for analytics; former is more honest about
  provenance.
- The original branch put `main_type` between `oncotree_code` and
  `parent`. Stick with that ordering for diff-readability.
