# cbio-kb ontology

The canonical ontology for cbio-kb is **cBioPortal + OncoTree**, fetched via
`cbio-kb ontology sync` and written as JSON under `schema/ontology/`.

| File | Source | Key field | What it is |
|---|---|---|---|
| `schema/ontology/genes.json` | cBioPortal `/api/genes` | `hugoGeneSymbol` | All HUGO gene symbols cBioPortal recognizes (~45k) with Entrez IDs |
| `schema/ontology/studies.json` | cBioPortal `/api/studies` | `studyId` | All cBioPortal study IDs (~535) — the canonical dataset slugs |
| `schema/ontology/cancer_types.json` | cBioPortal `/api/cancer-types` | `cancerTypeId` | cBioPortal cancer-type tree (mirrors OncoTree) |
| `schema/ontology/oncotree.json` | OncoTree `/api/tumorTypes` | `code` | Authoritative OncoTree codes (~897) |
| `schema/ontology/gene_panels.json` | cBioPortal `/api/gene-panels` | `genePanelId` | cBioPortal gene panel IDs (~69) — canonical method slugs for panels |
| `schema/ontology/sync_log.json` | — | — | Last sync timestamp + counts per source |
| `schema/ontology/_observed.md` | corpus | — | Terms agents observed in papers that are NOT in any canonical list. Curated for promotion. |

## Validation rules for agents

Before assigning ANY entity slug in a wiki page, the agent must check the
canonical lists. Use Bash + `grep`/`jq` against the JSON files (do not load
the whole genes.json — it's ~45k entries; grep for the specific symbol).

**Genes** — must be a `hugoGeneSymbol` in `genes.json`.
```bash
grep -o '"hugoGeneSymbol":"EGFR"' schema/ontology/genes.json | head -1
```

**Cancer types** — must be a `code` in `oncotree.json` (preferred) or a
`cancerTypeId` in `cancer_types.json`.
```bash
grep -o '"code":"LUAD"' schema/ontology/oncotree.json | head -1
```

**Datasets** — must be a `studyId` in `studies.json`. The cBioPortal `studyId`
IS the canonical slug — use it verbatim, do NOT transform underscores to hyphens.
```bash
grep -o '"studyId":"luad_tcga"' schema/ontology/studies.json | head -1
```

**Gene panels** — must be a `genePanelId` in `gene_panels.json`.
```bash
grep -o '"genePanelId":"IMPACT468"' schema/ontology/gene_panels.json | head -1
```

**Drugs** — cBioPortal does not expose a drug ontology. Use generic names
(lowercase, hyphenated). All drugs are corpus-grown; record them in
`_observed.md`.

**Methods** — if a method is a sequencing panel that exists in `gene_panels.json`,
use its `genePanelId`. Otherwise it is corpus-grown — record in `_observed.md`.

## When a term is NOT in cBioPortal

This is expected. Papers contain real concepts cBioPortal does not catalog
(novel gene aliases, unusual cancer subtypes, computational methods,
institutional cohorts, drugs).

In that case the agent must:

1. Use a corpus-derived slug (kebab-case, lowercase for non-gene/non-OncoTree).
2. Set `unverified: true` in the entity page frontmatter.
3. Append a line to `schema/ontology/_observed.md` in the form:
   ```
   - {kind}: {slug} — observed in PMID:{pmid} — note: {one-line context}
   ```
4. Never invent a HUGO symbol or an OncoTree code. If the canonical list
   does not contain it, it is corpus-grown and must be marked `unverified`.

## Refreshing

```bash
uv run cbio-kb ontology sync
```

Re-runs against cBioPortal + OncoTree and overwrites the JSON files. Safe to
run anytime; cBioPortal's APIs are read-only and cheap. Drift is expected —
re-run periodically (monthly is plenty).
