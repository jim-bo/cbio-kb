---
name: GRIDSS (Genome Rearrangement IDentification Software Suite)
slug: gridss
kind: method
canonical_source: corpus
unverified: true
tags: [structural-variant, wgs, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-09-10
---

# GRIDSS (Genome Rearrangement IDentification Software Suite)

## Overview

GRIDSS is an open-source software suite for the detection of genomic structural variants (SVs) from short-read sequencing data. It uses a breakpoint graph approach to identify SVs including deletions, duplications, inversions, and translocations with high sensitivity and specificity. GRIDSS is typically used as part of the Hartwig Medical Foundation WGS pipeline alongside PURPLE (purity/ploidy) and LINX (SV annotation) for comprehensive genomic profiling.

## Used by

- Used for structural variant calling in WGS of 25 metastatic cutaneous squamous cell carcinoma ([CSCC](../cancer_types/CSCC.md)) lymph node specimens; structural variant gene list (annotated via LINX/PURPLE) included [SMAD4](../genes/SMAD4.md), [CDKN2A](../genes/CDKN2A.md), [MYC](../genes/MYC.md), [PTPRD](../genes/PTPRD.md), [CALR](../genes/CALR.md), [EGFR](../genes/EGFR.md), [APC](../genes/APC.md), [CREBBP](../genes/CREBBP.md), and others; deletions and complex SVs predominated; two coding-coding fusions detected (STRN-DLG2, HEBP2-NTRK2) [PMID:35982973](../papers/35982973.md)
- Used (with Manta) for structural variant calling in whole-genome-sequenced Burkitt lymphoma and DLBCL tumors [PMID:36201743](../papers/36201743.md).
- Used (GRIDSS2, combined with Manta and SvABA) for structural variant calling in whole-genome-sequenced CDH1-wild-type invasive lobular carcinomas [PMID:38347189](../papers/38347189.md).
- Used (with LINX) for structural variant calling in whole-genome-sequenced SDHB-related paraganglioma/pheochromocytoma tumors [PMID:40097403](../papers/40097403.md).

## Notes

- Part of the Hartwig Medical Foundation open-source WGS pipeline (GRIDSS → PURPLE → LINX).
- Handles complex rearrangements and chromoplexy events common in high-TMB tumors.
- Reference: Cameron et al. Genome Research 2017.

## Sources

- [PMID:35982973](../papers/35982973.md)
- [PMID:36201743](../papers/36201743.md)
- [PMID:38347189](../papers/38347189.md)
- [PMID:40097403](../papers/40097403.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
