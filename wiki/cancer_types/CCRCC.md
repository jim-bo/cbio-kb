---
name: Renal Clear Cell Carcinoma
oncotree_code: CCRCC
main_type: Renal Cell Carcinoma
parent: RCC
tags:
  - kidney
  - renal
  - clear-cell
  - immunotherapy
  - tki
  - tumor-microenvironment
processed_by: crosslinker
processed_at: 2026-05-21
---

# Renal Clear Cell Carcinoma (CCRCC)

## Overview

Clear cell renal cell carcinoma (ccRCC) is the most common histologic subtype of renal cell carcinoma, arising from renal tubular epithelium and characterized by [VHL](../genes/VHL.md) loss and alterations in chromatin remodeling genes ([BAP1](../genes/BAP1.md), [SETD2](../genes/SETD2.md), [PBRM1](../genes/PBRM1.md)). It sits at OncoTree level 3 under the renal cell carcinoma ([RCC](../cancer_types/RCC.md)) branch. First-line treatment options include immune checkpoint inhibitors (ICI), tyrosine kinase inhibitors (TKI), and combination regimens; biomarker-driven therapy selection is an active area of investigation.

## Cohorts in the corpus

- TCGA-KIRC: n=491 ccRCC samples; included in the 14-cohort meta-analysis (total n=3,621). [PMID:22138691](../papers/22138691.md)
- IMmotion150: n=163 samples; IMmotion151: n=784 samples; JAVELIN Renal 101: n=701 samples — all included in the HiTME meta-cohort. [PMID:22138691](../papers/22138691.md)
- WU-RCC (Washington University): independent validation cohort, n=193 with DNA-seq and RNA-seq (n=157 with bulk RNA-seq); spatial proteomics MxIF on n=34. [PMID:22138691](../papers/22138691.md)

## Recurrent alterations

- [BAP1](../genes/BAP1.md) — mutations associated with TKI non-response; enriched in fibrotic IE/M and F HiTME subtypes. [PMID:22138691](../papers/22138691.md)
- [SETD2](../genes/SETD2.md) — mutations associated with TKI non-response in the WU-RCC validation cohort. [PMID:22138691](../papers/22138691.md)
- [PBRM1](../genes/PBRM1.md) — mutations enriched in TKI-high score group and in immune-enriched IE and IE/M HiTME subtypes. [PMID:22138691](../papers/22138691.md)
- [MTOR](../genes/MTOR.md) — activating mutations strongly associated with ICI and ICI+TKI non-response; 15 of 16 patients with MTOR-activating mutations were resistant to ICI regimens. [PMID:22138691](../papers/22138691.md)
- [KDM5C](../genes/KDM5C.md) — mutational frequency varied across ICI and TKI score groups. [PMID:22138691](../papers/22138691.md)
- [NF2](../genes/NF2.md) — mutations more prevalent in the fibrotic F HiTME subtype. [PMID:22138691](../papers/22138691.md)
- TCGA multi-platform characterization of 446 CCRCC primary nephrectomy specimens identified 19 significantly mutated genes ([VHL](../genes/VHL.md), [PBRM1](../genes/PBRM1.md), [SETD2](../genes/SETD2.md), [KDM5C](../genes/KDM5C.md), [PTEN](../genes/PTEN.md), [BAP1](../genes/BAP1.md), [MTOR](../genes/MTOR.md), [TP53](../genes/TP53.md) most significant), chromosome 3p loss in 91%, PI3K/AKT/mTOR pathway alteration in ~28%, and a metabolic Warburg shift correlating with worse survival [PMID:23792563](../papers/23792563.md)
- Mouse scRNA-seq (147,045 cells) with conditional Vhl inactivation resolved isoform-specific roles of [HIF1A](../genes/HIF1A.md) and HIF2A in CCRCC initiation: [HIF1A](../genes/HIF1A.md) drives early glycolysis and papillary cell loss; HIF2A drives cortical proximal tubule dedifferentiation and proliferation, supporting early [belzutifan](../drugs/belzutifan.md) use in [VHL](../genes/VHL.md) disease [PMID:23797736](../papers/23797736.md)
- Multiregion exome sequencing (M-seq) of 10 ccRCCs found 73–75% of driver alterations were subclonal; only chromosome 3p loss and [VHL](../genes/VHL.md) inactivation were truncal across all tumors — single-biopsy approaches systematically underestimate driver-mutation prevalence [PMID:24487277](../papers/24487277.md)
- TCGA multi-platform characterization of 66 ChRCC tumors identified [CCRCC](../cancer_types/CCRCC.md) as a comparative cohort (417 tumors); ChRCC has a 3-fold lower mutation rate than ccRCC (~0.4/Mb), a non-Warburg mitochondrial metabolism phenotype, and distinct distal-nephron cell-of-origin — underscoring biological separation between the two [RCC](../cancer_types/RCC.md) subtypes. [PMID:25155756](../papers/25155756.md)
- [URCC](../cancer_types/URCC.md) cohort (n=62, MSKCC) shows only 1/62 [VHL](../genes/VHL.md) mutations — stark contrast to ~75% in [CCRCC](../cancer_types/CCRCC.md); [URCC](../cancer_types/URCC.md) NF2-loss and mTORC1-hyperactive subsets are mutually exclusive and both lack [VHL](../genes/VHL.md) alteration [PMID:27713405](../papers/27713405.md).
- [PBRM1](../genes/PBRM1.md) loss-of-function was associated with clinical benefit from anti-PD-(L)1 therapy in metastatic CCRCC (9/11 CB vs 3/13 NCB, Fisher p=0.012; validated in 63-patient cohort, p=0.0071); PBRM1-LOF tumors showed upregulated JAK/STAT3 and hypoxia transcriptional programs [PMID:29301960](../papers/29301960.md)
- MC3 pan-cancer mutation-calling project used [KIRC](../cancer_types/KIRC.md) (clear cell [RCC](../cancer_types/RCC.md)) as a benchmark: running MutSig2CV and MuSiC2 on PASS variants yielded 10 SMGs each ([TP53](../genes/TP53.md), [PTEN](../genes/PTEN.md), VHL, [SETD2](../genes/SETD2.md), [PBRM1](../genes/PBRM1.md), [BAP1](../genes/BAP1.md), [MTOR](../genes/MTOR.md), and others); the unfiltered controlled MAF inflated these to 1,203 and 321 respectively, demonstrating the critical importance of the MC3 filtering strategy [PMID:29596782](../papers/29596782.md)
- Included in the MSK cWGTS pediatric/rare solid tumor cohort (n=114 patients, [mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md)); whole-genome + transcriptome sequencing added oncogenic findings beyond MSK-IMPACT in 54% of patients [PMID:35585047](../papers/35585047.md)

