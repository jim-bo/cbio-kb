---
name: Prostate Cancer PDX (MSK / MD Anderson, 2023)
studyId: prad_msk_mdanderson_2023
institution: Memorial Sloan Kettering Cancer Center / MD Anderson Cancer Center
size: 44
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [bulk-rna-seq, targeted-panel, whole-genome-seq]
panels: []
tags:
  - prostate-cancer
  - prad
  - pdx
  - neuroendocrine
  - patient-derived-xenograft
  - mda-pca-pdx
processed_by: entity-page-writer
processed_at: 2026-04-11
---

# Prostate Cancer PDX (MSK / MD Anderson, 2023)

## Overview

Multi-platform integrative genomic characterization of 44 patient-derived xenograft (PDX) models from 38 prostate cancer patients, including adenocarcinoma and neuroendocrine prostate cancer (NEPC) variants. Samples from primary sites and metastases; both therapy-naive and castration-resistant. Data deposited in cBioPortal as `prad_msk_mdanderson_2023` and dbGaP (phs003420.v1.p1). Cross-referenced with [prad_tcga](../datasets/prad_tcga.md) and [prad_su2c_2019](../datasets/prad_su2c_2019.md). [PMID:38488813](../papers/38488813.md)

## Composition

- 44 PDX models derived from 38 patients with [PRAD](../cancer_types/PRAD.md), including adenocarcinoma, [PRNE](../cancer_types/PRNE.md), poorly differentiated carcinomas, and sarcomatoid carcinomas. [PMID:38488813](../papers/38488813.md)
- Samples from primary sites and metastases (bone, lymph node, circulating tumor cells). [PMID:38488813](../papers/38488813.md)

## Assays / panels (linked)

- Whole-genome sequencing ([WGS](../methods/whole-genome-seq.md), 30X). [PMID:38488813](../papers/38488813.md)
- Targeted sequencing (T200.1 panel, 263 genes, 400X). [PMID:38488813](../papers/38488813.md)
- RNA-seq. [PMID:38488813](../papers/38488813.md)
- Mouse reads (mm10) filtered out; aligned to hg19. [PMID:38488813](../papers/38488813.md)

## Papers using this cohort

- [PMID:38488813](../papers/38488813.md) — Integrative Molecular Analyses of the MD Anderson Prostate Cancer Patient-derived Xenograft (MDA PCa PDX) Series.

## Notable findings derived from this cohort

- 91% of PDXs carried oncogenic alterations in at least one of [AR](../genes/AR.md), [RB1](../genes/RB1.md), [TP53](../genes/TP53.md), or [PTEN](../genes/PTEN.md). [PMID:38488813](../papers/38488813.md)
- [TMPRSS2](../genes/TMPRSS2.md)-[ERG](../genes/ERG.md) fusion in 13 PDX models; [TMPRSS2](../genes/TMPRSS2.md)-[ETV4](../genes/ETV4.md) fusion in 2 PDXs. [PMID:38488813](../papers/38488813.md)
- [CDK12](../genes/CDK12.md) alterations identified in 4 PDXs via multi-platform integration; biallelic mutations and structural/splicing-mediated inactivation would have been missed without integrative analysis. [PMID:38488813](../papers/38488813.md)
- [RB1](../genes/RB1.md) alterations significantly more frequent in NEPC than adenocarcinoma (P=0.0002); [RB1](../genes/RB1.md) and [AR](../genes/AR.md) expression significantly lower in NEPC. [PMID:38488813](../papers/38488813.md)
- [FGFR1](../genes/FGFR1.md) expression inversely correlated with promoter CpG methylation in PDXs and [prad_tcga](../datasets/prad_tcga.md); three downstream genes preferentially expressed in bone metastases in [prad_su2c_2019](../datasets/prad_su2c_2019.md). [PMID:38488813](../papers/38488813.md)

## Sources

- cBioPortal study `prad_msk_mdanderson_2023` [PMID:38488813](../papers/38488813.md).

*This page was processed by **entity-page-writer** on **2026-04-11**.*
