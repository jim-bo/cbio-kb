---
name: Diffuse Large B-Cell Lymphoma (TCGA, PanCancer Atlas 2018)
studyId: dlbc_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 48
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - dlbc
  - lymphoma
  - DLBCL
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-16
---

# Diffuse Large B-Cell Lymphoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Diffuse Large B-Cell Lymphoma PanCancer Atlas 2018 cohort is the DLBC arm of the TCGA PanCancer Atlas, available in cBioPortal as `dlbc_tcga_pan_can_atlas_2018`. It covers approximately 48 diffuse large B-cell lymphoma samples (OncoTree: [DLBCLNOS](../cancer_types/DLBCLNOS.md)) with uniformly reprocessed mutation calls (MC3 pipeline), copy-number, and RNA-seq expression. DLBC is one of the smaller TCGA disease cohorts; endpoint usage recommendations note only one endpoint (PFI) recommended with caution for DLBC due to limited follow-up data.

## Composition

- Cancer type: Diffuse Large B-Cell Lymphoma ([DLBCLNOS](../cancer_types/DLBCLNOS.md)), OncoTree code [DLBCLNOS](../cancer_types/DLBCLNOS.md).
- Approximately 48 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29625048](../papers/29625048.md) — TCGA PanCancer Atlas integrative molecular analysis (Hoadley et al., 2018)

## Notable findings derived from this cohort

- DLBC (C24 iCluster neighbor with [LAML](../cancer_types/LAML.md)) was included in the pan-cancer integrative molecular analysis across 33 cancer types (9,759 samples with complete four-platform data); DLBC showed limited cell-cycle pathway alterations consistent with lymphoma biology. [PMID:29625048](../papers/29625048.md)
- TCGA-CDR endpoint recommendations for DLBC: only one endpoint can be recommended (PFI used with caution); overall survival not recommended due to inadequate follow-up; underscores that pan-cancer survival analyses using this cohort should note this limitation. [PMID:29625048](../papers/29625048.md)

## Sources

- cBioPortal study: `dlbc_tcga_pan_can_atlas_2018`
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
