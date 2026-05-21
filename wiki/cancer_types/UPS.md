---
name: Undifferentiated Pleomorphic Sarcoma
oncotree_code: UPS
main_type: Soft Tissue Sarcoma
parent: SOFT_TISSUE
tags:
  - soft-tissue-sarcoma
  - genomically-complex
  - corpus-shorthand
canonical_source: corpus
unverified: true
processed_by: crosslinker
processed_at: 2026-05-21
---

# Undifferentiated Pleomorphic Sarcoma (UPS)

## Overview

Undifferentiated Pleomorphic Sarcoma is a high-grade, genomically complex soft tissue sarcoma without a specific line of differentiation. **Note:** The canonical OncoTree code for this entity is [MFH](../cancer_types/MFH.md) (Undifferentiated Pleomorphic Sarcoma/Malignant Fibrous Histiocytoma/High-Grade Spindle Cell Sarcoma). The code "UPS" is used as a shorthand in the dataset `sarcoma_mskcc_2022` and the Nacev 2022 paper; see [MFH](../cancer_types/MFH.md) for the canonical page.

## Cohorts in the corpus

- [sarcoma_mskcc_2022](../datasets/sarcoma_mskcc_2022.md): n=145 UPS in the 2,138-sarcoma MSK-IMPACT cohort — the fourth most common sarcoma histology in this study [PMID:35705560](../papers/35705560.md).
- [sarcoma_msk_2022](../datasets/sarcoma_msk_2022.md): UPS/MFH as a combined group in the 7,494-sarcoma FoundationOne Heme cohort [PMID:35705558](../papers/35705558.md).

## Recurrent alterations

- In the 2,138-sarcoma MSK-IMPACT cohort (n=145 UPS), median TMB was 2.6 mut/Mb (second highest after [ANGS](../cancer_types/ANGS.md)); 15% had TMB ≥5 mut/Mb; 6.7% had TMB ≥10 mut/Mb; WGD occurred in ~50%; WGD was associated with worse [OS](../cancer_types/OS.md) in metastatic UPS specifically (p=0.022); [NF1](../genes/NF1.md) deletions in 14%; [PTEN](../genes/PTEN.md) loss in 8%; [KMT2D](../genes/KMT2D.md) altered in 6%; epigenetic pathway altered in 42%; PI3K pathway in 20% [PMID:35705560](../papers/35705560.md).
- In a 7,494-sarcoma cohort, UPS/MFH showed 4q12 amplicon (KDR/PDGFRA/KIT) in 7.3%, 11q13 amplicon (CCND1/FGF) in 4.3% of UPS of bone, TMB ≥10 mut/Mb in 10.9%, high gLOH (≥19.3%) in 26.6%, CD274/PD-L1 amplification in 3.6%; kinase fusions in 3.6%; durable complete response to [pembrolizumab](../drugs/pembrolizumab.md) in a UPS patient with TMB 20 mut/Mb [PMID:35705558](../papers/35705558.md).

## Subtypes

- UPS of soft tissue vs UPS of bone — distinct amplicon landscapes (11q13 enriched in bone).
- Molecular subtypes by unsupervised clustering (Nacev 2022) — high intra-subtype entropy indicating multiple distinct genetic variants.

## Therapeutic landscape

- ICI with pembrolizumab for TMB ≥10 mut/Mb (3.9% of all sarcomas; 10.9% of UPS/MFH) — anecdotal complete response documented [PMID:35705558](../papers/35705558.md).
- WGD as adverse prognostic marker in metastatic UPS warrants prospective validation [PMID:35705560](../papers/35705560.md).
- NF1 deletions (14%) → MEK inhibitor rationale (Level 4) [PMID:35705560](../papers/35705560.md).

## Sources

- [PMID:35705558](../papers/35705558.md) — Gounder et al. 2022, 7,494-sarcoma FoundationOne Heme cohort.
- [PMID:35705560](../papers/35705560.md) — Nacev et al. 2022, 2,138-sarcoma MSK-IMPACT cohort.

*This page was processed by **crosslinker** on **2026-05-21**.*
