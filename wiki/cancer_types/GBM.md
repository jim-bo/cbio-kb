---
name: Glioblastoma Multiforme
oncotree_code: GBM
main_type: CNS/Brain Cancer
parent: DIFG
tags: []
processed_by: crosslinker
processed_at: 2026-05-21
---

# Glioblastoma Multiforme (GBM)

## Overview

Glioblastoma Multiforme (GBM) is a highly aggressive and common primary brain tumor. In the OncoTree hierarchy, it is categorized under [Diffuse Glioma (DIFG)](DIFG.md). In modern clinical practice and newer classification systems (e.g., WHO 2021), it is often discussed interchangeably with [Glioblastoma, IDH-Wildtype (GB)](GB.md), which represents the majority of cases historically diagnosed as GBM.

## Cohorts in the corpus

- **[TCGA Glioblastoma Multiforme (gbm_tcga)](../datasets/gbm_tcga.md)**: A landmark cohort of 592 cases (with an interim analysis of 206) that provided multi-platform molecular profiling [PMID:18772890](../papers/18772890.md).
- **[TCIA TCGA-GBM MRI Collection (tcia-tcga-gbm)](../datasets/tcia-tcga-gbm.md)**: Imaging data for 135 TCGA-GBM cases with expert-revised segmentation labels and radiomic features [PMID:28872634](../papers/28872634.md).

## Recurrent alterations

Nearly all GBMs (88-90%) exhibit alterations in three core signaling pathways:

- **RTK/RAS/PI3K pathway** (88% of cases):
    - **[EGFR](../genes/EGFR.md)**: Amplified in 45% of cases; also harbors novel missense mutations in the extracellular domain [PMID:18772890](../papers/18772890.md).
    - **[PTEN](../genes/PTEN.md)**: Frequently inactivated through mutation or deletion (36%) [PMID:18772890](../papers/18772890.md).
    - **[NF1](../genes/NF1.md)**: Somatic mutations and deletions occur in 18% of cases, identifying it as a major tumor suppressor in GBM [PMID:18772890](../papers/18772890.md).
    - **[PIK3R1](../genes/PIK3R1.md)**: Frequent mutations (10%) disrupt p110α interaction and activate the PI3K pathway [PMID:18772890](../papers/18772890.md).
    - Other alterations include **[ERBB2](../genes/ERBB2.md)** (8%), **[PIK3CA](../genes/PIK3CA.md)** (7%) [PMID:18772890](../papers/18772890.md).
- **p53 pathway** (78% of cases):
    - **[TP53](../genes/TP53.md)**: Mutated or deleted in 35% of cases [PMID:18772890](../papers/18772890.md).
    - **[CDKN2A](../genes/CDKN2A.md)** (p14ARF): Deleted in 49% of cases [PMID:18772890](../papers/18772890.md).
    - **[MDM2](../genes/MDM2.md)** (14%) and **[MDM4](../genes/MDM4.md)** (7%) [PMID:18772890](../papers/18772890.md).
- **RB pathway** (88% of cases):
    - **[CDKN2A/B](../genes/CDKN2A.md)** (p16INK4A/CDKN2B): Homozygous deletion of the locus is found in 52% of cases [PMID:18772890](../papers/18772890.md).
    - **[CDK4](../genes/CDK4.md)**: Amplified in 18% of cases [PMID:18772890](../papers/18772890.md).
    - **[RB1](../genes/RB1.md)**: Mutated or deleted in 11% of cases [PMID:18772890](../papers/18772890.md).
