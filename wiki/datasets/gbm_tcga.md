---
name: TCGA Glioblastoma Multiforme
studyId: gbm_tcga
institution: The Cancer Genome Atlas (TCGA)
size: 592
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - bulk-rna-seq
panels: []
tags:
  - glioblastoma
  - gbm
  - glioma
  - TCGA
  - wes
  - rna-seq
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# TCGA Glioblastoma Multiforme

## Overview

The TCGA GBM study is the canonical genomic and transcriptomic dataset for glioblastoma multiforme, assembled by The Cancer Genome Atlas Research Network. It comprises multi-platform molecular profiling of glioblastoma tumours and is hosted on cBioPortal as `gbm_tcga`. The companion TCIA imaging collection ([tcia-tcga-gbm](../datasets/tcia-tcga-gbm.md)) provides matched multi-parametric MRI scans with expert-revised tumour segmentation labels and extracted radiomic features published by Bakas et al. 2017. [PMID:28872634](../papers/28872634.md)

## Composition

- **Cancer type**: glioblastoma multiforme ([GB](../cancer_types/GB.md)), n=592.
- **Assays**: whole-exome sequencing, bulk RNA-seq, copy-number arrays, methylation arrays, and reverse-phase protein arrays.
- **Molecular counterpart**: paired with TCIA-hosted multi-parametric MRI scans (T1, T1-Gd, T2, T2-FLAIR) in [tcia-tcga-gbm](../datasets/tcia-tcga-gbm.md) (135 scans from 8 institutions).

## Assays / panels (linked)

- Whole-exome sequencing; bulk RNA-seq; copy-number arrays.

## Papers using this cohort

- [PMID:28872634](../papers/28872634.md) — Bakas et al. 2017, *Scientific Data*: Expert-revised MRI segmentation labels and >700 radiomic features released for 135 TCGA-GBM cases, complementing the genomic data in gbm_tcga to enable radiogenomic studies.

## Notable findings derived from this cohort

- Bakas et al. 2017 released expert-revised segmentation labels for 135 GBM cases (from the originating set of 262), achieving median DICE of 0.92 for whole tumour, 0.88 for tumour core, and 0.88 for enhancing tumour versus GLISTRboost automated labels. These labels became the reference for BraTS'17. [PMID:28872634](../papers/28872634.md)
- A panel of >700 radiomic features was extracted volumetrically from the manually revised labels, spanning intensity, volumetric, morphologic, texture (GLCM/GLRLM/GLSZM/NGTDM), wavelet, and glioma growth-model parameters — enabling downstream radiogenomic correlation with TCGA molecular profiles. [PMID:28872634](../papers/28872634.md)

## Sources

- cBioPortal study: `gbm_tcga` — https://www.cbioportal.org/study/summary?id=gbm_tcga
- TCGA GBM marker paper: Cancer Genome Atlas Research Network 2008, *Nature* (PMID 18772890).
- [PMID:28872634](../papers/28872634.md) — Bakas et al. 2017, *Scientific Data*, DOI 10.1038/sdata.2017.117.

*This page was processed by **entity-page-writer** on **2026-04-15**.*
