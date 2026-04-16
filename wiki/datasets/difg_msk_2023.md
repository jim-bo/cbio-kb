---
name: IDH-mutant Low-Grade Glioma Active Surveillance, MSK, Clin Cancer Res 2023
studyId: difg_msk_2023
institution: Memorial Sloan Kettering Cancer Center
size: 128 patients (73 with MSK-IMPACT sequencing)
reference_genome: GRCh37
canonical_source: 
unverified: 
assays: [targeted-panel]
panels: []
tags: [glioma, IDH-mutant, active-surveillance, tumor-growth-kinetics]
processed_by: entity-page-writer
processed_at: 2026-04-08
---

# IDH-mutant Low-Grade Glioma Active Surveillance, MSK, Clin Cancer Res 2023

## Overview

Retrospective MSKCC cohort of 128 consecutive adult patients with WHO 2016 Grade 2 IDH-mutant astrocytoma or oligodendroglioma evaluated 1997–2019, all observed without upfront chemoradiation after biopsy/resection. Built to characterize tumor volume growth rates (TVGR) during active surveillance and correlate with molecular grade [PMID:37910594](../papers/37910594.md).

## Composition

- 128 adult patients with WHO 2016 Grade 2 IDH-mutant glioma; 69 (53.9%) 1p19q codeleted oligodendrogliomas and 59 (46.1%) 1p19q intact astrocytomas [PMID:37910594](../papers/37910594.md).
- Cancer types: [DIFG](../cancer_types/DIFG.md), [ASTR](../cancer_types/ASTR.md), [ODG](../cancer_types/ODG.md).
- Median follow-up 6.3 years (range 0.5–23.1); median 8 MRI scans per patient (range 2–28) [PMID:37910594](../papers/37910594.md).
- MSK-IMPACT targeted sequencing on 73/128 patients with tissue available [PMID:37910594](../papers/37910594.md).
- Manual 3D volumetric T2/FLAIR segmentation with VASARI feature annotation.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — 468-gene targeted hybrid-capture NGS panel [PMID:37910594](../papers/37910594.md).

## Papers using this cohort

- [PMID:37910594](../papers/37910594.md) — Bhatia et al., Tumor Volume Growth Rates and Doubling Times during Active Surveillance of IDH-mutant Low-Grade Glioma, Clin Cancer Res 2024.

## Notable findings derived from this cohort

- Continuous TVGR = 10.46% per 6 months (95% CI 9.11–11.83), doubling time 3.5 years [PMID:37910594](../papers/37910594.md).
- CDKN2A/B homozygous deletion ("molecular grade-high") drove ~2× faster TVGR (19.17% vs 9.54% per 6 months, P<0.0001) [PMID:37910594](../papers/37910594.md).
- Joint longitudinal-survival model: each ln(tumor volume) unit increase → HR=3.83 for overall survival [PMID:37910594](../papers/37910594.md).
- Mutation landscape: codeleted tumors showed [TERT](../genes/TERT.md) promoter 100%, [CIC](../genes/CIC.md) 42%, [FUBP1](../genes/FUBP1.md) 24%; intact tumors [TP53](../genes/TP53.md) 94%, [ATRX](../genes/ATRX.md) 77% [PMID:37910594](../papers/37910594.md).

## Sources

- cBioPortal study `difg_msk_2023`; data also released on Synapse syn52658621 [PMID:37910594](../papers/37910594.md).

*This page was processed by **entity-page-writer** on **2026-04-08**.*
