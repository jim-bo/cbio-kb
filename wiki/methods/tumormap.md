---
name: TumorMap
slug: tumormap
kind: method
canonical_source: corpus
unverified: true
tags: [visualization, dimensionality-reduction, pan-cancer]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# TumorMap

## Overview

TumorMap is a web-based 2D visualization tool for exploring relationships between cancer samples based on their molecular profiles. It projects high-dimensional multi-omic data onto a hexagonal grid where similar samples are placed in proximity, enabling interactive exploration of molecular subtypes, clinical annotations, and genomic features across large cancer cohorts. TumorMap is developed at UCSC and was applied in TCGA PanCanAtlas analyses to display iCluster latent-variable distances across thousands of tumors.

## Used by

- Used to generate 2D visualization of iCluster latent-variable distances across ~10,000 TCGA PanCancer Atlas tumors from 33 cancer types, enabling visual exploration of the 28 integrated molecular subtypes [PMID:29625048](../papers/29625048.md).

## Notes

- Arranges samples on a hexagonal grid using neighbor-embedding of molecular similarity.
- Supports interactive overlays of clinical, genomic, and molecular annotations.
- Available as a public tool; applied to the full TCGA PanCancer Atlas cohort to complement iCluster classification with a navigable 2D map.
- Distinct from t-SNE or UMAP in that it uses an explicit hexagonal grid for stable, reproducible layout.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
