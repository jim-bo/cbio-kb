---
name: BreaKmer
slug: breakmer
kind: method
canonical_source: corpus
unverified: true
tags:
  - structural-variation
  - sv-calling
  - whole-exome-seq
  - somatic-sv
  - dlbcl
processed_by: crosslinker
processed_at: 2026-05-16
---

# BreaKmer

## Overview

BreaKmer is a computational method for detecting structural variants (SVs) — including translocations, inversions, deletions, and insertions — from targeted or whole-exome sequencing data. It uses a realignment approach on soft-clipped reads to identify split-read evidence for SV breakpoints. BreaKmer is particularly useful for hybrid capture-based sequencing where coverage depth is uneven.

## Used by

- Applied as one of four SV-calling algorithms in a WES study of 304 primary DLBCLs (with a spiked-in SV bait set, mean depth 221.4×); consensus calls from BreaKmer, Lumpy, dRanger, and SvABA identified SVs in 64% of tumors, including recurrent rearrangements of [IGH](../genes/IGH.md) (40%), [BCL2](../genes/BCL2.md) (21%), [BCL6](../genes/BCL6.md) (19%), [MYC](../genes/MYC.md) (8%), and CD274/PD-L2 (5%); Breakpointer used for validation [PMID:29713087](../papers/29713087.md)

## Notes

- Corpus-derived slug; not a cBioPortal canonical gene-panel identifier.
- Designed to work with capture-based sequencing (targeted or exome) rather than whole-genome sequencing.
- Output is typically used in ensemble/consensus SV calling pipelines alongside depth-of-coverage-based callers (e.g., Lumpy) and paired-end discordant-read callers (e.g., dRanger, SvABA).

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
