---
name: HMMCopy
slug: hmmcopy
kind: method
canonical_source: corpus
unverified: true
tags: [copy-number, low-coverage-wgs, hidden-markov-model]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# HMMCopy

## Overview

HMMCopy is a tool for estimating copy-number profiles from low-coverage (shallow) whole-genome sequencing data. It uses a hidden Markov model to segment normalized read-count data into discrete copy-number states, accounting for GC content and mappability biases. HMMCopy is suited for cost-effective copy-number profiling of cell lines, liquid biopsies, and other samples where deep WGS is impractical.

## Used by

- Applied to low-coverage WGS (MiSeq) data from AALE chr_3p-deleted cell clones alongside IchorCNA to detect subclonal copy-number changes during in vitro evolution, including the emergence of subclones with chromosome-3 duplication that rescued the 3p-deletion proliferation defect [PMID:29622463](../papers/29622463.md)

## Notes

- Designed for shallow WGS (~0.1–1×); does not require matched normal.
- Requires GC correction and mappability adjustment for accurate segmentation.
- Commonly paired with IchorCNA for tumor-fraction estimation in liquid biopsy applications.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
