---
name: G&T-Seq (Genome and Transcriptome Sequencing)
slug: g-and-t-seq
kind: method
canonical_source: corpus
unverified: true
tags:
  - single-cell
  - multi-omics
  - DNA-RNA
  - genome
  - transcriptome
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# G&T-Seq (Genome and Transcriptome Sequencing)

## Overview

G&T-Seq is a single-cell multi-omics protocol that simultaneously isolates and sequences both the genome (DNA) and the transcriptome (RNA) from the same individual cell. Each cell is physically separated into a DNA fraction and an RNA fraction prior to amplification, enabling matched somatic mutation profiling and gene-expression measurement from the same nucleus. In published applications, clonally expanded single cells are profiled by targeted or whole-exome sequencing on the DNA side and full-length [Smart-Seq2](../methods/smart-seq2.md)-based RNA-seq on the RNA side, producing paired genotype–phenotype data at single-cell resolution.

## Used by

- Tang et al. applied G&T-Seq to 133 clonally expanded individual melanocytes from 6 elderly donors across 19 anatomic sites, pairing UCSF500 targeted panel (509 genes) DNA sequencing with Smart-Seq2 RNA-seq; the matched design allowed cross-validation of somatic calls and identification of MDM2-expression correlation with mutation burden [PMID:33029006](../papers/33029006.md)

## Notes

- Requires single-cell clonal expansion or physical cell isolation before separation into DNA and RNA fractions.
- The DNA and RNA fractions from the same cell are processed independently, enabling each to be sequenced by the most appropriate platform or panel.
- Coverage and read depth depend on the downstream assay choice (targeted panel, WES, or full-length RNA-seq).
- In [PMID:33029006](../papers/33029006.md), sequencing was performed on Illumina HiSeq 2500 / NovaSeq; mean DNA coverage 489× (targeted), 86× (exome); mean RNA yield 7.75M reads per clone.

## Sources

- [PMID:33029006](../papers/33029006.md) — Tang et al., single-cell somatic mutation landscape of normal human melanocytes.

*This page was processed by **entity-page-writer** on **2026-05-16**.*
