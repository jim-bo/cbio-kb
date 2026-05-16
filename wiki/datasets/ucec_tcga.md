---
name: Uterine Corpus Endometrial Carcinoma (TCGA, Firehose Legacy)
studyId: ucec_tcga
institution: The Cancer Genome Atlas (TCGA)
size: 530
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
  - methylation
panels: []
tags:
  - ucec
  - endometrial-cancer
  - tcga
  - firehose-legacy
  - pan-cancer
processed_by: crosslinker
processed_at: 2026-05-16
---

# Uterine Corpus Endometrial Carcinoma (TCGA, Firehose Legacy)

## Overview

The TCGA [UCEC](../cancer_types/UCEC.md) cohort is the canonical reference dataset for uterine corpus endometrial carcinoma genomics, comprising ~530 cases profiled by The Cancer Genome Atlas through whole-exome sequencing, RNA-seq, SNP array copy-number analysis, and DNA methylation. This Firehose Legacy version (previously known as TCGA Provisional) uses source data from GDAC Firehose as of 2016-01-28. It provides the primary-tumor benchmark against which prospective clinical cohorts such as [ucec_msk_2018](../datasets/ucec_msk_2018.md) are compared for histologic composition and mutation frequency.

## Composition

- Approximately 530 endometrial tumors; predominantly primary-stage disease (contrast to [ucec_msk_2018](../datasets/ucec_msk_2018.md) which is 95% advanced).
- Histologic subtypes: endometrioid carcinoma (majority), serous carcinoma, mixed, and carcinosarcoma — all grouped under [UCEC](../cancer_types/UCEC.md).
- 39% MMR-deficient by IHC (vs. 13% in the MSK advanced-disease cohort, p=5×10⁻¹¹), reflecting histologic and stage differences.
- Median follow-up ~23 months at the time of publication; 19% of patients experienced disease recurrence.

## Assays / panels (linked)

- WES — whole-exome sequencing of tumor/normal pairs.
- RNA-seq — transcriptomic profiling.
- SNP array — allele-specific copy-number analysis.
- Methylation array — DNA methylation profiling (used for POLE/MSI/CN/transcriptomic molecular subtype classification).

## Papers using this cohort

- [PMID:30068706](../papers/30068706.md) — Soumerai et al. Clin Cancer Res 2018: Used as the primary-tumor reference for histology-matched comparisons to the MSK advanced endometrial cancer cohort.

## Notable findings derived from this cohort

- [PTEN](../genes/PTEN.md) alterations in 56% of TCGA UCEC vs. 22% in [ucec_msk_2018](../datasets/ucec_msk_2018.md) (p=8×10⁻⁹), reflecting the lower-grade endometrioid predominance of the primary-tumor TCGA cohort [PMID:30068706](../papers/30068706.md).
- [TP53](../genes/TP53.md) mutations in 36% of TCGA UCEC vs. 63% in [ucec_msk_2018](../datasets/ucec_msk_2018.md) (p=4×10⁻⁵), reflecting the high-grade/serous enrichment of the advanced-disease MSK cohort [PMID:30068706](../papers/30068706.md).
- 39% MMR-deficient by IHC in TCGA vs. 13% in [ucec_msk_2018](../datasets/ucec_msk_2018.md) (p=5×10⁻¹¹), driven by histologic composition differences [PMID:30068706](../papers/30068706.md).
- Copy-number cluster re-analysis of the TCGA UCEC cohort identified Cluster-A-like and Cluster-C-like subgroups, but heavy censoring (21 progression events among 81 patients with recurrence) prevented robust PFS outcome comparison [PMID:30068706](../papers/30068706.md).

## Sources

- cBioPortal study: `ucec_tcga`
- Source: GDAC Firehose stddata__2016_01_28; previously known as TCGA Provisional.

*This page was processed by **crosslinker** on **2026-05-16**.*
