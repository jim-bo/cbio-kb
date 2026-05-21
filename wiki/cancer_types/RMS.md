---
name: Rhabdomyosarcoma
oncotree_code: RMS
main_type: Soft Tissue Sarcoma
parent: SOFT_TISSUE
tags: [sarcoma, pediatric, rhabdomyosarcoma]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Rhabdomyosarcoma (RMS)

## Overview

Rhabdomyosarcoma is a Soft Tissue Sarcoma (parent SOFT_TISSUE). Subtypes include alveolar ([ARMS](./ARMS.md)), embryonal ([ERMS](./ERMS.md)), and spindle cell/sclerosing ([SCRMS](./SCRMS.md)) variants.

## Cohorts in the corpus

- [rms_msk_2023](../datasets/rms_msk_2023.md): 61 patients with extremity RMS treated at MSKCC January 2000–December 2021; median age 8; ~two-thirds lower extremity. MSK-IMPACT targeted DNA sequencing (410–505 genes) in 40% of patients [PMID:37315267](../papers/37315267.md).
- 35 paired primary/relapse RMS samples (18 FP-RMS / [ARMS](../cancer_types/ARMS.md), 17 FN-RMS / [ERMS](../cancer_types/ERMS.md)) from MSKCC (n=20) and Institut Curie (n=15); 5-year [OS](../cancer_types/OS.md) 33%; 10 patients with longitudinal ctDNA analysis from 62 plasma samples [PMID:37730754](../papers/37730754.md).

## Recurrent alterations

- 85% [FOXO1](../genes/FOXO1.md) fusion–positive [ARMS](../cancer_types/ARMS.md), 7 fusion-negative [ERMS](../cancer_types/ERMS.md), 2 [MYOD1](../genes/MYOD1.md)-mutant spindle cell/sclerosing RMS [PMID:37315267](../papers/37315267.md).
- 70% of [ARMS](../cancer_types/ARMS.md) carried [PAX3](../genes/PAX3.md)::[FOXO1](../genes/FOXO1.md); remainder [PAX7](../genes/PAX7.md)::[FOXO1](../genes/FOXO1.md) [PMID:37315267](../papers/37315267.md).
- [MED12](../genes/MED12.md) alterations, [CDK4](../genes/CDK4.md) amplifications, [CDKN2A](../genes/CDKN2A.md) deletions each 8–17% in [ARMS](../cancer_types/ARMS.md); CDK4/CDKN2A events mutually exclusive, enriched in acral/high-risk lesions, correlated with poor [OS](../cancer_types/OS.md) (P=.02) [PMID:37315267](../papers/37315267.md).
- WGS/WES/RNA-seq of 147 rhabdomyosarcoma tumor/normal pairs showed PAX-fusion status (PFP vs PFN) outperforms ARMS/ERMS histology for molecular classification; the RTK/RAS/PIK3CA axis is altered in 93% of WGS tumors, with [NRAS](../genes/NRAS.md), [KRAS](../genes/KRAS.md), [HRAS](../genes/HRAS.md), [FGFR4](../genes/FGFR4.md), [PIK3CA](../genes/PIK3CA.md), and novel drivers [FBXW7](../genes/FBXW7.md) (7.4% of PFN) and [BCOR](../genes/BCOR.md) (7%) as recurrent targets [PMID:24436047](../papers/24436047.md).
- Germline WES of 372 pediatric cancer patients (Düsseldorf) included rhabdomyosarcoma cases; [TP53](../genes/TP53.md) LP/PV carriers presented with rhabdomyosarcoma (solid tumor subgroup, 29.6% of LP/PV carriers); [TP53](../genes/TP53.md) burden OR=32.8 (p=7.83×10⁻⁸) [PMID:29489754](../papers/29489754.md)
- PPTC RMS PDX models (n=261 total cohort): Fusion+ [ARMS](../cancer_types/ARMS.md) carried PAX3-FOXO1; Fusion− [ERMS](../cancer_types/ERMS.md) had RAS-pathway mutations ([NRAS](../genes/NRAS.md), [HRAS](../genes/HRAS.md), [KRAS](../genes/KRAS.md), [NF1](../genes/NF1.md)) in 3/6 models; [MYCN](../genes/MYCN.md) and [CDK4](../genes/CDK4.md) focal amplifications observed; [MYOD1](../genes/MYOD1.md) overexpressed in all but IRS-68; median age 16y for [ARMS](../cancer_types/ARMS.md) vs 5y for [ERMS](../cancer_types/ERMS.md) [PMID:31693904](../papers/31693904.md).
- Rhabdomyosarcoma (RMS) was enrolled in MAPPYACTS (sarcomas 37% of 787 patients); CDK4/CDK6 amplifications recurrent in RMS were matched to CDK4/6 inhibitors (105 recommendations); FGFR1/2/3/4 alterations (27 events) occurred across RMS and other sarcomas [PMID:35292802](../papers/35292802.md)
- Included in the MSK cWGTS pediatric/rare solid tumor cohort (n=114 patients, [mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md)); whole-genome + transcriptome sequencing added oncogenic findings beyond MSK-IMPACT in 54% of patients [PMID:35585047](../papers/35585047.md)

## Subtypes

- [ARMS](./ARMS.md) — FOXO1-fusion-positive alveolar RMS (85%) [PMID:37315267](../papers/37315267.md).
- [ERMS](./ERMS.md) — fusion-negative embryonal RMS (n=7) [PMID:37315267](../papers/37315267.md).
- [SCRMS](./SCRMS.md) — MYOD1-mutant spindle cell/sclerosing RMS (n=2) [PMID:37315267](../papers/37315267.md).

## Therapeutic landscape

- One-third localized, 18% regional nodal, 51% distant metastases at diagnosis [PMID:37315267](../papers/37315267.md).
- Metastatic disease (HR 2.68, P=.004), high-risk group (HR 2.78, P=.010), and age ≥10 years (HR 2.26, P=.034) significantly affected [OS](../cancer_types/OS.md) [PMID:37315267](../papers/37315267.md).
- 5-year EFS/OS: metastatic 19%/29%; nodal involvement without distant mets 43%/66% [PMID:37315267](../papers/37315267.md).
- CDK4/6-directed strategies for CDK4-amplified or CDKN2A-deleted extremity RMS are untested [PMID:37315267](../papers/37315267.md).
- Liquid biopsy (36-gene custom panel + shallow WGS) detects alterations in 88% of patients at diagnosis and 90% at relapse; ctDNA monitoring of FP-RMS is implemented in the prospective FaR-RMS trial (NCT04625907) [PMID:37730754](../papers/37730754.md).

## Sources

- [PMID:37315267](../papers/37315267.md)
- [PMID:37730754](../papers/37730754.md)

- [PMID:24436047](../papers/24436047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29489754](../papers/29489754.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31693904](../papers/31693904.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35292802](../papers/35292802.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
