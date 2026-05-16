---
name: Mixed Cancer Types
oncotree_code: MIXED
main_type: Cancer of Unknown Primary
parent: OTHER
tags:
  - mixed-histology
  - breast
  - idc-ilc
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Mixed Cancer Types (MIXED)

## Overview

The MIXED OncoTree code designates tumors with mixed histologic features that do not cleanly fit a single cancer type. In the breast cancer context within this corpus, it specifically denotes mixed invasive ductal/invasive lobular carcinoma (mixed IDC/ILC), which accounts for approximately 3–11% of invasive breast cancers. These tumors contain elements of both ductal and lobular morphology and have historically been classified as a distinct entity, but molecular profiling indicates they are not a third hybrid class.

## Cohorts in the corpus

- [brca_tcga_pub2015](../datasets/brca_tcga_pub2015.md) — 88 mixed IDC/ILC tumors profiled alongside 127 [ILC](../cancer_types/ILC.md) and 490 [IDC](../cancer_types/IDC.md) samples; the largest molecular characterization of this histologic category to date [PMID:26451490](../papers/26451490.md).

## Recurrent alterations

- Mixed IDC/ILC tumors molecularly resolve into ILC-like (24/88) or IDC-like (64/88) classes by majority vote of three orthogonal classifiers (ISOpure, OncoSign-adapted, ElasticNet); [CDH1](../genes/CDH1.md) mutation status is the dominant discriminating feature — all CDH1-mutated mixed tumors classified as ILC-like [PMID:26451490](../papers/26451490.md).
- [CDH1](../genes/CDH1.md) alteration rate in mixed tumors is intermediate between [ILC](../cancer_types/ILC.md) (63%) and [IDC](../cancer_types/IDC.md) (2%), consistent with the histologic mixture [PMID:26451490](../papers/26451490.md).
- MET500 cohort (n=500 metastatic solid tumors across 20 cancer types) is the defining MIXED-lineage study in this corpus: top three types were PRAD (18.6%), BRCA (18.2%), and SARCNOS (8.4%); pan-cancer somatic landscape across lineages found TP53 (53.2%), CDKN2A (16%), PTEN (15.8%), PIK3CA (13.4%), AR (12.6%), and KRAS (10.2%) as most-altered genes. [PMID:28783718](../papers/28783718.md)
- Two of 18 patients in the cobimetinib histiocytosis trial (NCT02649972) had mixed histiocytosis; both responded (one harbored RAF1 K106N, validated as activating in Ba/F3), confirming MEK inhibition efficacy extends to mixed histiocytic neoplasms [PMID:30867592](../papers/30867592.md).

## Subtypes

- Mixed IDC/ILC tumors are not a third molecular entity; they are best characterized as ILC-like or IDC-like based on [CDH1](../genes/CDH1.md) status and multi-platform molecular profiles [PMID:26451490](../papers/26451490.md).
- The clinical designation "mixed ductal/lobular" aggregates tumors with "[IDC](../cancer_types/IDC.md) with lobular features" — a non-standardized pathology criterion that contributes to molecular heterogeneity in this category [PMID:26451490](../papers/26451490.md).

## Therapeutic landscape

- Treatment implications for mixed IDC/ILC depend on the molecular ILC-like vs IDC-like classification: ILC-like mixed tumors inherit the high pAKT/AKT pathway activation typical of [ILC](../cancer_types/ILC.md), suggesting potential benefit from PI3K/AKT/mTOR inhibition; IDC-like mixed tumors follow IDC biology [PMID:26451490](../papers/26451490.md).
- Metastatic surveillance for ILC-like mixed tumors should include anatomical (CT) rather than PET scanning, given low metabolic activity characteristic of ILC [PMID:26451490](../papers/26451490.md).

## Sources

- [PMID:26451490](../papers/26451490.md)
- [PMID:28783718](../papers/28783718.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:30867592](../papers/30867592.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
