---
name: Melanoma
oncotree_code: MEL
main_type: Melanoma
parent: SKIN
tags: [melanoma, skin]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Melanoma (MEL)

## Overview

Melanoma (OncoTree code MEL, parent [SKIN](../cancer_types/SKIN.md)) is a malignant neoplasm of melanocytes. In the corpus, melanoma appears primarily in the context of CNS metastases and CSF circulating tumor DNA profiling.

## Cohorts in the corpus

- [csf_msk_2024](../datasets/csf_msk_2024.md): Melanoma patients with CNS involvement were included in the MSK CSF ctDNA cohort (1,007 CSF samples from 711 patients across >90 tumor types) [PMID:39289779](../papers/39289779.md).
- Epidemiologic cohort (Northwestern University): 2,934 tanning bed users vs. 2,929 controls; exome sequencing of 182 single melanocytes from 26 donors. Dataset: [normal_skin_melanocytes_2024](../datasets/normal_skin_melanocytes_2024.md). [PMID:38895302](../papers/38895302.md)
- Pan-cancer liquid biopsy VTE cohort (MSK): melanoma comprised 7% of the 4,141-patient discovery cohort profiled by MSK-ACCESS. Dataset: [msk_ctdna_vte_2024](../datasets/msk_ctdna_vte_2024.md). [PMID:39147831](../papers/39147831.md)
- ATLAS classifier validation set: melanoma included in 22-class cancer site-of-origin and 8-class lineage models. [PMID:27634761](../papers/27634761.md)
- MSK pan-cancer [BRAF](../genes/BRAF.md) fusion study: MEL represented as a histology within the 97,024-sample cohort; [TERT](../genes/TERT.md) mutations co-occurred with [BRAF](../genes/BRAF.md) fusions in 64% of melanomas. [PMID:38922339](../papers/38922339.md)

## Recurrent alterations

- [BRAF](../genes/BRAF.md) p.V600E detected in CSF ctDNA from melanoma patients with leptomeningeal disease [PMID:39289779](../papers/39289779.md).
- [BRAF](../genes/BRAF.md) fusions (non-V600E): [TERT](../genes/TERT.md) mutations co-occur with BRAF fusions in 64% of melanoma BRAF fusion cases; melanoma is among the histologies in which BRAF fusions occur at low frequency as de novo or acquired events. [PMID:38922339](../papers/38922339.md)
- [TP53](../genes/TP53.md) was the most frequently altered gene across all tumor types in the CSF ctDNA cohort (49% of ctDNA-positive samples), including melanoma [PMID:39289779](../papers/39289779.md).
- [NF1](../genes/NF1.md) — most frequently pathogenically mutated gene in normal melanocytes from tanning bed users; multiple loss-of-function mutations observed. [PMID:38895302](../papers/38895302.md)
- [BRAF](../genes/BRAF.md) L597R and G466R pathogenic mutations identified in melanocytes from tanning cohort donors. [PMID:38895302](../papers/38895302.md)
- COSMIC mutational signature 11 significantly enriched in tanning bed users' melanocytes (P=0.0405), distinct from standard UV SBS7a signature. [PMID:38895302](../papers/38895302.md)
- CCLE pharmacogenomic profiling included melanoma cell lines among 947 lines tested across 24 drugs; elastic-net models predicted drug sensitivity from genomic features [PMID:22460905](../papers/22460905.md)
- WGS of 25 melanoma tumors identified PREX2 as a recurrently mutated driver and characterized KIT and BRAF alteration patterns [PMID:22622578](../papers/22622578.md)
- WES of 121 melanomas (Broad) identified MAP2K1, PPP6C, and RAC1 P29S as novel significantly mutated genes; median somatic mutation rate of 14.4/Mb with 82% UV-signature C>T transitions [PMID:22817889](../papers/22817889.md)
- WES of 147 melanomas (Yale) confirmed RAC1 P29S in 9.2% of sun-exposed tumors (third most common driver after BRAF/NRAS) and PPP6C mutations in 12.4% of sun-exposed tumors; three molecular melanoma classes defined by mutation burden and copy-number profile [PMID:22842228](../papers/22842228.md)
- Anti-PD-1 response genomics in 38 metastatic melanoma cases: IPRES transcriptional co-enrichment (mesenchymal transition, angiogenesis, hypoxia) marked innate resistance independently of mutational load; BRCA2 LOF mutations enriched in responders (OR=6.2) [PMID:26997480](../papers/26997480.md)
- In the MSK-IMPACT pan-cancer cohort, TERT promoter mutations were present in 49% of melanoma (predominantly cutaneous); UV mutation signatures predominated in melanoma; 56% of MEL patients harbored an OncoKB-actionable alteration (4th highest); a novel recurrent CDK5RAP2-BRAF fusion was identified in two melanomas; 75 non-melanoma BRAF V600 patients showed identical 71% clinical-benefit rate to melanoma BRAF V600 patients on BRAF-targeted therapy. [PMID:28481359](../papers/28481359.md)
- Included in pan-cancer pathway analysis of 9,125 TCGA tumors; MEL (melanoma) context referenced for BRAF hotspot mutations at 51% in SKCM and NRF2/oxidative-stress pathway data [PMID:29625050](../papers/29625050.md)

