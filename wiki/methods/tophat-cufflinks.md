---
name: TopHat/Cufflinks (Tuxedo Suite)
slug: tophat-cufflinks
kind: method
canonical_source: corpus
unverified: true
tags: []
processed_by: wiki-cli
processed_at: 2026-05-14
---

# TopHat/Cufflinks (Tuxedo Suite)

## Overview

The Tuxedo Suite is a bioinformatics pipeline for RNA-seq analysis consisting of TopHat2 (splice-aware short-read aligner using Bowtie2) and Cufflinks (transcript assembly and quantification). It maps reads to a reference genome while accounting for splicing, quantifies transcript abundance, and compares expression across conditions.

## Used by

- TopHat2/Bowtie2/Cufflinks (Tuxedo Suite) used for transcript mapping and quantification in the PIPseq pediatric precision oncology program at Columbia University Medical Center; relative gene expression was compared against a 124-transcriptome reference panel (13 blood, 20 liver, 24 kidney, 17 lung, 50 brain tissues) [PMID:28007021](../papers/28007021.md).
- Used TopHat/Cufflinks pipeline for RNA-seq alignment and transcript quantification [PMID:28373299](../papers/28373299.md)

## Notes

- TopHat2 aligns reads splice-aware using Bowtie2 as the underlying aligner.
- Cufflinks performs de novo transcript assembly and FPKM quantification.
- Used alongside FusionMap (applied to unmapped reads) in the PIPseq clinical RNA-seq pipeline.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28373299](../papers/28373299.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
