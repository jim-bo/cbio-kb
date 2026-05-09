---
name: BamBam
slug: bambam
kind: STRUCTURAL_VARIANT
canonical_source: corpus
unverified: true
tags: [structural-variant, sv-caller, wgs, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-09
---

# BamBam

## Overview

BamBam is a structural variant detection and comparative genomics tool that identifies somatic rearrangements by comparing matched tumor and normal BAM files. It detects discordant read pairs and split reads to call structural variants including deletions, inversions, tandem duplications, and translocations. BamBam was developed at the Broad Institute and used in TCGA large-scale cancer genomics projects.

## Used by

- Used alongside BreakDancer as a structural variant caller in the TCGA [GBM](../cancer_types/GBM.md) 2013 whole-genome sequencing analysis (n=42 tumor/normal pairs); contributed to the identification of 238 high-confidence somatic rearrangements, recurrent [EGFR](../genes/EGFR.md) intragenic events, and a chromothripsis event on chr1 spanning 7.5 Mb [PMID:24120142](../papers/24120142.md)

## Notes

- BamBam performs paired tumor-normal comparison to improve specificity for somatic SV calls over germline variation.
- Used in ensemble with BreakDancer in TCGA GBM to increase sensitivity and specificity for SV detection.
- Outputs are typically filtered and validated against orthogonal platforms.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
