---
name: CIBERSORT
slug: cibersort
kind: method
canonical_source: corpus
unverified: true
tags: [immune-deconvolution, digital-cytometry, rna-seq, support-vector-regression]
processed_by: crosslinker
processed_at: 2026-09-11
---

# CIBERSORT

## Overview

CIBERSORT is a computational deconvolution algorithm that estimates the relative proportions of 22 immune cell subsets in bulk gene-expression profiles, using support vector regression against the LM22 leukocyte signature matrix, without requiring physical cell sorting.

## Used by

- Run in [absolute](../methods/absolute.md) mode alongside ESTIMATE and xCell for immune/stromal deconvolution in a breast cancer proteogenomic cohort [PMID:36001024](../papers/36001024.md)

## Notes

- Predecessor to [CIBERSORTx](../methods/cibersortx.md), which adds batch correction and support for single-cell-derived reference signatures.
- Absolute mode produces cell-type scores in arbitrary units that are comparable across samples within a study but are not directly interpretable as cell fractions.

## Sources

- [PMID:36001024](../papers/36001024.md) — breast cancer proteogenomic cohort; CIBERSORT (absolute mode) run alongside ESTIMATE and xCell for immune/stromal deconvolution.

*This page was processed by **crosslinker** on **2026-09-11**.*
