---
name: Breast Cancer PI3K Inhibitor Trial (MSK, 2019)
studyId: brca_mskcc_2019
institution: Memorial Sloan Kettering Cancer Center
size: 33
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-ngs
panels:
  - msk-impact-panel
tags:
  - breast-cancer
  - pi3k-inhibitor
  - phase-ib
  - biomarker
  - er-positive
processed_by: crosslinker
processed_at: 2026-05-21
---

# Breast Cancer PI3K Inhibitor Trial (MSK, 2019)

## Overview

A correlative molecular dataset from a phase Ib trial combining the pan-PI3K inhibitor [buparlisib](../drugs/buparlisib.md) with [letrozole](../drugs/letrozole.md) in ER+/HER2- metastatic [breast cancer (BRCA)](../cancer_types/BRCA.md) at Memorial Sloan Kettering Cancer Center. Pre-study biopsies or archival FFPE tissue from 33 patients were profiled by 341-gene targeted NGS ([MSK-IMPACT](../methods/msk-impact-panel.md) [IMPACT341](../methods/IMPACT341.md)) and a custom NanoString [PAM50](../methods/pam50.md) codeset. The dataset was designed to identify genomic predictors of clinical benefit (CR/PR or SD ≥6 months) to PI3K + endocrine combination therapy [PMID:31552290](../papers/31552290.md).

## Composition

- **33 patients** with ER+/HER2- metastatic breast cancer, refractory to ≥1 prior line of endocrine therapy [PMID:31552290](../papers/31552290.md).
- **Disease setting:** [BRCA](../cancer_types/BRCA.md) (metastatic, endocrine-refractory); enrollees were from a phase Ib Stand Up to Cancer protocol (Mayer et al. JCO 2014) [PMID:31552290](../papers/31552290.md).
- **14 patients** with PAM50 subtype data (NanoString codeset on FFPE tissue) [PMID:31552290](../papers/31552290.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) 341-gene targeted NGS ([IMPACT341](../methods/IMPACT341.md)) on pre-study biopsies or archival FFPE tissue [PMID:31552290](../papers/31552290.md).
- Custom NanoString [PAM50](../methods/pam50.md) codeset on FFPE tissue (14 buparlisib-trial tumors) [PMID:31552290](../papers/31552290.md).

## Papers using this cohort

- [PMID:31552290](../papers/31552290.md) — Correlative molecular analysis of a phase Ib [buparlisib](../drugs/buparlisib.md) + [letrozole](../drugs/letrozole.md) trial; defines [PIK3CA](../genes/PIK3CA.md) + [MAP3K1](../genes/MAP3K1.md) co-mutation and luminal A PAM50 subtype as candidate predictive biomarkers for PI3K-inhibitor benefit in ER+/HER2- metastatic breast cancer.

## Notable findings derived from this cohort

- [PIK3CA](../genes/PIK3CA.md) activating mutations and [MAP3K1](../genes/MAP3K1.md) loss-of-function mutations independently mark patients with clinical benefit; co-alteration confers the highest clinical benefit rate (5/7 = 71% CBR) vs. 11% in double-wild-type [PMID:31552290](../papers/31552290.md).
- [MAP3K1](../genes/MAP3K1.md) alteration significantly improved progression-free survival (p=0.03, log-rank); [PIK3CA](../genes/PIK3CA.md) alteration also improved PFS (p=0.009, log-rank) [PMID:31552290](../papers/31552290.md).
- PAM50 analysis showed all 14 profiled tumors classified as luminal A or B; combined data from 14 buparlisib-trial and 12 alpelisib-trial tumors showed a trend toward luminal A enrichment among clinical benefiters (p=0.07, one-tailed Fisher's exact) [PMID:31552290](../papers/31552290.md).
- [MAP3K1](../genes/MAP3K1.md) mutations are interpreted as a surrogate marker for luminal A subtype rather than a direct PI3K-sensitivity driver, since shRNA/siRNA knockdown of [MAP3K1](../genes/MAP3K1.md) did not sensitize ER+ breast cancer cell lines to [buparlisib](../drugs/buparlisib.md) in vitro [PMID:31552290](../papers/31552290.md).
- Analyzed 1,756 tumors (1,261 metastatic) for [PIK3R1](../genes/PIK3R1.md) domain-clustering comparison; [PIK3R1](../genes/PIK3R1.md) alterations (2.3% of metastatic) were mutually exclusive with [PIK3CA](../genes/PIK3CA.md) mutations (p<0.001) and associated with shorter [OS](../cancer_types/OS.md) than PIK3CA-altered cases (HR 2.82, p<0.001) [PMID:35670774](../papers/35670774.md)

## Sources

- cBioPortal study: `brca_mskcc_2019`
- Primary publication: [PMID:31552290](../papers/31552290.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35670774](../papers/35670774.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
