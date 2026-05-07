---
name: Medulloblastoma (Broad, Nature 2012)
studyId: mbl_broad_2012
institution: Broad Institute / Children's Hospital Boston / Hospital for Sick Children Toronto
size: 92
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - MUTATION_EXTENDED
panels: []
tags:
  - medulloblastoma
  - pediatric
  - cns
  - broad
processed_by: entity-page-writer
processed_at: "2026-05-06"
---

# Medulloblastoma (Broad, Nature 2012)

## Overview

The Broad medulloblastoma dataset comprises 92 primary medulloblastoma tumor/normal pairs from pediatric patients, profiled by whole-exome sequencing (Pugh et al., Nature 2012). Samples were collected from Children's Hospital Boston, Hospital for Sick Children Toronto, and Children's Oncology Group/CHTN. The cohort spans all four molecular subgroups of medulloblastoma (WNT, [SHH](../genes/SHH.md), Group 3, Group 4) and is characterized by one of the lowest somatic mutation rates across cancer types (median 0.35/Mb), consistent with other pediatric tumors.

## Composition

- 92 primary medulloblastoma tumor/normal pairs
- Cancer type: [MBL](../cancer_types/MBL.md) (medulloblastoma)
- Molecular subgroups: 6 WNT, 23 SHH, 33 Group 3, 30 Group 4
- Median age and institutional breakdown not specified but samples from three major pediatric oncology centers
- Median somatic mutation rate: 0.35 non-silent mutations per megabase (median 12 non-silent mutations per tumor)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — hybrid capture of 193,094 exons from 18,863 genes; median 106X coverage
- [mutsig](../methods/mutsig.md) — significance testing for somatic mutations (q < 0.1 threshold)
- Validation: microfluidic PCR (Fluidigm) + single-molecule real-time sequencing (Pacific Biosciences); 19/20 mutations confirmed

## Papers using this cohort

- [PMID:22820256](../papers/22820256.md) — Pugh et al. Nature 2012 primary analysis

## Notable findings derived from this cohort

- 12 genes significantly mutated (q<0.1): [CTNNB1](../genes/CTNNB1.md), [PTCH1](../genes/PTCH1.md), [KMT2D](../genes/KMT2D.md) (MLL2), [DDX3X](../genes/DDX3X.md), [GPS2](../genes/GPS2.md), [TP53](../genes/TP53.md), [KDM6A](../genes/KDM6A.md), [BCOR](../genes/BCOR.md), [SMARCA4](../genes/SMARCA4.md), [LDB1](../genes/LDB1.md), [CTDNEP1](../genes/CTDNEP1.md), [CSNK2B](../genes/CSNK2B.md) [PMID:22820256](../papers/22820256.md)
- DDX3X mutated in 7 tumors (half of WNT subgroup, p=0.005); potentiates mutant beta-catenin transcriptional activity [PMID:22820256](../papers/22820256.md)
- N-CoR complex genes (GPS2, BCOR, LDB1) identified as recurrently mutated — novel finding in medulloblastoma [PMID:22820256](../papers/22820256.md)
- Histone methyltransferase gene set enriched for somatic mutations across 21 tumors (q=5.8e-9) [PMID:22820256](../papers/22820256.md)
- Older patients (16-31 years) had significantly higher mutation frequency (p=7.7e-5, Wilcoxon rank-sum test) [PMID:22820256](../papers/22820256.md)

## Sources

- [PMID:22820256](../papers/22820256.md) — Pugh et al. Nature 2012

*This page was processed by **entity-page-writer** on **2026-05-06**.*
