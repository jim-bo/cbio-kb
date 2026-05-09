---
name: MuTect
slug: mutect
kind: method
canonical_source: corpus
unverified: false
tags:
  - somatic-mutation
  - snv-calling
  - whole-exome-seq
  - whole-genome-seq
processed_by: entity-page-writer
processed_at: 2026-05-09
---

# MuTect

## Overview

MuTect is a Bayesian statistical framework for the sensitive and specific detection of somatic single-nucleotide variants (SNVs) in paired tumor/normal sequencing data. Developed at the Broad Institute, it uses a two-sample likelihood model to distinguish somatic mutations from germline variants and sequencing artifacts, with particular attention to low-allele-fraction variants in impure tumor samples. MuTect is widely applied in cancer exome and genome sequencing pipelines, typically paired with Indelocator for indel detection.

## Used by

- Applied alongside Indelocator, dRanger, BreakPointer, CLONET, ChainFinder, ABSOLUTE, and GISTIC v2 in WGS analysis of 57 prostate tumors; detected 356,136 somatic base-pair mutations across the cohort (mean 33 non-silent exonic per primary tumor) [PMID:23622249](../papers/23622249.md)
- Used for somatic SNV calling in 149 esophageal adenocarcinoma WES pairs (and 16 WGS pairs) alongside Indelocator; median 104 non-silent coding mutations per tumor at median genome-wide frequency 9.9/Mb [PMID:23525077](../papers/23525077.md)

## Notes

- Requires matched tumor/normal BAM files; not designed for tumor-only mode in its original implementation.
- Sensitivity is maintained down to ~5% variant allele fraction under typical WES coverage (80–100×).
- All candidate variants are typically followed by validation with orthogonal methods (e.g., Sequenom, deep digital sequencing).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-09**.*
