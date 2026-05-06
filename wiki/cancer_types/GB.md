---
name: Glioblastoma, IDH-Wildtype
oncotree_code: GB
main_type: Glioma
parent: ADIFG
tags: []
processed_by: crosslinker
processed_at: 2026-05-04
---

# Glioblastoma, IDH-Wildtype (GB)

## Overview

Glioblastoma, IDH-wildtype (GB) is the most common and aggressive primary brain tumor in adults, characterized by IDH-wildtype status and WHO grade 4 designation. On OncoTree it is a child of Adult Diffuse Glioma (ADIFG). It is distinguished from IDH-mutant astrocytoma by its wild-type IDH status, distinct epigenetic profile, and uniformly aggressive clinical course.

## Cohorts in the corpus

- Interim integrative analysis of 206 newly diagnosed glioblastoma ([GBM](../cancer_types/GBM.md)) cases from The Cancer Genome Atlas (TCGA), with 91 cases undergoing nucleotide sequence analysis. [PMID:18772890](../papers/18772890.md)
- 60 IDH-wildtype glioblastoma patients from the GLASS International consortium ([difg_glass](../datasets/difg_glass.md)), with matched initial and first-recurrent DNA methylation data (Illumina 450K/EPIC arrays). [PMID:38117484](../papers/38117484.md)
- LN229 ([EGFR](../genes/EGFR.md)−/low, GB cell line): negative-control model in ADC radiosensitization study — C-MMAE did not accumulate in LN229 xenografts and did not radiosensitize LN229 cells in vitro, confirming receptor-selectivity requirement. [PMID:27698471](../papers/27698471.md)
- Bakas 2017 published expert MRI segmentations and radiomic features for the TCGA-GBM collection (n=262 IDH-wildtype glioblastoma cases), providing multiparametric MRI (T1, T1Gd, T2, FLAIR) with manually delineated tumor sub-region labels and extracted radiomic features [PMID:28872634](../papers/28872634.md).

## Recurrent alterations

- Nearly all GBMs (88-90%) exhibit alterations in three core signaling pathways: **RTK/RAS/PI3K** (88% of cases; [EGFR](../genes/EGFR.md), [NF1](../genes/NF1.md), [PTEN](../genes/PTEN.md), [PIK3R1](../genes/PIK3R1.md)), **p53** (78% of cases; [TP53](../genes/TP53.md), [MDM2](../genes/MDM2.md), [CDKN2A](../genes/CDKN2A.md)), and **RB** (88% of cases; [RB1](../genes/RB1.md), [CDKN2A/B](../genes/CDKN2A.md), [CDK4](../genes/CDK4.md)). [PMID:18772890](../papers/18772890.md)
- [PIK3R1](../genes/PIK3R1.md) — frequent mutations (10%) identified in GBM, often in the iSH2 domain, which disrupt p110α interaction and activate the PI3K pathway. [PMID:18772890](../papers/18772890.md)
- [NF1](../genes/NF1.md) — somatic mutations and deletions occur in 18% of cases, identifying it as a major tumor suppressor in GBM. [PMID:18772890](../papers/18772890.md)
- Extracellular domain mutations in [EGFR](../genes/EGFR.md) (novel missense) and [ERBB2](../genes/ERBB2.md) (8% of cases) contribute to RTK pathway activation. [PMID:18772890](../papers/18772890.md)
- IDH-wildtype status defines GB: these tumors maintain stable epigenomes over time, with low global methylation at both initial diagnosis and recurrence (zero CpG probes showing differential methylation >15% between initial and recurrent tumors). [PMID:38117484](../papers/38117484.md)
- [TERT](../genes/TERT.md) — mutations co-occur with [BRAF](../genes/BRAF.md) fusions in gliomas (11% co-occurrence); [TERT](../genes/TERT.md) mutations found in glioma subset. [PMID:38922339](../papers/38922339.md)
- [EGFR](../genes/EGFR.md) — amplification is a hallmark of IDH-wildtype glioblastoma (not specifically quantified in these corpus studies).
- [EGFR](../genes/EGFR.md) low/absent expression in LN229 GB cells prevents C-MMAE binding, accumulation, and radiosensitization — confirms that [EGFR](../genes/EGFR.md) expression level, not mere tumor histology, gates ADC activity. [PMID:27698471](../papers/27698471.md)

## Subtypes

- IDH-wildtype glioblastoma has a stable epigenome compared to IDH-mutant gliomas, which undergo progressive demethylation at recurrence. [PMID:38117484](../papers/38117484.md)
- [BRAF](../genes/BRAF.md) fusions occur at low frequency (<1%) across gliomas; pilocytic astrocytoma (a pediatric low-grade glioma, not GB) has 56% [BRAF](../genes/BRAF.md) fusion prevalence; adult IDH-wildtype GB is not specifically enriched for BRAF fusions. [PMID:38922339](../papers/38922339.md)

## Therapeutic landscape

- *[MGMT](../genes/MGMT.md)* promoter methylation is a biomarker for response to alkylating agents like [temozolomide](../drugs/temozolomide.md). [PMID:18772890](../papers/18772890.md)
- Recurrent GBMs treated with [temozolomide](../drugs/temozolomide.md) may develop a hypermutator phenotype if they possess both *[MGMT](../genes/MGMT.md)* promoter methylation and mutations in mismatch repair genes (e.g., [MSH6](../genes/MSH6.md)). [PMID:18772890](../papers/18772890.md)
- Effective GBM treatment likely requires combination therapies targeting multiple core pathways (RTK, p53, RB). [PMID:18772890](../papers/18772890.md)
- Unlike IDH-mutant gliomas, IDH-wildtype GB does not show treatment-induced epigenetic evolution at recurrence; epigenomic stability means the tumor biology at recurrence resembles the primary tumor. [PMID:38117484](../papers/38117484.md)
- EGFR-directed ADC radiosensitization (C-MMAE) requires sufficient receptor surface expression; LN229 (EGFR-low GB) xenografts showed no C-MMAE accumulation by Cy5 fluorescence imaging and no radiosensitization, highlighting that not all GB tumors will be susceptible to EGFR-directed ADC approaches. [PMID:27698471](../papers/27698471.md)

## Sources

- [PMID:18772890](../papers/18772890.md) — Comprehensive genomic characterization defines human glioblastoma genes and core pathways (Nature, 2008)
- [PMID:38117484](../papers/38117484.md) — The Epigenetic Evolution of Glioma Is Determined by the [IDH1](../genes/IDH1.md) Mutation Status and Treatment Regimen (Cancer Research, 2024)
- [PMID:38922339](../papers/38922339.md) — Tumor-agnostic genomic and clinical analysis of BRAF fusions identify actionable targets (Clinical Cancer Research, 2024)
- [PMID:27698471](../papers/27698471.md)
- [PMID:28872634](../papers/28872634.md)

*This page was processed by **crosslinker** on **2026-05-04**.*
