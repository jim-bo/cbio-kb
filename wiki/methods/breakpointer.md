---
name: BreakPointer
slug: breakpointer
kind: method
canonical_source: corpus
unverified: false
tags:
  - structural-variation
  - rearrangement
  - whole-genome-seq
  - breakpoint-detection
processed_by: entity-page-writer
processed_at: 2026-05-09
---

# BreakPointer

## Overview

BreakPointer is a computational tool for fine-mapping structural variant breakpoints in whole-genome sequencing data. It uses discordant read-pair and split-read signals to refine the precise genomic coordinates of somatic rearrangements detected by broader SV callers such as dRanger. BreakPointer is typically applied after an initial SV discovery step to produce base-pair-resolution breakpoint coordinates suitable for downstream fusion annotation or PCR validation.

## Used by

- Applied alongside dRanger, MuTect, Indelocator, CLONET, ChainFinder, ABSOLUTE, and GISTIC v2 in WGS analysis of 57 prostate tumors to characterize chromoplexy rearrangement chains; 113 rearrangements were validated by PCR/resequencing [PMID:23622249](../papers/23622249.md)

## Notes

- Designed to complement dRanger (or equivalent paired-end SV discovery); not a standalone discovery tool.
- Outputs base-pair-resolution breakpoints, enabling downstream in-frame/out-of-frame fusion classification.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-09**.*
