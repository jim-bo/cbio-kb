---
name: Disambiguate
slug: disambiguate
kind: method
canonical_source: corpus
unverified: true
tags: [pdx, xenograft, read-classification, bioinformatics]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Disambiguate

## Overview

Disambiguate is a computational tool that separates sequencing reads originating from human tumor tissue from contaminating host-mouse reads in patient-derived xenograft (PDX) samples, by comparing alignments against human and mouse reference genomes.

## Used by

- Used to remove mouse reads (aligning to GRCh38 vs GRCm38) from RNA-seq, WES and WGS data in a 68-PDX pediatric solid-tumor cohort; PDXs with more than 50% mouse contamination were excluded from downstream analysis [PMID:37990009](../papers/37990009.md)

## Notes

- Mouse-contamination filtering is a standard preprocessing step for PDX genomic/transcriptomic pipelines, applied before variant calling or expression quantification.

## Sources

- [PMID:37990009](../papers/37990009.md) — pediatric solid-tumor PDX genomic landscape study; Disambiguate used to remove mouse reads and exclude highly contaminated PDX samples.

*This page was processed by **entity-page-writer** on **2026-09-10**.*
