---
name: HINT-ATAC Footprinting
slug: hint-atac-footprinting
kind: method
canonical_source: corpus
unverified: true
tags: [epigenomics, chromatin-accessibility, transcription-factor-binding, footprinting]
processed_by: crosslinker
processed_at: 2026-05-21
---

# HINT-ATAC Footprinting

## Overview

HINT-ATAC (High-resolution footprINT using ATAC-seq) is a computational method for identifying transcription factor (TF) binding [footprints](../methods/footprints.md) within ATAC-seq data. It uses digital genomic footprinting to infer TF occupancy from Tn5 insertion profiles, accounting for the Tn5 insertion bias inherent in ATAC-seq experiments. This enables high-resolution mapping of active TF binding sites genome-wide.

## Used by

- Used in [prad_organoids_msk_2022](../datasets/prad_organoids_msk_2022.md) to identify key transcription factors driving the four CRPC chromatin subtypes (CRPC-AR, CRPC-NE, CRPC-WNT, CRPC-SCL) from ATAC-seq data across 35 metastatic prostate cancer models [PMID:35617398](../papers/35617398.md)

## Notes

- Extends standard ATAC-seq footprinting by correcting for Tn5 sequence bias.
- Typically used in conjunction with motif enrichment analysis (e.g., JASPAR database) to assign TF identity to footprints.

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
