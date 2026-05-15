---
name: Prostate Adenocarcinoma
oncotree_code: PRAD
main_type: Prostate Cancer
parent: PROSTATE
tags: [prostate]
processed_by: wiki-cli
processed_at: 2026-05-14
---

# Prostate Adenocarcinoma (PRAD)

## Overview

OncoTree code for prostate adenocarcinoma.

## Cohorts in the corpus

- [msk_chord_2024](../datasets/msk_chord_2024.md) — 3,211 prostate cancer patients at MSK in the MSK-CHORD clinicogenomic harmonized real-world dataset [PMID:39506116](../papers/39506116.md).
- Commentary cohort: oligometastatic hormone-sensitive PRAD; synchronous de novo cases estimated at "several thousands" per year in the US; metachronous/oligorecurrent cases potentially the majority of men who progress to metastatic disease. No primary data collected. [PMID:28045614](../papers/28045614.md)
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
- [BRAF](../genes/BRAF.md) fusions in PRAD: [SND1](../genes/SND1.md) was the dominant 5' fusion partner in prostate adenocarcinoma [BRAF](../genes/BRAF.md) fusions (21% of PRAD [BRAF](../genes/BRAF.md) fusions). [PMID:38922339](../papers/38922339.md)
- No specific gene-level alterations identified for the oligometastatic hormone-sensitive state; genetic and transcriptomic profiling of hormone-sensitive localized and metastatic castration-resistant PRAD has been described but a hormone-sensitive oligometastatic data set was noted as "still unavailable." [PMID:28045614](../papers/28045614.md)
- [MSH2](../genes/MSH2.md), [MSH6](../genes/MSH6.md), [MLH1](../genes/MLH1.md), [PMS2](../genes/PMS2.md) — deleterious MMR gene alterations in 75% of MSI-H/dMMR PRAD patients. [PMID:38949888](../papers/38949888.md)
- Integrative genomic profiling of 218 PRAD tumors (MSKCC cohort) identified recurrent copy-number alterations and somatic mutations via SNP arrays and whole-exome sequencing [PMID:20579941](../papers/20579941.md)
- WES of 112 prostate adenocarcinoma tumors identified [SPOP](../genes/SPOP.md), [FOXA1](../genes/FOXA1.md), and [MED12](../genes/MED12.md) as recurrent driver genes [PMID:22610119](../papers/22610119.md)
- WES of 112 prostate tumors (Michigan cohort, [prad_mich](../datasets/prad_mich.md)) identified recurrent ETS family fusions and [SPOP](../genes/SPOP.md) mutations as key drivers of prostate adenocarcinoma [PMID:22722839](../papers/22722839.md)
- WGS of 55 treatment-naïve primary PRAD identified chromoplexy (chains of ≥5 interdependent rearrangements) in 88% of tumors; TMPRSS2-ERG fusion arose within chromoplexy chains in 58% of [ERG](../genes/ERG.md)+ cases; recurrent SCNA burden tracks with Gleason grade (p=0.0059) [PMID:23622249](../papers/23622249.md)
- CNA burden (fraction of autosomal genome with copy-number alterations) predicts biochemical recurrence (HR 1.09 per 1%, P<0.001) and metastasis in two independent prostatectomy cohorts (n=168 and n=104); prognostic independent of PSA, Gleason score, and the Stephenson nomogram, and measurable from FFPE needle biopsies by low-pass WGS [PMID:25024180](../papers/25024180.md)
- Seven patient-derived 3D organoid lines from metastatic CRPC recapitulated the molecular landscape of advanced prostate cancer, including [PTEN](../genes/PTEN.md) biallelic loss (6/7 lines), [TP53](../genes/TP53.md) inactivation (4/7), [CHD1](../genes/CHD1.md) deletion (3/7), [SPOP](../genes/SPOP.md) F133L hotspot (1/7, first in vitro model), and diverse [AR](../genes/AR.md) status; AR-amplified MSK-PCa2 was sensitive to [enzalutamide](../drugs/enzalutamide.md) and [everolimus](../drugs/everolimus.md) in vitro and in xenografts. [PMID:25201530](../papers/25201530.md)
- Prospective WES + transcriptome sequencing of 150 mCRPC bone/soft-tissue biopsies (SU2C-PCF Dream Team; dataset: [prad_su2c_2015](../datasets/prad_su2c_2015.md)): [AR](../genes/AR.md) altered in 62.7%, ETS fusions 56.7%, [TP53](../genes/TP53.md) 53.3%, [PTEN](../genes/PTEN.md) 40.7%; DNA-repair pathway (BRCA2/BRCA1/ATM) aberrations in 19.3% — substantially higher than primary PRAD; 89% of patients harbored a clinically actionable alteration; 8% had pathogenic germline variants; novel recurrent focal homozygous deletion of [ZBTB16](../genes/ZBTB16.md) at chr11q23 in 5% of cases [PMID:26000489](../papers/26000489.md)
- Prostate adenocarcinoma (PRAD) multi-omic profiling identified subtypes defined by ETS fusions, SPOP/FOXA1/IDH1 mutations, and distinct epigenetic signatures [PMID:26544944](../papers/26544944.md)
- Beltran et al. profiled 114 metastatic biopsies from 81 castration-resistant prostate cancer patients (51 CRPC-Adeno, 30 CRPC-NE); concurrent RB1+TP53 loss hallmarks neuroendocrine transdifferentiation (53.3% CRPC-NE vs 13.7% CRPC-Adeno); CYLD deleted in 51% CRPC-NE; 70-gene NEPC classifier (precision/recall >0.99) detects CRPC-NE in up to 8% of metastatic cases across external cohorts [PMID:26855148](../papers/26855148.md)
- WES + array-CGH + expression microarray on 176 tumors from 63 men with mCRPC (rapid autopsy cohort) showed high intra-individual metastatic concordance for key drivers ([AR](../genes/AR.md) amplification/mutation 63%, [TMPRSS2](../genes/TMPRSS2.md)-[ERG](../genes/ERG.md) 100% concordant); somatic FA-pathway or [ATM](../genes/ATM.md) defects predicted longer carboplatin response (log-rank P=0.02) [PMID:26928463](../papers/26928463.md)
- TRMT10A overexpressed in prostate cancer/mCRPC vs normal tissue (TCGA prad_tcga; n=500 tumor, n=52 normal); high TRMT10A IHC associated with shorter OS (P=0.014, log-rank) in 54 mCRPC patients; TRMT10A loss sensitizes BRCA1/2-WT mCRPC cells to PARPi (olaparib) by impairing ATM-dependent BRCA1 recruitment; USP10 inhibitor spautin-1 degrades TRMT10A and synergizes with olaparib in 22Rv1 CDX and two mCRPC PDX models [PMID:28068672](../papers/28068672.md)

