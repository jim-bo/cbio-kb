---
name: MSK Early-Onset Colorectal Cancer (JCO 2021)
studyId: crc_eo_2020
institution: Memorial Sloan Kettering Cancer Center
size: 1446
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels:
  - IMPACT341
  - IMPACT468
tags:
  - colorectal
  - CRC
  - early-onset
  - germline
  - MSK-IMPACT
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# MSK Early-Onset Colorectal Cancer (JCO 2021)

## Overview

The largest single-institution study comparing early-onset colorectal cancer (EO-CRC, age <50) with average-onset CRC (AO-CRC, age ≥50) at Memorial Sloan Kettering Cancer Center. The cohort includes 759 EO-CRC patients (151 aged ≤35; 608 aged 36–49) diagnosed between January 2014 and June 2019, and 687 AO-CRC patients as a comparator. Tumors were profiled with [MSK-IMPACT](../methods/msk-impact-panel.md) for somatic alterations, and blood-derived DNA was analyzed using a 76- or 88-gene germline panel. Published in JCO 2021; available on cBioPortal as `crc_eo_2020`. [PMID:34405229](../papers/34405229.md)

## Composition

- **EO-CRC:** 759 patients aged <50 (≤35: n=151; 36–49: n=608); **AO-CRC comparator:** 687 patients aged ≥50.
- Total N = 1,446 patients with clinical and genomic data.
- Tumor types: colon adenocarcinoma ([COAD](../cancer_types/COAD.md)) and rectal adenocarcinoma ([READ](../cancer_types/READ.md)).
- EO-CRC is predominantly left-sided (>80%) and rectal (33.7% rectal in ≤35 and 36–49 cohorts vs 22.6% AO).
- Somatic profiling on formalin-fixed paraffin-embedded tumor with matched normal blood by MSK-IMPACT 341- to 468-gene panels. Germline profiling on blood DNA using a 76-gene (n=351) or 88-gene (n=730) MSK-IMPACT germline panel including all ACMG cancer-predisposition genes.
- Exclusions for somatic/clinical comparison: known CRC predisposition syndromes, inflammatory bowel disease, and MMR-deficient tumors; these patients were retained in germline analysis. [PMID:34405229](../papers/34405229.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) (341–468-gene panels) — somatic mutations, small indels, CNAs, MSI, TMB.
- MSK-IMPACT germline panel (76- or 88-gene) — pathogenic/likely pathogenic germline variant detection.
- [OncoKB](../methods/oncokb-annotation.md) — oncogenic variant annotation and filtering.
- [Kaplan-Meier](../methods/kaplan-meier.md), [Cox proportional hazards](../methods/cox-proportional-hazards.md) — survival analyses.

## Papers using this cohort

- [PMID:34405229](../papers/34405229.md) — Cercek et al. compared somatic alteration frequencies, chemotherapy response, and overall survival in metastatic MSS EO-CRC vs AO-CRC; found no statistically significant differences after adjusting for tumor sidedness. Germline P/LP variant prevalence was 23.3% in patients aged ≤35 vs 14.1% in AO (p=0.01). [PMID:34405229](../papers/34405229.md)

## Notable findings derived from this cohort

- After adjusting for tumor sidedness, no statistically significant somatic gene-level or pathway-level differences remained between any EO-CRC and AO-CRC cohorts. Initial enrichment of [TP53](../genes/TP53.md) in 36–49 vs AO and lower RTK-RAS pathway frequency were explained by the left-sided predominance of EO-CRC. [PMID:34405229](../papers/34405229.md)
- Genome-wide measures (TMB, fraction of genome altered, WGD, LOH) did not differ between age cohorts. [PMID:34405229](../papers/34405229.md)
- Most common somatic alterations in EO-CRC MSS tumors: [APC](../genes/APC.md) 78.7%, [TP53](../genes/TP53.md) 82.1%, [KRAS](../genes/KRAS.md) 42.5%, [SMAD4](../genes/SMAD4.md) 15.5%, [PIK3CA](../genes/PIK3CA.md) 14.9%. [PMID:34405229](../papers/34405229.md)
- First-line chemotherapy response (radiographic response ~66–72%) and median overall survival (~47–56 months) in metastatic MSS disease did not differ across age cohorts. [PMID:34405229](../papers/34405229.md)
- Germline P/LP variant prevalence highest in patients aged ≤35 (23.3%) vs AO (14.1%, p=0.01); high-penetrance genes (12.1% vs 5.9%, p=0.02) dominated by Lynch syndrome MMR genes (n=9), [APC](../genes/APC.md) (n=3), and [POLD1](../genes/POLD1.md) (n=1). [PMID:34405229](../papers/34405229.md)
- Biallelic inactivation rate of germline P/LP variants was 51.7% in the ≤35 cohort vs 32.6% in AO (p=0.04), supporting these germline events as bona fide carcinogenic drivers in very early-onset disease. [PMID:34405229](../papers/34405229.md)

## Sources

- cBioPortal study: `crc_eo_2020` (canonical, verified).
- Primary publication: [PMID:34405229](../papers/34405229.md).

*This page was processed by **entity-page-writer** on **2026-05-16**.*
