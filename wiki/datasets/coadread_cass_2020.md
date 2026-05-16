---
name: Hunan CRC Tissue Microarray Cohort (CASS)
studyId: coadread_cass_2020
institution: Hunan Cancer Hospital
size: 80
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - immunohistochemistry
  - quantitative-rt-pcr
panels: []
tags:
  - colorectal-cancer
  - tissue-microarray
  - prognostic-biomarker
  - chinese-cohort
  - retrospective
processed_by: crosslinker
processed_at: 2026-05-16
---

# Hunan CRC Tissue Microarray Cohort (CASS)

## Overview

The coadread_cass_2020 cohort is an 80-patient tissue microarray from Hunan Cancer Hospital (AiFang Biological AF-CocSur2201), collected January 2018 – October 2018 with 5-year follow-up to October 2023. The cohort was used to validate [CGREF1](../genes/CGREF1.md) protein expression as a prognostic biomarker in colorectal cancer ([COADREAD](../cancer_types/COADREAD.md)). All patients underwent colectomy without neoadjuvant therapy, and MMR status was assessed by IHC. Note: the paper's bioinformatic analyses also drew on [TCGA CRC data](../datasets/coadread_tcga.md) via TIMER 2.0 and GEPIA2; the tissue microarray itself was an independent in-house cohort. [PMID:32888432](../papers/32888432.md)

## Composition

- **n = 80** CRC tissues with paired adjacent normal intestinal epithelial tissues.
- 44 male / 36 female; median age 61 (range 31–81).
- 49 right-colon, 31 left-colon primaries.
- All underwent colectomy without neoadjuvant therapy; MMR status assessed by [IHC](../methods/immunohistochemistry.md).
- Orthogonal validation cohort: 19 paired primary tumor and adjacent normal specimens for qRT-PCR.
- Reference genome GRCh37 (via TCGA GEPIA2 analysis layer). [PMID:32888432](../papers/32888432.md)

## Assays / panels (linked)

- [Immunohistochemistry](../methods/immunohistochemistry.md) — [CGREF1](../genes/CGREF1.md) protein quantified by immunoreactivity score (IRS = staining intensity × proportion, 0–12 scale); MMR status.
- [Quantitative RT-PCR](../methods/quantitative-rt-pcr.md) — CGREF1 mRNA normalized to GAPDH in 19 paired validation specimens.

## Papers using this cohort

- [PMID:32888432](../papers/32888432.md) — Liu et al. (2025): CGREF1 is over-expressed in 61.25% of CRC tissues by IHC; high CGREF1 expression is an independent predictor of shorter disease-free survival (HR 3.85, p=0.014) on multivariate Cox analysis.

## Notable findings derived from this cohort

- CGREF1 was over-expressed (IRS ≥ 4) in 49/80 (61.25%) of CRC tissues vs. 0/80 normal colorectal tissues (p=0.00001). [PMID:32888432](../papers/32888432.md)
- High CGREF1 expression correlated with advanced stage III–IV (p=0.006), lymph node-positive disease (p=0.007), venous invasion (p=0.043), and high-grade tumor budding Bd3 (p=0.017). [PMID:32888432](../papers/32888432.md)
- On multivariate Cox analysis, CGREF1 expression (HR 3.85, 95% CI 1.32–11.2, p=0.014) and venous invasion were the only independent predictors of disease-free survival. [PMID:32888432](../papers/32888432.md)
- CGREF1 expression was particularly elevated in regions of high-grade tumor budding (Bd3) at the invasive front. [PMID:32888432](../papers/32888432.md)

## Sources

- cBioPortal study `coadread_cass_2020`.
- Liu et al. (2025) *Journal of Cancer Research and Clinical Oncology* [PMID:32888432](../papers/32888432.md).

*This page was processed by **crosslinker** on **2026-05-16**.*
