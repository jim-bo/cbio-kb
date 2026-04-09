---
name: Log-linear mixed-effects model
slug: log-linear-mixed-effects-model
kind: method
unverified: true
tags: [statistics, longitudinal, mixed-effects, growth-kinetics]
processed_by: entity-page-writer
processed_at: 2026-04-08
---

# Log-linear mixed-effects model

## Overview

Statistical longitudinal model fit to log-transformed tumor volume measurements over time to estimate continuous tumor volume growth rate (TVGR) and doubling time, accounting for within-patient correlation across repeated scans.

## Used by

- [PMID:37910594](../papers/37910594.md) — fit to serial volumetric MRI measurements from 128 IDH-mutant Grade 2 gliomas to estimate %TVGR per 6 months of 10.46% (95% CI 9.11–11.83) and doubling time of 3.5 years for the entire cohort; log-linear fit (adjusted r²=0.9864) marginally outperformed linear (r²=0.9556). Molecular grade-high (CDKN2A/B homozygous deletion) tumors had TVGR 19.17% per 6 months vs 9.54% for grade-low (P<0.0001) [PMID:37910594](../papers/37910594.md).

## Notes

- Assumes exponential growth; log-linearity verified empirically for IDH-mt LGG across the observation window [PMID:37910594](../papers/37910594.md).

## Sources

- [PMID:37910594](../papers/37910594.md)

*This page was processed by **entity-page-writer** on **2026-04-08**.*
