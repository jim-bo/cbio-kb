---
name: MSKCC Prostate Cancer CNA Burden Cohort (2014)
studyId: prad_mskcc_2014
institution: Memorial Sloan Kettering Cancer Center
size: 104
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - COPY_NUMBER_ALTERATION
panels: []
tags:
  - prostate-cancer
  - copy-number
  - cna-burden
  - prad
  - array-cgh
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# MSKCC Prostate Cancer CNA Burden Cohort (2014)

## Overview

Contemporary cohort of 104 radical prostatectomy cases with matched normals, profiled at Memorial Sloan Kettering Cancer Center by high-resolution array comparative genomic hybridization (Agilent 1M-feature array-CGH). Assembled by Hieronymus et al. (2014) to validate CNA burden as a prognostic biomarker for biochemical recurrence (BCR) in primary prostate cancer, complementing the earlier 168-case [`prad_mskcc`](prad_mskcc.md) cohort (Taylor et al. 2010). Raw data deposited at GEO (GSE54691) and the MSKCC Prostate Cancer Genomics Data Portal.

## Composition

- Cancer type: primary prostate adenocarcinoma ([PRAD](../cancer_types/PRAD.md))
- 104 prostatectomy cases + matched germline normals; snap-frozen samples with >70% tumor content
- Median follow-up 6 years; BCR events n=24 (53 per 1,000 person-years); metastatic events n=3
- Key clinical variables: pretreatment PSA, biopsy and pathology Gleason score, postoperative Stephenson 5-year nomogram

## Assays / panels (linked)

- [array-cgh-agilent-1m](../methods/array-cgh-agilent-1m.md): Agilent 1M-feature array-CGH on snap-frozen tissue with Promega pooled-reference DNA; aligned to hg19
- Feasibility sub-study: 4 FFPE needle biopsies profiled by [agilent-244k](../methods/agilent-244k.md) and low-pass [whole-genome-seq](../methods/whole-genome-seq.md) (1–3× via Illumina HiSeq 2000, 100 bp paired-end, BWA alignment, hg19)

## Papers using this cohort

- [PMID:25024180](../papers/25024180.md) — Hieronymus et al. 2014, "Copy number alteration burden predicts prostate cancer relapse"

## Notable findings derived from this cohort

- CNA burden (fraction of autosomal genome with copy-number change) is associated with BCR: HR 1.05 per 1% CNA (95% CI 1.01–1.09, P=0.008); stratified at the 5.41% threshold, HR for BCR is 3.85 (P=0.001) [PMID:25024180](../papers/25024180.md)
- CNA burden remains prognostic for BCR after adjustment for pretreatment PSA, biopsy Gleason score, pathology Gleason score, and the postoperative Stephenson 5-year nomogram (HR 1.05, P=0.011) [PMID:25024180](../papers/25024180.md)
- In the Gleason 7 intermediate-risk subgroup, CNA burden ranges 0.003–50%; univariate HR for BCR is 1.06 (P=0.017), persisting after PSA and Stephenson adjustment [PMID:25024180](../papers/25024180.md)
- Low-pass WGS (1–3×) of FFPE needle biopsies yielded CNA profiles concordant with high-resolution array-CGH, including focal 3p13 deletions and arm-level gains/losses [PMID:25024180](../papers/25024180.md)

## Sources

- GEO: GSE54691
- cBioPortal studyId: prad_mskcc_2014

*This page was processed by **entity-page-writer** on **2026-05-11**.*
