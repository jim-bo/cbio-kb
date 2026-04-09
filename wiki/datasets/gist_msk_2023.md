---
name: "Gastrointestinal Stromal Tumor Genomic Risk Stratification, MSK, Clin Cancer Res 2023"
slug: gist_msk_2023
institution: Memorial Sloan Kettering Cancer Center
size: 501 patients (592 samples)
assays:
  - msk-impact-panel
tags:
  - GIST
  - risk-stratification
  - adjuvant-therapy
processed_by: entity-page-writer
processed_at: 2026-04-08
---

# Gastrointestinal Stromal Tumor Genomic Risk Stratification, MSK, Clin Cancer Res 2023

## Overview

MSKCC cohort of 501 [GIST](../cancer_types/GIST.md) patients (592 samples) diagnosed 1991–2021 profiled by MSK-IMPACT targeted sequencing. Used to build an elastic-net penalized Cox machine learning model producing a 3-tier genomic risk stratification for recurrence-free survival in primary localized gastric and small bowel GISTs in the adjuvant [imatinib](../drugs/imatinib.md) era [PMID:37477937](../papers/37477937.md).

## Composition

- 501 patients / 592 samples: 275 gastric (307 samples), 194 small bowel (244 samples), 32 rectal (41 samples; excluded from modeling) [PMID:37477937](../papers/37477937.md).
- Modeling cohort: 152 primary localized gastric and 80 small bowel GISTs; 41% of gastric and 53% of small bowel received adjuvant imatinib [PMID:37477937](../papers/37477937.md).
- Cancer type: [GIST](../cancer_types/GIST.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — targeted DNA NGS, 341–505 genes, matched tumor-normal [PMID:37477937](../papers/37477937.md).

## Papers using this cohort

- [PMID:37477937](../papers/37477937.md) — Dermawan et al., Novel Genomic Risk Stratification Model for Primary GIST in the Adjuvant Therapy Era, Clin Cancer Res 2023.

## Notable findings derived from this cohort

- Gastric GIST high-risk markers: chr1p deletion or [SDHB](../genes/SDHB.md) loss; intermediate: chr14q deletion or absence of [KIT](../genes/KIT.md) exon 11 mutation [PMID:37477937](../papers/37477937.md).
- Small bowel GIST high-risk markers: [MAX](../genes/MAX.md)/[MGA](../genes/MGA.md)/[MYC](../genes/MYC.md), [CDKN2A](../genes/CDKN2A.md), or [RB1](../genes/RB1.md) alterations; intermediate: chr1p deletion or chr5q amplification [PMID:37477937](../papers/37477937.md).
- Genomic model both upgrades and downgrades patients vs Miettinen/NIH-Fletcher/Joensuu schemes, implying conventional models may mis-stratify adjuvant-era patients [PMID:37477937](../papers/37477937.md).
- In 26 SDH-deficient GISTs, [TP53](../genes/TP53.md) mutations or chr1q amplification portend worse RFS/DSS [PMID:37477937](../papers/37477937.md).

## Sources

- cBioPortal study `gist_msk_2023` [PMID:37477937](../papers/37477937.md).

*This page was processed by **entity-page-writer** on **2026-04-08**.*
