---
name: Indelocator
slug: indelocator
kind: method
canonical_source: corpus
unverified: false
tags:
  - indel-calling
  - somatic-mutation
  - whole-exome-seq
  - whole-genome-seq
processed_by: entity-page-writer
processed_at: 2026-05-09
---

# Indelocator

## Overview

Indelocator is a somatic indel (insertion/deletion) caller developed at the Broad Institute. It detects small insertions and deletions in tumor/normal paired sequencing data by comparing read alignments and applying statistical filters to identify somatic events. Indelocator is commonly run in tandem with MuTect (which handles SNVs) to provide a complete somatic small-variant callset for cancer genome studies.

## Used by

- Applied alongside MuTect, dRanger, BreakPointer, CLONET, ChainFinder, ABSOLUTE, and GISTIC v2 in WGS analysis of 57 prostate tumors; total cohort had 356,136 somatic base-pair mutations with an average of 33 non-silent exonic mutations per primary tumor [PMID:23622249](../papers/23622249.md)
- Used for indel calling in 149 esophageal adenocarcinoma WGS/WES pairs alongside MuTect; median 104 non-silent coding mutations per tumor [PMID:23525077](../papers/23525077.md)

## Notes

- Designed for paired tumor/normal analysis; not intended for tumor-only calling.
- Typically used in conjunction with MuTect for comprehensive somatic SNV+indel discovery.
- Outputs feed into significance callers (e.g., MutSig) and manual validation workflows.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-09**.*