## Subtypes

- Metastatic melanoma with CNS involvement (brain metastases and leptomeningeal disease) represented in the CSF ctDNA cohort [PMID:39289779](../papers/39289779.md).
- Indoor tanning creates melanoma risk profile resembling familial melanoma: early onset, multiple primaries, and broad field of at-risk melanocytes. Tanning bed users had elevated melanoma risk (OR 2.0, 95% CI 1.38--2.98) after adjusting for age, family history, and sunburn history, with dose-dependent relationship (P<0.0001). [PMID:38895302](../papers/38895302.md)
- Lineage de-differentiation score was prognostic for survival in primary melanoma (HR 0.0001, P=0.001) and metastatic melanoma (HR 0.31, P=0.033) in the ATLAS classifier study. [PMID:27634761](../papers/27634761.md)

## Therapeutic landscape

- 50.7% of ctDNA-positive CSF samples across all tumor types carried a level 1 OncoKB actionable alteration; [BRAF](../genes/BRAF.md) V600E in melanoma is a level 1 actionable target [PMID:39289779](../papers/39289779.md).
- UV mutational signatures identified in CSF ctDNA from melanoma samples (n=3 among 35 high-TMB samples), aiding confirmation of melanoma as the primary tumor site [PMID:39289779](../papers/39289779.md).
- ctDNA detection associated with higher VTE risk (HR=2.49) in pan-cancer cohort including melanoma (7% of discovery cohort); anticoagulation associated with lower VTE in ctDNA-positive patients (adjusted HR=0.50). [PMID:39147831](../papers/39147831.md)
- Marketing claims that tanning beds are safer than sunlight are contradicted by elevated mutation burden specifically in low-CSD body sites; distinct signature 11 may serve as molecular marker to distinguish tanning-bed-induced melanomas. [PMID:38895302](../papers/38895302.md)

## Sources

- [PMID:27634761](../papers/27634761.md)
- [PMID:38895302](../papers/38895302.md)
- [PMID:38922339](../papers/38922339.md)
- [PMID:39147831](../papers/39147831.md)
- [PMID:39289779](../papers/39289779.md)

*This page was processed by **crosslinker** on **2026-05-04**.*
- [PMID:22460905](../papers/22460905.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
- [PMID:22622578](../papers/22622578.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
- [PMID:22817889](../papers/22817889.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
- [PMID:22842228](../papers/22842228.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
- [PMID:26997480](../papers/26997480.md)

- [PMID:28481359](../papers/28481359.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
