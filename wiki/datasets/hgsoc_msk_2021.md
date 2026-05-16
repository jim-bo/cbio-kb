---
name: High-Grade Serous Ovarian Cancer (MSK, NPJ Genome Med 2021)
studyId: hgsoc_msk_2021
institution: Memorial Sloan Kettering Cancer Center
size: 45
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - TARGETED_SEQUENCING
  - WHOLE_EXOME_SEQUENCING
panels:
  - msk-impact-panel
tags:
  - high-grade serous ovarian carcinoma
  - HGSOC
  - immune checkpoint inhibitor
  - network curvature
  - CNA
  - MSK-IMPACT
  - ICI
  - biomarker
processed_by: crosslinker
processed_at: 2026-05-16
---

# High-Grade Serous Ovarian Cancer (MSK, NPJ Genome Med 2021)

## Overview

hgsoc_msk_2021 is a Memorial Sloan Kettering cohort of 45 patients with recurrent high-grade serous ovarian carcinoma ([HGSOC](../cancer_types/HGSOC.md)) who were treated with immune checkpoint inhibitors (ICIs). Samples were drawn from the 69-patient ICI series published by Zamarin et al. (JCO 2020, PMID:32616680). Both targeted (MSK-IMPACT) and whole-exome sequencing data were used to derive gene-level copy-number alteration (CNA) profiles. The study introduced Ollivier–Ricci network curvature as a predictive biomarker for ICI response. Reference genome: hg19 (GRCh37).

## Composition

- Cancer type: [HGSOC](../cancer_types/HGSOC.md); broader category [OV](../cancer_types/OV.md)
- n = 45 patients (32 deaths at analysis); 32 metastatic and 13 primary (adnexal) samples
- Mean age 58 years; mean TMB 5.9 mut/Mb; 10/45 with BRCA1/2 mutations
- ICI regimens: 25 PD-1/PD-L1 monotherapy, 15 PD-1/PD-L1 + CTLA-4 combination, 4 PD-1/PD-L1 + other, 1 CTLA-4 monotherapy; agents included [nivolumab](../drugs/nivolumab.md), [ipilimumab](../drugs/ipilimumab.md), [avelumab](../drugs/avelumab.md), [olaparib](../drugs/olaparib.md) + [durvalumab](../drugs/durvalumab.md) combinations
- Sequencing: [MSK-IMPACT](../methods/msk-impact-panel.md) for tumor and matched normal; WES contributed to CNA calls
- CNA segments: [FACETS](../methods/facets.md), mapped to GRCh37 gene coordinates
- PPI scaffold: HPRD-derived, 3,489 genes / 9,710 edges

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — primary targeted panel NGS with matched normal sequencing

## Papers using this cohort

- [PMID:34819508](../papers/34819508.md) — Elkin et al., NPJ Genomic Medicine 2021: Geometric network analysis provides prognostic information in patients with HGSOC treated with immune checkpoint inhibitors

## Notable findings derived from this cohort

- Total Ollivier–Ricci network curvature (κG) stratified [OS](../cancer_types/OS.md) after ICI at the 25th-percentile cut-off: low-curvature (n=12) median OS 7.4 mo vs high-curvature (n=33) 20.3 mo (log-rank p = 0.00047); curvature outperformed TMB (p = 0.032), LST (p = 0.43), and [FGA](../genes/FGA.md) (p = 0.20) in the same cohort [PMID:34819508](../papers/34819508.md)
- Curvature was not prognostic in HGSOC patients who did not receive ICI, supporting a predictive (ICI-specific) rather than general prognostic interpretation; [TP53](../genes/TP53.md) had the largest positive Δκ risk (0.209) across all sub-analyses [PMID:34819508](../papers/34819508.md)

## Sources

- cBioPortal study: `https://www.cbioportal.org/study/summary?id=hgsoc_msk_2021`
- Citation: Elkin et al., NPJ Genomic Medicine 2021, [PMID:34819508](../papers/34819508.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
