---
name: Small Cell Lung Cancer
oncotree_code: SCLC
main_type: Small Cell Lung Cancer
parent: LNET
tags: []
processed_by: crosslinker
processed_at: 2026-05-03
---

# Small Cell Lung Cancer (SCLC)

## Overview

Small cell lung cancer (SCLC) is a neuroendocrine carcinoma of the lung characterized by neuroendocrine differentiation, near-universal loss of [TP53](../genes/TP53.md) and [RB1](../genes/RB1.md), and extremely aggressive clinical behavior. On OncoTree it is a child of Lung Neuroendocrine Tumor ([LNET](../cancer_types/LNET.md)). SCLC accounts for ~13--15% of lung cancers and is almost exclusively found in smokers. It is typically sensitive to initial chemotherapy but rapidly acquires resistance.

## Cohorts in the corpus

- Included as one of 22 cancer site-of-origin classes in the ATLAS classifier; ATLAS differentiation score distinguished [NSCLC](../cancer_types/NSCLC.md) from SCLC with AUC=0.963, enabling RNA-based identification of neuroendocrine transformation (zero-shot learning property). [PMID:27634761](../papers/27634761.md)
- [asclc_msk_2024](../datasets/asclc_msk_2024.md) — 600 consecutive de novo SCLC patients prospectively sequenced by [MSK-IMPACT](../methods/msk-impact-panel.md) at MSKCC; 20 (3%) identified as atypical SCLC (aSCLC, [RB1](../genes/RB1.md)+/[TP53](../genes/TP53.md)+, never/light smokers ≤10 pack-years). [PMID:39185963](../papers/39185963.md)

## Recurrent alterations

- This corpus study does not provide gene-level SCLC mutation frequencies from primary clinical cohorts. The ATLAS classifier uses ~632 RNA expression features for classification rather than genomic alteration profiles.
- aSCLC subset (3% of de novo SCLC): wild-type [RB1](../genes/RB1.md) and [TP53](../genes/TP53.md) by definition; chromothripsis in 84% (16/19 non-MSI cases); ecDNA amplification of [CCND1](../genes/CCND1.md) (30%), [CCND2](../genes/CCND2.md)/[CDK4](../genes/CDK4.md)/[MDM2](../genes/MDM2.md) (15%), or [MYCL](../genes/MYCL.md) (10%). [PMID:39185963](../papers/39185963.md)
- Carcinoid-associated mutations enriched in aSCLC: [ATM](../genes/ATM.md) 30% (vs. 3% in conventional SCLC, P=0.0003), [ARID1A](../genes/ARID1A.md) 25%, [MEN1](../genes/MEN1.md) 15%, [EIF1AX](../genes/EIF1AX.md) 10%. [PMID:39185963](../papers/39185963.md)
- aSCLC has low TMB (<2 mut/Mb in most cases) and lacks the smoking mutational signature; ASCL1-dominant (100%) and YAP1-negative subtype. [PMID:39185963](../papers/39185963.md)
- Comparator nsSCLC-[RB1](../genes/RB1.md)−/[TP53](../genes/TP53.md)− (never-smoker, RB1/TP53 co-inactivated) is enriched for [EGFR](../genes/EGFR.md) mutations (39%) and [KRAS](../genes/KRAS.md) mutations (6%), consistent with LUAD-to-SCLC transformation. [PMID:39185963](../papers/39185963.md)

## Subtypes

- ATLAS classifier demonstrated AUC=0.963 for distinguishing [NSCLC](../cancer_types/NSCLC.md) from SCLC by lineage de-differentiation score, supporting RNA-based neuroendocrine identification in clinical contexts. [PMID:27634761](../papers/27634761.md)
- Atypical SCLC (aSCLC): [RB1](../genes/RB1.md)+/[TP53](../genes/TP53.md)+, never/light smokers, younger at diagnosis (mean 53 vs. 67 yr, P<0.0001), lower Ki67 (mean 69% vs. 87%, P<0.0001), intermediate survival (median [OS](../cancer_types/OS.md) 58 months vs. 16 months for conventional SCLC). Pathogenetically linked to pulmonary [LNET](../cancer_types/LNET.md) via chromothripsis-driven oncogene amplification rather than RB1/TP53 loss. [PMID:39185963](../papers/39185963.md)
- Conventional smoking-associated SCLC (sSCLC): [RB1](../genes/RB1.md)−/TP53−, high TMB, APOBEC/tobacco signatures, median OS 16 months. [PMID:39185963](../papers/39185963.md)

## Therapeutic landscape

- The ATLAS lineage de-differentiation score identifies neuroendocrine transformation and anaplastic phenotypes, which are associated with worse prognosis and may guide treatment escalation or de-escalation decisions. [PMID:27634761](../papers/27634761.md)
- aSCLC has reduced platinum sensitivity: ORR 33% for [cisplatin](../drugs/cisplatin.md)/[carboplatin](../drugs/carboplatin.md) + [etoposide](../drugs/etoposide.md) (vs. ~70% historical for conventional SCLC). [PMID:39185963](../papers/39185963.md)
- [Temozolomide](../drugs/temozolomide.md) showed durable responses in 4/6 aSCLC patients (>10 months; up to 2 years); the two longest responders had the lowest [MGMT](../genes/MGMT.md) mRNA expression. [PMID:39185963](../papers/39185963.md)
- Universal high [DLL3](../genes/DLL3.md) and [SEZ6](../genes/SEZ6.md) expression in aSCLC (mean H-scores 278 and 240) supports investigation of DLL3- and SEZ6-targeted therapies in this subset. [PMID:39185963](../papers/39185963.md)
- Chromothripsis-driven [CDK4](../genes/CDK4.md)/[CCND2](../genes/CCND2.md) co-amplification in 15% of aSCLC provides rationale for CDK4/6 pathway inhibition. [PMID:39185963](../papers/39185963.md)

## Sources

- [PMID:27634761](../papers/27634761.md) — A platform-independent AI tumor lineage and site (ATLAS) classifier (Communications Biology, 2024)
- [PMID:39185963](../papers/39185963.md) — Rekhtman et al., atypical SCLC with RB1/TP53 proficiency and chromothripsis; MSKCC de novo SCLC cohort (2024).

*This page was processed by **crosslinker** on **2026-05-03**.*
