---
name: Germline Burden Test
slug: germline-burden-test
kind: method
canonical_source: corpus
unverified: true
tags: [germline, statistics, burden-testing]
processed_by: crosslinker
processed_at: 2026-05-15
---

# Germline Burden Test

## Overview

A gene-level statistical approach comparing the frequency of qualifying germline variants (typically (likely) pathogenic / pathogenic variants) in a case cohort against a reference population of controls. Common implementations use logistic regression or Fisher's exact test to test whether a gene is significantly enriched for rare deleterious variants in the cases. The method is used to identify cancer-predisposition genes when case numbers are insufficient for linkage studies.

## Used by

- Used in Daugs et al. to compare LP/PV frequencies in 25 HBOC-related genes across 372 pediatric cancer patients (cases) vs. gnomAD v3.1.1 non-cancer controls (n=74,023), using logistic regression and two-sided Fisher's exact tests (p < 0.05 threshold); identified [TP53](../genes/TP53.md), [CHEK2](../genes/CHEK2.md), [ATM](../genes/ATM.md), [NF1](../genes/NF1.md), and [NBN](../genes/NBN.md) as significantly enriched [PMID:29489754](../papers/29489754.md)

## Notes

- Results are sensitive to choice of control population; gnomAD non-cancer subsets are a common reference but may not fully exclude pre-symptomatic carriers.
- Multiple-testing burden scales with candidate gene set size; explicit correction is important.
- Statistical power is limited by small case cohorts; joint analysis across cohorts can augment power.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
