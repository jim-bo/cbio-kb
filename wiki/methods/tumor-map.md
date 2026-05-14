---
name: Tumor Map
slug: tumor-map
kind: method
canonical_source: corpus
unverified: true
tags: [visualization, dimensionality-reduction, multi-platform, pan-cancer]
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# Tumor Map

## Overview

Tumor Map is a web-based visualization and analysis tool developed at UCSC that projects multi-platform cancer genomic data onto a two-dimensional layout using dimensionality-reduction techniques (such as t-SNE or similar neighborhood-embedding methods). Samples from different tumor types or subtypes are arranged so that molecularly similar samples cluster together, enabling pan-cancer visualization and discovery of unexpected cross-cancer molecular similarities. The tool supports overlay of clinical, genomic, and expression features on the map.

## Used by

- Used for co-clustering and pan-cancer visualization of 1,122 TCGA diffuse glioma samples alongside other tumor types, enabling identification of molecular neighbors and cross-subtype relationships as part of the TCGA pan-glioma integrative analysis [PMID:26824661](../papers/26824661.md)

## Notes

- Originally developed at UCSC as part of the TCGA pan-cancer initiative.
- Supports overlay of genomic features (mutation, CNA, expression, methylation) on the map.
- Used to discover unexpected sample clusters that cross histologic or anatomic classification boundaries.
- Interactive web interface allows user-defined feature overlays and subtype annotation.

## Sources

- [PMID:26824661](../papers/26824661.md)

*This page was processed by **entity-page-writer** on **2026-05-14**.*
