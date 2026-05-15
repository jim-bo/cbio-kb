---
name: FusionMap
slug: fusionmap
kind: method
canonical_source: corpus
unverified: true
tags: []
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# FusionMap

## Overview

FusionMap is a bioinformatics tool for gene fusion detection from RNA sequencing data. It identifies candidate fusion transcripts by aligning unmapped reads to junction sequences spanning two different genomic loci, enabling discovery of novel and known gene fusions in tumor transcriptomes.

## Used by

- Applied to unmapped reads from TopHat2/Bowtie2 RNA-seq alignment in the PIPseq pediatric precision oncology program at Columbia University Medical Center; fusion detection contributed ~40% of clinically impactful results including diagnostic fusions (e.g., PAX7-FOXO1, EML4-NTRK3, EWSR1-FLI1) and therapeutic targets [PMID:28007021](../papers/28007021.md).

## Notes

- Operates on unmapped reads remaining after primary transcript alignment (Tuxedo Suite).
- Used in a CLIA-certified clinical RNA-seq pipeline at Columbia University Medical Center.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
