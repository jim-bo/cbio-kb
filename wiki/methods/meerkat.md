---
name: Meerkat
slug: meerkat
kind: method
canonical_source: corpus
unverified: true
tags: [structural-variant, bioinformatics]
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# Meerkat

## Overview

Meerkat is a computational tool for detecting somatic structural rearrangements (translocations, inversions, deletions, duplications) from paired-end whole-genome sequencing data using split-read and discordant read-pair signals.

## Used by

- Used in the TCGA ChRCC project to detect structural rearrangements from 50 WGS tumor/normal pairs (mean 16 rearrangements per case, range 0–207); identified recurrent genomic rearrangement breakpoints within ~10 kb upstream of the TERT transcription start site in 6/50 cases, a novel TERT-upregulation mechanism. [PMID:25155756](../papers/25155756.md)

## Notes

- Detects genome rearrangements from short-read WGS; outputs breakpoint positions and rearrangement classes.
- Used alongside kataegis identification in ChRCC; rearrangement breakpoints co-localized with APOBEC-pattern mutation clusters in a subset of cases.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-11**.*
