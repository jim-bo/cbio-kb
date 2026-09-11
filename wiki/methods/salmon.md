---
name: Salmon
slug: salmon
kind: method
canonical_source: corpus
unverified: true
tags: [rna-seq, quantification, expression, bioinformatics]
processed_by: crosslinker
processed_at: 2026-09-11
---

# Salmon

## Overview

Salmon is a lightweight, alignment-free tool for transcript-level quantification of RNA-seq data. It uses quasi-mapping and an expectation-maximization procedure to [estimate](../methods/estimate.md) transcript abundances (TPM, estimated counts) directly from raw reads against a transcriptome index, without requiring a full read alignment step.

## Used by

- Used for RNA-seq expression quantification feeding DESeq2 differential expression and GSVA pathway analysis in a 281-tumor Burkitt lymphoma / DLBCL genomic study [PMID:36201743](../papers/36201743.md).

## Notes

- Coverage, gene list, limitations.

## Sources
- [PMID:36201743](../papers/36201743.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
