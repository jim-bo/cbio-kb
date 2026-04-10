---
name: Non-Small Cell Lung Cancer
oncotree_code: NSCLC
main_type: Non-Small Cell Lung Cancer
parent: LUNG
tags: [lung, nsclc]
processed_by: crosslinker
processed_at: 2026-04-09
---

# Non-Small Cell Lung Cancer (NSCLC)

## Overview

Non-Small Cell Lung Cancer (parent LUNG); encompasses histologies including [LUAD](./LUAD.md) and [LUSC](./LUSC.md).

## Cohorts in the corpus

- [bm_nsclc_mskcc_2023](../datasets/bm_nsclc_mskcc_2023.md): 233 patients with resected NSCLC brain metastasis (BM) profiled by MSK-IMPACT — 180 (77%) [LUAD](../cancer_types/LUAD.md), 23 (10%) [LUSC](../cancer_types/LUSC.md), 30 (13%) other NSCLC. Matched samples: 47 primaries, 42 extracranial metastases. Median age 67; 80% current/former smokers [PMID:37591896](../papers/37591896.md).
- [msk_chord_2024](../datasets/msk_chord_2024.md): 7,809 NSCLC patients in the MSK-CHORD clinicogenomic harmonized real-world dataset at MSK [PMID:39506116](../papers/39506116.md).
- [csf_msk_2024](../datasets/csf_msk_2024.md): Lung cancer was the most common primary cancer type in the MSK CSF ctDNA cohort (n=188 patients); NSCLC patients profiled by MSK-IMPACT (IMPACT468/IMPACT505) on CSF samples [PMID:39289779](../papers/39289779.md).

## Recurrent alterations

- TMB was higher in BM vs EM (median 8.8 vs 5.8; p=0.00766); FGA was higher in BM vs EM (p=2.77e-06) and vs PT (p=2.27e-07) [PMID:37591896](../papers/37591896.md).
- [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) alterations more frequent in BM (34%) vs PT (13%, p=0.003, q=0.04); cell-cycle pathway alterations 56% BM vs 32% PT (p=0.004, q=0.041) [PMID:37591896](../papers/37591896.md).
- Paired BM–BM samples showed high genomic concordance vs lower concordance in synchronous BM/PT pairs [PMID:37591896](../papers/37591896.md).
- [NF1](../genes/NF1.md) alterations were more frequent in LMD patients (15%) [PMID:37591896](../papers/37591896.md).
- [HLA-B](../genes/HLA-B.md) mutations appeared as private BM events [PMID:37591896](../papers/37591896.md).
- [EGFR](../genes/EGFR.md) mutations and high-level amplification detected in CSF ctDNA from lung cancer patients; acquired resistance mutations including p.T790M, p.C797S, p.L792H, p.L718Q, p.L718V, p.G724S identified in serial CSF samples [PMID:39289779](../papers/39289779.md).
- [KRAS](../genes/KRAS.md) mutations detected in CSF ctDNA from lung cancer patients; also observed as off-target resistance alteration in EGFR-mutant patients [PMID:39289779](../papers/39289779.md).
- [ALK](../genes/ALK.md) [EML4](../genes/EML4.md)::ALK fusions in lung carcinomas; resistance mutations p.G1202R and p.G1269A detected in CSF upon targeted therapy progression [PMID:39289779](../papers/39289779.md).
- [MET](../genes/MET.md) amplification and exon 14 skipping mutations detected in CSF; resistance mutation p.Y1230N emerged on [crizotinib](../drugs/crizotinib.md) [PMID:39289779](../papers/39289779.md).
- [RET](../genes/RET.md) and [ROS1](../genes/ROS1.md) rearrangements with diverse gene partners detected in CSF ctDNA from lung carcinomas [PMID:39289779](../papers/39289779.md).
- [STK11](../genes/STK11.md) and [KEAP1](../genes/KEAP1.md) mutations detected in CSF ctDNA from lung cancer patients [PMID:39289779](../papers/39289779.md).

## Subtypes

- Among [LUAD](../cancer_types/LUAD.md) BM patients: LMD patients had more [EGFR](../genes/EGFR.md) alterations (45% vs 21%, p=0.044); local progressors had more [RB1](../genes/RB1.md) loss (24% vs 6%, p=0.022); multifocal regional progressors had [MYC](../genes/MYC.md) amplifications in 22% vs 0% (p=0.023) [PMID:37591896](../papers/37591896.md).

## Therapeutic landscape

- Non-canonical [EGFR](../genes/EGFR.md) mutations (L861Q, G719A/S, A755G, N771_H773dup) in BM may identify patients at elevated risk for LMD and partial resistance to [osimertinib](../drugs/osimertinib.md); persistence despite TKI therapy noted [PMID:37591896](../papers/37591896.md).
- Cell-cycle/[CDKN2A](../genes/CDKN2A.md)-B loss enrichment in BM suggests a rationale for CDK4/6-directed strategies in CNS-tropic NSCLC, not tested here [PMID:37591896](../papers/37591896.md).
- Leptomeningeal involvement was a strong predictor of CSF ctDNA positivity in NSCLC (OR 20.17, 95% CI 9.65-42.16, p < 0.0001). CSF ctDNA had greater sensitivity than positive cytology for leptomeningeal disease (85.4% vs. 61.7%) and greater negative predictive value (80% vs. 66%) [PMID:39289779](../papers/39289779.md).
- Lung carcinomas had the highest rate of level 1 OncoKB actionable alterations among all tumor types in the CSF ctDNA cohort; 50.7% of ctDNA-positive samples carried a level 1 actionable alteration [PMID:39289779](../papers/39289779.md).
- Serial CSF ctDNA profiling identified clonal evolution and emergence of resistance mechanisms (EGFR gatekeeper mutations, [ALK](../genes/ALK.md) resistance mutations, [MET](../genes/MET.md) resistance mutations), directly informing treatment changes [PMID:39289779](../papers/39289779.md).

## Sources

- [PMID:37591896](../papers/37591896.md)
- [PMID:39289779](../papers/39289779.md)
- [PMID:39506116](../papers/39506116.md)

*This page was processed by **crosslinker** on **2026-04-09**.*
