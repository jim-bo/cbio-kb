---
name: ssGSEA (single-sample Gene Set Enrichment Analysis)
slug: ssgsea
kind: method
canonical_source: corpus
unverified: true
tags: [pathway-analysis, gene-set-enrichment, transcriptomics, bioinformatics]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# ssGSEA (single-sample Gene Set Enrichment Analysis)

## Overview

ssGSEA computes a per-sample enrichment score for a given gene set from ranked gene expression data, allowing pathway or signature activity to be scored independently in each sample rather than across a group comparison as in standard GSEA. It is commonly used to derive immune, proliferation, or pathway-activity scores for downstream correlation with clinical or genomic variables.

## Used by

- Used (alongside GSEA/WebGestaltR and PTM-SEA) for pathway and immune scoring of RNA-seq and phosphoproteomics data in a 60-sample neoadjuvant chemotherapy TNBC proteogenomics cohort [PMID:36001024](../papers/36001024.md).

## Notes

- Coverage, gene list, limitations.

## Sources
- [PMID:36001024](../papers/36001024.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
