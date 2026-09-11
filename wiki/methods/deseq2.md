---
name: DESeq2
slug: deseq2
kind: method
canonical_source: corpus
unverified: true
tags: [differential-expression, rna-seq, bioinformatics, statistics]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# DESeq2

## Overview

DESeq2 is an R/Bioconductor package for differential gene-expression analysis of RNA-seq count data, using a negative-binomial generalized linear model with empirical Bayes shrinkage of dispersion and fold-change estimates.

## Used by

- Used for differential expression analysis of whole-transcriptome RNA-seq (STAR-aligned, Salmon-quantified) in a triple-negative breast cancer immunotherapy cohort [PMID:35121644](../papers/35121644.md)
- Used with Salmon quantification and GSVA/Kaplan-Meier survival analysis to assess expression and outcome differences among Burkitt lymphoma / DLBCL genetic subgroups [PMID:36201743](../papers/36201743.md)

## Notes

- Commonly paired with [Salmon](../methods/salmon.md) or STAR for upstream alignment/quantification before differential-expression testing.

## Sources

- [PMID:35121644](../papers/35121644.md) — triple-negative breast cancer immunotherapy cohort; DESeq2 differential expression on STAR/Salmon-processed RNA-seq.
- [PMID:36201743](../papers/36201743.md) — adult/pediatric Burkitt lymphoma WGS cohort; DESeq2 used with Salmon and GSVA for expression/outcome analysis.

*This page was processed by **entity-page-writer** on **2026-09-10**.*
