---
name: IchorCNA
slug: ichorcna
kind: method
canonical_source: corpus
unverified: true
tags: [copy-number, liquid-biopsy, tumor-fraction, low-coverage-wgs]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# IchorCNA

## Overview

IchorCNA is a tool for estimating tumor fraction and large-scale copy-number alterations from ultra-low-coverage whole-genome sequencing data (as low as 0.1×). It uses a probabilistic model (hidden Markov model) that jointly estimates tumor purity and copy-number states, making it particularly useful for cell-free DNA (liquid biopsy) applications and for tracking tumor evolution in cell-line experiments.

## Used by

- Applied to low-coverage MiSeq WGS data from AALE chr_3p-deleted cell clones alongside HMMCopy to monitor subclonal copy-number evolution during in vitro passaging; detected emergence of chromosome-3 duplication subclones that rescued the chr_3p-deletion proliferation defect [PMID:29622463](../papers/29622463.md)
- Applied to shallow WGS (~10M reads/sample) of cfDNA from 118 metastatic solid tumor patients at MSKCC for genome-wide z-score based tumor-fraction estimation; sWGS z-scores achieved AUC=0.925 for predicting high (≥10% mVAF) tumor fraction and were used to triage cf-IMPACT-negative samples to MSK-ACCESS (low z-score) or cf-WES (high z-score) [PMID:34059130](../papers/34059130.md)

## Notes

- Originally developed for cell-free DNA liquid biopsy; also applicable to low-coverage cell-line WGS.
- Jointly estimates tumor/aberrant-cell fraction and copy-number states without a matched normal.
- Minimum input: ~0.1× coverage; higher coverage improves resolution of focal events.

## Sources

- [PMID:29622463](../papers/29622463.md)
- [PMID:34059130](../papers/34059130.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*

*This page was processed by **wiki-cli** on **2026-05-16**.*
