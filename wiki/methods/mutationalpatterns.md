---
name: MutationalPatterns
slug: mutationalpatterns
kind: method
canonical_source: corpus
unverified: true
tags: [mutational-signatures, bioinformatics, r-package]
processed_by: crosslinker
processed_at: 2026-05-21
---

# MutationalPatterns

## Overview

MutationalPatterns is an R/Bioconductor package for comprehensive analysis of somatic mutational patterns and signatures. It supports extraction and refitting of mutational signatures (SBS, DBS, indel), strand-bias analysis, lesion-segregation scoring, and transcriptional strand asymmetry analysis. Version 3.x introduced improved NMF extraction and bootstrapped confidence estimation.

## Used by

- Used alongside SigProfiler to characterize mutational signatures in endometrial polyps (v3.4.1); identified SBS8 and SBS89 in addition to the SBS1/SBS5/SBS40 signatures called by SigProfiler [PMID:28445112](../papers/28445112.md)
- Used in [prostate_pcbm_swiss_2019](../datasets/prostate_pcbm_swiss_2019.md) for COSMIC signature decomposition in 168 prostate cancer brain metastasis samples; identified SBS3 (HRD) enrichment in PCBM vs CRPC500, and SBS1/SBS5 (aging), SBS16, SBS44 (MMR-deficiency) signatures [PMID:35504881](../papers/35504881.md)
- Used for mutational signature decomposition (COSMIC v3.2) in 25 metastatic [CSCC](../cancer_types/CSCC.md) WGS samples; confirmed SBS7a/SBS7b/SBS7c UV dominance (>80% of SNVs C>T transitions) and identified SBS32 attributable to [azathioprine](../drugs/azathioprine.md) immunosuppression in one patient [PMID:35982973](../papers/35982973.md)

## Notes

- Provides complementary signature assignments to SigProfiler; differences between tools reflect NMF initialization and regularization choices.
- Supports both de novo extraction and fitting of COSMIC reference signatures.
- Implemented in R; compatible with Bioconductor workflows.

## Sources

- [PMID:28445112](../papers/28445112.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35504881](../papers/35504881.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35982973](../papers/35982973.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
