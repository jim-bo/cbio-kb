---
name: Lung Adenocarcinoma (OncoSG, 2020)
studyId: luad_oncosg_2020
institution: Genome Institute of Singapore (GIS) / National University Cancer Institute Singapore
size: 110
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - rna-seq
panels: []
tags:
  - luad
  - lung
  - adenocarcinoma
  - never-smoker
  - asian
  - singapore
  - validation-cohort
processed_by: crosslinker
processed_at: 2026-05-16
---

# Lung Adenocarcinoma (OncoSG, 2020)

## Overview

The OncoSG [LUAD](../cancer_types/LUAD.md) cohort (cBioPortal `luad_oncosg_2020`) is a 110-sample lung adenocarcinoma dataset assembled by the Genome Institute of Singapore (GIS) from patients of predominantly East Asian ancestry, available via the European Genome-phenome Archive (EGA accession EGAD00001004421). All tumors are from never-smoker patients. The cohort is used as an independent external validation set for transcriptomic classifiers and prognostic signatures developed in larger discovery cohorts.

## Composition

- **110 never-smoker lung adenocarcinoma tumors** of Asian (predominantly East Asian) ancestry.
- Cancer type: [LUAD](../cancer_types/LUAD.md).
- All samples treatment-naive at time of collection.
- Subtype composition when classified by the Sherlock-Lung 60-gene signature [PMID:32015526](../papers/32015526.md): 35 steady / 64 proliferative / 11 chaotic.

## Assays / panels (linked)

- [rna-seq](../methods/rna-seq.md) — transcriptome profiling used for subtype classification and survival analyses.

## Papers using this cohort

- [PMID:32015526](../papers/32015526.md) — Zhao et al. 2025, *bioRxiv*: Used as external validation cohort for the Sherlock-Lung 60-gene NS-LUAD prognostic signature; steady subtype HR=0.32 (95% CI 0.12–0.87, p=0.026) for overall survival.

## Notable findings derived from this cohort

- External validation of the Sherlock-Lung 60-gene transcriptomic signature: classified 35 steady / 64 proliferative / 11 chaotic NS-LUAD tumors; steady subtype HR=0.32 (95% CI 0.12–0.87, p=0.026) for overall survival, remaining significant within TP53-wild-type cases; mortality c-index=0.682; expression subtype + stage achieved c-index=0.68, outperforming stage, mutation, or grade alone [PMID:32015526](../papers/32015526.md).
- The chaotic subtype arm (n=11) was underpowered for survival inference; authors flag this as a limitation requiring a larger Asian never-smoker cohort [PMID:32015526](../papers/32015526.md).

## Sources

- cBioPortal study: `luad_oncosg_2020`
- EGA accession: EGAD00001004421
- [PMID:32015526](../papers/32015526.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
