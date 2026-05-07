---
name: TCGA Kidney Renal Clear Cell Carcinoma (KIRC)
studyId: kirc_tcga
institution: The Cancer Genome Atlas (TCGA)
size: 491
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - rna-seq
  - scrna-seq
  - multiplexed-immunofluorescence
panels: []
tags:
  - ccRCC
  - kidney
  - clear-cell
  - TCGA
  - immunotherapy
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# TCGA Kidney Renal Clear Cell Carcinoma (KIRC)

## Overview

The TCGA KIRC dataset comprises 491 clear cell renal cell carcinoma (ccRCC) samples and is one of the primary anchor cohorts in large-scale multi-cohort ccRCC studies. It includes bulk RNA-seq, DNA-seq, and clinical outcome data. TCGA-KIRC has been extensively used as a reference for molecular subtyping, survival analysis, and immunotherapy biomarker discovery in ccRCC.

## Composition

- Cancer type: clear cell renal cell carcinoma ([CCRCC](../cancer_types/CCRCC.md)), n = 491.
- Assays: bulk [rna-seq](../methods/rna-seq.md), DNA-seq (NGS).
- Used as one of 14 public cohorts (n = 3,621 ccRCC samples total) in the HiTME meta-analysis [PMID:22138691](../papers/22138691.md).

## Assays / panels (linked)

- [rna-seq](../methods/rna-seq.md)

## Papers using this cohort

- [PMID:22138691](../papers/22138691.md) — HiTME ccRCC molecular subtyping and IO biomarker study (meta-cohort including TCGA-KIRC as anchor).

## Notable findings derived from this cohort

- Five HiTME immune tumor microenvironment subtypes (IE, IE/M, F, V, D) were defined using harmonized transcriptomic data from 14 cohorts including TCGA-KIRC; fibrotic subtypes IE/M and F had worst overall survival in the TCGA-KIRC cohort [PMID:22138691](../papers/22138691.md).
- [BAP1](../genes/BAP1.md), [SETD2](../genes/SETD2.md), and [PBRM1](../genes/PBRM1.md) mutations were associated with distinct HiTME subtypes and differential ICI/TKI response profiles [PMID:22138691](../papers/22138691.md).
- [MTOR](../genes/MTOR.md)-activating mutations associated with ICI non-response (15/16 patients resistant) in the meta-cohort anchored on TCGA-KIRC [PMID:22138691](../papers/22138691.md).

## Sources

- [PMID:22138691](../papers/22138691.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
