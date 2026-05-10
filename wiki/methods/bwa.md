---
name: BWA (Burrows-Wheeler Aligner)
slug: bwa
kind: method
canonical_source: corpus
unverified: true
tags: [alignment, short-read, dna-seq, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-09
---

# BWA (Burrows-Wheeler Aligner)

## Overview

BWA (Burrows-Wheeler Aligner) is a short-read alignment tool for mapping sequencing reads to a reference genome using the Burrows-Wheeler transform. It includes three algorithms: BWA-backtrack (for reads ≤100 bp), BWA-SW (for longer reads with local alignment), and BWA-MEM (the current standard, suitable for 70 bp – 1 Mb reads). BWA-MEM is the most widely used for WGS and WES alignment in cancer genomics pipelines and is distributed with the Broad GATK best-practices workflow.

## Used by

- Used to align paired tumor/normal WGS reads to hg19 for 28 metastatic neuroendocrine neoplasms in the BC Cancer POG program; downstream SNV/indel calling performed by Strelka, SV calling by ABySS/Trans-ABySS [PMID:24326773](../papers/24326773.md).
- Used for read alignment in paired tumor/normal whole-exome sequencing of grade II glioma initial/recurrent pairs (n=23) [PMID:24336570](../papers/24336570.md)

## Notes

- BWA-MEM is the recommended algorithm for reads ≥70 bp; BWA-backtrack was standard for early Illumina CASAVA-era data.
- PCR duplicate marking (e.g., Picard MarkDuplicates, samblaster) is typically applied after BWA alignment.
- Output is SAM/BAM format; coordinate-sorted and indexed BAMs are required for most downstream tools.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-09**.*
- [PMID:24336570](../papers/24336570.md)

*This page was processed by **wiki-cli** on **2026-05-09**.*
