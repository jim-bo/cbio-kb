---
name: FIREFLY
slug: firefly
kind: method
canonical_source: corpus
unverified: true
tags:
  - non-coding
  - promoter-mutation
  - transcription-factor-binding
  - gene-set-analysis
  - cholangiocarcinoma
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# FIREFLY

## Overview

FIREFLY is a computational method for identifying non-coding regulatory dysregulation at the gene-set level. It integrates protein-binding microarray (PBM) data for transcription factors (TFs) with somatic promoter-mutation calls from whole-genome sequencing to identify gene sets enriched for promoter mutations that alter TF binding and produce concordant transcriptional dysregulation. FIREFLY scores are computed at the gene-set level rather than per-mutation, making it sensitive to the diffuse signal of individually rare non-coding mutations.

## Used by

- Applied to 70 CCA WGS samples and 6,639 mutated promoters in the ICGC cholangiocarcinoma study; integrating protein-binding microarray data for 486 TFs identified four gene sets enriched for promoter mutations that alter TF binding and produce concordant transcriptional dysregulation. Two of the four sets are PRC2/H3K27me3 targets preferentially mutated in Cluster 1 (CpG-island hypermethylation subtype) [PMID:28667006](../papers/28667006.md)

## Notes

- Developed in the context of the ICGC cholangiocarcinoma study; does not predict directionality of expression change for individual mutations since TFs can be activators or repressors.
- Gene-set-level effects are inferred without per-mutation directionality.
- Whether the approach recovers analogous signals in other cancer types remains an open empirical question.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
