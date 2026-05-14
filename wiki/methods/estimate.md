---
name: ESTIMATE
slug: estimate
kind: method
canonical_source: corpus
unverified: true
tags: [immune-deconvolution, tumor-purity, stromal-scoring, expression-based]
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# ESTIMATE

## Overview

ESTIMATE (Estimation of STromal and Immune cells in MAlignant Tumor tissues using Expression data) is an algorithm that uses gene expression signatures to infer the proportions of stromal and immune cells in bulk tumor RNA-seq or microarray data. It produces three scores: an ImmuneScore (immune cell infiltration), a StromalScore (stromal cell content), and an ESTIMATEScore that combines both. Tumor purity can be estimated as the complement of the ESTIMATEScore. The method relies on pre-defined gene sets derived from non-negative matrix factorization of TCGA expression data.

## Used by

- Applied to TCGA diffuse glioma expression data as part of the pan-glioma integrative analysis to estimate stromal and immune cell infiltration and tumor purity across the 1,122-sample cohort; used alongside PARADIGM and Tumor Map for multi-platform integration [PMID:26824661](../papers/26824661.md)

## Notes

- Based on single-sample GSEA (ssGSEA) applied to two curated gene sets: a stromal signature and an immune signature.
- Tumor purity estimate correlates with but does not replace orthogonal estimates from DNA (e.g., ABSOLUTE, CLONET, FACETS).
- Validated across multiple TCGA cancer types; widely used in pan-cancer immunogenomics studies.
- Published by Yoshihara et al. (Nature Communications, 2013).

## Sources

- [PMID:26824661](../papers/26824661.md)

*This page was processed by **entity-page-writer** on **2026-05-14**.*
