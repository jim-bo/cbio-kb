---
name: RADCURE Head and Neck Cancer RT Dataset
studyId: radcure
institution: Princess Margaret Cancer Centre, Toronto, Canada
size: 3346
reference_genome: N/A
canonical_source: corpus
unverified: true
assays:
  - ct-imaging
  - dicom-rt-struct
panels: []
tags:
  - hnscc
  - head-and-neck
  - radiomics
  - tcia
  - ct
  - radiation-therapy
  - rt-planning
  - public-dataset
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# RADCURE Head and Neck Cancer RT Dataset

## Overview

RADCURE is a large open-source head and neck cancer CT dataset comprising 3346 patients treated with curative-intent radiotherapy at Princess Margaret Cancer Centre (Toronto, Canada). The dataset includes RT simulation CT scans, manually generated and QA-reviewed target and organ-at-risk contours in DICOM RT-STRUCT format, and longitudinal clinical metadata. It is designed as a resource for radiomics, auto-segmentation, and treatment outcome prediction research. Hosted on The Cancer Imaging Archive (TCIA) and published by Welch et al. 2024. [PMID:38362943](../papers/38362943.md)

## Composition

- **Cancer type**: [HNSC](../cancer_types/HNSC.md) (head and neck squamous cell carcinoma), n=3346.
- **Disease subsites**: oropharyngeal 50%, laryngeal 25%, nasopharyngeal 12%, hypopharyngeal 5%.
- **Demographics**: median age 63; 80% male.
- **Modality**: RT simulation CT acquired on systems from three manufacturers under standard clinical protocols.
- **Annotations**: manually generated target volumes (gross primary tumour, gross nodal volumes) and 19 organs-at-risk contours, reviewed at weekly RT quality assurance rounds; standardised nomenclature applied.
- **Clinical metadata**: demographic, clinical, and treatment information; staging per 7th edition TNM.
- **Follow-up**: median 5 years; 60% surviving at last follow-up.
- **Format**: images and contours as DICOM CT and RT-STRUCT; clinical data as CSV. [PMID:38362943](../papers/38362943.md)

## Assays / panels (linked)

- [CT imaging](../methods/ct-imaging.md) — RT simulation CT.
- [DICOM RT-STRUCT](../methods/dicom-rt-struct.md) — standardised organ-at-risk and target contours.

## Papers using this cohort

- [PMID:38362943](../papers/38362943.md) — Welch et al. 2024, *Medical Physics*: primary dataset descriptor; 3346 HNC RT planning CTs from Princess Margaret Cancer Centre with standardised RT-STRUCT contours and longitudinal outcomes.
- [PMID:37397861](../papers/37397861.md) — Kim et al. 2023, *Radiotherapy and Oncology*: RADCURE used as the primary training (n=1,802) and internal test (n=750) cohort in the HNSC prognostic-modeling challenge; split by diagnosis date (2005–2013 vs 2016–2018).

## Notable findings derived from this cohort

- A custom data-mining and processing system was built to extract imaging and structure-set data from the institution's RT planning and oncology information systems, linking each scan to longitudinal clinical outcomes. [PMID:38362943](../papers/38362943.md)
- Standardised RT-STRUCT nomenclature was applied across 3346 patients to improve interoperability for downstream radiomics and auto-segmentation research. [PMID:38362943](../papers/38362943.md)
- In the multi-institutional prognostic challenge, the top-performing model (MTLR + EMR + tumor volume) achieved AUROC = 0.823 on the RADCURE internal test set; adding deep radiomics to EMR did not improve AUROC. [PMID:37397861](../papers/37397861.md)

## Sources

- TCIA collection: RADCURE — https://www.cancerimagingarchive.net/collection/radcure/
- [PMID:38362943](../papers/38362943.md) — Welch et al. 2024, *Medical Physics*, DOI 10.1002/mp.16971.
- [PMID:37397861](../papers/37397861.md) — Kim et al. 2023, *Radiotherapy and Oncology*.

*This page was processed by **entity-page-writer** on **2026-04-15**.*
