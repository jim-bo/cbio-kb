---
name: TIDE
slug: tide
kind: method
canonical_source: corpus
unverified: true
tags: [immunotherapy, immune-evasion, tumor-microenvironment, biomarker, computational]
processed_by: crosslinker
processed_at: 2026-05-16
---

# TIDE

## Overview

TIDE (Tumor Immune Dysfunction and Exclusion) is a computational method that uses tumor bulk gene-expression data to predict the likelihood of response to immune checkpoint blockade (ICB). It models two primary immune-evasion mechanisms: T-cell dysfunction (exhaustion in inflamed tumors) and T-cell exclusion (immunologically cold tumors with high stromal/MDSC content). TIDE scores are derived from regression models trained on ICI clinical trial data and can be applied to any tumor with bulk RNA-seq. Higher TIDE scores indicate a lower predicted probability of ICB response.

## Used by

- Applied in the Sherlock-Lung NS-LUAD study (n=684 never-smoker lung adenocarcinomas) to predict ICB response across the three NMF-defined transcriptomic subtypes; steady tumors had the lowest TIDE scores (p=6.21×10⁻¹⁴) and were enriched in the bottom-20% TIDE quintile (p=1.09×10⁻⁹), while chaotic tumors were depleted; adding transcriptomic subtype to [CD274](../genes/CD274.md) (PD-L1) and [PDCD1](../genes/PDCD1.md) (PD-1) expression improved the R² of TIDE-score prediction from 0.093 to 0.25 (p=1.17×10⁻²²) [PMID:32015526](../papers/32015526.md).

## Notes

- TIDE is a computational prediction tool, not a direct assay; it does not replace functional immunological measurement.
- In the Sherlock-Lung study, TIDE inference was not validated in a cohort with paired transcriptomic and ICB outcome data — the authors explicitly note this limitation.
- TIDE scores can be computed via the TIDE web server (tide.dfci.harvard.edu) or the tidepy Python package from a gene expression matrix.
- Steady NS-LUAD tumors had lower abundances of MDSCs (p=4.77×10⁻¹⁹) and cancer-associated fibroblasts (p=1.44×10⁻¹⁰), consistent with their low TIDE scores.

## Sources

- [PMID:32015526](../papers/32015526.md) — Sherlock-Lung NS-LUAD ICB response prediction

*This page was processed by **crosslinker** on **2026-05-16**.*
