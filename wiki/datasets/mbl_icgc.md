---
name: Medulloblastoma (ICGC, Nature 2012)
studyId: mbl_icgc
institution: ICJG PedBrain Tumor Project
size: 125
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - whole-exome-seq
  - rna-seq
  - COPY_NUMBER_ALTERATION
panels: []
tags:
  - medulloblastoma
  - pediatric
  - cns
  - icgc
  - pedbrain
processed_by: entity-page-writer
processed_at: "2026-05-06"
---

# Medulloblastoma (ICGC, Nature 2012)

## Overview

The ICGC PedBrain medulloblastoma dataset comprises 125 matched pediatric medulloblastoma tumor/normal pairs from children aged 0-17 years, collected at primary diagnosis prior to adjuvant therapy (Jones et al., Nature 2012). The cohort uses an integrative design combining whole-genome sequencing, whole-exome sequencing, RNA-seq, and FISH. It spans all four molecular subgroups (WNT, [SHH](../genes/SHH.md), Group 3, Group 4) and was the first study to describe medulloblastoma fusion genes and to identify tetraploidy as a frequent early event in Group 3 and 4 tumors.

## Composition

- 125 pediatric medulloblastoma tumor/normal pairs (age 0-17 years)
- Cancer type: [MBL](../cancer_types/MBL.md)
- Molecular subgroups represented: WNT (n=15), SHH (n=30+), Group 3, Group 4
- Discovery set: WGS (n=39) + WES (n=21)
- Replication set: custom-capture sequencing of 2,734 genes (n=65)
- RNA sequencing: 28 cases
- Average somatic mutation rate: 0.52/Mb (mean 10.3 non-synonymous coding SNVs per tumor)

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — 39 discovery cases; 35-fold mean DNA coverage
- [whole-exome-seq](../methods/whole-exome-seq.md) — 21 discovery cases; 68-fold on-target mean coverage
- [rna-seq](../methods/rna-seq.md) — strand-specific, high-coverage; 28 cases
- [fish](../methods/fish.md) — validation of copy-number alterations and structural rearrangements

## Papers using this cohort

- [PMID:22832583](../papers/22832583.md) — Jones et al. Nature 2012 primary analysis

## Notable findings derived from this cohort

- 8 significantly mutated genes (MutSig): [CTNNB1](../genes/CTNNB1.md) (12%), [DDX3X](../genes/DDX3X.md) (8%), [PTCH1](../genes/PTCH1.md) (6%), [SMARCA4](../genes/SMARCA4.md) (5%), [KMT2D](../genes/KMT2D.md) (5%), [TP53](../genes/TP53.md) (4%), [KDM6A](../genes/KDM6A.md) (4%), [CTDNEP1](../genes/CTDNEP1.md) (3%) [PMID:22832583](../papers/22832583.md)
- Tetraploidy identified in 54% of Group 3 and 40% of Group 4 tumors; associated with significantly more large-scale copy-number alterations [PMID:22832583](../papers/22832583.md)
- First medulloblastoma fusion genes described: DNAJB6-SHH, LCLAT1-ERBB4, MLLT6-MRPL45 [PMID:22832583](../papers/22832583.md)
- 36% of cases (45/125) harbored a chromatin-modification gene mutation [PMID:22832583](../papers/22832583.md)
- Only 48% of non-synonymous DNA mutations detectable at RNA level; further 38% in genes with RPKM <1 [PMID:22832583](../papers/22832583.md)
- Positive correlation between genome-wide mutation rate and patient age (r2=0.35, p=7.8e-5) [PMID:22832583](../papers/22832583.md)

## Sources

- [PMID:22832583](../papers/22832583.md) — Jones et al. Nature 2012

*This page was processed by **entity-page-writer** on **2026-05-06**.*
