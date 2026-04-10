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
| `schema/ontology/molecular_profiles.json` | cBioPortal `/api/molecular-profiles` | `molecularAlterationType` | Profile Types for assays and methods |
| `schema/ontology/clinical_attributes.json`| cBioPortal `/api/clinical-attributes`| `clinicalAttributeId` | Clinical metadata fields for datasets |
| `schema/ontology/sync_log.json` | — | — | Last sync timestamp + counts per source |
| `schema/ontology/_observed.md` | corpus | — | Terms agents observed in papers that are NOT in any canonical list. Curated for promotion. |

## Molecular & Clinical Logic

| Concept | Source | Field | Usage |
| :--- | :--- | :--- | :--- |
| **Profile Type** | `/api/molecular-profiles` | `molecularAlterationType` | `method.kind` and `dataset.assays` |
| **Clinical Attr** | `/api/clinical-attributes` | `clinicalAttributeId` | `dataset.clinical_fields` / composition |
| **Drug** | OncoKB `/api/v1/drugs` | `drugName` | `drug.slug` |

## Validation rules for agents

Before assigning ANY entity slug in a wiki page, the agent must check the canonical lists using:
```bash
uv run cbio-kb ontology lookup "<slug>"
```

**Genes** — must be a `hugoGeneSymbol` in `genes.json`.
**Cancer types** — must be a `code` in `oncotree.json` (preferred) or a `cancerTypeId` in `cancer_types.json`.
**Datasets** — must be a `studyId` in `studies.json`. The cBioPortal `studyId` IS the canonical slug.
**Gene panels** — must be a `genePanelId` in `gene_panels.json`.
**Drugs** — Agents should verify against OncoKB `/api/v1/drugs`. If found, use `canonical_source: oncokb` and `unverified: false`. Otherwise, `canonical_source: corpus` and `unverified: true`.
**Methods** — If it's a sequencing panel, use `genePanelId`. For assays, use `molecularAlterationType`. If neither, `unverified: true` and `canonical_source: corpus`.

## The "Verify-then-Observe" Workflow

When an agent finds a concept, it must classify it:
1. **Canonical**: Exists in cBioPortal API. Set `canonical_source: cbioportal` (or `oncotree`) and `unverified: false`.
2. **Standardized but Off-Catalog**: Valid standard (e.g. HUGO symbol) but not in sync JSON yet. Set `canonical_source: cbioportal` and `unverified: true`.
3. **Learned / Corpus-Grown**: Entirely new (e.g. new assay). Set `canonical_source: corpus` and `unverified: true`. Add to `_observed.md`.

## When a term is NOT in cBioPortal

1. Use a corpus-derived slug (kebab-case, lowercase).
2. Set `unverified: true` and `canonical_source: corpus` in the frontmatter.
3. Append a line to `schema/ontology/_observed.md` in the form:
   ```
   - {kind}: {slug} — observed in PMID:{pmid} — note: {one-line context}
   ```

## Refreshing

```bash
uv run cbio-kb ontology sync
```
