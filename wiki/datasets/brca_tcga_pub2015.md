---
name: TCGA Breast Invasive Carcinoma (TCGA, Cell 2015)
studyId: brca_tcga_pub2015
institution: The Cancer Genome Atlas (TCGA) Research Network
size: 817
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
  - MIRNA_EXPRESSION
  - METHYLATION
  - PROTEIN_LEVEL
panels: []
tags:
  - tcga
  - breast-cancer
  - invasive-lobular-carcinoma
  - multi-platform-profiling
  - intrinsic-subtypes
  - ilc
  - idc
processed_by: crosslinker
processed_at: 2026-05-14
---

# TCGA Breast Invasive Carcinoma (TCGA, Cell 2015)

## Overview

The 2015 TCGA breast cancer dataset (brca_tcga_pub2015) is the comprehensive multi-platform molecular characterization of 817 primary breast tumors published by Ciriello et al. in Cell (2015). It expands on the original 2012 TCGA breast study ([brca_tcga_pub](../datasets/brca_tcga_pub.md)) by including a histology-enriched design: 127 invasive lobular carcinoma ([ILC](../cancer_types/ILC.md)), 490 invasive ductal carcinoma ([IDC](../cancer_types/IDC.md)), 88 mixed IDC/ILC, and 112 other histologies. The primary aim was to characterize the molecular landscape of ILC relative to IDC across DNA, RNA, protein, and epigenomic dimensions. Validation of ILC transcriptional subtypes was performed in the [brca_metabric](brca_metabric.md) cohort.

## Composition

- 817 primary breast tumors: 127 [ILC](../cancer_types/ILC.md), 490 [IDC](../cancer_types/IDC.md), 88 mixed IDC/ILC, 112 other histologies.
- ILC PAM50 subtype composition: 83% Luminal A, 94% (113/120) ER+ by IHC.
- Platforms: whole-exome sequencing, RNA-seq, miRNA-seq, Affymetrix SNP6 (copy number), HM27 and HM450 methylation arrays, RPPA (reverse-phase protein arrays, n=633). Whole-genome bisulfite sequencing in 5 samples for methylation validation.
- Reference genome: hg19.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [mirna-seq](../methods/mirna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)
- [hm27-methylation-array](../methods/hm27-methylation-array.md)
- [hm450-methylation-array](../methods/hm450-methylation-array.md)
- [rppa](../methods/rppa.md)

## Papers using this cohort

- [PMID:26451490](../papers/26451490.md) — Ciriello et al. 2015, Cell — "Comprehensive molecular portraits of invasive lobular breast cancer."

## Notable findings derived from this cohort

- ILC-enriched mutations vs IDC: [CDH1](../genes/CDH1.md) 63% vs 2% (q=3.94E-53); [TBX3](../genes/TBX3.md) 9% vs 2%; [PIK3CA](../genes/PIK3CA.md) 48% vs 33%; [FOXA1](../genes/FOXA1.md) 7% vs 2%; [TP53](../genes/TP53.md) depleted in ILC (8% vs 44%) [PMID:26451490](../papers/26451490.md).
- [CDH1](../genes/CDH1.md) alterations detected in 120/127 (95%) ILC cases; CDH1 promoter DNA hypermethylation was not observed, contradicting older MSP-based reports [PMID:26451490](../papers/26451490.md).
- ILC has the highest pAKT activity of any breast cancer subtype — comparable to HER2+ and Basal-like — driven by upstream RTK alterations and [PTEN](../genes/PTEN.md) loss rather than [PIK3CA](../genes/PIK3CA.md) mutation per se [PMID:26451490](../papers/26451490.md).
- Three ILC transcriptional subtypes identified (reactive-like, immune-related, proliferative); validated in [brca_metabric](brca_metabric.md); proliferative ILC had worse DSS and [OS](../cancer_types/OS.md) [PMID:26451490](../papers/26451490.md).
- Mixed IDC/ILC tumors resolve molecularly into ILC-like or IDC-like classes (not a third hybrid entity); CDH1 status is the dominant classifier [PMID:26451490](../papers/26451490.md).

## Sources

- Ciriello G et al. "Comprehensive molecular portraits of invasive lobular breast cancer." Cell. 2015;163(2):506-519. [PMID:26451490](../papers/26451490.md). DOI: 10.1016/j.cell.2015.09.033.

*This page was processed by **crosslinker** on **2026-05-14**.*
