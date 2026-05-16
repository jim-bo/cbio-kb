---
name: Cox Proportional Hazards
slug: cox-proportional-hazards
kind: method
canonical_source: corpus
unverified: true
tags: [statistics, survival-analysis, regression]
processed_by: crosslinker
processed_at: 2026-05-16
---

# Cox Proportional Hazards

## Overview

Cox proportional hazards regression is a semi-parametric survival analysis model that relates the hazard of an event (e.g., death, disease progression) to one or more covariates without requiring specification of the baseline hazard function. The model assumes that the hazard ratio between any two subjects remains constant (proportional) over time — the proportional-hazards assumption. It is the standard method for multivariable survival analysis in oncology and clinical trials, producing hazard ratios (HR) and confidence intervals as the primary effect-size metrics.

## Used by

- Used with proportional-hazards-assumption testing (Grambsch & Therneau 1994) to assess clinical outcome endpoints ([OS](../cancer_types/OS.md), PFI, DFI, DSS) across 11,160 TCGA patients in 33 cancer types; high-stage (III/IV) vs low-stage (I/II) HRs were significantly >1 in most cancer types with sufficient event capture [PMID:29625055](../papers/29625055.md).

## Notes

- Implemented in R (survival package); analysis in TCGA-CDR performed in R 3.2.2.
- Proportional-hazards assumption should be tested (e.g., scaled Schoenfeld residuals); violations were noted for a minority of cancer type–endpoint combinations in the TCGA-CDR.
- Commonly paired with Kaplan-Meier curves for visualization and log-rank tests for unadjusted comparison.
- [LUSC](../cancer_types/LUSC.md) example from TCGA-CDR: never-disease-free vs disease-free patients, HR = 6.68 (95% CI 4.25–10.51, FDR q < 0.05).

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
