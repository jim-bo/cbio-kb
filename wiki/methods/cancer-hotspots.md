---
name: Cancer Hotspots
slug: cancer-hotspots
kind: method
canonical_source: corpus
unverified: true
tags: [mutation-annotation, hotspot-detection, driver-discovery]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Cancer Hotspots

## Overview

Cancer Hotspots is a statistical method for identifying recurrently mutated positions in cancer genomes using 2D linear protein sequence proximity. Mutations at a given amino acid position are considered a hotspot if they occur more frequently than expected by chance across a large cancer cohort. The method provides a complementary approach to 3D structural hotspot analysis (3D Hotspots) and is available as a public resource at cancerhotspots.org.

## Used by

- Applied (alongside 3D protein-structure hotspot analysis) to annotate driver mutations in 9,125 TCGA PanCanAtlas tumors across 33 cancer types, contributing to the identification of 89% of tumors carrying at least one pathway driver alteration [PMID:29625050](../papers/29625050.md).

## Notes

- Identifies hotspots based on recurrence at specific amino acid positions in the linear protein sequence.
- Complements 3D Hotspots, which uses structural proximity rather than linear position.
- Part of the TCGA PanCanAtlas driver-annotation suite alongside MutSigCV, GISTIC 2.0, OncoKB, and RESET.
- Available as a public web resource; commonly used with OncoKB for oncogenicity classification.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
