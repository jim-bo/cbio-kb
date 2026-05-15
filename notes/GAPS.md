# Knowledge Base Gaps

Audit performed 2026-04-11 after processing 22 new papers (batch bringing total to 43 papers).

## Current wiki inventory

| Section | Pages |
|---|---|
| Papers | 43 |
| Genes | 250 |
| Cancer types | 70 |
| Datasets | 48 |
| Drugs | 51 |
| Methods | 51 |
| Themes | 0 |

---

## 1. Missing entity pages (stubs)

11 entity pages are referenced by existing wiki content but have no corresponding page:

### Cancer types (6)
- `ATC` — Anaplastic Thyroid Carcinoma (likely should map to existing `THAP`)
- `DLBCL` — should map to existing `DLBCLNOS`
- `ESAD` — Esophageal Adenocarcinoma (may overlap with `ESCA` or `EGC`)
- `MPM` — Malignant Peritoneal Mesothelioma (distinct from `PLMESO`)
- `OV` — Ovarian Cancer, generic (may overlap with `HGSOC`, `OVT`)
- `PAST` — Pilocytic Astrocytoma (distinct from `ASTR`)

### Datasets (2)
- `paad_icgc` — ICGC Pancreatic Adenocarcinoma cohort
- `paad_tcga` — TCGA Pancreatic Adenocarcinoma cohort

### Genes (3)
- `FANCA` — Fanconi Anemia Complementation Group A
- `RAD51B` — RAD51 Paralog B (HRD pathway)
- `TGFBR2` — TGF-beta receptor type 2

**Remediation:** Create stub pages or redirect aliases. For `ATC`/`DLBCL`/`ESAD`/`OV`, consider whether these are alias issues (should point to existing pages) or genuinely distinct OncoTree codes needing their own pages.

---

## 2. Unverified ontology terms

2 terms used in paper frontmatter are not in the canonical cBioPortal ontology:

