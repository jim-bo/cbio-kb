---
name: 3' RNA sequencing (3' RNA-seq)
slug: 3prime-rna-seq
kind: method
canonical_source: corpus
unverified: true
tags: [rna-seq, transcriptomics, 3-prime]
processed_by: crosslinker
processed_at: 2026-05-14
---

# 3' RNA sequencing (3' RNA-seq)

## Overview

3' RNA-seq (also called 3'-end sequencing or QuantSeq) is a strand-specific RNA sequencing approach that sequences only the 3' end of polyadenylated transcripts. It provides gene-level expression quantification at lower cost than full-length RNA-seq and is particularly useful for FFPE and low-quality RNA samples. The Lexogen QuantSeq 3' mRNA-Seq Library Prep FWD kit is a common implementation. Reads are biased toward the 3' end, making it less suitable for isoform analysis or fusion detection.

## Used by

- Used in endometrial polyp genomic characterization to quantify gene expression from 25 polyps and 6 normal endometrium samples, enabling identification of HMGA1/HMGA2 rearrangement-driven expression changes including [PLAG1](../genes/PLAG1.md) and [ZMAT3](../genes/ZMAT3.md) upregulation [PMID:28445112](../papers/28445112.md)

## Notes

- Reads are enriched toward the 3' end of transcripts, limiting isoform-level resolution.
- Suitable for samples with degraded RNA or FFPE material.
- Lower per-sample cost than full-length RNA-seq makes it attractive for large cohorts.
- Not suitable for gene fusion detection; paired full-length RNA-seq or targeted panels are required for fusions.

## Sources

- [PMID:28445112](../papers/28445112.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
