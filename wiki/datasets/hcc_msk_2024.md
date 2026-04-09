---
name: "Biliary Tract and Hepatocellular Carcinoma Hidden-Genome Classifier, MSK, Clin Cancer Res 2024"
slug: hcc_msk_2024
institution: Memorial Sloan Kettering Cancer Center
size: 1370 patients (527 IHC classified)
assays:
  - msk-impact-panel
tags:
  - biliary-tract-cancer
  - cholangiocarcinoma
  - classifier
  - prognosis
processed_by: entity-page-writer
processed_at: 2026-04-08
---

# Biliary Tract and Hepatocellular Carcinoma Hidden-Genome Classifier, MSK, Clin Cancer Res 2024

## Overview

MSK cohort of 1,370 patients with histologically confirmed biliary tract cancer, hepatocellular carcinoma, or biphenotypic IHC/HCC tumors sequenced 2003–2022 by MSK-IMPACT. Used to train and apply a supervised "hidden-genome" machine-learning classifier that scores each intrahepatic cholangiocarcinoma's genetic similarity to EHC/GBC versus [HCC](../cancer_types/HCC.md) reference classes [PMID:38864854](../papers/38864854.md).

## Composition

- 1,370 patients total; 527 [IHCH](../cancer_types/IHCH.md) classified against reference classes [EHCH](../cancer_types/EHCH.md), [GBC](../cancer_types/GBC.md), and [HCC](../cancer_types/HCC.md) [PMID:38864854](../papers/38864854.md).
- Sequenced on MSK-IMPACT panels 341/410/468/505; 341 genes common across versions were used [PMID:38864854](../papers/38864854.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — targeted hybrid-capture panel [PMID:38864854](../papers/38864854.md).

## Papers using this cohort

- [PMID:38864854](../papers/38864854.md) — Song et al., A Novel Approach to Quantify Heterogeneity of Intrahepatic Cholangiocarcinoma: the Hidden-Genome Classifier, Clin Cancer Res 2024.

## Notable findings derived from this cohort

- 410 IHC (78%) had >50% genetic homology with EHC/GBC; 122 (23%) exceeded >90% homology ("biliary-class"), characterized by [KRAS](../genes/KRAS.md), [SMAD4](../genes/SMAD4.md), and [CDKN2A](../genes/CDKN2A.md) loss [PMID:38864854](../papers/38864854.md).
- 117 IHC (22%) had >50% homology with HCC; 30 (5.7%) exceeded >90% ("HCC-class"), characterized by [TERT](../genes/TERT.md) alterations [PMID:38864854](../papers/38864854.md).
- Median OS (unresectable): biliary-class 1.0 y vs non-biliary-class 1.8 y; (resectable): 2.4 y vs 5.1 y [PMID:38864854](../papers/38864854.md).
- Classifier predicted OS independently of [FGFR2](../genes/FGFR2.md) and [IDH1](../genes/IDH1.md) alterations and outperformed histologic subtyping [PMID:38864854](../papers/38864854.md).

## Sources

- cBioPortal study `hcc_msk_2024` [PMID:38864854](../papers/38864854.md).

*This page was processed by **entity-page-writer** on **2026-04-08**.*
