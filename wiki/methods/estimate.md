---
name: ESTIMATE
slug: estimate
kind: method
canonical_source: corpus
unverified: true
tags: [immune-deconvolution, tumor-purity, stromal-scoring, expression-based]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# ESTIMATE

## Overview

ESTIMATE (Estimation of STromal and Immune cells in MAlignant Tumor tissues using Expression data) is an algorithm that uses gene expression signatures to infer the proportions of stromal and immune cells in bulk tumor RNA-seq or microarray data. It produces three scores: an ImmuneScore (immune cell infiltration), a StromalScore (stromal cell content), and an ESTIMATEScore that combines both. Tumor purity can be estimated as the complement of the ESTIMATEScore. The method relies on pre-defined gene sets derived from non-negative matrix factorization of TCGA expression data.

## Used by

- Applied to TCGA diffuse glioma expression data as part of the pan-glioma integrative analysis to estimate stromal and immune cell infiltration and tumor purity across the 1,122-sample cohort; used alongside PARADIGM and Tumor Map for multi-platform integration [PMID:26824661](../papers/26824661.md)
- Applied to CCA transcriptome data to quantify immune infiltration, revealing elevated immune scores in both Cluster 2 and 3, but only Cluster 3 specifically upregulated immune-checkpoint genes (PDCD1, PDCD1LG2, BTLA) [PMID:28667006](../papers/28667006.md)
- ESTIMATE and Bindea immune signatures applied to 206 TCGA sarcomas; NK-cell infiltration was the only immune signature correlated with disease-specific survival across multiple histologies [PMID:29100075](../papers/29100075.md)
- Used to derive tumor-purity estimates from TCGA GBM data (n=172) for comparison with the recurrent GBM anti-PD-1 cohort; PTEN-mutant tumors had lower purity (p=0.028) [PMID:30742119](../papers/30742119.md)
- Used in the Sherlock-Lung NS-LUAD study (n=684 tumors) to estimate tumor purity from RNA-seq data as part of the cell-composition deconvolution workflow [PMID:32015526](../papers/32015526.md).

## Notes

- Based on single-sample GSEA (ssGSEA) applied to two curated gene sets: a stromal signature and an immune signature.
- Tumor purity estimate correlates with but does not replace orthogonal estimates from DNA (e.g., ABSOLUTE, CLONET, FACETS).
- Validated across multiple TCGA cancer types; widely used in pan-cancer immunogenomics studies.
- Published by Yoshihara et al. (Nature Communications, 2013).

## Sources

- [PMID:26824661](../papers/26824661.md)

*This page was processed by **entity-page-writer** on **2026-05-14**.*
- [PMID:28667006](../papers/28667006.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29100075](../papers/29100075.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:30742119](../papers/30742119.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:32015526](../papers/32015526.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
