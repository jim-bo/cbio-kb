---
name: TCIA H&N1 HNSCC (MAASTRO)
studyId: tcia-hn1-maastro
institution: MAASTRO Clinic, Maastricht, Netherlands
size: 136
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

# TCIA H&N1 HNSCC (MAASTRO)

## Overview

The H&N1 collection comprises 136 head and neck squamous cell carcinoma ([HNSC](../cancer_types/HNSC.md)) patients treated at MAASTRO Clinic (Maastricht, Netherlands). It served as the first HNSCC validation cohort in Aerts et al. 2014, testing cross-disease transferability of the [NSCLC](../cancer_types/NSCLC.md)-trained radiomic prognostic signature. CT scans and survival data are hosted on TCIA. [PMID:24892406](../papers/24892406.md)

## Composition

- **Cancer type**: [HNSC](../cancer_types/HNSC.md) (head and neck squamous cell carcinoma), n=136.
- **Modality**: CT; head-and-neck immobilisation protocol (reduced motion artefact vs. free-breathing lung CT).
- **Annotations**: manual tumour delineations; HPV status available for a subset.
- **Clinical data**: treatment records, TNM staging, overall survival.
- **Role in Aerts 2014**: first cross-disease validation of the NSCLC-derived four-feature radiomic signature. [PMID:24892406](../papers/24892406.md)

## Assays / panels (linked)

- [CT radiomics](../methods/ct-radiomics.md) — 440-feature library applied with Lung1-derived feature definitions.

## Papers using this cohort

- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*: H&N1 used as first HNSCC validation; the four-feature signature achieved concordance index 0.69 (P=7.99 × 10⁻⁷, Wilcoxon).

## Notable findings derived from this cohort

- 135 / 440 radiomic features (31%) were significantly prognostic in H&N1 at FDR 10% using Lung1-derived median thresholds. [PMID:24892406](../papers/24892406.md)
- Signature + TNM significantly improved over TNM alone; signature performance was comparable to TNM staging in H&N1. [PMID:24892406](../papers/24892406.md)
- No significant association between the radiomic signature and HPV status (P=0.17, combined H&N1+H&N2), supporting the signature's complementarity to HPV-based stratification. [PMID:24892406](../papers/24892406.md)

## Sources

- TCIA collection: Head-Neck-PET-CT — https://www.cancerimagingarchive.net/collection/head-neck-pet-ct/
- [PMID:24892406](../papers/24892406.md) — Aerts et al. 2014, *Nature Communications*, DOI 10.1038/ncomms5006.

*This page was processed by **crosslinker** on **2026-04-15**.*
