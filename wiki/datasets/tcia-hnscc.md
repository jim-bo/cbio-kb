---
name: TCIA HNSCC Collection (MD Anderson)
studyId: tcia-hnscc
institution: The University of Texas MD Anderson Cancer Center
size: 215
reference_genome: N/A
canonical_source: corpus
unverified: true
assays:
  - pet-ct-imaging
  - ct-imaging
  - dicom-rt-planning
panels: []
tags:
  - hnscc
  - head-and-neck
  - tcia
  - ct
  - pet-ct
  - radiotherapy
  - body-composition
  - sarcopenia
  - hpv
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# TCIA HNSCC Collection (MD Anderson)

## Overview

The TCIA HNSCC collection is a clinical imaging archive of 215 head and neck squamous cell carcinoma ([HNSC](../cancer_types/HNSC.md)) patients treated with curative-intent radiotherapy at MD Anderson Cancer Center (October 2003 – August 2013). It includes pre- and post-treatment PET-CT and RT simulation CT scans, RT planning DICOMs (RTPLAN, RTSTRUCT, RTDOSE), and a clinical spreadsheet with body composition measurements, HPV status, staging, and survival outcomes. Published by Grossberg et al. 2018 as TCIA collection DOI 10.7937/K9/TCIA.2017.umz8dv6s (433,384 DICOM files across 3,225 series). [PMID:30179230](../papers/30179230.md)

## Composition

- **Cancer type**: [HNSC](../cancer_types/HNSC.md), n=215 (screened from 2,840 consecutive patients).
- **Subsite**: 73% oropharyngeal primaries (base of tongue 51%, tonsil 43%); 85.5% male.
- **Treatment**: 59% (127/215) received concurrent chemotherapy, 98% of whom received platinum-based regimens ([cisplatin](../drugs/cisplatin.md)); 13% postoperative RT. Mean RT dose 68.66 Gy (28–40 fractions).
- **Imaging**: pre-treatment whole-body PET-CT in 212/215 (98.6%); follow-up PET-CT in 213/215 (99.1%); RT simulation CT for all. Multiple scanner makes (GE, Philips, Picker, Marconi).
- **HPV status**: assessed by in situ hybridisation for high-risk HPV subtypes; AJCC 7th edition TNM staging.
- **Body composition**: pre- and post-RT skeletal muscle and adipose cross-sectional area at L3 vertebra measured in Pinnacle v9.6 using HU thresholds; lumbar skeletal muscle index (SMI) and adipose index (ADI) normalised to height².
- **Scale**: 433,384 DICOM files, 3,225 series, 765 studies. Each patient contributes pre-treatment CT/PET-CT, simulation CT, RTPLAN, RTSTRUCT, RTDOSE, and post-treatment imaging. [PMID:30179230](../papers/30179230.md)

## Assays / panels (linked)

- [PET-CT imaging](../methods/pet-ct-imaging.md) — FDG PET-CT pre- and post-treatment.
- [CT imaging](../methods/ct-imaging.md) — RT simulation CT and body composition analysis at L3.
- [DICOM RT planning](../methods/dicom-rt-planning.md) — RTPLAN, RTSTRUCT, RTDOSE.

## Papers using this cohort

- [PMID:30179230](../papers/30179230.md) — Grossberg et al. 2018, *Scientific Data*: primary dataset descriptor; 215 HNSCC patients with multi-timepoint PET-CT, RT planning DICOMs, and body composition annotations at L3.
- [PMID:37397861](../papers/37397861.md) — Kim et al. 2023, *Radiotherapy and Oncology*: MDACC subset (n=627 oropharynx) used as external validation; validated externally by Dana-Farber Cancer Institute collaborators using pretrained challenge models.

## Notable findings derived from this cohort

- Unique body composition annotations: pre- and post-RT skeletal muscle (HU −29 to 150) and adipose (HU −190 to −30) CSA at L3, with skeletal-muscle depletion defined at SMI <52.4 cm²/m² (men) / <38.5 cm²/m² (women). Total lean body mass and fat mass derived via published formulae. [PMID:30179230](../papers/30179230.md)
- Technical validation required 2–6 curation revisions per subject (mean 3.17) to resolve DICOM inconsistencies; 90.7% of subjects had series/study inconsistency issues on initial intake. [PMID:30179230](../papers/30179230.md)
- On the MDACC subset, only the top combined model (MTLR + EMR + volume) beat tumor volume alone, and by a small margin; external generalizability was limited compared with the RADCURE internal test set. [PMID:37397861](../papers/37397861.md)

## Notes

- Kim et al. 2023 ([PMID:37397861](../papers/37397861.md)) uses a 627-patient oropharynx subset curated from the same TCIA HNSCC collection as Grossberg 2018; exact subset provenance is not reconciled in the paper. The canonical collection size (n=215) reflects the Grossberg 2018 descriptor.

## Sources

- TCIA collection: HNSCC — TCIA DOI 10.7937/K9/TCIA.2017.umz8dv6s
- [PMID:30179230](../papers/30179230.md) — Grossberg et al. 2018, *Scientific Data*, DOI 10.1038/sdata.2018.173.
- [PMID:37397861](../papers/37397861.md) — Kim et al. 2023, *Radiotherapy and Oncology*.

*This page was processed by **entity-page-writer** on **2026-04-15**.*