## Subtypes

Five harmonized immune tumor microenvironment (HiTME) subtypes were defined by density-based clustering of functional gene expression signatures across 3,621 ccRCC samples from 14 cohorts: [PMID:22138691](../papers/22138691.md)

- **IE (immune-enriched, nonfibrotic):** Highest ICI and TKI responder proportions; best prognosis.
- **IE/M (immune-enriched, myeloid immunosuppressive):** Elevated ICI responder proportion but fibrotic features; worst overall survival in TCGA-KIRC.
- **F (fibrotic-myeloid immunosuppressive):** Largest proportion of ICI non-responders; worst overall survival.
- **V (highly vascularized):** High TKI responder proportion.
- **D (immune desert):** Immunologically cold.

## Therapeutic landscape

- An integrated gradient-boosting decision-tree model classifies ccRCC patients as ICI/ICI-combo-preferred (56%), TKI-preferred (41%), or non-responsive (3%), validated across IMmotion151 and JAVELIN Renal 101 cohorts. [PMID:22138691](../papers/22138691.md)
- ICI/ICI-combo-preferred patients had significantly longer PFS with [atezolizumab](../drugs/atezolizumab.md)+[bevacizumab](../drugs/bevacizumab.md) vs. [sunitinib](../drugs/sunitinib.md) (IMmotion151, p=0.00005) and with [avelumab](../drugs/avelumab.md)+[axitinib](../drugs/axitinib.md) vs. [sunitinib](../drugs/sunitinib.md) (JAVELIN, p=0.000007). [PMID:22138691](../papers/22138691.md)
- MTOR-activating mutations and antigen presentation gene mutations may serve as molecular exclusion criteria for ICI therapy. [PMID:22138691](../papers/22138691.md)
- ICI response model achieved ROC-AUC=0.77 (training) and ROC-AUC=0.78 (JAVELIN validation), outperforming all published single-biomarker signatures. [PMID:22138691](../papers/22138691.md)
- TKI response model achieved ROC-AUC=0.74 on validation (n=822), outperforming JAVELIN Angio, IMmotion150 Angio, proliferation, and macrophage signatures. [PMID:22138691](../papers/22138691.md)

## Sources

- [PMID:22138691](../papers/22138691.md) — Five HiTME ccRCC TME subtypes and multi-omic ICI/TKI response prediction models (meta-cohort n=3,621; validation WU-RCC n=193).
- [PMID:23792563](../papers/23792563.md)
- [PMID:23797736](../papers/23797736.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:24487277](../papers/24487277.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25155756](../papers/25155756.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27713405](../papers/27713405.md)

- [PMID:29301960](../papers/29301960.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29596782](../papers/29596782.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
