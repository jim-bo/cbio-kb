# cbio-kb Agent Contract

This file is the contract every cbio-kb subagent must read before doing work.
It defines the rules, the page templates, and the controlled vocabulary.

## Hard rules

1. **Never write to `raw/`.** It is the immutable source layer. Read only.
2. **Wiki pages always have YAML frontmatter.** See templates in `schema/templates/`.
3. **Always cite by PMID** as `[PMID:12345678](../papers/12345678.md)` (path relative to the citing page).
4. **Cross-link aggressively.** Every mention of a known gene/cancer-type/dataset/drug/method
   in any wiki page is rewritten as a link to its canonical page.
5. **Do not edit `wiki/index.md`** — it is regenerated deterministically by `uv run cbio-kb wiki build-index`.
6. **Conflicts are recorded, not resolved.** When papers disagree, write both positions
   with citations and (if material) flag in `wiki/themes/open_questions.md`.
7. **Prefer specificity** — sample sizes, p-values, cohort identifiers, OncoTree codes,
   exact gene symbols. Avoid hedging language ("some studies suggest").
8. **Idempotent writes.** If a page already exists, append/merge — do not overwrite.
10. **Provenance tracking.** Every wiki page must include `processed_by: {agent_name}` and `processed_at: {YYYY-MM-DD}` in the frontmatter. Every page must also conclude with a small italicized footer: `*This page was processed by **{agent_name}** on **{YYYY-MM-DD}**.*`

## Entity types

Extract and link these from every paper. **Every entity slug must be
validated against the canonical lists in `schema/ontology/*.json` before
use** — see `schema/ontology.md` for the validation protocol.

- **Genes** — HUGO symbol from `schema/ontology/genes.json` (`hugoGeneSymbol`).
  Page: `wiki/genes/{SYMBOL}.md`.
- **Cancer types** — OncoTree `code` from `schema/ontology/oncotree.json`.
  Page: `wiki/cancer_types/{CODE}.md`.
- **Datasets / cohorts** — `studyId` from `schema/ontology/studies.json`,
  used VERBATIM (do not transform underscores to hyphens).
  Page: `wiki/datasets/{studyId}.md`.
- **Drugs** — generic name, lowercase, hyphenated. Corpus-grown (no canonical
  list). Page: `wiki/drugs/{slug}.md`.
- **Methods / panels** — `genePanelId` from `schema/ontology/gene_panels.json`
  if it's a known panel; otherwise corpus-grown slug.
  Page: `wiki/methods/{slug}.md`.
- **Themes** — cross-paper concepts (resistance, co-mutation, TMB).
  Page: `wiki/themes/{slug}.md`.

## Validation against cBioPortal

For each candidate slug, before writing it to a wiki page, you MUST validate
it against the canonical ontology. Run:
`uv run cbio-kb ontology lookup "<slug>"` via Bash.

1. If `found: true` in the JSON response, use the `canonical_id` exactly as
   returned. Set `canonical_source: cbioportal` (or `oncotree` or `oncokb`) and `unverified: false`.
2. If `found: false`, the tool will return `suggestions`. If a suggestion is
   clearly the right canonical term (e.g., "TP-53" -> "TP53"), use it.
3. If no canonical match exists:
   - Use a corpus-derived slug (kebab-case for non-gene/non-OncoTree).
   - Set `unverified: true` and `canonical_source: corpus` in the entity page frontmatter.
   - Append one line to `schema/ontology/_observed.md` in the form
     `- {kind}: {slug} — observed in PMID:{pmid} — note: {brief}`.

**Never invent a HUGO symbol or an OncoTree code.** If the lookup tool
doesn't confirm it, it is unverified. Drugs should be manually verified against OncoKB. Datasets must specify `reference_genome`.

## Tool affordances

- `Read` / `Write` / `Edit` — wiki I/O.
- `Grep` / `Glob` — search the wiki.
- `Bash` — all CLI commands must be run via `uv run`.
  - Validation: `uv run cbio-kb ontology lookup "<slug>"`
  - Passage retrieval: `uv run cbio-kb index search -q "<query>" --rerank`
  - Linting: `uv run cbio-kb lint`

## Page templates

See `schema/templates/`:

- `paper.md` — one per PMID, in `wiki/papers/`.
- `gene.md` — one per HUGO symbol, in `wiki/genes/`.
- `cancer_type.md` — one per OncoTree code, in `wiki/cancer_types/`.
- `dataset.md` — one per cohort/dataset, in `wiki/datasets/`.
- `drug.md` — one per drug, in `wiki/drugs/`.
- `method.md` — one per method/panel, in `wiki/methods/`.
- `theme.md` — one per theme, in `wiki/themes/`.

Required sections in each template are non-negotiable; the linter enforces them.
