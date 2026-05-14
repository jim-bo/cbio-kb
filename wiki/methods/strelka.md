---
name: Strelka
slug: strelka
kind: method
canonical_source: corpus
unverified: true
tags: [variant-calling, snv, indel, somatic, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-14
---

# Strelka

## Overview

Strelka (and its successor Strelka2) is a somatic small-variant caller for matched tumor-normal whole-genome or whole-exome sequencing data. It uses a Bayesian statistical model to call single-nucleotide variants (SNVs) and small insertions/deletions (indels), explicitly accounting for sequencing error rates, local depth variation, and tumor purity. Strelka2 added support for germline variant calling and improved sensitivity for indels in homopolymer regions.

## Used by

- Used to call somatic SNVs and indels from paired tumor/normal WGS data (hg19 BWA alignment) for 28 metastatic neuroendocrine neoplasms in the BC Cancer Personalized OncoGenomics (POG) program; results fed into TMB estimation (median 2.19 mut/Mb), mutational signature analysis, and actionability assessment [PMID:24326773](../papers/24326773.md).
- Used for somatic variant calling in whole-genome sequencing of four CRC primary/metastasis trios to validate MSK-IMPACT findings. [PMID:25164765](../papers/25164765.md)
- Used for somatic variant calling in [MPNST](../cancer_types/MPNST.md) WES discovery cohort (15 tumors) [PMID:25240281](../papers/25240281.md)
- Strelka used for somatic SNV calling in whole-exome sequencing of adrenocortical carcinoma [PMID:26095796](../papers/26095796.md)

## Notes

- Designed for paired tumor-normal analysis; lower sensitivity in tumor-only or low-purity samples than in high-purity matched pairs.
- Strelka (v1) and Strelka2 (v2) have different calling models; downstream comparisons should specify version.
- Commonly used alongside structural-variant callers (ABySS, Manta) in comprehensive WGS pipelines.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25164765](../papers/25164765.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25240281](../papers/25240281.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26095796](../papers/26095796.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
