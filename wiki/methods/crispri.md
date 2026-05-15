---
name: CRISPRi (CRISPR Interference)
slug: crispri
kind: method
canonical_source: corpus
unverified: true
tags:
  - crispr
  - gene-silencing
  - enhancer-perturbation
  - functional-genomics
  - prostate-cancer
processed_by: crosslinker
processed_at: 2026-05-15
---

# CRISPRi (CRISPR Interference)

## Overview

CRISPRi uses a catalytically dead Cas9 (dCas9) fused to a transcriptional repressor domain (e.g., KRAB) guided by single-guide RNAs (sgRNAs) to silence target genomic loci without cutting DNA. Unlike canonical CRISPR-Cas9 editing, CRISPRi is reversible and does not introduce permanent sequence alterations. It is commonly applied to silence enhancers or promoters in a locus-specific manner, establishing causal links between non-coding regulatory elements and target gene expression.

## Used by

- dCas9 + sgRNAs targeting the rs4519489 enhancer region used in 22Rv1 and PC3 prostate cancer cells; CRISPRi silencing of the rs4519489 locus significantly reduced [NOL10](../genes/NOL10.md) mRNA (P=9.79×10⁻⁵ and P=4.79×10⁻⁴ respectively), establishing a direct causal link between the enhancer and NOL10 expression [PMID:28927585](../papers/28927585.md)

## Notes

- CRISPRi is locus-specific and reversible, making it well-suited to characterize the regulatory activity of non-coding elements without permanently altering the sequence.
- Complementary to CRISPR base editing, which permanently changes the allele.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
