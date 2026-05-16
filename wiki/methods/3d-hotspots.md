---
name: 3D Hotspots
slug: 3d-hotspots
kind: method
canonical_source: corpus
unverified: true
tags: [mutation-annotation, hotspot-detection, structural-biology]
processed_by: crosslinker
processed_at: 2026-05-16
---

# 3D Hotspots

## Overview

3D Hotspots is a method for identifying recurrently mutated amino acid positions in cancer by considering three-dimensional protein structure rather than only linear (1D) sequence proximity. It clusters somatic mutations onto structural models to detect hotspots where spatially proximate residues are frequently mutated, even if they are linearly distant in the primary sequence. This complements the 2D (linear) [cancer-hotspots](../methods/cancer-hotspots.md) approach and improves detection of structurally relevant driver mutations in oncoproteins.

## Used by

- Used alongside the 2D cancer-hotspots method to annotate driver mutations in 9,125 TCGA PanCanAtlas tumors across 33 cancer types; 3D structural hotspots contributed to identification of [CDKN2A](../genes/CDKN2A.md) promoter methylation (RESET) and pathway-level alteration calls [PMID:29625050](../papers/29625050.md).

## Notes

- Requires 3D structural data (PDB models); may have lower sensitivity for proteins lacking solved or modelled structures.
- Used in conjunction with 2D linear hotspot analysis (cancer-hotspots) and OncoKB annotation for comprehensive driver mutation identification.
- Part of the TCGA PanCanAtlas driver-annotation suite alongside MutSigCV, GISTIC 2.0, and RESET.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
