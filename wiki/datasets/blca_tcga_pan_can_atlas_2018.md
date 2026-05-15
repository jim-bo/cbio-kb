---
name: Bladder Urothelial Carcinoma (TCGA, PanCancer Atlas 2018)
studyId: blca_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 411
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - blca
  - bladder
  - urothelial
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-15
---

# Bladder Urothelial Carcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Bladder Urothelial Carcinoma PanCancer Atlas 2018 cohort is the [BLCA](../cancer_types/BLCA.md) arm of the TCGA PanCancer Atlas, available in cBioPortal as `blca_tcga_pan_can_atlas_2018`. It covers approximately 411 bladder urothelial carcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. BLCA had greater than 90% concordance with the legacy PanCan12 MAF for mutation calls.

## Composition

- Cancer type: Bladder Urothelial Carcinoma ([BLCA](../cancer_types/BLCA.md)), OncoTree code BLCA.
- Approximately 411 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline; >90% concordance with PanCan12 legacy calls.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion catalog (Gao et al., 2018)

## Notable findings derived from this cohort

- [FGFR3](../genes/FGFR3.md)-[TACC3](../genes/TACC3.md) is the most recurrent kinase fusion in BLCA (2.0% of samples), one of the highest rates across all cancer types for this specific activating inframe kinase fusion; [FGFR3](../genes/FGFR3.md) is a druggable target nominated across 15 cancer types by DEPO annotation [PMID:29617662](../papers/29617662.md).
- Pan-cancer fusion analysis (9,624 TCGA tumors) placed BLCA among cancer types with median 1 fusion per sample; FGFR3 and [TACC3](../genes/TACC3.md) emerge as the defining recurrent fusion partners for this tumor type [PMID:29617662](../papers/29617662.md).
- BLCA had greater than 90% concordance between MC3 mutation calls and the legacy PanCan12 MAF, indicating stable and reproducible mutation calling for this tumor type across pipeline iterations [PMID:29617662](../papers/29617662.md).

## Sources

- cBioPortal study: `blca_tcga_pan_can_atlas_2018`
- [PMID:29617662](../papers/29617662.md)

*This page was processed by **crosslinker** on **2026-05-15**.*
