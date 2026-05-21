---
name: Prostate Adenocarcinoma (MSK, Clin Cancer Res. 2022)
studyId: prad_pik3r1_msk_2021
institution: Memorial Sloan Kettering Cancer Center
size: 1417
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MSK-IMPACT (IMPACT341, IMPACT410, IMPACT468)
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - prostate cancer
  - PIK3R1
  - PI3K pathway
  - paired tumor-normal
processed_by: crosslinker
processed_at: 2026-05-21
---

# Prostate Adenocarcinoma (MSK, Clin Cancer Res. 2022)

## Overview

MSK-IMPACT targeted sequencing cohort of 1,417 prostate adenocarcinoma patients (after FACETS QC from 2,735 sequenced) at Memorial Sloan Kettering Cancer Center. The study was designed to characterize [PIK3R1](../genes/PIK3R1.md) alterations across the full spectrum of prostate cancer, from primary disease through metastatic castration-resistant prostate cancer (mCRPC). Tumor-normal paired capture sequencing was performed using MSK-IMPACT panels (IMPACT341/IMPACT410/IMPACT468; 340/410/468 genes, all containing PIK3R1). Samples with MSI-sensor >10 or TMB >20 mut/Mb were excluded to avoid passenger PIK3R1 events.

## Composition

- 825 (58%) primary and 592 (42%) metastatic samples
- Metastatic sub-categories: mCSPC and mCRPC
- FDG-PET sub-cohort: 313 patients (71 primary, 242 metastases) with hybrid FDG-PET/CT
- Cancer type: prostate adenocarcinoma ([PRAD](../cancer_types/PRAD.md))
- Reference genome: hg19

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md): [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md) panels
- [FACETS](../methods/facets.md) for allelic copy number and clonality
- [GISTIC](../methods/gistic.md) for recurrent copy-number alterations
- [OncoKB](../methods/oncokb-annotation.md) v2.8 for oncogenicity annotation

## Papers using this cohort

- [PMID:35670774](../papers/35670774.md) — Chakraborty et al., Clin Cancer Res 2022. Primary study: PIK3R1 alterations in prostate cancer.

## Notable findings derived from this cohort

- PIK3R1 driver alterations enriched in metastatic vs primary prostate cancer (5.0% vs 2.7%, p=0.030); 51/1,417 patients (3.6%) total; PIK3R1 copy-number loss enriched in metastases (36% vs 24%, p<0.001); truncating mutations cluster in the c-SH2 domain; PIK3R1-altered tumors uniquely associated with elevated FDG-PET avidity (p=0.002, FDR=0.039) and sensitivity to AKT inhibitors in patient-derived organoids [PMID:35670774](../papers/35670774.md)

## Sources

- cBioPortal study: `prad_pik3r1_msk_2021`
- Citation: Chakraborty et al. Clin Cancer Research 2022 [PMID:35670774](../papers/35670774.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
