---
name: TopHat-Fusion
slug: tophat-fusion
kind: method
canonical_source: corpus
unverified: true
tags: [fusion-calling, rna-seq, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-11
---

# TopHat-Fusion

## Overview

TopHat-Fusion is an extension of the TopHat RNA-seq aligner that detects gene fusions by identifying reads that span fusion junctions. It aligns reads to the genome, then searches for split-read evidence where portions of a read map to different genomic loci, indicative of a chimeric transcript.

## Used by

- Applied in ICGC PedBrain pilocytic astrocytoma study (n=73 cases with matched RNA-seq) alongside [defuse](../methods/defuse.md) for fusion gene discovery; identified novel [NTRK2](../genes/NTRK2.md) fusions ([QKI](../genes/QKI.md):[NTRK2](../genes/NTRK2.md), [NACC2](../genes/NACC2.md):NTRK2) and novel [BRAF](../genes/BRAF.md) fusion partners ([RNF130](../genes/RNF130.md), [CLCN6](../genes/CLCN6.md), [MKRN1](../genes/MKRN1.md), [GNAI1](../genes/GNAI1.md)) [PMID:23817572](../papers/23817572.md)
- Applied to 80 rhabdomyosarcoma RNA-seq samples (Illumina HiSeq2000 100 bp PE) for fusion transcript detection; identified PAX3-NCOA1, PAX3-INO80D, and other cryptic rearrangements in histologically fusion-negative [ARMS](../cancer_types/ARMS.md) tumors [PMID:24436047](../papers/24436047.md)
- TopHat (with Cufflinks) used for RNA-seq alignment and expression quantification in 25 TETs; fusion detection performed using FusionMap and DeFuse; 7 of 25 tumors had fusion transcripts identified [PMID:24974848](../papers/24974848.md)

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Predecessor approach to STAR-Fusion and Arriba; used in TCGA-era fusion detection pipelines.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24436047](../papers/24436047.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24974848](../papers/24974848.md)

*This page was processed by **wiki-cli** on **2026-05-11**.*
