---
name: STAR Aligner
slug: star-aligner
kind: method
canonical_source: corpus
unverified: true
tags: [rna-seq, alignment, spliced-reads]
processed_by: crosslinker
processed_at: 2026-05-15
---

# STAR Aligner

## Overview

[STAR](../genes/STAR.md) (Spliced Transcripts Alignment to a Reference) is a high-speed RNA-seq read aligner that handles spliced alignments across intron-exon boundaries and chimeric reads spanning gene fusions. It uses a seed-search-extension strategy to align reads efficiently to large genomes. STAR is widely used as the primary alignment step for RNA-seq pipelines that include fusion detection (STAR-Fusion) or quantification (RSEM).

## Used by

- Used for RNA-seq alignment in AALE chr_3p-deleted cell experiments (HiSeq 2500 PE100) as part of the STAR + RSEM + edgeR pipeline for differential expression analysis [PMID:29622463](../papers/29622463.md)

## Notes

- STAR generates chimeric alignment output that STAR-Fusion uses for fusion detection.
- Requires 2-pass mapping mode for optimal splice-junction detection in RNA-seq.
- High memory requirements (~30 [GB](../cancer_types/GB.md) for human genome index).

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