## Subtypes

- MSI-H/dMMR (2.8%) vs. TMB-H/MSS (1.5%) vs. TMB-L/MSS (95.7%) distinct subgroups by immunogenicity; both MSI-H and TMB-H/MSS are more commonly Gleason grade group 5 (62% and 59% vs. 40%, P<0.001). [PMID:38949888](../papers/38949888.md)
- Oligometastatic PRAD (≤5 radiographically visible metastatic lesions) operationalized as a clinically defined intermediate state on the metastatic spectrum; working definition endorsed pending a biologic/genomic definition. [PMID:28045614](../papers/28045614.md)
- NEPC/PRNE: defined by [AR](../genes/AR.md) expression loss, [RB1](../genes/RB1.md) enrichment; DDR pathway transcriptomically upregulated. ATLAS RNA classifier distinguishes PRAD from [PRNE](../cancer_types/PRNE.md) with AUC=0.834. [PMID:38488813](../papers/38488813.md) [PMID:27634761](../papers/27634761.md)

## Therapeutic landscape

- NLP-augmented integrated models outperformed stage- or genomics-only models for overall-survival prediction [PMID:39506116](../papers/39506116.md).
- MSI-H/dMMR PRAD: 45% RECIST ORR and 65% PSA50 response with immune checkpoint blockade (n=27 treated); MSI-H/dMMR patients should receive somatic tumor testing per NCCN recommendations. [PMID:38949888](../papers/38949888.md)
- TMB-H/MSS PRAD: 0% RECIST response with ICB despite FDA approval of [pembrolizumab](../drugs/pembrolizumab.md) for TMB-H tumors; TMB alone is an insufficient biomarker in PRAD. [PMID:38949888](../papers/38949888.md)
- [FGFR1](../genes/FGFR1.md) downstream signature (NRP2, LRP4, TGFBI) stratifies patients for FGFR-targeted therapy in bone-metastatic CRPC; PARP inhibition investigated in NEPC. [PMID:38488813](../papers/38488813.md)
- ctDNA detection associated with higher VTE rates in PRAD patients (5% of pan-cancer cohort); anticoagulation associated with lower VTE in ctDNA-positive patients (adjusted HR=0.50). [PMID:39147831](../papers/39147831.md)
- ATLAS lineage de-differentiation score prognostic for prostate cancer survival and neuroendocrine transformation detection. [PMID:27634761](../papers/27634761.md)
- ROBIN OligoMET center (U54 CA273956; UMB, Weill Cornell Medicine, Thomas Jefferson University) conducts parallel co-clinical studies in oligometastatic PRAD: the TERPS Phase II RCT (NCT05223803) of metastasis-directed SABR had enrolled 47 patients (80+ screened) as of writing; digital-pathology multimodal AI, plasma proteomics, and T-cell receptor repertoire analyses yielded preliminary SABR-benefit signatures. Preclinical dietary interventions showed low-fat/calorie-restricted diets enhanced radiosensitivity while ketogenic diets promoted radio-resistance. These findings catalyzed the biomarker-designed KNIGHTS integral-biomarker RCT (NCT06212583). OligoMET also explicitly investigates molecular drivers of poorer outcomes in African-American patients. [PMID:41941260](../papers/41941260.md)
- Local metastasis-directed therapies (e.g., SABR) in oligometastatic hormone-sensitive PRAD may alter natural history by ablating macroscopic metastases acting as "communal sanctuaries" seeded by circulating tumor cells from multiple sites (self-seeding model); current standard of care remains systemic ADT and any local therapies should be implemented in a clinical trial. [PMID:28045614](../papers/28045614.md)
- 14q32-encoded microRNA signatures and blood-based biomarkers proposed as candidate oligometastatic biomarkers in PRAD, analogous to [NSCLC](../cancer_types/NSCLC.md), but none are clinically validated. [PMID:28045614](../papers/28045614.md)

