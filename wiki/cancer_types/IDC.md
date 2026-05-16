---
name: Breast Invasive Ductal Carcinoma
oncotree_code: IDC
main_type: Breast Cancer
parent: BRCA
tags:
  - breast
  - invasive
  - ductal
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Breast Invasive Ductal Carcinoma (IDC)

## Overview

Breast Invasive Ductal Carcinoma (IDC) is the most common histologic subtype of invasive breast cancer, arising from the ductal epithelium of the breast. It sits at OncoTree level 3 under [BRCA](../cancer_types/BRCA.md). IDC encompasses all four intrinsic molecular subtypes (Luminal A, Luminal B, HER2-enriched, Basal-like) and is the reference comparator for understanding the distinct molecular biology of rarer breast histologies such as invasive lobular carcinoma ([ILC](../cancer_types/ILC.md)).

## Cohorts in the corpus

- [brca_tcga_pub2015](../datasets/brca_tcga_pub2015.md) — 490 IDC samples profiled by whole-exome sequencing, RNA-seq, miRNA-seq, copy number (SNP6), DNA methylation, and RPPA; constitutes the primary IDC cohort in the TCGA comprehensive breast study [PMID:26451490](../papers/26451490.md).
- [brca_metabric](../datasets/brca_metabric.md) — used as a validation cohort for transcriptional subtype survival analyses [PMID:26451490](../papers/26451490.md).
- [brca_tcga_pub](../datasets/brca_tcga_pub.md) — cited for TP53/PIK3CA co-mutation cross-species comparisons in ER+ breast cancer modeling [PMID:26437033](../papers/26437033.md).

## Recurrent alterations

- [TP53](../genes/TP53.md) mutation: 44% of IDC vs 8% of [ILC](../cancer_types/ILC.md) (q=1.9E-14); IDC-enriched, reflecting high Basal-like and HER2-enriched representation [PMID:26451490](../papers/26451490.md).
- [PIK3CA](../genes/PIK3CA.md) mutation: 33% of IDC vs 48% of [ILC](../cancer_types/ILC.md); less frequent in IDC than ILC but present across all subtypes [PMID:26451490](../papers/26451490.md).
- [GATA3](../genes/GATA3.md) mutation: IDC-enriched in Luminal A comparison (20% LumA IDC vs 5% LumA ILC, q=0.003) [PMID:26451490](../papers/26451490.md).
- [MYC](../genes/MYC.md) focal amplification: IDC-enriched (27% IDC vs 6% ILC, q=7.42E-7) [PMID:26451490](../papers/26451490.md).
- [CCNE1](../genes/CCNE1.md) focal amplification: IDC-enriched (7% IDC vs 0% ILC, q=0.01) [PMID:26451490](../papers/26451490.md).
- [CDH1](../genes/CDH1.md) mutation: 2% of IDC vs 63% of ILC (q=3.94E-53); E-cadherin loss is the defining molecular feature distinguishing ILC from IDC [PMID:26451490](../papers/26451490.md).
- Invasive ductal carcinoma histology was produced in rat models by combined [NF1](../genes/NF1.md)+[TP53](../genes/TP53.md) Indel editing (uniformly invasive, moderately differentiated) and PIK3CA-H1047R+[TP53](../genes/TP53.md) Indel editing (invasive with papillary features) [PMID:26437033](../papers/26437033.md).
- WES of 216 metastatic breast carcinomas (SAFIR01/SAFIR02/SHIVA/MOSCATO trials) encompassing predominantly IDC tumors: ESR1, RB1, PALB2, TSC1/TSC2, and APOBEC enrichments characterize the metastatic vs primary mutation landscape; all ESR1-mutant patients had received prior endocrine therapy [PMID:28027327](../papers/28027327.md)
- IDC comprised 92.0% of Korean SMC breast tumors vs 74.4% of TCGA BRCA (p<0.001); SMC IDC showed higher TP53 (47.9%) and ERBB2 (20%) somatic alteration rates and greater HRD-signature (S3) enrichment in TNBC (85% HRD-positive) [PMID:29713003](../papers/29713003.md)

## Subtypes

- Intrinsic subtypes (PAM50) in IDC: Luminal A 41%, with higher proportions of Luminal B, HER2-enriched, and Basal-like compared with ILC; IDC spans the full molecular spectrum [PMID:26451490](../papers/26451490.md).
- Mixed IDC/ILC cases (n=88) molecularly resolve into IDC-like (64/88) or ILC-like (24/88) by majority vote of three classifiers; [CDH1](../genes/CDH1.md) status is the dominant discriminating feature [PMID:26451490](../papers/26451490.md).

## Therapeutic landscape

- [PIK3CA](../genes/PIK3CA.md)+TP53 co-mutated IDC tumors show transcriptional concordance with rat Pik3caH1047R/Tp53Indel models (Fisher's exact p<1×10^-14 for overlapping up-regulated genes), supporting cross-species translational relevance for endocrine and combination therapy studies [PMID:26437033](../papers/26437033.md).
- AKT pathway activity in IDC is subtype-dependent; LumA IDC has substantially lower pAKT than ILC, HER2-enriched, or Basal-like IDC [PMID:26451490](../papers/26451490.md).

## Sources

- [PMID:26451490](../papers/26451490.md) — Ciriello et al., *Comprehensive molecular portraits of invasive lobular breast cancer*, Cell 2015.
- [PMID:26437033](../papers/26437033.md) — Bu et al., *Rat somatic genome editing enables ER+ breast cancer modeling*, bioRxiv 2025.

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:28027327](../papers/28027327.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:29713003](../papers/29713003.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
