---
name: Soft Tissue and Bone Sarcoma (MSK, Nat Commun 2022)
studyId: sarcoma_msk_2022
institution: Memorial Sloan Kettering Cancer Center / Foundation Medicine
size: 7494
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - FoundationOne Heme (465 genes + RNA-seq)
panels:
  - foundationone-heme
tags:
  - sarcoma
  - soft tissue
  - bone
  - tumor-only sequencing
  - FoundationOne
processed_by: crosslinker
processed_at: 2026-05-21
---

# Soft Tissue and Bone Sarcoma (MSK, Nat Commun 2022)

## Overview

Targeted sequencing of 7,494 soft tissue and bone sarcoma samples across 44 histologies, profiled from 2012–2018 using FoundationOne Heme (hybrid-capture DNA sequencing of 465 genes, median 704x coverage, plus RNA-seq of 333 rearrangement genes). This is a tumor-only profiling dataset. A clinical sub-cohort of 118 adult sarcoma patients at MSK with linked outcomes was used to assess real-world actionability. Reads were aligned to hg19 via BWA v0.5.9. Actionability was assessed using OncoKB levels with data cutoff June 8, 2021. Note: this dataset (FoundationOne Heme, tumor-only) is distinct from `sarcoma_mskcc_2022` (MSK-IMPACT, paired tumor-normal).

## Composition

- 81.0% soft tissue (n=6,067), 14.7% bone (n=1,105), 4.3% other (n=322)
- Median age 53 (range <1–89); 53.4% female
- Pediatric-adolescent-young-adult (P-AYA, ≤30 years): 21.8% (1,636/7,494)
- Translocation-associated: n=1,724 (23.0%); genomically complex/other: n=5,770 (77.0%)
- Most common subtypes: sarcoma NOS 17.2%, leiomyosarcoma ([LMS](../cancer_types/LMS.md)) 12.7%
- Cancer type: soft tissue sarcoma / bone sarcoma

## Assays / panels (linked)

- [FoundationOne Heme](../methods/foundationone.md): 465-gene DNA panel + RNA-seq of 333 rearrangement genes; tumor-only
- [OncoKB](../methods/oncokb.md) annotation for actionability levels
- COSMIC v2 (30 signatures) mutational signature decomposition

## Papers using this cohort

- [PMID:35705558](../papers/35705558.md) — Gounder et al., Nat Commun 2022. Primary study: comprehensive genomic profiling of 7,494 sarcomas.

## Notable findings derived from this cohort

- 31.7% (2,372/7,494) harbored ≥1 OncoKB actionable alteration; diagnostic reclassification in 10.5% of cases; [TP53](../genes/TP53.md) pathway altered in 47.8%, Rb pathway in 46.8%; kinase fusions actionable in 2.6%; novel TNS1-ALK fusion in leiomyosarcoma (16 cases); MMR-D in 2.1%, MSI-H in 0.29%; HRD-pathway alterations in 2.5%; TMB ≥10 mut/Mb in 3.9%; [CD274](../genes/CD274.md) amplification in 1.0% [PMID:35705558](../papers/35705558.md)

## Sources

- cBioPortal study: `sarcoma_msk_2022`
- Citation: Gounder et al. Nat Commun 2022 [PMID:35705558](../papers/35705558.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
