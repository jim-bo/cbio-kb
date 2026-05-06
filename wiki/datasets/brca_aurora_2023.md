---
name: AURORA US Metastatic Breast Cancer Study (2023)
studyId: brca_aurora_2023
institution: UNC Lineberger Comprehensive Cancer Center / AURORA US Network
size: 55
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - dna-methylation-array
panels: []
tags:
  - breast-cancer
  - metastasis
  - multiomics
  - epigenetics
  - immune-evasion
  - dna-methylation
  - subtype-switching
  - hla-loss
processed_by: crosslinker
processed_at: 2026-05-05
---

# AURORA US Metastatic Breast Cancer Study (2023)

## Overview

The AURORA US Metastasis Project is a multiomics cohort profiling matched primary and metastatic tumor specimens from females with metastatic breast cancer. Conducted through the AURORA US network, the dataset includes 55 participants, 51 primary tumors, and 102 metastases assayed by whole-exome sequencing, low-pass whole-genome sequencing (5x), RNA-seq (rRNA depletion), and EPIC DNA methylation arrays. 88/153 specimens had all four assays; 141/153 had three of four. The dataset is available on cBioPortal as `brca_aurora_2023`.

## Composition

- 55 female participants with metastatic [BRCA](../cancer_types/BRCA.md) (breast cancer); 51 primary tumors and 102 metastases.
- Median age at primary diagnosis: 49 years; 18% African American, 7% Hispanic.
- Metastatic sites: liver (n=28), lung (n=13), lymph nodes (n=12), brain (n=11), other (n=16).
- 20 participants had samples collected at autopsy.
- Key clinical fields: PAM50 subtype, metastatic site, lines of prior therapy (median 3, range 0–20), race/ethnicity.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — tumor and germline
- [whole-genome-seq](../methods/whole-genome-seq.md) — low-pass (5x) for copy-number profiling
- [rna-seq](../methods/rna-seq.md) — rRNA-depleted transcriptome
- [epic-methylation-array](../methods/epic-methylation-array.md) — EPIC 850K DNA methylation profiling

## Papers using this cohort

- [PMID:36585450](../papers/36585450.md) — Garcia-Recio et al., *Nature Cancer* 2023. Multiomics profiling of primary and metastatic breast tumors from the AURORA US network.

## Notable findings derived from this cohort

- Expression subtype switching occurred in 13/39 (33%) of primary-metastasis pairs; basal-like was the most stable subtype (15/16 concordant) while luminal/HER2E subtypes switched in 8/19 individuals [PMID:36585450](../papers/36585450.md).
- [HLA-A](../genes/HLA-A.md) was epigenetically silenced via promoter hypermethylation in 23 tumors (12 individuals) and via focal deletions in 23 samples (8 participants); metastases with [HLA-A](../genes/HLA-A.md) silencing showed reduced immune infiltrates and higher predicted neoantigen burdens (P=0.002 in basal-like tumors) [PMID:36585450](../papers/36585450.md).
- Liver metastases showed the lowest immune cell features in 9/14 individuals with multiple metastatic sites profiled; brain metastases had 48 immune/stromal signatures lower than matched primaries [PMID:36585450](../papers/36585450.md).
- 11 DNA segments were more frequently amplified in metastases (q<0.05), including regions overlapping [MYC](../genes/MYC.md) and [MDM4](../genes/MDM4.md); [ESR1](../genes/ESR1.md) activating mutations were identified in 4 metastatic cases consistent with endocrine therapy resistance [PMID:36585450](../papers/36585450.md).

## Sources

- cBioPortal study: `brca_aurora_2023`
- Associated publication: [PMID:36585450](../papers/36585450.md)

*This page was processed by **crosslinker** on **2026-05-05**.*
