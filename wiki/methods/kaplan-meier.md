---
name: Kaplan-Meier
slug: kaplan-meier
kind: method
canonical_source: corpus
unverified: true
tags: [statistics, survival-analysis, visualization]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Kaplan-Meier

## Overview

The Kaplan-Meier (KM) estimator is a non-parametric method for estimating the survival function from time-to-event data, accounting for censored observations. It produces a step-function [estimate](../methods/estimate.md) of the probability of surviving past a given time point. KM curves are the standard visualization for survival data in oncology, and the log-rank test is used to assess differences between groups. The KM estimator is implemented in the `survival` package in R and is the foundational survival analysis tool used across virtually all clinical and genomic studies.

## Used by

- Used to generate survival curves for [OS](../cancer_types/OS.md), PFI, DFI, and DSS endpoints across 11,160 TCGA patients in 33 cancer types (TCGA Pan-Cancer Clinical Data Resource); paired with Cox proportional hazards regression for multivariable analysis; analysis performed in R 3.2.2 [PMID:29625055](../papers/29625055.md).
- Kaplan-Meier survival curves generated for OS and PFS analysis in 178 stage IV cholangiocarcinoma patients; progression-free survival on first-line chemo assessed in 158 patients [PMID:29848569](../papers/29848569.md)
- Kaplan-Meier survival curves used to compare PFS across FACETS copy-number clusters (A, B, C) and histologic/grade subgroups in 189 advanced endometrial cancer patients [PMID:30068706](../papers/30068706.md)

## Notes

- KM curves in TCGA-CDR breast cancer analysis were truncated at 10-year follow-up; ER+ patients showed significantly better PFI (p = 0.005), DFI (p = 0.001), and DSS (p = 0.009) than ER- patients.
- KM-derived median OS for TCGA [GBM](../cancer_types/GBM.md) = 12.6 months, median PFI = 6.1 months — values between the two arms of Stupp et al. 2005.
- Commonly paired with Cox proportional hazards regression; log-rank test used for unadjusted group comparisons.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
- [PMID:29848569](../papers/29848569.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30068706](../papers/30068706.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
