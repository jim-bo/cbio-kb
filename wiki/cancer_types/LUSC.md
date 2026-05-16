---
name: Lung Squamous Cell Carcinoma
oncotree_code: LUSC
main_type: Non-Small Cell Lung Cancer
parent: NSCLC
tags: [lung, nsclc, squamous]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Lung Squamous Cell Carcinoma (LUSC)

## Overview

Lung Squamous Cell Carcinoma is a Non-Small Cell Lung Cancer histology (parent [NSCLC](../cancer_types/NSCLC.md)).

## Cohorts in the corpus

- [nsclc_ctdx_msk_2022](../datasets/nsclc_ctdx_msk_2022.md): LUSC was included alongside [LUAD](../cancer_types/LUAD.md) in the 1,127-patient advanced [NSCLC](../cancer_types/NSCLC.md) ctDNA cohort profiled by Resolution Bioscience ctDx Lung at MSK and GenesisCare [PMID:36357680](../papers/36357680.md).
- [bm_nsclc_mskcc_2023](../datasets/bm_nsclc_mskcc_2023.md): 23/233 (10%) of the resected [NSCLC](../cancer_types/NSCLC.md) brain metastasis cohort were LUSC [PMID:37591896](../papers/37591896.md).
- Bakr 2018 published the NSCLC-Radiogenomics Stanford cohort with 45/211 patients being LUSC; pre-treatment CT imaging paired with RNA-seq and somatic mutation data, providing an imaging-genomics resource for LUSC [PMID:30325352](../papers/30325352.md).

## Recurrent alterations

