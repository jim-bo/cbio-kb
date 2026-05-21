---
name: SvABA
slug: svaba
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
processed_at: 2026-05-21
---

# SvABA

## Overview

SvABA (Structural Variation and Breakpoint Assembly) is a genome-wide structural variant detection method that uses local sequence assembly of de Bruijn graphs on re-aligned reads to identify insertions, deletions, inversions, and translocations. It is designed for both whole-genome and targeted sequencing data and performs local assembly at candidate breakpoint regions, enabling fine-resolution breakpoint characterization. SvABA can operate on tumor-only or tumor-normal paired samples.

## Used by

- One of four SV-calling algorithms applied to 304 DLBCLs using targeted SV bait capture (mean depth 221.4×); consensus calls from SvABA, BreaKmer, Lumpy, and dRanger defined SVs in 64% of tumors, including recurrent [IGH](../genes/IGH.md) (40%), [BCL2](../genes/BCL2.md) (21%), [BCL6](../genes/BCL6.md) (19%), [MYC](../genes/MYC.md) (8%), and CD274/PD-L2 (5%) rearrangements [PMID:29713087](../papers/29713087.md)
- Applied alongside DELLY in the PCAWG pan-cancer WGS study (n=2,658 tumors) as an SV caller; consensus SV calls achieved ~90% sensitivity and ~97.5% precision across 38 tumor types [PMID:32025007](../papers/32025007.md).
- Used in [mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md) cWGTS pipeline for structural variant detection from whole-genome sequencing in 114 pediatric/AYA solid tumor patients; SVs were a principal value-add of WGS over panel/exome assays [PMID:35585047](../papers/35585047.md)

## Notes

- Corpus-derived slug; not a cBioPortal canonical gene-panel identifier.
- Local sequence assembly approach provides precise breakpoint sequences, which is advantageous for detecting complex rearrangements and small insertions/deletions at SV junctions.
- Commonly used alongside Lumpy (coverage-based), dRanger (paired-end), and split-read methods in consensus SV pipelines to improve sensitivity and specificity.

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32025007](../papers/32025007.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
