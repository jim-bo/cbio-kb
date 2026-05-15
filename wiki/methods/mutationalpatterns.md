---
name: MutationalPatterns
slug: mutationalpatterns
kind: method
canonical_source: corpus
unverified: true
tags: [mutational-signatures, bioinformatics, r-package]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# MutationalPatterns

## Overview

MutationalPatterns is an R/Bioconductor package for comprehensive analysis of somatic mutational patterns and signatures. It supports extraction and refitting of mutational signatures (SBS, DBS, indel), strand-bias analysis, lesion-segregation scoring, and transcriptional strand asymmetry analysis. Version 3.x introduced improved NMF extraction and bootstrapped confidence estimation.

## Used by

- Used alongside SigProfiler to characterize mutational signatures in endometrial polyps (v3.4.1); identified SBS8 and SBS89 in addition to the SBS1/SBS5/SBS40 signatures called by SigProfiler [PMID:28445112](../papers/28445112.md)

## Notes

- Provides complementary signature assignments to SigProfiler; differences between tools reflect NMF initialization and regularization choices.
- Supports both de novo extraction and fitting of COSMIC reference signatures.
- Implemented in R; compatible with Bioconductor workflows.

## Sources

- [PMID:28445112](../papers/28445112.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
