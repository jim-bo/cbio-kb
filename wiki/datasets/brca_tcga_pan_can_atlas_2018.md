---
name: Breast Invasive Carcinoma (TCGA, PanCancer Atlas 2018)
studyId: brca_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 1084
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - brca
  - breast
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-15
---

# Breast Invasive Carcinoma (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA Breast Invasive Carcinoma PanCancer Atlas 2018 cohort is the breast cancer arm of the TCGA PanCancer Atlas, available in cBioPortal as `brca_tcga_pan_can_atlas_2018`. It encompasses approximately 1,084 breast invasive carcinoma samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number profiles, and RNA-seq expression. The cohort spans all major molecular subtypes (luminal A, luminal B, HER2-enriched, basal-like, and claudin-low).

## Composition

- Cancer type: Breast Invasive Carcinoma ([BRCA](../cancer_types/BRCA.md)), OncoTree code [BRCA](../cancer_types/BRCA.md).
- Approximately 1,084 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline; BRCA showed >90% concordance with legacy PanCan12 calls.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE; includes HER2-amplified, copy-number-high basal, and diploid luminal subtypes.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion catalog (Gao et al., 2018)

## Notable findings derived from this cohort

- Pan-cancer RNA-seq fusion analysis (9,624 TCGA tumors) identified 9 [ESR1](../genes/ESR1.md) fusions in BRCA (8 luminal A/B), with strict mutual exclusivity with [ESR1](../genes/ESR1.md) point mutations; ESR1 expression was elevated in fusion-positive samples, suggesting a promoter-swap mechanism distinct from the resistance-associated ESR1 mutations seen in endocrine-treated metastatic BRCA [PMID:29617662](../papers/29617662.md).
- Four [ERBB2](../genes/ERBB2.md) fusions were identified across TCGA cancer types; 3 of 4 had HPV integration within 1 Mb of [ERBB2](../genes/ERBB2.md), with partner genes [PPP1R1B](../genes/PPP1R1B.md) and [IKZF3](../genes/IKZF3.md) being genomic neighbors suggesting local instability-driven rearrangement as an alternative mechanism of HER2 dysregulation distinct from amplification [PMID:29617662](../papers/29617662.md).
- Breast cancer (BRCA) had among the highest concordance (>90%) between MC3 mutation calls and the legacy PanCan12 MAF, indicating stable mutation calling across pipeline versions for this tumor type [PMID:29617662](../papers/29617662.md).
- Pan-cancer aneuploidy analysis placed BRCA in the epithelial cluster (alongside [LUAD](../cancer_types/LUAD.md) and [HCC](../cancer_types/HCC.md)) defined by 1q gain; copy-number-high serous-like endometrial cancers cluster with BRCA basal-like as a notable inter-disease grouping [PMID:29617662](../papers/29617662.md).

## Sources

- cBioPortal study: `brca_tcga_pan_can_atlas_2018`
- [PMID:29617662](../papers/29617662.md)

*This page was processed by **crosslinker** on **2026-05-15**.*