- [STK11](../genes/STK11.md) alterations differ in BM subtype: 22% in [LUAD](../cancer_types/LUAD.md) BM vs 0% in SCC BM (p=0.01) [PMID:37591896](../papers/37591896.md).
- Analyzed within the broader [NSCLC](../cancer_types/NSCLC.md) ctDNA cohort where pathogenic [TP53](../genes/TP53.md), [EGFR](../genes/EGFR.md), or [KRAS](../genes/KRAS.md) alterations detected in ctDNA (vs tissue only) were associated with worse prognosis [PMID:36357680](../papers/36357680.md).
- In a 247-patient advanced [NSCLC](../cancer_types/NSCLC.md) cohort (15% squamous/LUSC), multimodal DyAM model integrating CT [radiomics](../methods/radiomics.md), PD-L1 IHC, and genomics achieved AUC=0.80 for ICI response prediction; the model handles missing modalities and provides modality-specific risk scores enabling clinical interpretability [PMID:36038778](../papers/36038778.md)
- TCGA WES of 178 lung squamous cell carcinomas defined the genomic landscape: near-universal CDKN2A loss, TP53 mutation, and frequent KEAP1/NFE2L2 alterations [PMID:22960745](../papers/22960745.md)
- Pan-NSCLC WES of 660 LUAD and 484 LUSC tumour/normal pairs (nsclc_tcga_broad_2016); LUSC had median somatic mutation rate 9.7/Mb and 20 SMGs; novel LUSC driver RASA1; TP53, CDKN2A, and PIK3CA were significantly more frequently mutated in LUSC than LUAD (p<0.01); LUSC genetic landscape more closely resembled HNSC and BLCA than LUAD; 53% of LUSCs had ≥5 predicted neoepitopes [PMID:27158780](../papers/27158780.md)
- LUSC had a 97% pre-operative ctDNA detection rate (30/31 cases) in the TRACERx cohort, compared with 19% for LUAD; non-adenocarcinoma histology, lymphovascular invasion, and high Ki67 were independent predictors of ctDNA detection on multivariable logistic regression. [PMID:28445469](../papers/28445469.md)
- Squamous cell lung cancer comprised 14% (34/240) of the anti-PD-(L)1 NSCLC MSK-IMPACT cohort used to validate targeted NGS-based TMB as an immunotherapy biomarker; LUSC mutational signatures were used as a comparison reference in the vulvar SCC WES landscape study [PMID:29337640](../papers/29337640.md)
- LUSC mutational signatures (TCGA) were used as a reference comparison cohort in the first whole-exome sequencing landscape of vulvar squamous cell carcinoma; signature profiles were compared across HPV(+) and HPV(-) etiologic subgroups [PMID:29422544](../papers/29422544.md)
- MC3 pan-cancer mutation-calling project (10,510 TCGA pairs) included LUSC; LUSC and LUAD had the largest median SNVs per sample, consistent with tobacco-mutagen exposure [PMID:29596782](../papers/29596782.md)
- Pan-cancer fusion study (9,624 TCGA samples) identified FGFR3–TACC3 in 1.2% of LUSC samples; FGFR3 is a druggable target across 15 cancer types [PMID:29617662](../papers/29617662.md)
- Pan-cancer aneuploidy study placed LUSC in the squamous arm-level cluster (chr_3p loss + chr_3q gain); chr_3p was deleted in ~80% of LUSC tumors and chr_3q gained in >60%; co-occurrence was significantly above chance (chi-square p = 0.0386); the squamous signature was most prominent in LUSC [PMID:29622463](../papers/29622463.md)
- Included in TCGA PanCancer Atlas; LUSC co-clusters in pan-squamous iClusters C10, C25, C27 sharing dNp63/TAp63 squamous signaling; JAK2/STAT upregulation shared with pan-SCC [PMID:29625048](../papers/29625048.md)
- LUSC shows 4% germline vs 89% somatic genome-integrity disruption; among the cancer types with highest somatic genome-integrity disruption rates [PMID:29625049](../papers/29625049.md)
- NRF2/oxidative-stress pathway alteration rate 25% in LUSC, highest pan-cancer; PI3K pathway alteration rate 68% in LUSC; NRF2+PI3K co-alteration concentrated in squamous lung [PMID:29625050](../papers/29625050.md)
- Included in TCGA Pan-Cancer Clinical Data Resource (11,160 patients, 33 cancer types); all four endpoints (OS, PFI, DFI, DSS) recommended without reservation for LUSC; LUSC never-disease-free cases had HR=6.68 (95% CI 4.25-10.51) for new tumor events [PMID:29625055](../papers/29625055.md)
- In PCAWG, lung squamous cell carcinoma showed high chromothripsis frequency; [SOX2](../genes/SOX2.md) amplification via chromothripsis was identified as a late event (many SNVs predated the amplification); chromothripsis was clonal and early in lung squamous [PMID:32025007](../papers/32025007.md).

## Subtypes

- Not further subdivided in this corpus.

## Therapeutic landscape

- ctDNA detection is an independent poor prognostic marker in advanced [NSCLC](../cancer_types/NSCLC.md) (HR 2.05, P<0.001), with ctDNA-guided matching to targeted therapy conferring [OS](../cancer_types/OS.md) benefit (HR 0.63, P<0.001) [PMID:36357680](../papers/36357680.md).
- ATLAS RNA-expression classifier (trained on 8,249 samples including TCGA/CCLE) achieved 91.4% accuracy for cancer site classification; LUSC distinguished within the 22-class site classifier with lineage de-differentiation score prognostic for survival (HR 0.24, P=0.001) [PMID:27634761](../papers/27634761.md).

## Sources

- [PMID:27634761](../papers/27634761.md)
- [PMID:36357680](../papers/36357680.md)
- [PMID:37591896](../papers/37591896.md)
- [PMID:30325352](../papers/30325352.md)

- [PMID:36038778](../papers/36038778.md)

*This page was processed by **crosslinker** on **2026-05-06**.*
- [PMID:22960745](../papers/22960745.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
- [PMID:27158780](../papers/27158780.md)

- [PMID:28445469](../papers/28445469.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29337640](../papers/29337640.md)
- [PMID:29422544](../papers/29422544.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29596782](../papers/29596782.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29617662](../papers/29617662.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29622463](../papers/29622463.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:32025007](../papers/32025007.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
