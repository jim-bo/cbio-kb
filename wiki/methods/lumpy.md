---
name: Lumpy
slug: lumpy
kind: method
canonical_source: corpus
unverified: true
tags:
  - structural-variation
  - sv-calling
  - whole-exome-seq
  - whole-genome-seq
  - somatic-sv
  - dlbcl
processed_by: crosslinker
processed_at: 2026-05-16
---

# Lumpy

## Overview

Lumpy is a probabilistic framework for structural variant (SV) detection that integrates multiple signals — split reads, discordant paired-end reads, and read-depth — using a general combinatorial scoring function. It is designed to detect a broad spectrum of SVs including deletions, duplications, inversions, and translocations. By probabilistically combining evidence types rather than requiring all signals to agree, Lumpy achieves higher sensitivity than single-evidence methods, particularly for low-coverage data.

## Used by

- One of four SV-calling algorithms applied to 304 DLBCLs using a targeted SV bait capture set (mean depth 221.4×); consensus calls from Lumpy, BreaKmer, dRanger, and SvABA defined SVs in 64% of tumors (189/296), with the most frequently rearranged genes being [IGH](../genes/IGH.md) (40%), [BCL2](../genes/BCL2.md) (21%), [BCL6](../genes/BCL6.md) (19%), [MYC](../genes/MYC.md) (8%), and CD274/PDCD1LG2 (5%) [PMID:29713087](../papers/29713087.md)

## Notes

- Corpus-derived slug; not a cBioPortal canonical gene-panel identifier.
- Lumpy uses a probabilistic model that can combine evidence from different sequencing library types (e.g., paired-end and split-reads) into a unified SV call.
- Typically integrated in ensemble SV pipelines alongside assembly-based methods (SvABA), read-pair methods (dRanger), and split-read methods (BreaKmer) to maximize sensitivity and specificity.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
