---
name: Whole-Genome Bisulfite Sequencing
slug: whole-genome-bisulfite-seq
kind: method
canonical_source: corpus
unverified: true
tags: [epigenomics, dna-methylation, sequencing, bisulfite]
processed_by: crosslinker
processed_at: 2026-05-14
---

# Whole-Genome Bisulfite Sequencing

## Overview

Whole-genome bisulfite sequencing (WGBS) is the gold-standard method for measuring DNA methylation at single-base resolution across the entire genome. Sodium bisulfite treatment converts unmethylated cytosines to uracil (read as thymine after PCR) while leaving 5-methylcytosine unchanged, enabling direct detection of methylated versus unmethylated CpG (and non-CpG) sites by sequencing. WGBS provides unbiased, genome-wide coverage but requires high sequencing depth (typically 20–30× per strand) and significant DNA input, making it expensive relative to array-based methylation profiling.

## Used by

- Run on 5 TCGA breast tumor samples as a validation experiment in the TCGA ILC/IDC multi-platform study (n=817) to confirm Illumina HumanMethylation450 BeadChip calls; validated the key finding that [CDH1](../genes/CDH1.md) promoter DNA hypermethylation is absent in [ILC](../cancer_types/ILC.md), contradicting older MSP-based reports. [PMID:26451490](../papers/26451490.md)

## Notes

- WGBS requires bisulfite conversion followed by library preparation; strand-specific protocols (e.g., PBAT) minimize input DNA requirements.
- Typical applications: CpG island methylation, differentially methylated regions (DMRs), allele-specific methylation, imprinting.
- Distinguishes 5-methylcytosine (5mC) from 5-hydroxymethylcytosine (5hmC) requires oxidative bisulfite sequencing (oxBS) or TET-assisted bisulfite sequencing (TAB-seq).
- Array-based methods (HM450, EPIC) cover ~450K–850K CpGs; WGBS covers ~28 million CpGs genome-wide.

## Sources

- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
