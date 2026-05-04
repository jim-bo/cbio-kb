---
name: Hepatocellular Carcinoma
oncotree_code: HCC
main_type: Hepatobiliary Cancer
parent: LIVER
tags: [liver, hepatobiliary]
processed_by: crosslinker
processed_at: 2026-05-03
---

# Hepatocellular Carcinoma (HCC)

## Overview

Primary liver cancer of hepatocellular origin.

## Cohorts in the corpus

- [hcc_msk_2024](../datasets/hcc_msk_2024.md) — HCC cases used as a training reference class for the hidden-genome classifier of intrahepatic cholangiocarcinoma, within a 1,370-patient MSK biliary/HCC MSK-IMPACT cohort (2003–2022) [PMID:38864854](../papers/38864854.md).

## Recurrent alterations

- HCC reference class characterized by [TERT](../genes/TERT.md) alterations; "HCC-class" [IHCH](IHCH.md) (IHC tumors with >90% HCC homology, 5.7%) likewise exhibit [TERT](../genes/TERT.md) alterations [PMID:38864854](../papers/38864854.md).
- Multi-omics of 256 HCC samples (CNV + DNA methylation + gene expression) identified five molecular subgroups with distinct survival rates; this integrative analysis was cited as a paradigm for multi-omics cancer subtyping. [PMID:37119971](../papers/37119971.md)
- Six lipid-metabolic axes are reprogrammed in HCC: enhanced lipid uptake ([CD36](../genes/CD36.md), FATPs, FABPs), de novo lipogenesis ([FASN](../genes/FASN.md), [SCD](../genes/SCD.md), [ACACA](../genes/ACACA.md)), fatty acid oxidation ([CPT1A](../genes/CPT1A.md), [PPARA](../genes/PPARA.md)), suppression of ferroptosis ([SLC7A11](../genes/SLC7A11.md), [GPX4](../genes/GPX4.md)), bioactive lipid synthesis (PGE2, LPA), and cholesterol biosynthesis ([HMGCR](../genes/HMGCR.md), [SQLE](../genes/SQLE.md)). [PMID:38355797](../papers/38355797.md)
- [CD36](../genes/CD36.md) upregulated in HCC; drives Src/AKT/mTOR and YAP signaling, promotes metastasis, and is implicated in radiotherapy resistance. [PMID:38355797](../papers/38355797.md)
- [SLC27A4](../genes/SLC27A4.md) (FATP4) upregulated in HCC; selectively imports MUFAs to protect against ferroptosis and confers [sorafenib](../drugs/sorafenib.md) resistance. [PMID:38355797](../papers/38355797.md)
- Wnt/β-catenin ([APC](../genes/APC.md) loss or [CTNNB1](../genes/CTNNB1.md) mutation)-driven HCC is addicted to FAO via PPARα/CPT1 activation. [PMID:38355797](../papers/38355797.md)
- [ACLY](../genes/ACLY.md)-driven DNL suppresses cGAS-STING pathway to decrease PD-L1 expression and promote resistance to anti-PD-L1 therapy. [PMID:38355797](../papers/38355797.md)
- cfDNA profiling via [MSK-ACCESS](../methods/ACCESS129.md) (129-gene panel) detects alterations in 92.2% of advanced HCC patients (N=51); most frequently mutated genes: [TERT](../genes/TERT.md) promoter 57%, [TP53](../genes/TP53.md) 47%, [CTNNB1](../genes/CTNNB1.md) 37%, [ARID1A](../genes/ARID1A.md) 18%, [TSC2](../genes/TSC2.md) 14% [PMID:37769223](../papers/37769223.md).
- Plasma-tissue concordance 92.5% in matched samples; 27% of paired samples harbored cfDNA-exclusive alterations, of which 40% were OncoKB actionable [PMID:37769223](../papers/37769223.md).
- WNT-beta-catenin pathway altered in 45% and PI3K-AKT-mTOR pathway in 25% of HCC cfDNA cases; actionable [TSC1](../genes/TSC1.md)/[TSC2](../genes/TSC2.md) alterations in 18% [PMID:37769223](../papers/37769223.md).

## Subtypes

- Five molecular subgroups identified by CNV + methylation + expression multi-omics in 256 HCC samples, each with distinct survival rates (Liu et al., as reviewed by Babu & Snyder). [PMID:37119971](../papers/37119971.md)
- MAFLD-related HCC (≥49% of all HCC): epidemiology — MAFLD affects >25% of adults worldwide; MAFLD as the sole underlying liver disease in ~12% of HCC patients. ICI responsiveness may differ from viral HCC but evidence is inconsistent. [PMID:38355797](../papers/38355797.md)

## Therapeutic landscape

- HCC-class IHC has markedly better [OS](../cancer_types/OS.md) than biliary-class IHC, independent of FGFR2/IDH1 alterations [PMID:38864854](../papers/38864854.md).
- Standard-of-care response rates in HCC: [atezolizumab](../drugs/atezolizumab.md) + [bevacizumab](../drugs/bevacizumab.md) 26%–28%, [lenvatinib](../drugs/lenvatinib.md) 16%–23% (median PFS < 12 months); objective response rate for subsequent TKIs/ICIs after progression on atezolizumab + bevacizumab is ~7%. [PMID:38355797](../papers/38355797.md)
- Anti-CD36 antibody PLT012 suppressed HCC progression preclinically, recruited cytotoxic CD8 T cells, suppressed [FOXP3](../genes/FOXP3.md)+ Tregs, and sensitized HCC to ICIs. [PMID:38355797](../papers/38355797.md)
- Targeting lipid metabolism ([CD36](../genes/CD36.md), FATP4, FABP1/5, [FASN](../genes/FASN.md), [SCD](../genes/SCD.md), CPT1, [ACLY](../genes/ACLY.md), [HMGCR](../genes/HMGCR.md)) proposed as a strategy to resensitize HCC to TKIs ([sorafenib](../drugs/sorafenib.md), [lenvatinib](../drugs/lenvatinib.md), [regorafenib](../drugs/regorafenib.md)) and ICIs ([atezolizumab](../drugs/atezolizumab.md), [nivolumab](../drugs/nivolumab.md), [pembrolizumab](../drugs/pembrolizumab.md)). [PMID:38355797](../papers/38355797.md)
- Multi-omics subtyping (CNV + methylation + expression) of HCC cited as a paradigm enabling therapy stratification based on molecular subgroup. [PMID:37119971](../papers/37119971.md)

## Sources

- [PMID:37769223](../papers/37769223.md)
- [PMID:38864854](../papers/38864854.md)
- [PMID:38355797](../papers/38355797.md) — lipid metabolism and therapy resistance in HCC (review, 2024).
- [PMID:37119971](../papers/37119971.md) — Babu & Snyder, multi-omics precision health review; HCC multi-omics subtyping cited (2023).

*This page was processed by **crosslinker** on **2026-05-03**.*
