---
name: Glioblastoma Multiforme
oncotree_code: GBM
main_type: CNS/Brain Cancer
parent: DIFG
tags: []
processed_by: entity-page-writer
processed_at: 2025-05-15
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

## Subtypes

- **Hypermutator phenotype**: Identified in recurrent GBMs treated with [temozolomide](../drugs/temozolomide.md) that harbor both *[MGMT](../genes/MGMT.md)* promoter methylation and mismatch repair (MMR) deficiencies (e.g., *[MSH6](../genes/MSH6.md)* mutations) [PMID:18772890](../papers/18772890.md).

## Therapeutic landscape

- **Alkylating agents**: **[Temozolomide](../drugs/temozolomide.md)** is a standard treatment; **[MGMT](../genes/MGMT.md)** promoter methylation is a biomarker for response [PMID:18772890](../papers/18772890.md).
- **Combination therapies**: Analysis of core pathway alterations suggests that effective treatment likely requires targeting multiple components within the RTK/RAS/PI3K, p53, and RB pathways [PMID:18772890](../papers/18772890.md).

## Sources

- [PMID:18772890](../papers/18772890.md) — Cancer Genome Atlas Research Network. Comprehensive genomic characterization defines human glioblastoma genes and core pathways. *Nature*. 2008.
- [PMID:28872634](../papers/28872634.md) — Bakas S, et al. Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features. *Sci Data*. 2017.

*This page was processed by **entity-page-writer** on **2025-05-15**.*
