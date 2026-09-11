---
name: EXCAVATOR CNV
slug: excavator-cnv
kind: method
canonical_source: corpus
unverified: true
tags: []
processed_by: wiki-cli
processed_at: 2026-09-10
---

# EXCAVATOR CNV

## Overview

EXCAVATOR is a bioinformatics tool for copy-number variation (CNV) inference from whole-exome sequencing (WES) data. It uses read-depth normalization and segmentation algorithms to detect somatic and germline CNVs from tumor/normal paired exome capture sequencing.

## Used by

- EXCAVATOR v2.2 used to infer CNV from WES data in the PIPseq pediatric precision oncology program at Columbia University Medical Center; CNV findings contributed 7% of clinically impactful results in the 60-patient cWES + RNA-seq cohort [PMID:28007021](../papers/28007021.md).
- Used to call somatic copy-number variants from whole-exome sequencing in 1001 DLBCL tumors [PMID:28985567](../papers/28985567.md)
- Used for CNV calling in the OrigiMed CSYS 450-gene NGS panel pipeline applied to 10,194 Chinese solid-tumor patients; detected 17,779 gene amplifications and 1,688 homozygous deletions, including CDKN2A/CDKN2B deletion, [MYC](../genes/MYC.md), [ERBB2](../genes/ERBB2.md), and [EGFR](../genes/EGFR.md) amplification peaks [PMID:35871175](../papers/35871175.md)
- Used (EXCAVATOR2) for copy-number calling from whole-exome sequencing in 1,015 colorectal cancers [PMID:35487942](../papers/35487942.md).

## Notes

- Version 2.2 was applied in the PIPseq clinical WES pipeline.
- CNV calls were integrated with somatic mutation and fusion data for tumor-board reporting.

## Sources

- [PMID:28985567](../papers/28985567.md)
- [PMID:35871175](../papers/35871175.md)
- [PMID:35487942](../papers/35487942.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
