---
name: Strelka
slug: strelka
kind: method
canonical_source: corpus
unverified: true
tags: [variant-calling, snv, indel, somatic, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Strelka

## Overview

Strelka (and its successor Strelka2) is a somatic small-variant caller for matched tumor-normal whole-genome or whole-exome sequencing data. It uses a Bayesian statistical model to call single-nucleotide variants (SNVs) and small insertions/deletions (indels), explicitly accounting for sequencing error rates, local depth variation, and tumor purity. Strelka2 added support for germline variant calling and improved sensitivity for indels in homopolymer regions.

## Used by

- Used to call somatic SNVs and indels from paired tumor/normal WGS data (hg19 BWA alignment) for 28 metastatic neuroendocrine neoplasms in the BC Cancer Personalized OncoGenomics (POG) program; results fed into TMB estimation (median 2.19 mut/Mb), mutational signature analysis, and actionability assessment [PMID:40328872](../papers/40328872.md).
- Used for somatic variant calling in whole-genome sequencing of four CRC primary/metastasis trios to validate MSK-IMPACT findings. [PMID:25164765](../papers/25164765.md)
- Used for somatic variant calling in [MPNST](../cancer_types/MPNST.md) WES discovery cohort (15 tumors) [PMID:25240281](../papers/25240281.md)
- Strelka used for somatic SNV calling in whole-exome sequencing of adrenocortical carcinoma [PMID:26095796](../papers/26095796.md)
- Used for SNV calling in whole-genome sequencing of 46 matched primary/recurrent medulloblastoma samples alongside MutationSeq; contributed to characterization of massive genetic divergence (mean <12% shared events) between primary and recurrent tumor clones [PMID:26760213](../papers/26760213.md).
- Used alongside Indelocator for indel calling in 619 CRC FFPE tumor/normal WES pairs; only calls concordant between both tools were retained [PMID:27149842](../papers/27149842.md)
- Used Strelka for somatic indel and SNV calling in paired tumor-normal samples [PMID:28373299](../papers/28373299.md)
- Applied alongside MuTect, SomaticSniper, and VarScan for somatic variant calling in 68 paired melanoma WES samples; intersection-based approach used to increase specificity [PMID:29033130](../papers/29033130.md)
- Strelka used for somatic variant calling in 35 metastatic [CCRCC](../cancer_types/CCRCC.md) paired tumor/normal WES samples alongside MuTect for the PBRM1-immunotherapy response study [PMID:29301960](../papers/29301960.md)
- Used to call indels (v1.0.11) across 1,013 prostate tumor/normal pairs in the prad_p1000 dataset [PMID:29610475](../papers/29610475.md)
- Used for somatic indel calling in the uniform reanalysis of 249 MSS tumor/normal WES samples from seven ICB cohorts; combined with MuTect (SNVs) and Oncotator (annotation) [PMID:30150660](../papers/30150660.md)

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
- [PMID:26760213](../papers/26760213.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:27149842](../papers/27149842.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28373299](../papers/28373299.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29301960](../papers/29301960.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29610475](../papers/29610475.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:30150660](../papers/30150660.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
