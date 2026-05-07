---
name: CellMiner
slug: cellminer
kind: pharmacogenomics-database
canonical_source: corpus
unverified: true
tags:
  - pharmacogenomics
  - drug-sensitivity
  - nci-60
  - pattern-comparison
  - web-tool
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# CellMiner

## Overview

CellMiner is a web-based suite of genomic and pharmacological tools for exploring transcript and drug activity patterns in the NCI-60 cancer cell line panel. It integrates multi-platform mRNA expression data (5 microarray platforms, 22,217 genes), microRNA data (360 miRNAs, Agilent V2), and drug activity data (GI50 values for 18,549 compounds from 47,540 tested via NCI Developmental Therapeutics Program sulforhodamine B assay). The core functionality is a Pattern Comparison tool that identifies genes or drugs with activity profiles correlated with a user-supplied input pattern, using Pearson's r with probe-level quality filtering (1.2 log2 range; r ≥ 0.30 or ≥ 0.60 for probe retention).

## Used by

- [cellline_nci60](../datasets/cellline_nci60.md) — primary dataset for all CellMiner analyses.
- [PMID:22802077](../papers/22802077.md) — original CellMiner publication describing the tool and demonstrating its use for [EGFR](../genes/EGFR.md) inhibitor class identification and colon-specific drug pattern matching.

## Notes

- Z-score integration across 5 transcript platforms provides composite expression estimates with built-in quality control.
- Pattern Comparison using [erlotinib](../drugs/erlotinib.md) (NSC 718781) as input correctly ranked [gefitinib](../drugs/gefitinib.md), [lapatinib](../drugs/lapatinib.md), and [afatinib](../drugs/afatinib.md) as top correlated drugs (3rd, 5th, 6th out of 18,549), validating the approach for identifying mechanistically related drugs [PMID:22802077](../papers/22802077.md).
- Correlations are Pearson's r; no multiple-comparisons correction is applied in the default output (p < 0.05 threshold); downstream functional validation is required.
- Drug queries require NCI NSC numbers, which may limit clinical researcher accessibility.
- Corpus-grown slug — not currently in the cBioPortal gene panels or molecular profiles ontologies.

## Sources

- [PMID:22802077](../papers/22802077.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
