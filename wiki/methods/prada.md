---
name: PRADA (Pipeline for RNA-seq Data Analysis)
slug: prada
kind: EXPRESSION
canonical_source: corpus
unverified: true
tags: [rna-seq, fusion-detection, bioinformatics, pipeline]
processed_by: crosslinker
processed_at: 2026-05-09
---

# PRADA (Pipeline for RNA-seq Data Analysis)

## Overview

PRADA (Pipeline for RNA-seq Data Analysis) is a computational framework developed at MD Anderson Cancer Center for processing and analyzing RNA sequencing data in cancer genomics. It supports alignment, expression quantification, fusion transcript detection, alternative splicing analysis, and variant calling from RNA-seq data. PRADA was specifically used in TCGA studies to identify gene fusions, intragenic structural variants, and splice variants from transcriptome data.

## Used by

- Used to analyze 164 [GBM](../cancer_types/GBM.md) transcriptomes in the TCGA GBM 2013 study; detected 228 fusion transcripts in 106/164 samples including recurrent EGFR-SEPT14 (n=6), SEC61G-EGFR (n=4), FGFR3-TACC3 (n=2) fusions, as well as novel [EGFR](../genes/EGFR.md) Δ12–13 and Δ14–15 splice variants and [PDGFRA](../genes/PDGFRA.md) intragenic variants [PMID:24120142](../papers/24120142.md)

## Notes

- PRADA uses two-pass BLAT alignment against genome and transcriptome references to detect chimeric fusion transcripts.
- Outputs include gene-level expression estimates (RPKM), fusion calls with junction-spanning read support, and isoform-level analyses.
- Particularly effective for detecting intragenic structural variants in driver oncogenes like EGFR and PDGFRA.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