## Sources

- [PMID:27634761](../papers/27634761.md)
- [PMID:38488813](../papers/38488813.md)
- [PMID:38922339](../papers/38922339.md)
- [PMID:38949888](../papers/38949888.md)
- [PMID:39147831](../papers/39147831.md)
- [PMID:39506116](../papers/39506116.md)
- [PMID:41941260](../papers/41941260.md)
- [PMID:28045614](../papers/28045614.md)
- [PMID:20579941](../papers/20579941.md)
- [PMID:22610119](../papers/22610119.md)
- [PMID:22722839](../papers/22722839.md)
- [PMID:23622249](../papers/23622249.md) — Baca et al. Punctuated evolution of prostate cancer genomes. *Cell* 2013.
- [PMID:25024180](../papers/25024180.md)
- [PMID:25201530](../papers/25201530.md)
- [PMID:26000489](../papers/26000489.md)
- [PMID:26544944](../papers/26544944.md)
- [PMID:26855148](../papers/26855148.md)

- [PMID:26928463](../papers/26928463.md) — Kumar et al., WES + array-CGH + expression microarray on 176 mCRPC tumors from 63 men (rapid autopsy); intra-individual metastatic concordance and FA-pathway/ATM carboplatin response biomarker

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28068672](../papers/28068672.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
