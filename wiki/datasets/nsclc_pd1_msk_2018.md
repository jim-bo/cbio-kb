---
name: MSK NSCLC Anti-PD-1 Prospective Cohort (2018)
studyId: nsclc_pd1_msk_2018
institution: Memorial Sloan Kettering Cancer Center
size: 240
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - whole-exome-sequencing
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - immunotherapy
  - tumor-mutation-burden
  - pd-l1
  - biomarker
  - resistance
  - targeted-ngs
  - nsclc
  - anti-pd-1
processed_by: crosslinker
processed_at: 2026-05-15
---

# MSK NSCLC Anti-PD-1 Prospective Cohort (2018)

## Overview

Retrospective cohort of 240 patients with advanced non-small-cell lung cancer ([NSCLC](../cancer_types/NSCLC.md)) treated with anti-PD-(L)1 therapy at Memorial Sloan Kettering Cancer Center between April 2011 and January 2017, all profiled by [MSK-IMPACT](../methods/msk-impact-panel.md) targeted next-generation sequencing. The primary scientific contribution of this cohort was establishing that tumor mutation burden (TMB) measured on a targeted panel correlates with whole-exome estimates and predicts durable clinical benefit from immunotherapy in [NSCLC](../cancer_types/NSCLC.md). A separate comparison cohort of 1,836 non-ICI-treated NSCLC patients sequenced on MSK-IMPACT 2014–2017 was included for prognostic vs. predictive discrimination. [PMID:29337640](../papers/29337640.md)

## Composition

- **240 advanced NSCLC patients** treated with anti-PD-1 or anti-PD-L1 therapy (alone or with anti-CTLA-4) at MSKCC. [PMID:29337640](../papers/29337640.md)
- **Histology:** 78% adenocarcinoma ([LUAD](../cancer_types/LUAD.md)), 14% squamous ([LUSC](../cancer_types/LUSC.md)), 8% other. [PMID:29337640](../papers/29337640.md)
- **Treatment:** 86% PD-(L)1 monotherapy ([nivolumab](../drugs/nivolumab.md), [pembrolizumab](../drugs/pembrolizumab.md), [atezolizumab](../drugs/atezolizumab.md), [durvalumab](../drugs/durvalumab.md)); 14% PD-(L)1 + CTLA-4 combination ([ipilimumab](../drugs/ipilimumab.md)). [PMID:29337640](../papers/29337640.md)
- **Endpoints:** RECIST 1.1; durable clinical benefit (DCB) = CR/PR/SD lasting >6 months; no durable benefit (NDB) = PD or SD ≤6 months. 49 (20%) had CR/PR; 69 (29%) had DCB; 158 (66%) NDB. [PMID:29337640](../papers/29337640.md)
- **Validation subset:** 49 patients had paired whole-exome sequencing for TMB correlation. [PMID:29337640](../papers/29337640.md)
- **PD-L1 IHC:** Available for 84 patients (22C3, 28-8, E1L3N antibodies). [PMID:29337640](../papers/29337640.md)
- **Comparison cohort:** 1,836 non-ICI-treated NSCLC patients sequenced on MSK-IMPACT 2014–2017 (to assess prognostic vs. predictive nature of TMB). [PMID:29337640](../papers/29337640.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) targeted NGS, mean coverage 744x:
  - [IMPACT341](../methods/IMPACT341.md): 56 patients
  - [IMPACT410](../methods/IMPACT410.md): 164 patients
  - [IMPACT468](../methods/IMPACT468.md): 20 patients
- [whole-exome-sequencing](../methods/whole-exome-sequencing.md): 49 patients (validation subset for TMB correlation). [PMID:29337640](../papers/29337640.md)

## Papers using this cohort

- [PMID:29337640](../papers/29337640.md) — Rizvi et al. 2018, *Journal of Clinical Oncology* — "Molecular Determinants of Response to Anti-Programmed Cell Death (PD)-1 and Anti-Programmed Death-Ligand 1 (PD-L1) Blockade in Patients With Non-Small-Cell Lung Cancer Profiled With Targeted Next-Generation Sequencing"

## Notable findings derived from this cohort

- TMB by MSK-IMPACT correlated with TMB by whole-exome sequencing (Spearman r=0.86, P<0.001), validating targeted panel as a practical TMB surrogate. [PMID:29337640](../papers/29337640.md)
- Median TMB was significantly higher in DCB vs. NDB patients (8.5 vs. 6.6 SNVs/Mb, P=0.006); DCB rate above the 50th TMB percentile was 38.6% vs. 25.1% below (P=0.009). [PMID:29337640](../papers/29337640.md)
- TMB is predictive, not prognostic: in the non-ICI comparison cohort, higher TMB was associated with worse survival, ruling out a generic favorable prognosis effect. [PMID:29337640](../papers/29337640.md)
- TMB and PD-L1 are independent predictors (r=0.19, P=0.08); combining TMB-high + PD-L1 ≥1% gave 50% DCB rate vs. 18% when both low. [PMID:29337640](../papers/29337640.md)
- [EGFR](../genes/EGFR.md)-mutant tumors were underrepresented in DCB (7% of EGFR-mutant patients achieved DCB; FDR-adjusted P=0.013). [PMID:29337640](../papers/29337640.md)
- [STK11](../genes/STK11.md) mutations were enriched in NDB (FDR-adjusted P=0.007 vs. non-ICI cohort), consistent with LKB1-loss driving low tumor inflammation. [PMID:29337640](../papers/29337640.md)
- High fraction of copy-number-altered genome ([FGA](../genes/FGA.md)) was enriched in NDB patients (median 0.16 vs. 0.11, P=0.007). [PMID:29337640](../papers/29337640.md)
- MDM2/MDM4 amplification (n=8) did not show hyperprogression in this series (HR 1.4, P=0.44), in contrast to prior reports. [PMID:29337640](../papers/29337640.md)

## Sources

- cBioPortal study: `nsclc_pd1_msk_2018`
- DOI: [10.1200/JCO.2017.75.3384](https://doi.org/10.1200/JCO.2017.75.3384)

*This page was processed by **crosslinker** on **2026-05-15**.*
