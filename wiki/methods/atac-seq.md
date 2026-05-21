---
name: ATAC-seq
slug: atac-seq
kind: method
canonical_source: corpus
unverified: false
tags: [epigenomics, chromatin-accessibility, sequencing]
processed_by: wiki-cli
processed_at: 2026-05-21
---

# ATAC-seq

## Overview

Assay for Transposase-Accessible Chromatin using sequencing (ATAC-seq) profiles genome-wide chromatin accessibility by using Tn5 transposase to preferentially insert sequencing adapters into open chromatin regions. The resulting reads map to nucleosome-free regions, enhancers, promoters, and other regulatory elements, revealing the active regulatory landscape of a cell population.

## Used by

- Used as the primary epigenomic profiling modality across 35 newly profiled metastatic CRPC models (22 organoids, 6 PDXs, 7 cell lines), identifying 861,195 reproducible peaks and defining four chromatin-based CRPC subtypes (CRPC-AR, CRPC-NE, CRPC-WNT, CRPC-SCL) in [prad_organoids_msk_2022](../datasets/prad_organoids_msk_2022.md) [PMID:35617398](../papers/35617398.md)
- Reviewed as a chromatin-accessibility profiling modality in multi-omics integration; highlighted in thyroid cancer study (Sanghi et al.) linking gene-body enhancers to correlated RNA/protein expression [PMID:37119971](../papers/37119971.md)

## Notes

- Generates genome-wide chromatin accessibility maps; particularly informative for identifying active enhancers and cell-type-specific regulatory elements.
- Commonly paired with RNA-seq and ChIP-seq for integrated epigenomic characterization.
- Consensus peak calling across replicates is standard; tools such as MACS2 are used for peak calling.

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:37119971](../papers/37119971.md)

*This page was processed by **wiki-cli** on **2026-05-21**.*
