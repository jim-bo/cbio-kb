---
name: Mixed Cancer Types
oncotree_code: MIXED
main_type: Cancer of Unknown Primary
parent: OTHER
tags:
  - mixed-histology
  - breast
  - idc-ilc
processed_by: crosslinker
processed_at: 2026-05-21
---

# Mixed Cancer Types (MIXED)

## Overview

The MIXED OncoTree code designates tumors with mixed histologic features that do not cleanly fit a single cancer type. In the breast cancer context within this corpus, it specifically denotes mixed invasive ductal/invasive lobular carcinoma (mixed IDC/ILC), which accounts for approximately 3–11% of invasive breast cancers. These tumors contain elements of both ductal and lobular morphology and have historically been classified as a distinct entity, but molecular profiling indicates they are not a third hybrid class.

## Cohorts in the corpus

- [brca_tcga_pub2015](../datasets/brca_tcga_pub2015.md) — 88 mixed IDC/ILC tumors profiled alongside 127 [ILC](../cancer_types/ILC.md) and 490 [IDC](../cancer_types/IDC.md) samples; the largest molecular characterization of this histologic category to date [PMID:26451490](../papers/26451490.md).

## Recurrent alterations

- Mixed IDC/ILC tumors molecularly resolve into ILC-like (24/88) or IDC-like (64/88) classes by majority vote of three orthogonal classifiers (ISOpure, OncoSign-adapted, ElasticNet); [CDH1](../genes/CDH1.md) mutation status is the dominant discriminating feature — all CDH1-mutated mixed tumors classified as ILC-like [PMID:26451490](../papers/26451490.md).
- [CDH1](../genes/CDH1.md) alteration rate in mixed tumors is intermediate between [ILC](../cancer_types/ILC.md) (63%) and [IDC](../cancer_types/IDC.md) (2%), consistent with the histologic mixture [PMID:26451490](../papers/26451490.md).
- MET500 cohort (n=500 metastatic solid tumors across 20 cancer types) is the defining MIXED-lineage study in this corpus: top three types were [PRAD](../cancer_types/PRAD.md) (18.6%), [BRCA](../cancer_types/BRCA.md) (18.2%), and [SARCNOS](../cancer_types/SARCNOS.md) (8.4%); pan-cancer somatic landscape across lineages found [TP53](../genes/TP53.md) (53.2%), [CDKN2A](../genes/CDKN2A.md) (16%), [PTEN](../genes/PTEN.md) (15.8%), [PIK3CA](../genes/PIK3CA.md) (13.4%), [AR](../genes/AR.md) (12.6%), and [KRAS](../genes/KRAS.md) (10.2%) as most-altered genes. [PMID:28783718](../papers/28783718.md)
- Two of 18 patients in the [cobimetinib](../drugs/cobimetinib.md) histiocytosis trial (NCT02649972) had mixed histiocytosis; both responded (one harbored [RAF1](../genes/RAF1.md) K106N, validated as activating in Ba/F3), confirming MEK inhibition efficacy extends to mixed histiocytic neoplasms [PMID:30867592](../papers/30867592.md).
- CCLE multi-omic study (1,072 cancer cell lines) constitutes a pan-cancer ([MIXED](../cancer_types/MIXED.md)) resource; key findings include reciprocal LDHA/LDHB paralogue synthetic lethalities gated by promoter methylation, [TERT](../genes/TERT.md) promoter mutations in 16.7% of 503 lines, and [MDM4](../genes/MDM4.md) exon-6 inclusion as a biomarker for MDM2-inhibitor sensitivity [PMID:31068700](../papers/31068700.md).
- Integrative genomic/transcriptomic study of 133 combined hepatocellular-intrahepatic cholangiocarcinoma (cHCC-ICC) cases classified by Allen-Lisa criteria; [TP53](../genes/TP53.md) mutated in 49.2%, [TERT](../genes/TERT.md) promoter C228T in 22.9%, [MYC](../genes/MYC.md) amplified in 73%; Nestin ([NES](../genes/NES.md)) IHC positive in 81.3% of cHCC-ICC and proposed as a diagnostic/prognostic biomarker (median [OS](../cancer_types/OS.md) 18.7 mo Nestin+ vs 46.6 mo Nestin-) [PMID:31130341](../papers/31130341.md).
- CCLE proteomics profiled 375 cancer cell lines from 22 lineages including mixed tissue types; primary axis of proteome variation organized by coordinated pathway expression rather than tissue lineage or mutation burden [PMID:31978347](../papers/31978347.md).
- OncoMark N-MTL hallmark classifier trained on 3.1M single cells from 14 tumor sites including hematologic/mixed histology; MIXED cancer types from 941 patients (Weizmann 3CA) used in training corpus; hallmark scores rise monotonically with AJCC stage across pan-cancer datasets [PMID:35121966](../papers/35121966.md)
- Used as a cohort-level tag in MSK cWGTS pediatric/rare solid tumor study (n=114 patients, [mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md)) to denote mixed pediatric/rare entity cohort; not a primary disease designation [PMID:35585047](../papers/35585047.md)

## Subtypes

- Mixed IDC/ILC tumors are not a third molecular entity; they are best characterized as ILC-like or IDC-like based on [CDH1](../genes/CDH1.md) status and multi-platform molecular profiles [PMID:26451490](../papers/26451490.md).
- The clinical designation "mixed ductal/lobular" aggregates tumors with "[IDC](../cancer_types/IDC.md) with lobular features" — a non-standardized pathology criterion that contributes to molecular heterogeneity in this category [PMID:26451490](../papers/26451490.md).

## Therapeutic landscape

- Treatment implications for mixed IDC/ILC depend on the molecular ILC-like vs IDC-like classification: ILC-like mixed tumors inherit the high pAKT/AKT pathway activation typical of [ILC](../cancer_types/ILC.md), suggesting potential benefit from PI3K/AKT/mTOR inhibition; IDC-like mixed tumors follow [IDC](../cancer_types/IDC.md) biology [PMID:26451490](../papers/26451490.md).
- Metastatic surveillance for ILC-like mixed tumors should include anatomical (CT) rather than PET scanning, given low metabolic activity characteristic of [ILC](../cancer_types/ILC.md) [PMID:26451490](../papers/26451490.md).

## Sources

- [PMID:26451490](../papers/26451490.md)
- [PMID:28783718](../papers/28783718.md)

- [PMID:30867592](../papers/30867592.md)
- [PMID:31068700](../papers/31068700.md) — Ghandi et al. CCLE multi-omic profiling (Nature 2019).
- [PMID:31130341](../papers/31130341.md) — Xue et al. cHCC-ICC pan-Asia genomic study (Cancer Cell 2019).


- [PMID:31978347](../papers/31978347.md)

- [PMID:35121966](../papers/35121966.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
