---
name: Single-cell DNA sequencing
slug: single-cell-dna-seq
kind: method
canonical_source: corpus
unverified: true
tags: [single-cell, dna-sequencing, clonal-evolution, tumor-heterogeneity]
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Single-cell DNA sequencing

## Overview

Single-cell DNA sequencing (scDNA-seq) resolves somatic mutation co-occurrence and clonal architecture at the level of individual cells, overcoming the averaging effect of bulk sequencing. Commercial implementations such as Mission Bio Tapestri use microfluidic droplet partitioning combined with targeted amplicon sequencing (hundreds of amplicons covering tens to hundreds of genes) to genotype thousands of single cells per sample. This technology is particularly powerful for studying tumor heterogeneity, clonal co-occurrence of resistance mutations, and cell-to-cell variation in copy number.

## Used by

- Applied on C106 resistant KRASG12C-mutant colorectal cancer cells using the Mission Bio Tapestri platform (317 amplicons, 54 genes) to resolve co-occurrence of acquired resistance mutations (NRASG12D clonal, APCQ879* subclonal) at single-cell resolution [PMID:36355783](../papers/36355783.md)

## Notes

- Mission Bio Tapestri is a targeted amplicon-based approach; coverage is limited to the designed amplicon panel rather than the entire genome.
- Sensitivity for low-frequency somatic events and structural variants (large indels, CNVs) is lower than bulk WGS but co-occurrence information is uniquely available only at single-cell resolution.
- Cell numbers per run are typically in the thousands; rare subclones at <1% frequency may be missed.

## Sources

- [PMID:36355783](../papers/36355783.md) — KRASG12C-mutant CRC resistance study; Tapestri scDNA-seq on C106 resistant cells to characterize clonal architecture of acquired resistance.

*This page was processed by **entity-page-writer** on **2026-05-06**.*
