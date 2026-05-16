---
name: SFyNCS
slug: sfyncs
kind: method
canonical_source: corpus
unverified: true
tags: [fusion-detection, rna-seq, bioinformatics, structural-variant]
processed_by: crosslinker
processed_at: 2026-05-16
---

# SFyNCS

## Overview

SFyNCS (Splice-site-spanning Fusions in Non-Canonical Splicing) is an RNA-seq-based gene fusion detection tool. Version 0.15 was applied in the Sherlock-Lung NS-LUAD study alongside [STAR-Fusion](../methods/star-fusion.md). It is designed to detect a broad range of fusion transcripts, including those arising from structural variants or non-canonical splicing events. Results from SFyNCS and STAR-Fusion were intersected with matched whole-genome sequencing structural-variant calls to confirm genomic support for detected fusions.

## Used by

- Used in the Sherlock-Lung NS-LUAD study (n=684 never-smoker lung adenocarcinomas) alongside [STAR-Fusion](../methods/star-fusion.md); the combined pipeline detected 11,947 fusions across 638/684 tumors, of which 54.3% were supported by matched WGS structural variants; the most frequent in-frame fusions were EML4-ALK (33 tumors) and KIF5B-RET (8 tumors); a novel recurrent PARG-BMS1 fusion was identified in 5 tumors [PMID:32015526](../papers/32015526.md).

## Notes

- Typically run on STAR-aligned BAM files ([STAR](../genes/STAR.md) v2.7.3 in the Sherlock-Lung study).
- Fusion support from WGS SVs (54.3% in Sherlock-Lung) serves as orthogonal validation; fusions without WGS support may still be real but have lower confidence.
- Proliferative NS-LUAD subtypes had significantly higher mean fusion counts (22.1) than steady (13.9) or chaotic (10.7) subtypes.

## Sources

- [PMID:32015526](../papers/32015526.md) — Sherlock-Lung NS-LUAD fusion detection

*This page was processed by **crosslinker** on **2026-05-16**.*
