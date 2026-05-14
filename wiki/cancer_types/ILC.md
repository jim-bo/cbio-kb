---
name: Breast Invasive Lobular Carcinoma
oncotree_code: ILC
main_type: Breast Cancer
parent: BRCA
tags:
  - breast
  - invasive
  - lobular
  - e-cadherin-loss
  - pi3k-akt
processed_by: crosslinker
processed_at: 2026-05-14
---

# Breast Invasive Lobular Carcinoma (ILC)

## Overview

Breast Invasive Lobular Carcinoma (ILC) is the second most common histologic subtype of invasive breast cancer (~10–15% of cases), defined by loss of E-cadherin ([CDH1](../genes/CDH1.md)) function and characteristic single-file infiltration of the stroma. It sits at OncoTree level 3 under [BRCA](../cancer_types/BRCA.md). ILC is predominantly Luminal A (83% of ILC vs 41% of [IDC](../cancer_types/IDC.md)), ER-positive (94%), and has the highest pAKT activity of any breast cancer subtype. Its diffuse metastatic pattern (GI tract, peritoneum) and poor detection on PET distinguish it clinically from [IDC](../cancer_types/IDC.md).

## Cohorts in the corpus

- [brca_tcga_pub2015](../datasets/brca_tcga_pub2015.md) — 127 ILC samples profiled by whole-exome sequencing, RNA-seq, miRNA-seq, copy number (SNP6), DNA methylation, and RPPA (633 samples); the primary ILC discovery cohort [PMID:26451490](../papers/26451490.md).
- [brca_metabric](../datasets/brca_metabric.md) — validation cohort (median follow-up 7.2 years) used for ILC transcriptional subtype survival analyses [PMID:26451490](../papers/26451490.md).

## Recurrent alterations

- [CDH1](../genes/CDH1.md) mutation: 63% of ILC vs 2% of [IDC](../cancer_types/IDC.md) (q=3.94E-53); 83% truncating; biallelic loss (mutation + 16q heterozygous loss) in 95% of ILC; no promoter hypermethylation detected [PMID:26451490](../papers/26451490.md).
- [PIK3CA](../genes/PIK3CA.md) mutation: 48% of ILC vs 33% of IDC (q=0.02); not associated with pAKT levels in this dataset [PMID:26451490](../papers/26451490.md).
- [PTEN](../genes/PTEN.md) inactivation (homozygous deletion + mutation): 14% in Luminal A ILC vs 3% in Luminal A IDC (p=9E-4); mutually exclusive with [PIK3CA](../genes/PIK3CA.md) [PMID:26451490](../papers/26451490.md).
- [FOXA1](../genes/FOXA1.md) mutation: 7% of ILC (vs 2% IDC, q=0.08); all ILC mutations cluster in the fork-head W2 wing loop (I176, D226 hotspot residues); associated with increased [FOXA1](../genes/FOXA1.md) mRNA, suggesting gain-of-function [PMID:26451490](../papers/26451490.md).
- [TBX3](../genes/TBX3.md) mutation: 9% of ILC vs 2% of IDC (q=0.003) [PMID:26451490](../papers/26451490.md).
- [RUNX1](../genes/RUNX1.md) mutation: 10% of ILC vs 3% of IDC (q=0.008) [PMID:26451490](../papers/26451490.md).
- [TP53](../genes/TP53.md) mutation: ILC-depleted (8% ILC vs 44% IDC, q=1.9E-14), consistent with predominantly Luminal A biology [PMID:26451490](../papers/26451490.md).
- [ERBB2](../genes/ERBB2.md) amplification and mutations identified among upstream drivers of AKT activation in ILC [PMID:26451490](../papers/26451490.md).
- pAKT-S473 and pAKT-T308 levels are highest in ILC among all breast cancer subtypes, matching levels seen in HER2+ and Basal-like IDC, despite predominantly Luminal A classification [PMID:26451490](../papers/26451490.md).

## Subtypes

- Three ILC transcriptional subtypes defined by consensus hierarchical clustering of 106 Luminal A ILC (TCGA; validated in METABRIC):
  - *Reactive-like*: high stromal/epithelial signaling (keratins, kallikreins, [EGFR](../genes/EGFR.md), [MET](../genes/MET.md), [PDGFRA](../genes/PDGFRA.md), [KIT](../genes/KIT.md)); low tumor purity; better disease-specific survival (HR=0.47, p=0.038) [PMID:26451490](../papers/26451490.md).
  - *Immune-related*: high ILs, chemokines, MHC, TNFs, [IDO1](../genes/IDO1.md), [IFNG](../genes/IFNG.md); macrophage-dominated microenvironment [PMID:26451490](../papers/26451490.md).
  - *Proliferative*: high cell-cycle and DNA-repair proteins (Cyclin E1, FoxM1, [PCNA](../genes/PCNA.md), pChk1-S345, [BRCA2](../genes/BRCA2.md)); worse disease-specific survival (HR=2.0, p=0.025) [PMID:26451490](../papers/26451490.md).
- Mixed IDC/ILC tumors (n=88) resolve into ILC-like (24/88) or IDC-like (64/88) classes; [CDH1](../genes/CDH1.md) status is the dominant discriminating feature; no third hybrid entity is supported [PMID:26451490](../papers/26451490.md).
- ILC is predominantly Luminal A (83%) and ER-positive (94%, 113/120 by IHC) [PMID:26451490](../papers/26451490.md).

## Therapeutic landscape

- PI3K/AKT/mTOR inhibition is proposed as a priority strategy for ILC given the highest average pAKT levels of any breast cancer subtype and frequent [PTEN](../genes/PTEN.md) inactivation; 40% of ILC samples carry upstream AKT pathway alterations by MEMo analysis [PMID:26451490](../papers/26451490.md).
- Lower [GATA3](../genes/GATA3.md) and reduced total/phospho-ER in Luminal A ILC are consistent with prior reports of improved aromatase inhibitor ([letrozole](../drugs/letrozole.md)) vs tamoxifen response [PMID:26451490](../papers/26451490.md).
- Prognostic stratification by mRNA subtype (reactive-like vs proliferative) carries survival differences (p=0.023–0.038 in METABRIC), suggesting potential for trial stratification [PMID:26451490](../papers/26451490.md).

## Sources

- [PMID:26451490](../papers/26451490.md) — Ciriello et al., *Comprehensive molecular portraits of invasive lobular breast cancer*, Cell 2015.

*This page was processed by **crosslinker** on **2026-05-14**.*
