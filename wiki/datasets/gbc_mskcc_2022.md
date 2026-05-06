---
name: MSK Gallbladder Carcinoma 2022
studyId: gbc_mskcc_2022
institution: Memorial Sloan Kettering Cancer Center
size: 233
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MSK-IMPACT
panels:
  - msk-impact-panel
tags:
  - gallbladder
  - biliary
  - GBC
  - MSK-IMPACT
processed_by: crosslinker
processed_at: 2026-05-06
---

# MSK Gallbladder Carcinoma 2022

## Overview

The largest single-institution genomic characterization of gallbladder carcinoma ([GBC](../cancer_types/GBC.md)) to date, from Memorial Sloan Kettering Cancer Center. The study profiled 244 samples from 233 patients collected between 2014 and 2021 using [MSK-IMPACT](../methods/msk-impact-panel.md) (341–505 gene panel versions), with median sequencing coverage of 634X. Dataset deposited in cBioPortal as `gbc_mskcc_2022`.

## Composition

- 233 patients / 244 samples of [GBC](../cancer_types/GBC.md), collected 2014–2021 at Memorial Sloan Kettering Cancer Center.
- 57% primary tumors, 43% metastases; 85% adenocarcinomas, 10% carcinomas with squamous differentiation, 5% neuroendocrine carcinomas.
- Median age at collection: 66 years (range 37–90); 63% Caucasian, 12% African American, 12% Asian.
- 67% stage IV, 18% stage III at time of collection.
- Microsatellite instability assessed via MSIsensor, MiMSI, and IDYLLA MSI; variants annotated with OncoKB.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — 341–505 gene panel versions; median coverage 634X (range 72X–1150X)

## Papers using this cohort

- [PMID:36228155](../papers/36228155.md) — Primary genomic characterization of GBC; identifies frequent alterations, prognostic biomarkers, and actionable targets.

## Notable findings derived from this cohort

- Most frequent oncogenic mutations: [TP53](../genes/TP53.md) (63%), [CDKN2A](../genes/CDKN2A.md) (21%), [SMAD4](../genes/SMAD4.md) (19%), [ARID1A](../genes/ARID1A.md) (18%), [ERBB2](../genes/ERBB2.md) (15% combined mutation + amplification); most frequent CNAs: CDKN2A/CDKN2B deletions (14%), [MDM2](../genes/MDM2.md) amplification (11%), ERBB2 amplification (10%), [CCNE1](../genes/CCNE1.md) amplification (9%) [PMID:36228155](../papers/36228155.md).
- SMAD4 LOF mutations independently associated with reduced [OS](../cancer_types/OS.md) in metastatic disease (multivariate HR 2.11, p = 0.012); [STK11](../genes/STK11.md) LOF mutations also independently associated with reduced OS (multivariate HR 3.76, p = 0.004) [PMID:36228155](../papers/36228155.md).
- Actionable alterations (OncoKB levels 1, 3A, or 3B) identified in 35.2% of patients; 18% of metastatic patients received biomarker-directed therapy or enrolled in clinical trials based on MSK-IMPACT findings; 6 tumors (3%) were MSI-High [PMID:36228155](../papers/36228155.md).
- LMNA::[NTRK1](../genes/NTRK1.md) fusion identified in 1 patient (OncoKB level 1); [KRAS](../genes/KRAS.md) G12C in 2 patients (level 3A); [FGFR3](../genes/FGFR3.md)::[TACC3](../genes/TACC3.md) in-frame fusion in 1 patient; no recurrent structural variants were identified [PMID:36228155](../papers/36228155.md).

## Sources

- cBioPortal study: `gbc_mskcc_2022`

*This page was processed by **crosslinker** on **2026-05-06**.*
