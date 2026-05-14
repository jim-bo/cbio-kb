---
name: Prostate Adenocarcinoma (TCGA, 2015)
studyId: prad_tcga
institution: The Cancer Genome Atlas
size: 499
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [bulk-rna-seq, methylation-array, snp-microarray, whole-exome-seq]
panels: []
tags: [prostate-cancer, prad, tcga, multi-platform]
processed_by: wiki-cli
processed_at: 2026-05-14
---

# Prostate Adenocarcinoma (TCGA, 2015)

## Overview

TCGA multi-platform genomic characterization of prostate adenocarcinoma, representing one of the foundational reference datasets for prostate cancer genomics. Used as a comparator in studies of prostate cancer PDX models and [FGFR1](../genes/FGFR1.md) expression patterns. [PMID:38488813](../papers/38488813.md)

## Composition

- 499 prostate adenocarcinoma ([PRAD](../cancer_types/PRAD.md)) patients; multi-platform TCGA profiling. [PMID:38488813](../papers/38488813.md)
- Used as cross-reference validation for promoter CpG methylation–expression correlations of [FGFR1](../genes/FGFR1.md) and other prostate cancer driver genes. [PMID:38488813](../papers/38488813.md)

## Assays / panels (linked)

- Whole-exome sequencing, RNA-seq, DNA methylation arrays, copy-number analysis. [PMID:38488813](../papers/38488813.md)

## Papers using this cohort

- [PMID:38488813](../papers/38488813.md) — Integrative Molecular Analyses of the MD Anderson Prostate Cancer Patient-derived Xenograft (MDA PCa PDX) Series.
- [PMID:26855148](../papers/26855148.md) — Beltran et al. 2016, *Nature Medicine*: queried for NEPC classifier validation (n=460 treatment-naïve adenocarcinomas scored NEPC-high at 0%).

## Notable findings derived from this cohort

- [FGFR1](../genes/FGFR1.md) promoter CpG methylation inversely correlated with [FGFR1](../genes/FGFR1.md) expression in both PDXs and TCGA-PRAD, confirming epigenetic regulation of FGFR1 in prostate cancer. [PMID:38488813](../papers/38488813.md)
- Queried for the NEPC classifier validation (n=460 treatment-naïve adenocarcinomas); 0% scored NEPC-high, confirming the classifier's specificity for castration-resistant neuroendocrine disease [PMID:26855148](../papers/26855148.md)

## Sources

- cBioPortal study `prad_tcga` [PMID:38488813](../papers/38488813.md).
- [PMID:26855148](../papers/26855148.md) — Beltran et al. 2016, *Nature Medicine*: NEPC classifier validation using this cohort (n=460 treatment-naïve adenocarcinomas).

*This page was processed by **entity-page-writer** on **2026-05-14**.*
