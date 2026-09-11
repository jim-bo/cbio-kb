---
name: Quantitative RT-PCR (qRT-PCR)
slug: quantitative-rt-pcr
kind: method
canonical_source: corpus
unverified: true
tags: [pcr, transcriptomics, gene-expression, validation]
processed_by: wiki-cli
processed_at: 2026-09-10
---

# Quantitative RT-PCR (qRT-PCR)

## Overview

Reverse-transcription quantitative PCR for measuring mRNA expression levels. Used in the corpus for biomarker validation, clinical diagnostic panel development, and confirmation of expression changes identified by microarray or RNA-seq.

## Used by

- A 13-gene qRT-PCR panel ([TERT](../genes/TERT.md), [IGF2](../genes/IGF2.md), GJB2, [TEK](../genes/TEK.md), [TIAM1](../genes/TIAM1.md), CXCL12, [TOP2A](../genes/TOP2A.md), A2M, PLG, [CDKN2A](../genes/CDKN2A.md), [PDGFRA](../genes/PDGFRA.md), [MKI67](../genes/MKI67.md), THBS1) used in [HCC](../cancer_types/HCC.md) to distinguish dysplastic cirrhotic nodules from early [HCC](../cancer_types/HCC.md); a 3-gene panel ([GPC3](../genes/GPC3.md), LYVE1, survivin/BIRC5) achieves 95% sensitivity and 94% specificity for discriminating high-grade dysplastic nodules from tumors <2 cm [PMID:25369299](../papers/25369299.md).
- Used to validate EWS::[FLI1](../genes/FLI1.md) target gene expression ([EZH2](../genes/EZH2.md), [IGF1](../genes/IGF1.md), [NGFR](../genes/NGFR.md), [PADI2](../genes/PADI2.md), [DKK2](../genes/DKK2.md), [NR0B1](../genes/NR0B1.md), [PRKCB](../genes/PRKCB.md)) in transduced heMSCs and siRNA knockdown experiments. [PMID:41136396](../papers/41136396.md)
- Used to assess [CDKN2A](../genes/CDKN2A.md) status and detect EWSR1-ETS fusion transcripts in Ewing sarcoma samples [PMID:25223734](../papers/25223734.md)
- Quantitative RT-PCR used to validate gene expression findings in adrenocortical carcinoma [PMID:26095796](../papers/26095796.md)
- Quantitative RT-PCR used to validate RNA expression results in proteogenomic analysis of ovarian cancer [PMID:40694421](../papers/40694421.md)
- RT-PCR used to validate MYBL1-NFIB and other [MYBL1](../genes/MYBL1.md) fusion transcripts, and to quantify [MYB](../genes/MYB.md) and [MYBL1](../genes/MYBL1.md) mRNA expression in all 102 salivary adenoid cystic carcinomas demonstrating mutually exclusive high expression [PMID:26631609](../papers/26631609.md).
- Quantitative RT-PCR used to validate MYB and MYB-target gene expression changes following BET bromodomain inhibitor JQ1 treatment in grade-2 and grade-3 ACC primagrafts [PMID:26829750](../papers/26829750.md)
- qRT-PCR used to quantify DUX4 and ERGalt expression in B-ALL cell lines and patient-derived xenografts in the DUX4/ERG B-ALL subtype study. [PMID:27776115](../papers/27776115.md)
- Quantitative RT-PCR used to confirm that spautin-1 reduced TRMT10A protein but not mRNA levels, establishing post-transcriptional (proteasomal) regulation [PMID:41071892](../papers/41071892.md).
- RT-qPCR used to validate RNA-seq-derived NOL10 cell-cycle signature gene set (DLGAP5, MCM4, KIF20B, DIAPH3, SUV39H1, CENPE, GINS2, HMGB3, CDC6) and to measure NOL10 and USF1 expression changes after CRISPR perturbations and knockdown experiments across DU145, 22Rv1, LNCaP, and PC3 cells [PMID:41062477](../papers/41062477.md)
- Used to confirm MAP3K1 shRNA knockdown efficiency (~70% mRNA reduction) in T47D cells before functional assessment of PI3K-inhibitor sensitization; knockdown abolished buparlisib-induced p-cJUN induction without affecting p-AKT suppression [PMID:31552290](../papers/31552290.md).
- qRT-PCR normalized to GAPDH validated CGREF1 mRNA overexpression in 15/19 (78.9%) CRC paired tumor/normal specimens; confirmed TIMER 2.0 and GEPIA2 bioinformatic findings [PMID:41125935](../papers/41125935.md)
- Validated mtDNA copy-number calls (from ExomeDepth) by D-loop/B2M qRT-PCR in a 1015-exome colorectal cancer cohort [PMID:35487942](../papers/35487942.md).
- Validated the PRADA/STAR-Fusion-detected LRPAP1-PDGFRA fusion by RT-PCR in a pediatric solid-tumor PDX study [PMID:37990009](../papers/37990009.md).
- Used TaqMan qRT-PCR (normalized to GAPDH) to validate AXIN2/CDH1 siRNA-knockdown effects in CDH1-intact invasive lobular breast carcinoma [PMID:38347189](../papers/38347189.md).

## Notes

- Appropriate for clinical deployment given low cost and FFPE compatibility; panels must be validated across platforms for cross-center use.
- The 3-gene [HCC](../cancer_types/HCC.md) panel ([GPC3](../genes/GPC3.md), LYVE1, survivin) provides a practical complement to IHC for small-nodule diagnosis [PMID:25369299](../papers/25369299.md).

## Sources
- [PMID:41136396](../papers/41136396.md)
- [PMID:25223734](../papers/25223734.md)
- [PMID:26095796](../papers/26095796.md)
- [PMID:40694421](../papers/40694421.md)
- [PMID:26631609](../papers/26631609.md)
- [PMID:26829750](../papers/26829750.md)
- [PMID:27776115](../papers/27776115.md)
- [PMID:41071892](../papers/41071892.md)
- [PMID:41062477](../papers/41062477.md)
- [PMID:31552290](../papers/31552290.md)
- [PMID:41125935](../papers/41125935.md)
- [PMID:35487942](../papers/35487942.md)
- [PMID:37990009](../papers/37990009.md)
- [PMID:38347189](../papers/38347189.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
