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
- PFS analysis by Kaplan-Meier with log-rank testing stratified by PIK3CA and MAP3K1 genotype in 33 metastatic ER+/HER2- breast cancer patients; MAP3K1 alteration improved PFS (p=0.03), PIK3CA alteration improved PFS (p=0.009); co-alteration showed greatest benefit (p=0.02 trend test) [PMID:31552290](../papers/31552290.md).
- Kaplan-Meier curves generated for time-to-castration-resistance and overall survival in 424 mCSPC patients; high-volume vs. low-volume and genomic-alteration subgroups compared [PMID:32220891](../papers/32220891.md)
- Used to display OS and time-to-CRPC in 1,465 prostate cancer patients stratified by CDK12 alteration status (CDK12-WT vs CDK12-altered vs CDK12-Bi) [PMID:32317181](../papers/32317181.md)
- RECIST v1.1 imaging assessments and Kaplan-Meier survival analysis used in the FUTURE trial to evaluate PFS and DOR across 7 biomarker-matched arms in 69 refractory metastatic TNBC patients [PMID:32719455](../papers/32719455.md)
- Used for PFS and OS estimation from first-line chemotherapy start in 430 MSS mCRC patients; revealed significantly longer OS/PFS for N-terminal vs C-terminal APC truncating mutations [PMID:32730818](../papers/32730818.md)
- Kaplan-Meier analysis in 80-patient CRC tissue microarray showed high CGREF1 expression associated with significantly shorter overall survival (log-rank p<0.0001) [PMID:32888432](../papers/32888432.md)
- Kaplan-Meier estimators (starting from enucleation date) used to model event-free survival in 83 retinoblastoma specimens; BCOR mutations associated with worse metastasis-free survival (nominal p=0.03) [PMID:33466343](../papers/33466343.md)
- Kaplan-Meier / log-rank analysis used to compare time-to-treatment failure across MAPK driver groups in 322 melanoma patients on PD-1 or nivo+ipi; driver-group effect p<0.0001 [PMID:33509808](../papers/33509808.md)
- Kaplan-Meier OS estimates used throughout 412-patient iCCA cohort to assess prognostic impact of TP53, KRAS, and CDKN2A alterations [PMID:33765338](../papers/33765338.md)
- Kaplan-Meier analysis used to compare OS across genomic subgroups in 487 EAC/EGJ patients; median OS 31.6 months overall (CIT 42.5 mo vs. PIT 22.8 mo, p<0.001) [PMID:33795256](../papers/33795256.md)

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
- [PMID:31552290](../papers/31552290.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:32220891](../papers/32220891.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:32317181](../papers/32317181.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:32719455](../papers/32719455.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:32730818](../papers/32730818.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:32888432](../papers/32888432.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:33466343](../papers/33466343.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:33509808](../papers/33509808.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:33765338](../papers/33765338.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:33795256](../papers/33795256.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