- TCGA 2013 multi-platform analysis of 543 primary GBM identified 71 significantly mutated genes; [EGFR](../genes/EGFR.md) altered in 57% (rearrangements, EGFRvIII, novel splice variants); [TERT](../genes/TERT.md) promoter mutations in 84% of deep-coverage cases; [MGMT](../genes/MGMT.md) methylation predicted TMZ response only in classical subtype; proneural survival advantage attributable to G-CIMP epigenotype [PMID:24120142](../papers/24120142.md).
- All 6 hypermutated recurrent grade II astrocytomas (arising after [temozolomide](../drugs/temozolomide.md) therapy) progressed to GBM, acquiring TMZ-signature driver mutations in the RB and AKT–mTOR pathways ([RB1](../genes/RB1.md), [CDKN2A](../genes/CDKN2A.md), [PIK3CA](../genes/PIK3CA.md), [PTEN](../genes/PTEN.md), [MTOR](../genes/MTOR.md)), with validated in vivo mTORC1 hyperactivation [PMID:24336570](../papers/24336570.md).
- TCGA pan-glioma study included 590 GBM cases (56% of 1,122-patient cohort); GBM enriched for TERTp mutations, chr7 gain/chr10 loss, and IDH-wildtype methylation subtypes (Classic-like, Mesenchymal-like, LGm6-GBM); LGm6-GBM cluster had MAPK-pathway alterations in 32% of cases [PMID:26824661](../papers/26824661.md)
- MC3 pan-cancer mutation-calling project (10,510 TCGA pairs) included GBM as one of 33 cancer types; the MC3 MAF provides the somatic variant backbone for [gbm_tcga_pan_can_atlas_2018](../datasets/gbm_tcga_pan_can_atlas_2018.md) in cBioPortal [PMID:29596782](../papers/29596782.md)
- Pan-cancer fusion study (9,624 TCGA samples) included GBM; GBM fusions included chromosome 7 gains in IDH-wildtype GBM; druggable fusions covered 6% of pan-can samples including GBM [PMID:29617662](../papers/29617662.md)
- Pan-cancer aneuploidy study found GBM has the highest rate of any arm-level event (99% of samples, mean score 8.2); IDH-wildtype GBM is characterized by chromosome 7 gain and chromosome 10 loss; GBM clusters in the neural-lineage arm-level group with [LGG](../cancer_types/LGG.md) and melanoma [PMID:29622463](../papers/29622463.md)
- Included in TCGA PanCancer Atlas integrative molecular analysis; IDH1-wildtype LGG co-clusters with GBM in iCluster C23; GBM/LGG (IDH1wt) distinguished by EGFR-driven methylation cluster [PMID:29625048](../papers/29625048.md)
- [EGFR](../genes/EGFR.md) drives methylation cluster 16 in LGG and GBM; LGG/GBM split by methylation cluster not mRNA cluster — IDH1-mutant LGGs occupy methylation cluster 1 (330/351 IDH1-mutant) while EGFR-driven LGG/GBM occupy cluster 16 [PMID:29625049](../papers/29625049.md)
- EGFR altered in 50% of GBM tumors (mutation/amplification/fusion); EGFR amplification co-occurs with KIT/PDGFRA 4q12 amplification in glioma; [CDK4](../genes/CDK4.md)+PI3K combination actionable in 7% of GBM [PMID:29625050](../papers/29625050.md)
- Included in TCGA Pan-Cancer Clinical Data Resource (11,160 patients, 33 cancer types); GBM had shortest median follow-up (~12 months); TCGA-derived median [OS](../cancer_types/OS.md)=12.6 months and PFI=6.1 months, consistent with Stupp 2005 standard-care arms [PMID:29625055](../papers/29625055.md)
- GBM (grade IV) comprised 46/85 (54%) of the adult diffuse glioma liquid-biopsy cohort; in IDH-WT GBM, CSF ctDNA positivity was associated with median OS of 2.04 vs 9.89 months (ctDNA− log-rank p=6.24×10⁻⁵), and truncal alterations (EGFR amplification, CDKN2A/B deletions) were 100% concordant between CSF and tumor in non-hypermutated cases. [PMID:30675060](../papers/30675060.md)
- Longitudinal profiling of 66 recurrent GBM patients treated with PD-1 inhibitors ([nivolumab](../drugs/nivolumab.md) or [pembrolizumab](../drugs/pembrolizumab.md); [gbm_columbia_2019](../datasets/gbm_columbia_2019.md)) showed [PTEN](../genes/PTEN.md) mutations enriched in non-responders (23/32 vs 3/13, OR=8.5, p=0.0063) and MAPK pathway alterations ([BRAF](../genes/BRAF.md), [PTPN11](../genes/PTPN11.md)) enriched in responders; TMB did not predict response [PMID:30742119](../papers/30742119.md).
- In a 923-patient glioma cohort, IDH-WT and IDH-mutant glioblastoma (GBM; n=649 IDH-WT) represented the majority; BRAF V600 mutations were clonal and nearly exclusive to epithelioid IDH-WT GBMs (17/17); 32% of patients harbored actionable lesions (OncoKB levels 1-3); 60% of targeted-therapy recipients were IDH-WT GBMs [PMID:31263031](../papers/31263031.md).
- A Mayo Clinic PDX panel of 96 glioblastoma lines (from 261 patients, 36% engraftment rate; 93 IDH-wildtype, 2 IDH-mutant GBM) recapitulated canonical GBM drivers at frequencies comparable to TCGA: [TERT](../genes/TERT.md) promoter 86%, [CDKN2A](../genes/CDKN2A.md) deletion 70%, PTEN alteration 48%, [TP53](../genes/TP53.md) 36%, EGFR alteration 45%; [PDGFRA](../genes/PDGFRA.md) amplification was absent from all 83 sequenced PDX despite ~15% expected frequency; [MGMT](../genes/MGMT.md) methylation predicted [temozolomide](../drugs/temozolomide.md) response [PMID:31852831](../papers/31852831.md)
- CPTAC proteogenomic profiling of 99 treatment-naive GBMs across 10 omics platforms recapitulated three TCGA subtypes (proneural-like, mesenchymal-like, classical-like) but reclassified 29% of tumors; mixed-subtype tumors (n=12) had significantly worse survival (log-rank p=1.7e-4); TERT promoter mutations were present in 74% and MGMT promoter hypermethylation in 42%; EGFR structural variants with amplification in 45/99 tumors drove convergent phospho-signaling through PTPN11 Y62 and [PLCG1](../genes/PLCG1.md) Y783; drug-connectivity analysis nominated MAPK inhibitors for NF1-altered and broader kinase inhibitors for EGFR-altered GBMs [PMID:33577785](../papers/33577785.md)
- In the GLASS longitudinal cohort (n=128 IDH-wild-type GBM patients with RNA-seq), dominant transcriptional subtype switched in 49% at recurrence (most commonly classical → mesenchymal); acquired [NF1](../genes/NF1.md) mutations drove mesenchymal transition with significant granulocyte increases [PMID:35649412](../papers/35649412.md).

