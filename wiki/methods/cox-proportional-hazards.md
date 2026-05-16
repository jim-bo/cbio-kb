---
name: Cox Proportional Hazards
slug: cox-proportional-hazards
kind: method
canonical_source: corpus
unverified: true
tags: [statistics, survival-analysis, regression]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Cox Proportional Hazards

## Overview

Cox proportional hazards regression is a semi-parametric survival analysis model that relates the hazard of an event (e.g., death, disease progression) to one or more covariates without requiring specification of the baseline hazard function. The model assumes that the hazard ratio between any two subjects remains constant (proportional) over time — the proportional-hazards assumption. It is the standard method for multivariable survival analysis in oncology and clinical trials, producing hazard ratios (HR) and confidence intervals as the primary effect-size metrics.

## Used by

- Used with proportional-hazards-assumption testing (Grambsch & Therneau 1994) to assess clinical outcome endpoints ([OS](../cancer_types/OS.md), PFI, DFI, DSS) across 11,160 TCGA patients in 33 cancer types; high-stage (III/IV) vs low-stage (I/II) HRs were significantly >1 in most cancer types with sufficient event capture [PMID:29625055](../papers/29625055.md).
- Applied in multivariate survival analysis of 178 stage IV cholangiocarcinoma patients; CDKN2A/B and ERBB2 alterations remained significantly associated with shorter OS and PFS on first-line chemotherapy [PMID:29848569](../papers/29848569.md)
- Used for survival analysis of PFS in 189 advanced endometrial cancer patients profiled by MSK-IMPACT; Kaplan-Meier and Cox models compared PFS across FACETS copy-number clusters and histologic subgroups [PMID:30068706](../papers/30068706.md)
- Multivariable Cox proportional-hazards model confirmed SMAD4 mutation as an independent predictor of worse OS in GBCA (HR 2.01, 95% CI 1.02–3.94; P=0.043) after adjusting for stage, gallstone status, and sex [PMID:30427539](../papers/30427539.md)
- Cox regression adjusting for cancer type, age, ICI drug class, and year of ICI start confirmed TMB as an independent predictor of OS in 1,662 ICI-treated advanced cancer patients (continuous TMB HR 0.985/unit, p = 3.4 × 10⁻⁷; binary top-20% HR 0.61, p = 1.3 × 10⁻⁷) [PMID:30643254](../papers/30643254.md)
- Used as a component of the non-homogeneous semi-Markov multistate model in the METABRIC breast cancer recurrence study (n=3,240 patients); IntClust subtypes added C-index 0.70 vs 0.63 at 10 years in late ER+/HER2- relapse prediction [PMID:30867590](../papers/30867590.md)
- Used in multivariate survival analysis of 128 taxane-naive mCRPC patients starting first-line ARSI; [RB1](../genes/RB1.md) alteration was the only molecular feature independently associated with both overall survival (RR=3.31) and time on first-line ARSI (RR=6.56) [PMID:31061129](../papers/31061129.md)

## Notes

- Implemented in R (survival package); analysis in TCGA-CDR performed in R 3.2.2.
- Proportional-hazards assumption should be tested (e.g., scaled Schoenfeld residuals); violations were noted for a minority of cancer type–endpoint combinations in the TCGA-CDR.
- Commonly paired with Kaplan-Meier curves for visualization and log-rank tests for unadjusted comparison.
- [LUSC](../cancer_types/LUSC.md) example from TCGA-CDR: never-disease-free vs disease-free patients, HR = 6.68 (95% CI 4.25–10.51, FDR q < 0.05).

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
- [PMID:29848569](../papers/29848569.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30068706](../papers/30068706.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30427539](../papers/30427539.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30643254](../papers/30643254.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30867590](../papers/30867590.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31061129](../papers/31061129.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
