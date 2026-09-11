---
name: GSVA (Gene Set Variation Analysis)
slug: gsva
kind: method
canonical_source: corpus
unverified: true
tags: [pathway-analysis, gene-sets, single-sample-scoring, transcriptomics]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# GSVA (Gene Set Variation Analysis)

## Overview

GSVA is a single-sample gene-set enrichment method that converts a gene-by-sample expression matrix into a gene-set-by-sample enrichment matrix, allowing pathway-level scoring without predefined phenotype groups.

## Used by

- Used with MSigDB c2.cgp, c6, c7 and hallmark v6.0 gene sets (plus CIBERSORT and single-cell immune signatures) for single-sample pathway scoring of tumor RNA-seq in a neoadjuvant pembrolizumab glioblastoma trial (n=28 tumors) [PMID:30742122](../papers/30742122.md).
- Used for expression- and outcome-linked pathway scoring in whole-genome/RNA-sequenced Burkitt lymphoma and DLBCL tumors, alongside Salmon/DESeq2 quantification and Kaplan-Meier survival analysis [PMID:36201743](../papers/36201743.md).

## Notes

- Distinct from ssGSEA, though both are single-sample pathway-scoring methods used across the corpus; papers sometimes report both.

## Sources

- [PMID:30742122](../papers/30742122.md)
- [PMID:36201743](../papers/36201743.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
