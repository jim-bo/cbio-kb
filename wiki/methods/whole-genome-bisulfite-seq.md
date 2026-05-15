---
name: Whole-Genome Bisulfite Sequencing
slug: whole-genome-bisulfite-seq
kind: method
canonical_source: corpus
unverified: true
tags: [epigenomics, dna-methylation, sequencing, bisulfite]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# Whole-Genome Bisulfite Sequencing

## Overview

Whole-genome bisulfite sequencing (WGBS) is the gold-standard method for measuring DNA methylation at single-base resolution across the entire genome. Sodium bisulfite treatment converts unmethylated cytosines to uracil (read as thymine after PCR) while leaving 5-methylcytosine unchanged, enabling direct detection of methylated versus unmethylated CpG (and non-CpG) sites by sequencing. WGBS provides unbiased, genome-wide coverage but requires high sequencing depth (typically 20–30× per strand) and significant DNA input, making it expensive relative to array-based methylation profiling.

## Used by

- Run on 5 TCGA breast tumor samples as a validation experiment in the TCGA ILC/IDC multi-platform study (n=817) to confirm Illumina HumanMethylation450 BeadChip calls; validated the key finding that [CDH1](../genes/CDH1.md) promoter DNA hypermethylation is absent in [ILC](../cancer_types/ILC.md), contradicting older MSP-based reports. [PMID:26451490](../papers/26451490.md)
- Bisulfite sequencing of the CDH1 promoter CpG island (with Sanger readout) detected hypermethylation in 4/5 CDH1 wild-type plasmacytoid bladder tumors and 0 CDH1-mutant or urothelial NOS tumors, explaining E-cadherin loss in mutation-negative cases. [PMID:26901067](../papers/26901067.md)
- Applied to 40 MRT tumor/normal pairs plus 3 MRT cell lines, 3 hESC lines, and 4 NPCs; promoter CGI clustering identified two methylation sub-groups correlated with patient age (sub-group A enriched for patients >1 year; p=0.0013). Tumor-suppressor promoters (RASSF1, IRX1, TWIST2, DLEC1, TBX5) gained methylation vs hESC (Fisher p=0.02). [PMID:26977886](../papers/26977886.md)

## Notes

- WGBS requires bisulfite conversion followed by library preparation; strand-specific protocols (e.g., PBAT) minimize input DNA requirements.
- Typical applications: CpG island methylation, differentially methylated regions (DMRs), allele-specific methylation, imprinting.
- Distinguishes 5-methylcytosine (5mC) from 5-hydroxymethylcytosine (5hmC) requires oxidative bisulfite sequencing (oxBS) or TET-assisted bisulfite sequencing (TAB-seq).
- Array-based methods (HM450, EPIC) cover ~450K–850K CpGs; WGBS covers ~28 million CpGs genome-wide.

## Sources

- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26901067](../papers/26901067.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26977886](../papers/26977886.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
