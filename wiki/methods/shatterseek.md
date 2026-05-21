---
name: ShatterSeek
slug: shatterseek
kind: method
canonical_source: corpus
unverified: true
tags: [structural-variation, chromothripsis, wgs]
processed_by: wiki-cli
processed_at: 2026-05-21
---

# ShatterSeek

## Overview

ShatterSeek is a computational algorithm that detects chromothripsis — a catastrophic, one-step rearrangement process producing complex structural variants — from whole-genome sequencing data. It integrates copy-number oscillation patterns and structural breakpoint clustering to identify samples with chromothriptic events.

## Used by

- Applied to deep WGS data from 38 cutaneous melanoma samples; complex structural rearrangements detected by ShatterSeek were significantly enriched in the Triple-WT subtype (11/16 ShatterSeek events in Triple-WT, Fisher's p = 0.00098); 7/7 Triple-WT samples with complex rearrangements lacked the UV mutational signature, suggesting an alternative mutational mechanism. [PMID:26091043](../papers/26091043.md)
- Applied to aSCLC WGS data to detect chromothripsis; identified chromothripsis in 16/19 (84%) non-MSI aSCLC, predominantly on chromosomes 11, 12, and 1; average 565 SVs per case (range up to >1,900); used as gold standard against which MSK-IMPACT panel-based oscillating CNA detection was benchmarked (100% specificity, 77% sensitivity) [PMID:39185963](../papers/39185963.md)

## Notes

- Requires deep WGS for reliable chromothripsis calling; low-pass WGS is insufficient.
- In TCGA [SKCM](../cancer_types/SKCM.md), 119 additional low-pass WGS samples were used for copy-number segmentation but not for ShatterSeek analysis.

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:39185963](../papers/39185963.md)

*This page was processed by **wiki-cli** on **2026-05-21**.*
