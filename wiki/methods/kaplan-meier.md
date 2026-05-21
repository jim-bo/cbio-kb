---
name: Kaplan-Meier
slug: kaplan-meier
kind: method
canonical_source: corpus
unverified: true
tags: [statistics, survival-analysis, visualization]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Kaplan-Meier

## Overview

The Kaplan-Meier (KM) estimator is a non-parametric method for estimating the survival function from time-to-event data, accounting for censored observations. It produces a step-function [estimate](../methods/estimate.md) of the probability of surviving past a given time point. KM curves are the standard visualization for survival data in oncology, and the log-rank test is used to assess differences between groups. The KM estimator is implemented in the `survival` package in R and is the foundational survival analysis tool used across virtually all clinical and genomic studies.

## Used by

- Used to generate survival curves for [OS](../cancer_types/OS.md), PFI, DFI, and DSS endpoints across 11,160 TCGA patients in 33 cancer types (TCGA Pan-Cancer Clinical Data Resource); paired with Cox proportional hazards regression for multivariable analysis; analysis performed in R 3.2.2 [PMID:29625055](../papers/29625055.md).
- Kaplan-Meier survival curves generated for [OS](../cancer_types/OS.md) and PFS analysis in 178 stage IV cholangiocarcinoma patients; progression-free survival on first-line chemo assessed in 158 patients [PMID:29848569](../papers/29848569.md)
- Kaplan-Meier survival curves used to compare PFS across FACETS copy-number clusters (A, B, C) and histologic/grade subgroups in 189 advanced endometrial cancer patients [PMID:30068706](../papers/30068706.md)
- Kaplan-Meier survival curves used to compare outcomes by genotype (PI3K-mTOR pathway and WNT/β-catenin alterations) in 127 [HCC](../cancer_types/HCC.md) patients on [sorafenib](../drugs/sorafenib.md) or immune checkpoint inhibitors [PMID:30373752](../papers/30373752.md)
- Kaplan-Meier survival analysis used to compare overall survival by [SMAD4](../genes/SMAD4.md) mutation status in 81 GBCA patients; SMAD4-mutant patients had median [OS](../cancer_types/OS.md) 10.4 mo vs 24.8 mo [PMID:30427539](../papers/30427539.md)
- Kaplan-Meier [OS](../cancer_types/OS.md) analysis in 1,662 ICI-treated advanced cancer patients showed top-20%-by-histology TMB-high group HR 0.52 (95% CI 0.42–0.64); no OS benefit for high TMB in 5,371 non-ICI-treated patients (HR 1.12, p = 0.11) [PMID:30643254](../papers/30643254.md)
- Used for survival analysis in 429 mCRPC patients; log-rank tests compared OS curves; Nestin-positive vs. Nestin-negative groups and PLC transcriptomic cluster comparisons were evaluated [PMID:31061129](../papers/31061129.md)
- Applied in the pan-Asia cHCC-ICC study (133 cases); Nestin-positive (n=104) vs. Nestin-negative median OS was 18.7 mo vs. 46.6 mo (p<0.0001, log-rank); PLC transcriptomic clusters P1/P2 had significantly poorer prognosis than P3/P4 (p<0.0001) [PMID:31130341](../papers/31130341.md)
- PFS analysis by Kaplan-Meier with log-rank testing stratified by [PIK3CA](../genes/PIK3CA.md) and [MAP3K1](../genes/MAP3K1.md) genotype in 33 metastatic ER+/HER2- breast cancer patients; [MAP3K1](../genes/MAP3K1.md) alteration improved PFS (p=0.03), [PIK3CA](../genes/PIK3CA.md) alteration improved PFS (p=0.009); co-alteration showed greatest benefit (p=0.02 trend test) [PMID:31552290](../papers/31552290.md).
- Kaplan-Meier curves generated for time-to-castration-resistance and overall survival in 424 mCSPC patients; high-volume vs. low-volume and genomic-alteration subgroups compared [PMID:32220891](../papers/32220891.md)
- Used to display OS and time-to-CRPC in 1,465 prostate cancer patients stratified by [CDK12](../genes/CDK12.md) alteration status (CDK12-WT vs CDK12-altered vs CDK12-Bi) [PMID:32317181](../papers/32317181.md)
- RECIST v1.1 imaging assessments and Kaplan-Meier survival analysis used in the FUTURE trial to evaluate PFS and DOR across 7 biomarker-matched arms in 69 refractory metastatic TNBC patients [PMID:32719455](../papers/32719455.md)
- Used for PFS and OS estimation from first-line chemotherapy start in 430 MSS mCRC patients; revealed significantly longer OS/PFS for N-terminal vs C-terminal [APC](../genes/APC.md) truncating mutations [PMID:32730818](../papers/32730818.md)
- Kaplan-Meier analysis in 80-patient CRC tissue microarray showed high [CGREF1](../genes/CGREF1.md) expression associated with significantly shorter overall survival (log-rank p<0.0001) [PMID:32888432](../papers/32888432.md)
- Kaplan-Meier estimators (starting from enucleation date) used to model event-free survival in 83 retinoblastoma specimens; [BCOR](../genes/BCOR.md) mutations associated with worse metastasis-free survival (nominal p=0.03) [PMID:33466343](../papers/33466343.md)
- Kaplan-Meier / log-rank analysis used to compare time-to-treatment failure across MAPK driver groups in 322 melanoma patients on PD-1 or nivo+ipi; driver-group effect p<0.0001 [PMID:33509808](../papers/33509808.md)
- Kaplan-Meier OS estimates used throughout 412-patient iCCA cohort to assess prognostic impact of [TP53](../genes/TP53.md), [KRAS](../genes/KRAS.md), and [CDKN2A](../genes/CDKN2A.md) alterations [PMID:33765338](../papers/33765338.md)
- Kaplan-Meier analysis used to compare OS across genomic subgroups in 487 EAC/EGJ patients; median OS 31.6 months overall (CIT 42.5 mo vs. PIT 22.8 mo, p<0.001) [PMID:33795256](../papers/33795256.md)
- Used to [estimate](../methods/estimate.md) overall survival for 573 intrahepatic cholangiocarcinoma ([IHCH](../cancer_types/IHCH.md)) patients stratified by initial treatment (resection, HAIC, SYS) and nodal status; key OS estimates: N0 resection 59.9 months, HAIC 24.9 months, SYS 13.7 months (P<0.001); N1 resection 19.7 vs HAIC 18.1 months (P=0.560) [PMID:33963001](../papers/33963001.md)
- Applied in the MSK early-onset colorectal cancer cohort (759 EO-CRC patients vs 687 AO-CRC) for somatic and germline profiling at Memorial Sloan Kettering Cancer Center [PMID:34405229](../papers/34405229.md)
- Used in [lgsoc_mapk_msk_2022](../datasets/lgsoc_mapk_msk_2022.md) for univariate OS analysis across 119 LGSC patients; MAPK pathway alteration (p=0.005) and platinum sensitivity (p=0.001) were associated with improved OS by KM analysis [PMID:35443055](../papers/35443055.md)
- Kaplan-Meier survival analysis applied for progression-free and overall survival in MSK-IMPACT prostate cancer cohorts and in KM-plotter pan-cancer datasets (gastric, liver, [NSCLC](../cancer_types/NSCLC.md)) for [PIK3R1](../genes/PIK3R1.md) mRNA associations [PMID:35670774](../papers/35670774.md)
- Kaplan-Meier analysis used to compare progression-free survival among 119 MSI-H/MMR-D endometrial cancer patients stratified by MMR-deficiency mechanism (germline, somatic, MLH1-promoter-hypermethylation); MLH1ph associated with inferior PFS (p=0.005) [PMID:35849120](../papers/35849120.md)
- Used for overall survival analysis in the Beat [AML](../cancer_types/AML.md) Waves 1–4 cohort (n=805 AML patients); [PEAR1](../genes/PEAR1.md) expression stratified OS with hazard ratios comparable to the LSC17 leukemic stem-cell signature across age strata [PMID:35868306](../papers/35868306.md)

## Notes

- KM curves in TCGA-CDR breast cancer analysis were truncated at 10-year follow-up; ER+ patients showed significantly better PFI (p = 0.005), DFI (p = 0.001), and DSS (p = 0.009) than ER- patients.
- KM-derived median OS for TCGA [GBM](../cancer_types/GBM.md) = 12.6 months, median PFI = 6.1 months — values between the two arms of Stupp et al. 2005.
- Commonly paired with Cox proportional hazards regression; log-rank test used for unadjusted group comparisons.

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29848569](../papers/29848569.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30068706](../papers/30068706.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30373752](../papers/30373752.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30427539](../papers/30427539.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30643254](../papers/30643254.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31061129](../papers/31061129.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31552290](../papers/31552290.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32220891](../papers/32220891.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32317181](../papers/32317181.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32719455](../papers/32719455.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32730818](../papers/32730818.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32888432](../papers/32888432.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33466343](../papers/33466343.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33509808](../papers/33509808.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33765338](../papers/33765338.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33795256](../papers/33795256.md)

- [PMID:33963001](../papers/33963001.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34405229](../papers/34405229.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35443055](../papers/35443055.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35670774](../papers/35670774.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35849120](../papers/35849120.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35868306](../papers/35868306.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
