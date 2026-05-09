---
name: STAR (Spliced Transcripts Alignment to a Reference)
slug: star
kind: method
canonical_source: corpus
unverified: true
tags: [alignment, rna-seq, splice-aware, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-09
---

# STAR (Spliced Transcripts Alignment to a Reference)

## Overview

STAR is a splice-aware RNA-seq alignment tool that maps short reads to a reference genome while accurately resolving splice junctions. It uses a suffix array–based approach with two-pass alignment to detect novel splice junctions in the first pass and include them in the genome index for the second pass. STAR is the standard aligner for bulk RNA-seq quantification pipelines (typically paired with RSEM or featureCounts for expression estimation) and supports fusion-gene detection via STARFusion.

## Used by

- Used to align RNA-seq reads to hg38 for 28 metastatic neuroendocrine neoplasms ([pog570_bcgsc_2020](../datasets/pog570_bcgsc_2020.md)) in the BC Cancer POG WGTA pipeline; paired with RSEM for transcript-level quantification; expression data drove 6 of 10 clinical benefit outcomes in this cohort [PMID:24326773](../papers/24326773.md).

## Notes

- STAR requires large memory (typically 30–40 [GB](../cancer_types/GB.md) RAM for human genome); genome index must be pre-built and is version/annotation-specific.
- Two-pass mode is recommended to improve sensitivity for novel splice junction detection.
- Commonly paired with RSEM (transcript-level) or featureCounts/HTSeq (gene-level) for expression quantification.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
