---
name: TCGA Pan-Cancer Atlas Colorectal Adenocarcinoma 2018
studyId: coadread_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 526
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - colorectal
  - TCGA
  - pan-cancer
  - copy-number
processed_by: crosslinker
processed_at: 2026-05-06
---

# TCGA Pan-Cancer Atlas Colorectal Adenocarcinoma 2018

## Overview

The TCGA Pan-Cancer Atlas colorectal adenocarcinoma cohort, accessed via cBioPortal, comprising 526 cases profiled with whole-exome sequencing, RNA-seq, and SNP arrays as part of the broader TCGA Pan-Cancer Atlas initiative. Widely used as a reference cohort for copy number, mutation frequency, and survival analyses in colorectal cancer.

## Composition

- 526 colorectal adenocarcinoma ([COADREAD](../cancer_types/COADREAD.md)) cases.
- Includes colon ([COAD](../cancer_types/COAD.md)) and rectal ([READ](../cancer_types/READ.md)) adenocarcinomas.
- Multi-omic profiling: whole-exome sequencing, copy number (SNP array), RNA-seq.
- Accessible via cBioPortal.

## Assays / panels (linked)

- Whole-exome sequencing (WES)
- RNA-seq
- SNP array (copy number)

## Papers using this cohort

- [PMID:36334560](../papers/36334560.md) — Bioinformatic analysis of [FBXO7](../genes/FBXO7.md) copy number loss in CRC; 526 cases used for copy number, expression, and survival analyses.

## Notable findings derived from this cohort

- FBXO7 shallow deletions (heterozygous loss) occur in 32.5% (169/526) of CRC cases; deep deletions are rare (<0.2%); FBXO7 shallow deletions associate with increased genome instability (fraction altered, aneuploidy score, tumor break load; q < 0.0001) and worse overall, progression-free, and disease-specific survival (log rank, p < 0.05) [PMID:36334560](../papers/36334560.md).

## Sources

- cBioPortal study: `coadread_tcga_pan_can_atlas_2018`

*This page was processed by **crosslinker** on **2026-05-06**.*
