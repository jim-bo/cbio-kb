---
name: Prostate Adenocarcinoma
oncotree_code: PRAD
parent: PROSTATE
tags: [prostate]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# Prostate Adenocarcinoma (PRAD)

## Overview

OncoTree code for prostate adenocarcinoma.

## Cohorts in the corpus

- [msk_chord_2024](../datasets/msk_chord_2024.md) — 3,211 prostate cancer patients at MSK in the MSK-CHORD clinicogenomic harmonized real-world dataset [PMID:39506116](../papers/39506116.md).
- [prad_msk_mdanderson_2023](../datasets/prad_msk_mdanderson_2023.md) — 44 PDX models from 38 prostate cancer patients at MD Anderson Cancer Center, spanning adenocarcinoma and NEPC, profiled by WGS, T200.1 targeted sequencing, and RNA-seq. [PMID:38488813](../papers/38488813.md)
- [prostate_msk_2024](../datasets/prostate_msk_2024.md) — 2,257 PRAD patients at MSK sequenced by MSK-IMPACT (3,244 tumors); subgroups: 63 MSI-H/dMMR (2.8%), 33 TMB-H/MSS (1.5%). [PMID:38949888](../papers/38949888.md)
- [msk_ctdna_vte_2024](../datasets/msk_ctdna_vte_2024.md) — PRAD comprised 5% of the 4,141-patient liquid biopsy VTE discovery cohort. [PMID:39147831](../papers/39147831.md)
- ATLAS classifier validation — PRAD included in the 22-class site-of-origin model; de-differentiation score distinguishes PRAD from [PRNE](../cancer_types/PRNE.md) (AUC=0.834). [PMID:27634761](../papers/27634761.md)

## Recurrent alterations

- Included in pan-cancer MSK-IMPACT pathway and metastasis analyses [PMID:39506116](../papers/39506116.md).
- 91% of PDX models harbored oncogenic alterations in at least one of [AR](../genes/AR.md), [RB1](../genes/RB1.md), [TP53](../genes/TP53.md), or [PTEN](../genes/PTEN.md). [PMID:38488813](../papers/38488813.md)
- [TMPRSS2](../genes/TMPRSS2.md)-[ERG](../genes/ERG.md) fusion detected in 13/44 PDX models; correlated with [ERG](../genes/ERG.md) overexpression in AR-expressing models. [PMID:38488813](../papers/38488813.md)
- [CDK12](../genes/CDK12.md) biallelic loss via dual mutations or structural variation in 4 PDX models; CDK12-loss-associated focal copy-number gains observed. [PMID:38488813](../papers/38488813.md)
- 63 (2.8%) patients had MSI-H/dMMR tumors, 33 (1.5%) had TMB-H/MSS tumors among 2,257 PRAD patients. MSI-H/dMMR had significantly higher TMB than TMB-H/MSS (median 41 vs. 15 mut/Mb, P<0.01). [PMID:38949888](../papers/38949888.md)
- [BRAF](../genes/BRAF.md) fusions in PRAD: [SND1](../genes/SND1.md) was the dominant 5' fusion partner in prostate adenocarcinoma BRAF fusions (21% of PRAD BRAF fusions). [PMID:38922339](../papers/38922339.md)
- [MSH2](../genes/MSH2.md), [MSH6](../genes/MSH6.md), [MLH1](../genes/MLH1.md), [PMS2](../genes/PMS2.md) — deleterious MMR gene alterations in 75% of MSI-H/dMMR PRAD patients. [PMID:38949888](../papers/38949888.md)

## Subtypes

- MSI-H/dMMR (2.8%) vs. TMB-H/MSS (1.5%) vs. TMB-L/MSS (95.7%) distinct subgroups by immunogenicity; both MSI-H and TMB-H/MSS are more commonly Gleason grade group 5 (62% and 59% vs. 40%, P<0.001). [PMID:38949888](../papers/38949888.md)
- NEPC/PRNE: defined by [AR](../genes/AR.md) expression loss, [RB1](../genes/RB1.md) enrichment; DDR pathway transcriptomically upregulated. ATLAS RNA classifier distinguishes PRAD from PRNE with AUC=0.834. [PMID:38488813](../papers/38488813.md) [PMID:27634761](../papers/27634761.md)

## Therapeutic landscape

- NLP-augmented integrated models outperformed stage- or genomics-only models for overall-survival prediction [PMID:39506116](../papers/39506116.md).
- MSI-H/dMMR PRAD: 45% RECIST ORR and 65% PSA50 response with immune checkpoint blockade (n=27 treated); MSI-H/dMMR patients should receive somatic tumor testing per NCCN recommendations. [PMID:38949888](../papers/38949888.md)
- TMB-H/MSS PRAD: 0% RECIST response with ICB despite FDA approval of [pembrolizumab](../drugs/pembrolizumab.md) for TMB-H tumors; TMB alone is an insufficient biomarker in PRAD. [PMID:38949888](../papers/38949888.md)
- [FGFR1](../genes/FGFR1.md) downstream signature (NRP2, LRP4, TGFBI) stratifies patients for FGFR-targeted therapy in bone-metastatic CRPC; PARP inhibition investigated in NEPC. [PMID:38488813](../papers/38488813.md)
- ctDNA detection associated with higher VTE rates in PRAD patients (5% of pan-cancer cohort); anticoagulation associated with lower VTE in ctDNA-positive patients (adjusted HR=0.50). [PMID:39147831](../papers/39147831.md)
- ATLAS lineage de-differentiation score prognostic for prostate cancer survival and neuroendocrine transformation detection. [PMID:27634761](../papers/27634761.md)
- ROBIN OligoMET center (U54 CA273956; UMB, Weill Cornell Medicine, Thomas Jefferson University) conducts parallel co-clinical studies in oligometastatic PRAD: the TERPS Phase II RCT (NCT05223803) of metastasis-directed SABR had enrolled 47 patients (80+ screened) as of writing; digital-pathology multimodal AI, plasma proteomics, and T-cell receptor repertoire analyses yielded preliminary SABR-benefit signatures. Preclinical dietary interventions showed low-fat/calorie-restricted diets enhanced radiosensitivity while ketogenic diets promoted radio-resistance. These findings catalyzed the biomarker-designed KNIGHTS integral-biomarker RCT (NCT06212583). OligoMET also explicitly investigates molecular drivers of poorer outcomes in African-American patients. [PMID:41941260](../papers/41941260.md)

## Sources

- [PMID:27634761](../papers/27634761.md)
- [PMID:38488813](../papers/38488813.md)
- [PMID:38922339](../papers/38922339.md)
- [PMID:38949888](../papers/38949888.md)
- [PMID:39147831](../papers/39147831.md)
- [PMID:39506116](../papers/39506116.md)
- [PMID:41941260](../papers/41941260.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
