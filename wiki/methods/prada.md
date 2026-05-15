---
name: PRADA (Pipeline for RNA-seq Data Analysis)
slug: prada
kind: EXPRESSION
canonical_source: corpus
unverified: true
tags: [rna-seq, fusion-detection, bioinformatics, pipeline]
processed_by: wiki-cli
processed_at: 2026-05-14
---

# PRADA (Pipeline for RNA-seq Data Analysis)

## Overview

PRADA (Pipeline for RNA-seq Data Analysis) is a computational framework developed at MD Anderson Cancer Center for processing and analyzing RNA sequencing data in cancer genomics. It supports alignment, expression quantification, fusion transcript detection, alternative splicing analysis, and variant calling from RNA-seq data. PRADA was specifically used in TCGA studies to identify gene fusions, intragenic structural variants, and splice variants from transcriptome data.

## Used by

- Used to analyze 164 [GBM](../cancer_types/GBM.md) transcriptomes in the TCGA GBM 2013 study; detected 228 fusion transcripts in 106/164 samples including recurrent EGFR-SEPT14 (n=6), SEC61G-EGFR (n=4), FGFR3-TACC3 (n=2) fusions, as well as novel [EGFR](../genes/EGFR.md) Δ12–13 and Δ14–15 splice variants and [PDGFRA](../genes/PDGFRA.md) intragenic variants [PMID:24120142](../papers/24120142.md)
- PRADA used alongside deFuse for fusion-gene discovery in TCGA diffuse glioma RNA-seq data (n=649 fusion profiles); fusions integrated with mutations and CNAs for pathway-level alteration analysis [PMID:26824661](../papers/26824661.md)
- PRADA fusion-calling pipeline applied to RNA-seq data from 495 ADC and 476 SqCC samples; identified novel MET-CAPZA2, KIF5B-MET, TRIM24-NTRK2, and NTRK2-TP63 fusions [PMID:27158780](../papers/27158780.md)

## Notes

- PRADA uses two-pass BLAT alignment against genome and transcriptome references to detect chimeric fusion transcripts.
- Outputs include gene-level expression estimates (RPKM), fusion calls with junction-spanning read support, and isoform-level analyses.
- Particularly effective for detecting intragenic structural variants in driver oncogenes like EGFR and PDGFRA.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
