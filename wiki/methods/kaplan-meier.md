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
- Kaplan-Meier survival curves used to compare outcomes by genotype (PI3K-mTOR pathway and WNT/β-catenin alterations) in 127 HCC patients on sorafenib or immune checkpoint inhibitors [PMID:30373752](../papers/30373752.md)
- Kaplan-Meier survival analysis used to compare overall survival by SMAD4 mutation status in 81 GBCA patients; SMAD4-mutant patients had median OS 10.4 mo vs 24.8 mo [PMID:30427539](../papers/30427539.md)
- Kaplan-Meier OS analysis in 1,662 ICI-treated advanced cancer patients showed top-20%-by-histology TMB-high group HR 0.52 (95% CI 0.42–0.64); no OS benefit for high TMB in 5,371 non-ICI-treated patients (HR 1.12, p = 0.11) [PMID:30643254](../papers/30643254.md)
- Used for survival analysis in 429 mCRPC patients; log-rank tests compared OS curves; Nestin-positive vs. Nestin-negative groups and PLC transcriptomic cluster comparisons were evaluated [PMID:31061129](../papers/31061129.md)
- Applied in the pan-Asia cHCC-ICC study (133 cases); Nestin-positive (n=104) vs. Nestin-negative median OS was 18.7 mo vs. 46.6 mo (p<0.0001, log-rank); PLC transcriptomic clusters P1/P2 had significantly poorer prognosis than P3/P4 (p<0.0001) [PMID:31130341](../papers/31130341.md)

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
- [PMID:30373752](../papers/30373752.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30427539](../papers/30427539.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30643254](../papers/30643254.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31061129](../papers/31061129.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
