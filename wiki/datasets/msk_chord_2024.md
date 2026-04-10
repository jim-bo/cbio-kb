---
name: "MSK-CHORD Clinicogenomic Harmonized Real-World Dataset, Nature 2024"
slug: msk_chord_2024
institution: Memorial Sloan Kettering Cancer Center
size: 24950 patients
assays:
  - msk-impact-panel
tags:
  - real-world-data
  - nlp
  - clinicogenomics
  - survival-prediction
processed_by: crosslinker
processed_at: 2026-04-10
---

# MSK-CHORD Clinicogenomic Harmonized Real-World Dataset, Nature 2024

## Overview

MSK-CHORD integrates NLP annotations of free-text clinician, radiology and pathology notes with structured medication, demographic, tumor registry and tumor genomic data from 24,950 MSK patients sequenced on MSK-IMPACT, spanning five cancer types. Built to enable real-world survival prediction and metastasis-site discovery from unstructured EHR data [PMID:39506116](../papers/39506116.md).

## Composition

- 24,950 MSK patients with MSK-IMPACT tumor sequencing [PMID:39506116](../papers/39506116.md).
- Five cancer types: [NSCLC](../cancer_types/NSCLC.md) (n=7,809), [BRCA](../cancer_types/BRCA.md) (n=5,368), [COADREAD](../cancer_types/COADREAD.md) (n=5,543), [PRAD](../cancer_types/PRAD.md) (n=3,211), [PAAD](../cancer_types/PAAD.md) (n=3,109) [PMID:39506116](../papers/39506116.md).
- 705,241 radiology reports annotated by NLP transformer models for organ-specific metastasis and progression [PMID:39506116](../papers/39506116.md).
- NLP models trained/validated against Project GENIE BPC (PRISSMM) MSK-BPC ground truth (n=3,202 patients, 38,719 radiology reports) [PMID:39506116](../papers/39506116.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — targeted hybrid-capture panel.
- [nlp-prissmm](../methods/nlp-prissmm.md) — NLP annotation pipeline on PRISSMM schema.

## Papers using this cohort

- [PMID:39506116](../papers/39506116.md) — Jee et al., Automated real-world data integration improves cancer outcome prediction, Nature 2024.

## Notable findings derived from this cohort

- Integrated multimodal models with NLP-derived sites-of-disease features outperformed genomics-only or stage-only models for overall survival [PMID:39506116](../papers/39506116.md).
- NLP per-site metastasis classification AUCs 0.85–0.99 across bone, liver, lung, lymph node, adrenal, pleura, CNS [PMID:39506116](../papers/39506116.md).
- [SETD2](../genes/SETD2.md) driver mutations in 3% of [LUAD](../cancer_types/LUAD.md) (204/5,957) predict longer [OS](../cancer_types/OS.md), lower CNS metastasis, and longer immune checkpoint blockade response independent of TMB [PMID:39506116](../papers/39506116.md).
- [RB1](../genes/RB1.md) oncogenic alterations enriched in brain and liver metastases [PMID:39506116](../papers/39506116.md).

## Sources

- cBioPortal study `msk_chord_2024`; released as a public resource [PMID:39506116](../papers/39506116.md).

*This page was processed by **crosslinker** on **2026-04-10**.*
