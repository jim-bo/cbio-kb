---
name: EXPANDS
slug: expands
kind: method
canonical_source: corpus
unverified: true
tags:
  - clonal-evolution
  - subclonal-reconstruction
  - copy-number
  - snv
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# EXPANDS

## Overview

EXPANDS (Expanding Ploidy and Allele Frequency on Nested Subpopulations) is a computational method for inferring clonal population structure from bulk tumor sequencing data. It integrates somatic SNV allele frequencies and copy-number information to reconstruct the number and composition of co-existing tumor subclones, estimate their prevalence, and build phylogenetic relationships between subpopulations.

## Used by

- Used alongside PyClone for clonal-prevalence inference in 14 germline-matched medulloblastoma WGS pairs; EXPANDS modelling confirmed branched clonal evolution in all 14 cases and detected increased clonal-population counts post-therapy in 71.4% of patients [PMID:26760213](../papers/26760213.md).

## Notes

- Operates on paired SNV and copy-number segmentation data from bulk tumor sequencing.
- Returns estimates of subclonal population frequencies and a phylogenetic tree of clonal populations.
- Validated for use with WGS and WES data; sensitivity is limited by sequencing depth and purity.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-14**.*
