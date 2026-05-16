---
name: STAR Aligner
slug: star-aligner
kind: method
canonical_source: corpus
unverified: true
tags: [rna-seq, alignment, spliced-reads]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# STAR Aligner

## Overview

[STAR](../genes/STAR.md) (Spliced Transcripts Alignment to a Reference) is a high-speed RNA-seq read aligner that handles spliced alignments across intron-exon boundaries and chimeric reads spanning gene fusions. It uses a seed-search-extension strategy to align reads efficiently to large genomes. STAR is widely used as the primary alignment step for RNA-seq pipelines that include fusion detection (STAR-Fusion) or quantification (RSEM).

## Used by

- Used for RNA-seq alignment in AALE chr_3p-deleted cell experiments (HiSeq 2500 PE100) as part of the STAR + RSEM + edgeR pipeline for differential expression analysis [PMID:29622463](../papers/29622463.md)
- Used to align RNA-seq reads in the GBM anti-PD-1 immunotherapy study (38 longitudinal transcriptomes); downstream pathway scoring performed by ssGSEA/GSEA [PMID:30742119](../papers/30742119.md)
- Used for RNA-seq alignment in the pan-Asia cHCC-ICC study (97 tumors / 77 cases); transcripts subsequently quantified for differential expression analysis and transcriptomic cluster assignment [PMID:31130341](../papers/31130341.md)
- Used for RNA-seq alignment in the high-grade UTUC study (32 tumors: WCM n=17, BCM-MDA n=15); aligned reads used for luminal subtype calling, immune cluster classification, and FGFR3 outlier expression analysis [PMID:31278255](../papers/31278255.md)

## Notes

- STAR generates chimeric alignment output that STAR-Fusion uses for fusion detection.
- Requires 2-pass mapping mode for optimal splice-junction detection in RNA-seq.
- High memory requirements (~30 [GB](../cancer_types/GB.md) for human genome index).

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
- [PMID:30742119](../papers/30742119.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31278255](../papers/31278255.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
