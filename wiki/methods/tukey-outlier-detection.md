---
name: Tukey Outlier Detection
slug: tukey-outlier-detection
kind: method
canonical_source: corpus
unverified: true
tags: [statistics, outlier-detection, expression]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# Tukey Outlier Detection

## Overview

Tukey's method for outlier detection uses the interquartile range (IQR) to define extreme values: a value is classified as an outlier if it falls more than 1.5 × IQR below Q1 or above Q3 (mild outlier), or more than 3 × IQR beyond the quartiles (extreme outlier). In transcriptomics, the method is applied to identify samples with aberrantly high or low expression of a given gene or gene set relative to the distribution across a cohort.

## Used by

- Used in the TCGA pan-cancer fusion analysis to identify expression outliers among fusion-partner genes; over-expression outlier status (6–28% of kinase-partner fusions depending on cancer type) was used to support an oncogenic promoter-swap or gene-activation mechanism for kinase fusions [PMID:29617662](../papers/29617662.md)

## Notes

- Simple, assumption-free method that does not require normality.
- Applied per-cancer-type to avoid confounding by cross-cancer expression differences.
- Threshold choice (1.5× vs. 3× IQR) affects sensitivity/specificity; exact threshold used in PMID:29617662 was consistent with the 1.5× IQR convention.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
