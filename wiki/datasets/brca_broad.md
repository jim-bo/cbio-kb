---
name: Breast Cancer — Broad WES/WGS (brca_broad)
studyId: brca_broad
institution: Broad Institute
size: 103
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - STRUCTURAL_VARIANT
  - COPY_NUMBER_ALTERATION
panels: []
tags:
  - breast-cancer
  - wes
  - wgs
  - fusion
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Breast Cancer — Broad WES/WGS (brca_broad)

## Overview

A cohort of 108 primary, treatment-naive breast carcinoma/normal DNA pairs (patients from Mexico n=54 and Vietnam n=49) assembled by the Broad Institute. 103 pairs underwent whole-exome sequencing (33 Mb target, median 85.1% bases at ≥30x) and 22 pairs underwent whole-genome sequencing at 30x. Mutation calling used [MutSig](../methods/mutsig.md); copy-number used ABSOLUTE/HAPSEG; rearrangements were called with dRanger. An additional 235 samples were screened for the MAGI3-AKT3 fusion by RT-PCR.

## Composition

- 103 primary breast tumors with matched normal DNA for WES; 22 pairs with WGS.
- Subtypes represented: Luminal A, Luminal B, HER2-enriched, basal-like.
- Cancer type: [BRCA](../cancer_types/BRCA.md).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 33 Mb target, median 85.1% at 30x.
- [whole-genome-seq](../methods/whole-genome-seq.md) — 30x, 22 pairs; structural variant discovery.
- [mutsig](../methods/mutsig.md) — statistical identification of significantly mutated genes.

## Papers using this cohort

- [PMID:22722202](../papers/22722202.md) — Comprehensive genomic characterization of breast cancer (Banerji et al., 2012).

## Notable findings derived from this cohort

- Six significantly mutated genes (FDR < 0.1): [TP53](../genes/TP53.md) (27%), [PIK3CA](../genes/PIK3CA.md) (27%), [AKT1](../genes/AKT1.md) (6%), [GATA3](../genes/GATA3.md) (4%), [MAP3K1](../genes/MAP3K1.md) (3%), [CBFB](../genes/CBFB.md) (4%) [PMID:22722202](../papers/22722202.md).
- [CBFB](../genes/CBFB.md) identified as significantly mutated in breast cancer for the first time — 4 ER+ samples with truncating mutations [PMID:22722202](../papers/22722202.md).
- Recurrent [MAGI3](../genes/MAGI3.md)-[AKT3](../genes/AKT3.md) fusion found in 8/235 (3.4%) additional samples, including 5/72 (6.9%) triple-negative cases; represents an activating in-frame fusion kinase [PMID:22722202](../papers/22722202.md).
- [AKT1](../genes/AKT1.md) and [PIK3CA](../genes/PIK3CA.md) mutations were mutually exclusive; combined PI3K pathway activation in ~33% of tumors [PMID:22722202](../papers/22722202.md).
- [ERBB2](../genes/ERBB2.md) activating S310F mutations found in 2 samples without [ERBB2](../genes/ERBB2.md) amplification [PMID:22722202](../papers/22722202.md).
- GSK-690693 (AKT inhibitor) and MK-2206 tested as potential therapeutic options targeting AKT pathway alterations including the MAGI3-AKT3 fusion [PMID:22722202](../papers/22722202.md).

## Sources

- [PMID:22722202](../papers/22722202.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