## Subtypes

- **Hypermutator phenotype**: Identified in recurrent GBMs treated with [temozolomide](../drugs/temozolomide.md) that harbor both *[MGMT](../genes/MGMT.md)* promoter methylation and mismatch repair (MMR) deficiencies (e.g., *[MSH6](../genes/MSH6.md)* mutations) [PMID:18772890](../papers/18772890.md).

## Therapeutic landscape

- **Alkylating agents**: **[Temozolomide](../drugs/temozolomide.md)** is a standard treatment; **[MGMT](../genes/MGMT.md)** promoter methylation is a biomarker for response [PMID:18772890](../papers/18772890.md).
- **Combination therapies**: Analysis of core pathway alterations suggests that effective treatment likely requires targeting multiple components within the RTK/RAS/PI3K, p53, and RB pathways [PMID:18772890](../papers/18772890.md).

## Sources

- [PMID:18772890](../papers/18772890.md) — Cancer Genome Atlas Research Network. Comprehensive genomic characterization defines human glioblastoma genes and core pathways. *Nature*. 2008.
- [PMID:28872634](../papers/28872634.md) — Bakas S, et al. Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features. *Sci Data*. 2017.
- [PMID:24120142](../papers/24120142.md)
- [PMID:24336570](../papers/24336570.md)
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29596782](../papers/29596782.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29617662](../papers/29617662.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29622463](../papers/29622463.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29625050](../papers/29625050.md)

- [PMID:29625055](../papers/29625055.md)
- [PMID:30675060](../papers/30675060.md)
- [PMID:30742119](../papers/30742119.md)
- [PMID:31263031](../papers/31263031.md) — Jonsson et al. MSK glioma prospective cohort (Clinical Cancer Research 2019).

*This page was processed by **crosslinker** on **2026-05-21**.*

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31852831](../papers/31852831.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33577785](../papers/33577785.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35649412](../papers/35649412.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
