---
name: TCGA Kidney Renal Clear Cell Carcinoma — Publication Cohort
studyId: kirc_tcga_pub
institution: The Cancer Genome Atlas (TCGA)
size: 446
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - affymetrix-snp6
  - rna-seq
  - mirna-seq
  - 450k-methylation-array
  - rppa
panels: []
tags:
  - ccRCC
  - kidney
  - clear-cell
  - TCGA
  - integrated-genomics
  - multi-platform
processed_by: crosslinker
processed_at: 2026-05-09
---

# TCGA Kidney Renal Clear Cell Carcinoma — Publication Cohort

## Overview

The TCGA clear cell renal cell carcinoma (ccRCC; [CCRCC](../cancer_types/CCRCC.md)) publication cohort, analyzed in the landmark TCGA Research Network paper (Nature 2013, PMID:23792563). This is the primary-analysis cohort referenced as `kirc_tcga_pub` in cBioPortal, distinct from the full deposited study (`kirc_tcga`). It encompasses 446 primary nephrectomy specimens with histologically confirmed ccRCC subjected to multi-platform molecular characterization. A "Core" subset of 372 samples had data across all platforms.

## Composition

- 446 primary nephrectomy specimens, histologically confirmed clear cell RCC ([CCRCC](../cancer_types/CCRCC.md)); ≥60% tumor nuclei by pathology review (median 85%).
- 372-sample "Core" set with data across all platforms; 446-sample "Extended" set with data on at least one platform.
- Whole-exome sequencing on 417 tumors yielding 36,353 putative somatic mutations; whole-genome sequencing on 22 tumors for calibration (83% WES mutation call confirmation rate).
- Copy number: Affymetrix SNP 6.0 arrays.
- mRNA: RNA sequencing; miRNA: miRNA sequencing; DNA methylation: 450K Human Methylation arrays (n=224 for [SETD2](../genes/SETD2.md) analysis); protein: Reverse Phase Protein Arrays (RPPA).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)
- [rna-seq](../methods/rna-seq.md)
- [450k-methylation-array](../methods/450k-methylation-array.md)

## Papers using this cohort

- [PMID:23792563](../papers/23792563.md) — The Cancer Genome Atlas Research Network 2013, "Comprehensive molecular characterization of clear cell renal cell carcinoma," *Nature*.

## Notable findings derived from this cohort

- 19 significantly mutated genes (q<0.1) identified; top 8 (q<0.00001): [VHL](../genes/VHL.md), [PBRM1](../genes/PBRM1.md), SETD2, [KDM5C](../genes/KDM5C.md), [PTEN](../genes/PTEN.md), [BAP1](../genes/BAP1.md), [MTOR](../genes/MTOR.md), and [TP53](../genes/TP53.md). Only BAP1 mutation correlated with worse survival [PMID:23792563](../papers/23792563.md).
- Chromosome 3p loss in 91% of samples, encompassing VHL, PBRM1, BAP1, and SETD2; 14q loss (including [HIF1A](../genes/HIF1A.md)) in 45%; 5q gain in 67% [PMID:23792563](../papers/23792563.md).
- PI3K/AKT/mTOR pathway altered in ~28% of tumors by MEMo mutual-exclusivity analysis; [EGFR](../genes/EGFR.md) over-expressed and phosphorylated in the alteration module [PMID:23792563](../papers/23792563.md).
- SETD2 mutation associated with regional DNA hypomethylation at non-promoter CpG sites (n=2,557 differentially methylated loci; FDR=0.001) [PMID:23792563](../papers/23792563.md).
- Recurrent SFPQ-TFE3 fusion in 5 samples, all VHL wildtype with X(p11) rearrangements [PMID:23792563](../papers/23792563.md).
- Four mRNA subtypes (m1–m4) with differential survival: m1 enriched for PBRM1 mutations (39%); m3 for [CDKN2A](../genes/CDKN2A.md) deletion and PTEN mutation; m4 for BAP1 and MTOR mutations [PMID:23792563](../papers/23792563.md).
- Metabolic shift toward Warburg phenotype (decreased AMPK/Krebs cycle, increased pentose phosphate pathway and fatty acid synthesis) correlated with worse survival; mRNA, miRNA, and protein signatures added prognostic power beyond clinical variables in multivariate Cox analysis [PMID:23792563](../papers/23792563.md).

## Sources

- [PMID:23792563](../papers/23792563.md)
- TCGA Data Portal / GDC

*This page was processed by **crosslinker** on **2026-05-09**.*
