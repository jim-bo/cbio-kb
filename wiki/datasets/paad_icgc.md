---
name: ICGC Pancreatic Adenocarcinoma
studyId: paad_icgc
institution: International Cancer Genome Consortium (ICGC)
size: 607
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [whole-genome-seq]
panels: []
tags: [pancreatic-cancer, pdac, icgc, multi-national]
processed_by: entity-page-writer
processed_at: 2026-04-11
---

# ICGC Pancreatic Adenocarcinoma

## Overview

The ICGC Pancreatic Adenocarcinoma dataset (cBioPortal study ID: `paad_icgc`) is a multi-institutional whole-genome sequencing cohort assembled under the International Cancer Genome Consortium (ICGC). It encompasses two major sub-cohorts: the Australian pancreatic cancer genome initiative (PACA-AU, n=375) and the Canadian pancreatic cancer genome project (PACA-CA, n=232), together comprising approximately 607 patients with pancreatic ductal adenocarcinoma (PAAD). The dataset is available on cBioPortal with reference genome hg19.

## Composition

- **Cancer type:** Pancreatic Adenocarcinoma ([PAAD](../cancer_types/PAAD.md))
- **PACA-AU sub-cohort:** ~375 patients from Australia
- **PACA-CA sub-cohort:** ~232 patients from Canada
- **Total:** ~607 patients with matched genomic and (in a subset) survival data
- **Assay:** Whole-genome sequencing
- **Reference genome:** hg19

## Assays / panels (linked)

- Whole-genome sequencing (WGS) — high-depth tumor/normal paired WGS enabling comprehensive detection of somatic SNVs, indels, copy number alterations, and structural variants.

## Papers using this cohort

- [Distinct clinical outcomes and biological features of specific KRAS mutants in human pancreatic cancer](../papers/39214094.md) — McIntyre et al., *Cancer Cell* 2024 [PMID:39214094](../papers/39214094.md)

## Notable findings derived from this cohort

- Used as part of a pooled 950-patient external validation cohort (together with [paad_tcga](../datasets/paad_tcga.md) and the Sausen resectable cohort) to validate KRAS allele-specific survival associations in PDAC; 855 patients with matched genomic and survival data were analyzed [PMID:39214094](../papers/39214094.md).
- In the pooled external cohort, KRAS^G12D^ was associated with the worst median overall survival (15.6 months) compared to KRAS^G12R^ (20.8 months), KRAS^G12V^ (22.4 months), and KRAS^WT^ (27 months; log-rank p=0.006) [PMID:39214094](../papers/39214094.md).
- Multivariate analysis in the pooled cohort confirmed KRAS^G12R^ (HR 0.77, 95% CI 0.60–0.99, p=0.038) and KRAS^G12V^ (HR 0.71, 95% CI 0.58–0.88, p=0.02) as independently predictive of better overall survival relative to KRAS^G12D^ [PMID:39214094](../papers/39214094.md).
- Absence of tumor suppressor co-mutations ([TP53](../genes/TP53.md)/[SMAD4](../genes/SMAD4.md)/[CDKN2A](../genes/CDKN2A.md)) was independently associated with improved OS in the external multi-cohort validation (HR 0.72, 95% CI 0.56–0.92, p=0.009) [PMID:39214094](../papers/39214094.md).

## Sources

- cBioPortal study page: https://www.cbioportal.org/study/summary?id=paad_icgc
- ICGC Data Portal: https://dcc.icgc.org/projects/PACA-AU and https://dcc.icgc.org/projects/PACA-CA

*This page was processed by **entity-page-writer** on **2026-04-11**.*
