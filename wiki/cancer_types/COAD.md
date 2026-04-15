---
name: Colon Adenocarcinoma
oncotree_code: COAD
main_type: Colorectal Cancer
parent: COADREAD
tags: [colorectal, gi-oncology]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# Colon Adenocarcinoma (COAD)

## Overview

Colon Adenocarcinoma is a Colorectal Cancer (parent [COADREAD](../cancer_types/COADREAD.md)).

## Cohorts in the corpus

- [coad_silu_2022](../datasets/coad_silu_2022.md): 348 treatment-naive primary colon cancer patients (AC-ICAM) with matched tumor and healthy colon tissue, profiled by [RNA-seq](../methods/rna-seq.md), WES, deep TCRβ-seq, 16S rRNA-seq, and tumor WGS; median follow-up 4.6 years [PMID:37202560](../papers/37202560.md).
- [coadread_tcga](../datasets/coadread_tcga.md) used as a comparator [PMID:37202560](../papers/37202560.md).
- HCT-116 (HER2−, COAD cell line): negative-control model in ADC radiosensitization study — T-DM1 IC50 >100 nM and no tumor-growth benefit from adding T-DM1 to IR in HCT-116 xenografts, demonstrating receptor-selectivity of the approach. [PMID:27698471](../papers/27698471.md)

## Recurrent alterations

- No single driver gene is proposed as a biomarker; the paper's gene-level claims focus on the 20-gene Immunologic Constant of Rejection (ICR) module [PMID:37202560](../papers/37202560.md).
- [ERBB2](../genes/ERBB2.md) (HER2): HCT-116 is HER2− (T-DM1 IC50 >100 nM), serving as the definitive HER2-negative colon cancer negative control demonstrating receptor-selectivity of ADC radiosensitization. [PMID:27698471](../papers/27698471.md)
- The ICR signature includes [IFNG](../genes/IFNG.md), [TBX21](../genes/TBX21.md), [CD8A](../genes/CD8A.md), [CD8B](../genes/CD8B.md), [IL12B](../genes/IL12B.md), [STAT1](../genes/STAT1.md), [IRF1](../genes/IRF1.md), [CCL5](../genes/CCL5.md), [CXCL9](../genes/CXCL9.md), [CXCL10](../genes/CXCL10.md), [GNLY](../genes/GNLY.md), [PRF1](../genes/PRF1.md), [GZMA](../genes/GZMA.md), [GZMB](../genes/GZMB.md), [GZMH](../genes/GZMH.md), [CD274](../genes/CD274.md), [CTLA4](../genes/CTLA4.md), [FOXP3](../genes/FOXP3.md), [IDO1](../genes/IDO1.md), [PDCD1](../genes/PDCD1.md) [PMID:37202560](../papers/37202560.md).

## Subtypes

- ICR consensus clustering segregates tumors into ICR-high (hot), ICR-medium, and ICR-low (cold) [PMID:37202560](../papers/37202560.md).
- ICR outperforms consensus molecular subtype (CMS) and MSI classifications for prognosis and retains prognostic value within the CMS4/mesenchymal subtype [PMID:37202560](../papers/37202560.md).
- ICR prognostic effect: ICR-high vs ICR-low HR=0.54 (95% CI 0.34–0.86, P=0.0095); ICR-medium vs ICR-low HR=0.63 (0.43–0.91, P=0.014) [PMID:37202560](../papers/37202560.md).
- Quantifying genetic immunoediting further refines ICR's prognostic value [PMID:37202560](../papers/37202560.md).
- A *Ruminococcus bromii*-driven microbiome signature combined with ICR (mICRoScore) identifies patients with excellent survival probability [PMID:37202560](../papers/37202560.md).

## Therapeutic landscape

- Paper does not directly test predictive utility for immunotherapy in colon cancer [PMID:37202560](../papers/37202560.md).
- HCT-116 (HER2−) colon xenografts showed no benefit from T-DM1 + IR vs. IR alone, confirming that receptor expression is required for ADC-mediated radiosensitization. [PMID:27698471](../papers/27698471.md)
- [TRIM24](../genes/TRIM24.md)-BRAF fusions identified in 43% of BRAF-fusion-positive colorectal cases; frequent co-mutations include [RNF43](../genes/RNF43.md) (64%), [TP53](../genes/TP53.md) (57%), [KMT2D](../genes/KMT2D.md) (43%), [MSH3](../genes/MSH3.md) (42%), and [ARID1A](../genes/ARID1A.md) (36%) [PMID:38922339](../papers/38922339.md).

## Sources

- [PMID:37202560](../papers/37202560.md)
- [PMID:38922339](../papers/38922339.md)
- [PMID:27698471](../papers/27698471.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
