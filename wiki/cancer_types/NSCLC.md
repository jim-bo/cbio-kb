---
name: Non-Small Cell Lung Cancer
oncotree_code: NSCLC
main_type: Non-Small Cell Lung Cancer
parent: LUNG
tags: [lung, nsclc]
processed_by: entity-page-writer
processed_at: 2026-04-08
---

# Non-Small Cell Lung Cancer (NSCLC)

## Overview

Non-Small Cell Lung Cancer (parent LUNG); encompasses histologies including [LUAD](./LUAD.md) and [LUSC](./LUSC.md).

## Cohorts in the corpus

- [bm_nsclc_mskcc_2023](../datasets/bm_nsclc_mskcc_2023.md): 233 patients with resected NSCLC brain metastasis (BM) profiled by MSK-IMPACT — 180 (77%) [LUAD](../cancer_types/LUAD.md), 23 (10%) [LUSC](../cancer_types/LUSC.md), 30 (13%) other NSCLC. Matched samples: 47 primaries, 42 extracranial metastases. Median age 67; 80% current/former smokers [PMID:37591896](../papers/37591896.md).
- [msk_chord_2024](../datasets/msk_chord_2024.md): 7,809 NSCLC patients in the MSK-CHORD clinicogenomic harmonized real-world dataset at MSK [PMID:39506116](../papers/39506116.md).

## Recurrent alterations

- TMB was higher in BM vs EM (median 8.8 vs 5.8; p=0.00766); FGA was higher in BM vs EM (p=2.77e-06) and vs PT (p=2.27e-07) [PMID:37591896](../papers/37591896.md).
- [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) alterations more frequent in BM (34%) vs PT (13%, p=0.003, q=0.04); cell-cycle pathway alterations 56% BM vs 32% PT (p=0.004, q=0.041) [PMID:37591896](../papers/37591896.md).
- Paired BM–BM samples showed high genomic concordance vs lower concordance in synchronous BM/PT pairs [PMID:37591896](../papers/37591896.md).
- [NF1](../genes/NF1.md) alterations were more frequent in LMD patients (15%) [PMID:37591896](../papers/37591896.md).
- [HLA-B](../genes/HLA-B.md) mutations appeared as private BM events [PMID:37591896](../papers/37591896.md).

## Subtypes

- Among [LUAD](../cancer_types/LUAD.md) BM patients: LMD patients had more [EGFR](../genes/EGFR.md) alterations (45% vs 21%, p=0.044); local progressors had more [RB1](../genes/RB1.md) loss (24% vs 6%, p=0.022); multifocal regional progressors had [MYC](../genes/MYC.md) amplifications in 22% vs 0% (p=0.023) [PMID:37591896](../papers/37591896.md).

## Therapeutic landscape

- Non-canonical [EGFR](../genes/EGFR.md) mutations (L861Q, G719A/S, A755G, N771_H773dup) in BM may identify patients at elevated risk for LMD and partial resistance to [osimertinib](../drugs/osimertinib.md); persistence despite TKI therapy noted [PMID:37591896](../papers/37591896.md).
- Cell-cycle/CDKN2A-B loss enrichment in BM suggests a rationale for CDK4/6-directed strategies in CNS-tropic NSCLC, not tested here [PMID:37591896](../papers/37591896.md).

## Sources

- [PMID:37591896](../papers/37591896.md)
- [PMID:39506116](../papers/39506116.md)

*This page was processed by **entity-page-writer** on **2026-04-08**.*
