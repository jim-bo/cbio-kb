---
name: Label-free proteomics (shotgun LC-MS/MS)
slug: label-free-proteomics
kind: method
canonical_source: corpus
unverified: true
tags:
  - proteomics
  - mass-spectrometry
  - label-free
  - shotgun-proteomics
  - multi-omics
processed_by: crosslinker
processed_at: 2026-05-16
---

# Label-free proteomics (shotgun LC-MS/MS)

## Overview

Label-free quantitative proteomics uses liquid chromatography tandem mass spectrometry (LC-MS/MS) without chemical labeling to measure protein abundance across samples. Quantitation relies on peptide feature intensities (spectral intensity or spectral count) extracted from individual runs and compared computationally after normalization. Label-free proteomics allows analysis of larger sample sets than labeled approaches (no multiplexing limit) but requires careful between-run normalization and is generally considered less precise than TMT-based methods for small sample-number experiments. In the CPTAC program, label-free data were used to complement TMT data and to increase the total number of tumors analyzed.

## Used by

- Applied to 100 CPTAC colon cancer tumors ([coad_cptac_2019](../datasets/coad_cptac_2019.md)) alongside TMT global and phosphoproteomics; average label-free protein profiles correlated with TCGA colorectal proteomics at Pearson r=0.96 and with 100 tumor averages from different cancer types at lower r; identified cancer-associated proteins broadly consistent with TMT findings [PMID:31031003](../papers/31031003.md)

## Notes

- In the CPTAC colon study, label-free proteomics covered 100 tumors vs 96 for TMT (which required matched NATs), providing slightly larger n for tumor-centric analyses.
- The high inter-study correlation (r=0.96 with TCGA CRC) supports the reproducibility of label-free protein profiles across platforms and cohorts.
- Not in cBioPortal gene-panels or molecular-profiles ontologies; corpus-grown slug.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
