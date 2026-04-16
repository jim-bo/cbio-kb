---
name: TCIA H&N2 HNSCC (VU University Medical Center)
studyId: tcia-hn2-vumc
institution: VU University Medical Center, Amsterdam, Netherlands
size: 95
reference_genome: N/A
canonical_source: corpus
unverified: true
assays:
  - ct-imaging
panels: []
tags:
  - hnscc
  - head-and-neck
  - radiomics
  - tcia
  - ct
  - validation-cohort
processed_by: entity-page-writer
processed_at: 2026-04-15
processed_by: crosslinker
---

# TCIA H&N2 HNSCC (VU University Medical Center)

## Overview

The H&N2 collection comprises 95 head and neck squamous cell carcinoma ([HNSC](../cancer_types/HNSC.md)) patients treated at VU University Medical Center (Amsterdam, Netherlands). It served as the second independent HNSCC validation cohort in Aerts et al. 2014. CT scans and survival data are hosted on TCIA. [PMID:24892406](../papers/24892406.md)

## Composition

- **Cancer type**: [HNSC](../cancer_types/HNSC.md), n=95.
- **Modality**: CT; head-and-neck immobilisation protocol.
- **Clinical data**: treatment records, TNM staging, HPV status (subset), overall survival.
- **Role in Aerts 2014**: second cross-disease validation of the [NSCLC](../cancer_types/NSCLC.md)-derived four-feature radiomic signature. [PMID:24892406](../papers/24892406.md)

## Assays / panels (linked)

- [CT radiomics](../methods/ct-radiomics.md) — 440-feature library applied with Lung1-derived feature definitions.

## Papers using this cohort

- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*: H&N2 used as second HNSCC validation; the four-feature signature achieved concordance index 0.69 (P=3.53 × 10⁻⁶, Wilcoxon).

## Notable findings derived from this cohort

- 186 / 440 radiomic features (42%) were significantly prognostic in H&N2 at FDR 10% using Lung1-derived median thresholds. [PMID:24892406](../papers/24892406.md)
- Signature outperformed TNM in H&N2; signature + TNM significantly improved over TNM alone. [PMID:24892406](../papers/24892406.md)
- Signature retained prognostic performance in the HPV-negative subgroup (CI=0.66, n=130, combined H&N1+H&N2 76% of patients), supporting added value to HPV-only stratification. [PMID:24892406](../papers/24892406.md)

## Sources

- TCIA collection: Head-Neck-PET-CT — https://www.cancerimagingarchive.net/collection/head-neck-pet-ct/
- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*, DOI 10.1038/ncomms5006.

*This page was processed by **crosslinker** on **2026-04-15**.*