- `pcawg` (dataset) — referenced in PMID:36723991. PCAWG is a well-known pan-cancer WGS resource (https://www.cbioportal.org/study/summary?id=pancan_pcawg_2020). Needs remediation.
- `AST` (cancer type) — referenced in PMID:37910594. Likely a typo for `ASTR` (Astrocytoma). Should be corrected in the paper page frontmatter.

---

## 3. Frontmatter completeness gaps

### Datasets — 23 pages missing `reference_genome`, `canonical_source`, and/or `unverified`

These are older dataset pages created before the template was fully stabilized:

| Dataset | Missing fields |
|---|---|
| all_stjude_2015 | reference_genome, canonical_source, unverified |
| appendiceal_msk_2022 | reference_genome, canonical_source, unverified |
| bladder_msk_2023 | reference_genome, canonical_source, unverified |
| bm_nsclc_mskcc_2023 | reference_genome, canonical_source, unverified |
| chl_sccc_2023 | reference_genome, canonical_source, unverified |
| cll_broad_2022 | reference_genome, canonical_source, unverified |
| coad_silu_2022 | reference_genome, canonical_source, unverified |
| coadread_tcga | reference_genome, canonical_source, unverified |
| csf_msk_2024 | reference_genome, canonical_source, unverified |
| difg_msk_2023 | reference_genome, canonical_source, unverified |
| gist_msk_2023 | reference_genome, canonical_source, unverified |
| hcc_msk_2024 | reference_genome, canonical_source, unverified |
| luad_mskcc_2023_met_organotropism | reference_genome, canonical_source, unverified |
| makeanimpact_ccr_2023 | reference_genome, canonical_source, unverified |
| msk_ch_2023 | reference_genome, canonical_source, unverified |
| msk_chord_2024 | reference_genome, canonical_source, unverified |
| msk_impact_2017 | reference_genome, canonical_source, unverified |
| mtnn_msk_2022 | reference_genome, canonical_source, unverified |
| nsclc_ctdx_msk_2022 | reference_genome, canonical_source, unverified |
| pancreas_msk_2024 | reference_genome, canonical_source, unverified |
| pcawg | reference_genome, canonical_source |
| pcnsl_msk_2024 | reference_genome, canonical_source, unverified |
| rms_msk_2023 | reference_genome, canonical_source, unverified |

**Remediation:** Run `uv run cbio-kb wiki reprocess-frontmatter --sections datasets --dry-run` to preview, then apply. Most can be set to `reference_genome: GRCh37` or `GRCh38`, `canonical_source: cbioportal`, `unverified: false` for MSK datasets.

### Drugs — 37 pages missing `canonical_source`; 4 also missing `unverified`

All 37 drug pages from the first generation of entity-page-writer runs lack `canonical_source`. The template expects this field (e.g., `canonical_source: oncokb` or `canonical_source: corpus`).

4 drugs also missing `unverified`: lenalidomide, methotrexate, temozolomide, tirabrutinib.

**Remediation:** Tier 1 frontmatter reprocess. For drugs with FDA approvals in oncology, set `canonical_source: oncokb`. For supportive-care agents (leucovorin, prednisone), set `canonical_source: corpus`.

### Methods — 33 pages missing `canonical_source`; 5 with non-canonical `kind`

33 method pages lack `canonical_source`. Additionally, 5 MSK panel pages (ACCESS129, IMPACT341, IMPACT410, IMPACT468, IMPACT505) have `kind: method` instead of `kind: gene-panel`, triggering a lint warning.

**Remediation:** Set `canonical_source: msk` for MSK panels, `canonical_source: illumina` for array platforms, `canonical_source: corpus` for analytical methods. Fix `kind` to `gene-panel` for the 5 IMPACT/ACCESS pages.

---

## 4. Non-canonical assay references in datasets

80 lint warnings for dataset `assays` fields referencing method slugs that aren't in `gene_panels.json`. Examples:

- `whole-exome-seq`, `rna-seq`, `whole-genome-seq` — these are generic method types, not gene panels. The linter flags them because the `assays` field was designed for panel IDs.
- `ctdna`, `germline-seq`, `copy-number`, `rna-fusion` — ad-hoc assay descriptors not in any canonical list.
- `methylation-array`, `proteomics`, `scrna-seq` — valid methods but not gene panels.

**Remediation options:**
1. Expand the canonical assay vocabulary in `gene_panels.json` to include non-panel method types.
2. Split the `assays` field into `panels` (canonical gene panels only) and `methods` (broader assay types).
3. Accept these as corpus-grown and add `unverified: true` to affected dataset pages.

---

## 5. Themes — empty section

The `wiki/themes/` directory has zero pages. The theme-synthesizer agent has never been run. Cross-cutting themes visible in the corpus include:

- **BRAF fusions across cancer types** — PMID:38922339 covers 10+ cancer types
- **MSI/dMMR and immunotherapy response** — PMIDs 38653864, 38949888, 38758238
- **Racial disparities in genomic profiles** — PMID:37651310 (endometrial), others
- **ctDNA as a prognostic biomarker** — PMIDs 37769223, 39147831, 37406106
- **TP53 as a universal prognostic marker** — referenced in 16/22 new papers
- **cGAS-STING innate immunity in gynecologic cancers** — PMID:39386723
- **Neuroendocrine differentiation across cancer types** — PMIDs 38488813 (PRNE), 38758238 (PTAD)

---

## 6. Template and schema issues

### Drug template lacks `canonical_source` default
The `schema/templates/drug.md` template includes `canonical_source` but entity-page-writer (sonnet) inconsistently populates it. First-generation drug pages (pre-batch) all lack it.

### Dataset `assays` field semantics
The field conflates gene panels (IMPACT505, ACCESS129) with broad method categories (whole-exome-seq, rna-seq). This creates 80+ lint warnings and makes the field less useful for filtering.

### Cancer type alias/synonym handling
Several cancer types have multiple valid OncoTree codes or common abbreviations (DLBCL vs DLBCLNOS, ATC vs THAP, OV vs HGSOC). There is no alias resolution mechanism — crosslinker links to whatever page exists, and stubs accumulate for the alternative names.

### No `title` field in entity frontmatter
Entity pages use `name`, `symbol`, etc. instead of `title`. Quarto listing pages needed `field-links` added manually (fixed in this session) to make table rows clickable. Adding `title` as a computed/alias field would make Quarto integration more seamless.

---

## 7. Suggested priority order

| Priority | Action | Effort | Impact |
|---|---|---|---|
| 1 | Run Tier 1 frontmatter reprocess for datasets, drugs, methods | Zero cost (deterministic Python) | Clears ~150 lint warnings |
| 2 | Create the 11 stub entity pages | Low (entity-page-writer, 1 dispatch) | Eliminates all stub warnings |
| 3 | Fix 2 unverified terms (pcawg, AST) | Manual edit | Eliminates unverified warnings |
| 5 | Resolve assay field semantics (schema decision) | Design discussion needed | Prevents recurring 80+ warnings |
| 6 | Add cancer type alias/redirect mechanism | Code change to crosslinker/linter | Prevents stub accumulation |
