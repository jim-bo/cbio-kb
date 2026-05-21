---
name: STAR Aligner
slug: star-aligner
kind: method
canonical_source: corpus
unverified: true
tags: [rna-seq, alignment, spliced-reads]
processed_by: crosslinker
processed_at: 2026-05-21
---

# STAR Aligner

## Overview

[STAR](../genes/STAR.md) (Spliced Transcripts Alignment to a Reference) is a high-speed RNA-seq read aligner that handles spliced alignments across intron-exon boundaries and chimeric reads spanning gene fusions. It uses a seed-search-extension strategy to align reads efficiently to large genomes. [STAR](../genes/STAR.md) is widely used as the primary alignment step for RNA-seq pipelines that include fusion detection (STAR-Fusion) or quantification (RSEM).

## Used by

- Used for RNA-seq alignment in AALE chr_3p-deleted cell experiments (HiSeq 2500 PE100) as part of the [STAR](../genes/STAR.md) + RSEM + edgeR pipeline for differential expression analysis [PMID:29622463](../papers/29622463.md)
- Used to align RNA-seq reads in the [GBM](../cancer_types/GBM.md) anti-PD-1 immunotherapy study (38 longitudinal transcriptomes); downstream pathway scoring performed by ssGSEA/GSEA [PMID:30742119](../papers/30742119.md)
- Used for RNA-seq alignment in the pan-Asia cHCC-ICC study (97 tumors / 77 cases); transcripts subsequently quantified for differential expression analysis and transcriptomic cluster assignment [PMID:31130341](../papers/31130341.md)
- Used for RNA-seq alignment in the high-grade [UTUC](../cancer_types/UTUC.md) study (32 tumors: WCM n=17, BCM-MDA n=15); aligned reads used for luminal subtype calling, immune cluster classification, and [FGFR3](../genes/FGFR3.md) outlier expression analysis [PMID:31278255](../papers/31278255.md)
- [STAR](../genes/STAR.md) aligner used for RNA-seq alignment in bulk transcriptomic profiling of 43 [SCLC](../cancer_types/SCLC.md) PDX models in the MSK PDX resource [PMID:35440124](../papers/35440124.md).
- Used for RNA-seq alignment in the [mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md) cWGTS pipeline (STAR two-pass alignment) for whole-transcriptome sequencing in 101/114 pediatric/AYA solid tumor patients [PMID:35585047](../papers/35585047.md)
- STAR aligner used for bulk RNA-seq processing in 392 longitudinal glioma samples from the GLASS expansion cohort (alongside kallisto for expression quantification) [PMID:35649412](../papers/35649412.md)

## Notes

- STAR generates chimeric alignment output that STAR-Fusion uses for fusion detection.
- Requires 2-pass mapping mode for optimal splice-junction detection in RNA-seq.
- High memory requirements (~30 [GB](../cancer_types/GB.md) for human genome index).

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30742119](../papers/30742119.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31278255](../papers/31278255.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35440124](../papers/35440124.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35649412](../papers/35649412.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
