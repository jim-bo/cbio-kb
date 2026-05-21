---
name: Cox Proportional Hazards
slug: cox-proportional-hazards
kind: method
canonical_source: corpus
unverified: true
tags: [statistics, survival-analysis, regression]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Cox Proportional Hazards

## Overview

Cox proportional hazards regression is a semi-parametric survival analysis model that relates the hazard of an event (e.g., death, disease progression) to one or more covariates without requiring specification of the baseline hazard function. The model assumes that the hazard ratio between any two subjects remains constant (proportional) over time — the proportional-hazards assumption. It is the standard method for multivariable survival analysis in oncology and clinical trials, producing hazard ratios (HR) and confidence intervals as the primary effect-size metrics.

## Used by

- Used with proportional-hazards-assumption testing (Grambsch & Therneau 1994) to assess clinical outcome endpoints ([OS](../cancer_types/OS.md), PFI, DFI, DSS) across 11,160 TCGA patients in 33 cancer types; high-stage (III/IV) vs low-stage (I/II) HRs were significantly >1 in most cancer types with sufficient event capture [PMID:29625055](../papers/29625055.md).
- Applied in multivariate survival analysis of 178 stage IV cholangiocarcinoma patients; CDKN2A/B and [ERBB2](../genes/ERBB2.md) alterations remained significantly associated with shorter [OS](../cancer_types/OS.md) and PFS on first-line chemotherapy [PMID:29848569](../papers/29848569.md)
- Used for survival analysis of PFS in 189 advanced endometrial cancer patients profiled by MSK-IMPACT; Kaplan-Meier and Cox models compared PFS across FACETS copy-number clusters and histologic subgroups [PMID:30068706](../papers/30068706.md)
- Multivariable Cox proportional-hazards model confirmed [SMAD4](../genes/SMAD4.md) mutation as an independent predictor of worse OS in GBCA (HR 2.01, 95% CI 1.02–3.94; P=0.043) after adjusting for stage, gallstone status, and sex [PMID:30427539](../papers/30427539.md)
- Cox regression adjusting for cancer type, age, ICI drug class, and year of ICI start confirmed TMB as an independent predictor of OS in 1,662 ICI-treated advanced cancer patients (continuous TMB HR 0.985/unit, p = 3.4 × 10⁻⁷; binary top-20% HR 0.61, p = 1.3 × 10⁻⁷) [PMID:30643254](../papers/30643254.md)
- Used as a component of the non-homogeneous semi-Markov multistate model in the METABRIC breast cancer recurrence study (n=3,240 patients); IntClust subtypes added C-index 0.70 vs 0.63 at 10 years in late ER+/HER2- relapse prediction [PMID:30867590](../papers/30867590.md)
- Used in multivariate survival analysis of 128 taxane-naive mCRPC patients starting first-line ARSI; [RB1](../genes/RB1.md) alteration was the only molecular feature independently associated with both overall survival (RR=3.31) and time on first-line ARSI (RR=6.56) [PMID:31061129](../papers/31061129.md)
- Used for multivariable survival analysis in the Sherlock-Lung NS-LUAD study (n=684 tumors, age/sex/stage adjusted): steady HR=0.43 (95% CI 0.30–0.63), chaotic HR=1.4 (95% CI 0.99–2.0); stage I subset chaotic HR=2.5–3.7 [PMID:32015526](../papers/32015526.md).
- Used for time-to-event regression in 424 mCSPC patients; adjusted HR for castration resistance 1.84 (95% CI 1.40–2.41) for high-volume vs. low-volume disease [PMID:32220891](../papers/32220891.md)
- Applied in 1,465 prostate cancer patients to adjust OS for age, Gleason, PSA, visceral metastasis, and [FGA](../genes/FGA.md); CDK12-altered patients had aHR 1.80 (95% CI 1.12–2.89; p=0.024) for shorter OS [PMID:32317181](../papers/32317181.md)
- Used for multivariate survival analysis in 430 MSS mCRC patients; [APC](../genes/APC.md) mutation (N-terminal) associated with longer PFS (HR 0.68, p<0.001) and OS (HR 0.56, p<0.001) [PMID:32730818](../papers/32730818.md)
- Univariate and multivariate Cox analyses in 80-patient CRC tissue microarray identified [CGREF1](../genes/CGREF1.md) expression (HR 3.85, 95% CI 1.32–11.2, p=0.014) and venous invasion as independent predictors of disease-free survival [PMID:32888432](../papers/32888432.md)
- Cox proportional-hazards regression (backward selection of univariately significant covariates) used to model time-to-treatment failure in 322 melanoma patients on frontline PD-1 or nivo+ipi therapy in R 3.4.4 [PMID:33509808](../papers/33509808.md)
- Cox proportional-hazards regression (univariate and multivariate) used to model OS in 412 iCCA patients, adjusted for nodal disease, multifocal liver disease, and lymphovascular invasion in R 4.0.0 [PMID:33765338](../papers/33765338.md)
- Cox proportional-hazards multivariable model (adjusting for age, clinical stage, tumor grade, treatment intent) used to assess independent OS predictors in 487 EAC/EGJ patients; Harrell's C-index rose from 0.68 to 0.71 with genomic variables added [PMID:33795256](../papers/33795256.md)
- Used in multivariable survival analysis of 573 liver-limited intrahepatic cholangiocarcinoma ([IHCH](../cancer_types/IHCH.md)) patients; Cox model demonstrated HAIC vs resection HR 2.09 (95% CI 1.6–2.8) in N0 disease but equivalent HR 0.81 (95% CI 0.5–1.3) in N1 disease; treatment × nodal-status interaction term was significant (P<0.001) [PMID:33963001](../papers/33963001.md)
- Used in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for somatic variant calling and genomic analysis of the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)
- Applied in the MSK early-onset colorectal cancer cohort (759 EO-CRC patients vs 687 AO-CRC) for somatic and germline profiling at Memorial Sloan Kettering Cancer Center [PMID:34405229](../papers/34405229.md)
- Used as a baseline method in the OncoMark hallmark-classification study; standard baselines including logistic regression, random forest, XGBoost, and Cox models collapsed to near-zero hallmark probabilities on cancer samples, while the OncoMark MTL framework preserved discrimination [PMID:35121966](../papers/35121966.md)
- Applied in [lgsoc_mapk_msk_2022](../datasets/lgsoc_mapk_msk_2022.md) multivariate survival analysis (n=90 landmark cohort): MAPK pathway alteration (HR 2.5 for absence, p=0.019) and platinum sensitivity (HR 0.4, p=0.005) were independently associated with OS in LGSC [PMID:35443055](../papers/35443055.md)
- Used in [prad_organoids_msk_2022](../datasets/prad_organoids_msk_2022.md) to demonstrate CRPC-SCL subtype association with shorter time on next-generation ARSI among 56 SU2C patients with time-on-treatment data (Cox log-rank) [PMID:35617398](../papers/35617398.md)

## Notes

- Implemented in R (survival package); analysis in TCGA-CDR performed in R 3.2.2.
- Proportional-hazards assumption should be tested (e.g., scaled Schoenfeld residuals); violations were noted for a minority of cancer type–endpoint combinations in the TCGA-CDR.
- Commonly paired with Kaplan-Meier curves for visualization and log-rank tests for unadjusted comparison.
- [LUSC](../cancer_types/LUSC.md) example from TCGA-CDR: never-disease-free vs disease-free patients, HR = 6.68 (95% CI 4.25–10.51, FDR q < 0.05).

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29848569](../papers/29848569.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30068706](../papers/30068706.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30427539](../papers/30427539.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30643254](../papers/30643254.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30867590](../papers/30867590.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31061129](../papers/31061129.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32015526](../papers/32015526.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32220891](../papers/32220891.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32317181](../papers/32317181.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32730818](../papers/32730818.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32888432](../papers/32888432.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33509808](../papers/33509808.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33765338](../papers/33765338.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33795256](../papers/33795256.md)

- [PMID:33963001](../papers/33963001.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34493867](../papers/34493867.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34405229](../papers/34405229.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35121966](../papers/35121966.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35443055](../papers/35443055.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35617398](../papers/35617398.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
