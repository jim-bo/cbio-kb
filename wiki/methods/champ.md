---
name: ChAMP (Chip Analysis Methylation Pipeline)
slug: champ
kind: method
canonical_source: corpus
unverified: true
tags: [methylation, dna-methylation, illumina-epic, bioinformatics, epigenomics]
processed_by: crosslinker
processed_at: 2026-05-16
---

# ChAMP (Chip Analysis Methylation Pipeline)

## Overview

ChAMP is an R/Bioconductor pipeline for analyzing Illumina Infinium methylation array data (450K and EPIC arrays). It handles quality control, normalization, batch correction, and differential methylation analysis at the probe (DMP) and region (DMR) level. ChAMP is commonly paired with DMRcate for regional DMR detection.

## Used by

- Used to identify differentially methylated probes (DMPs) and regions (DMRs) from Infinium MethylationEPIC array data in 40 upper-tract urothelial carcinoma ([UTUC](../cancer_types/UTUC.md)) tumors ([utuc_igbmc_2021](../datasets/utuc_igbmc_2021.md)); the analysis defined two epigenetic clusters (EpiC-high hypermethylated vs EpiC-low hypomethylated) with DMR-enriched pathways including PRC2/MLL targets and ZEB1/SMARCA2 target genes [PMID:33397444](../papers/33397444.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- ChAMP integrates QC filtering (removing sex chromosomes and low-quality probes), BMIQ normalization, ComBat batch correction, singular-value decomposition (SVD) cell-type estimation, and differential analysis via limma.
- Outputs include beta-value matrices, M-value matrices, DMP tables, and DMR tables.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
