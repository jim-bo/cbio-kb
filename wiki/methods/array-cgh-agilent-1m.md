---
name: Agilent 1M Human Oligonucleotide aCGH
slug: array-cgh-agilent-1m
kind: COPY_NUMBER_ALTERATION
canonical_source: corpus
unverified: true
tags: [copy-number, array-cgh, agilent]
processed_by: crosslinker
processed_at: 2026-05-09
---

# Agilent 1M Human Oligonucleotide aCGH

## Overview

Array comparative genomic hybridization (aCGH) using the Agilent 1M human oligonucleotide microarray platform. Tumor DNA is co-hybridized with reference normal DNA; resulting log2 ratios are segmented (e.g., by circular binary segmentation) and subjected to copy-number calling algorithms such as RAE. At ~1 million probes, the platform provides high-resolution somatic copy-number alteration (SCNA) detection across the genome.

## Used by

- Applied to 97 high-grade urothelial carcinomas of the bladder ([BLCA](../cancer_types/BLCA.md)) cohybridized with reference normal DNA; segmented by circular binary segmentation and analyzed with the RAE algorithm at FDR <1%; identified two distinct CNA-burden subsets and recurrent focal amplifications including [ERBB2](../genes/ERBB2.md) (17q12) and [CCND1](../genes/CCND1.md) (11q13.2–13.3) [PMID:23897969](../papers/23897969.md)

## Notes

- Co-hybridization with reference normal DNA controls for dye bias; circular binary segmentation is the standard downstream segmentation approach.
- High-CNA-burden bladder tumors identified by this platform had structural-aberration loads second only to serous ovarian cancer across 14 tumor types (n=5,135).
- Superseded in large-scale studies by SNP 6.0 arrays and WGS-based CNA inference, but remains in use for clinical and research validation.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
