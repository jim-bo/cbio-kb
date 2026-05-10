---
name: TruSight Oncology 500 (TSO500)
slug: trusight-oncology-500
kind: method
canonical_source: corpus
unverified: true
tags:
  - targeted-panel
  - dna-seq
  - rna-seq
  - fusion-detection
  - illumina
processed_by: crosslinker
processed_at: 2026-05-09
---

# TruSight Oncology 500 (TSO500)

## Overview

TruSight Oncology 500 (TSO500) is an Illumina hybrid-capture targeted sequencing panel covering 523 genes for DNA variant detection (SNVs, indels, CNVs, TMB, MSI) and 55 genes for RNA fusion and splice-variant detection. It is designed for tumor-only sequencing workflows on Illumina NovaSeq or NextSeq instruments. Variant filtering in clinical/research applications typically uses ClinVar-benign exclusion and population allele frequency thresholds to distinguish somatic from germline events in the absence of matched normal.

## Used by

- Illumina TruSight Oncology 500 (DNA + RNA) panel applied to 31/88 sinonasal adenoid cystic carcinoma cases on NovaSeq 6000; identified pathogenic mutations in 21/31 (68%) tumors including [BCOR](../genes/BCOR.md) (19%), [NOTCH1](../genes/NOTCH1.md) (14%), [EP300](../genes/EP300.md) (14%); panel detected four noncanonical RNA fusions but missed ~10% of AdCCs detectable only by FISH [PMID:24418857](../papers/24418857.md)

## Notes

- Tumor-only workflow; no matched normal required. Germline contamination and rare variants of unknown significance remain a concern without paired normal sequencing.
- RNA fusion detection via the TSO500 panel can miss rearrangements lacking a known fusion partner at the RNA level; complementary FISH is recommended for MYB/MYBL1/NFIB/EWSR1 rearrangements in adenoid cystic carcinoma.
- Unverified corpus-grown slug; TSO500 is not a cBioPortal gene panel identifier.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
