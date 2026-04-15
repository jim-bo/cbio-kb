---
name: ctDNA and Venous Thromboembolism (MSK, 2024)
studyId: msk_ctdna_vte_2024
institution: Memorial Sloan Kettering Cancer Center
size: 5567
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [ctdna]
panels: []
tags:
  - ctdna
  - venous-thromboembolism
  - vte
  - msk-access
  - liquid-biopsy
  - pan-cancer
processed_by: crosslinker
processed_at: 2026-04-11
---

# ctDNA and Venous Thromboembolism (MSK, 2024)

## Overview

Pan-cancer liquid biopsy cohort from Memorial Sloan Kettering Cancer Center used to develop and validate a ctDNA-based prediction model for cancer-associated venous thromboembolism (VTE). Includes a discovery cohort (n=4,141) and a prospective validation cohort (n=1,426), all sequenced with [MSK-ACCESS](../methods/ACCESS129.md). A companion international generalizability cohort for [NSCLC](../cancer_types/NSCLC.md) is available as [nsclc_ctdx_msk_2022](../datasets/nsclc_ctdx_msk_2022.md). [PMID:39147831](../papers/39147831.md)

## Composition

- **Discovery cohort**: 4,141 patients with any cancer type, plasma sequenced with [MSK-ACCESS](../methods/ACCESS129.md) (129 genes) at MSK (June 2019–September 2022). 61% ctDNA-positive; 11% developed VTE after plasma draw. [PMID:39147831](../papers/39147831.md)
- **Prospective validation cohort**: 1,426 patients with any cancer type (September 2022–September 2023). [PMID:39147831](../papers/39147831.md)
- Cancer type breakdown (discovery): [NSCLC](../cancer_types/NSCLC.md) 34%, breast 13%, pancreatic 10%, melanoma 7%, prostate 5%, bladder 5%, plus 53 other cancer types. [PMID:39147831](../papers/39147831.md)

## Assays / panels (linked)

- [MSK-ACCESS](../methods/ACCESS129.md) 129-gene plasma panel. [PMID:39147831](../papers/39147831.md)

## Papers using this cohort

- [PMID:39147831](../papers/39147831.md) — DNA liquid biopsy-based prediction of cancer-associated venous thromboembolism.

## Notable findings derived from this cohort

- ctDNA detection associated with higher VTE rates (HR=2.49, 95% CI: 1.99–3.11, P<0.001). Dose-dependent relationship: highest VAF quartile had greatest VTE risk. [PMID:39147831](../papers/39147831.md)
- In multivariate analysis, ctDNA detection (HR=1.66), cfDNA concentration (HR=1.61), Khorana score, number of disease organ sites, and chemotherapy receipt were all independently associated with VTE. [PMID:39147831](../papers/39147831.md)
- ctDNA-VTE association held across most cancer types with notable exceptions of bladder, hepatobiliary, and colorectal cancers. [PMID:39147831](../papers/39147831.md)
- ctDNA detection remained significant for VTE prediction even after controlling for tissue-confirmed gene-level alterations including [KRAS](../genes/KRAS.md), [STK11](../genes/STK11.md), and [KEAP1](../genes/KEAP1.md). [PMID:39147831](../papers/39147831.md)

## Sources

- cBioPortal study `msk_ctdna_vte_2024` [PMID:39147831](../papers/39147831.md).

*This page was processed by **crosslinker** on **2026-04-11**.*
