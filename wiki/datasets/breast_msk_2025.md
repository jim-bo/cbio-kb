---
name: Breast Cancer (MSK, Nat Genet 2025)
studyId: breast_msk_2025
institution: Memorial Sloan Kettering Cancer Center
size: 3879
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - whole-genome-seq
panels: []
tags:
  - breast-cancer
  - msk-impact
  - apobec-mutagenesis
  - mutational-signatures
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Breast Cancer (MSK, Nat Genet 2025)

## Overview

An MSK-IMPACT clinicogenomic cohort of 3,880 high-quality breast cancer samples from 3,117 patients (341–505 gene panel versions, sequenced 2014–2021, data freeze June 2022), used to deconvolute dominant mutational signatures (APOBEC3, HRD, Clock) per sample with the SigMA tool. cBioPortal study record: 3,879 clinical cases, hg19. [PMID:40379787](../papers/40379787.md)

## Composition

- 3,880 samples / 3,117 patients after excluding sequencing-estimated tumor purity <20% from an initial 5,831 retrieved. [PMID:40379787](../papers/40379787.md)
- Cancer type: [BRCA](../cancer_types/BRCA.md). Receptor-subtype composition: 2,133 (68.4%) HR+/HER2−, 276 (8.9%) HR+/HER2+, 149 (4.8%) HR−/HER2+, 559 (17.9%) TNBC. [PMID:40379787](../papers/40379787.md)
- Longitudinal subset: 449 HR+/HER2− patients with 2 sequential MSK-IMPACT samples and 43 with ≥3. [PMID:40379787](../papers/40379787.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) tumor-normal targeted sequencing, 341–505 gene panel versions. [PMID:40379787](../papers/40379787.md)
- Deep [whole-genome sequencing](../methods/whole-genome-seq.md) validation — 5 paired primary/metastatic samples (MSK-BR-WGS series) plus 29 breast cancer cell lines. [PMID:40379787](../papers/40379787.md)

## Papers using this cohort

- [PMID:40379787](../papers/40379787.md) — Gupta et al., *Nature Genetics* (2025): source publication for this cohort (APOBEC3-driven mutagenesis in breast cancer).

## Notable findings derived from this cohort

## Sources

- cBioPortal study ID: breast_msk_2025 (name, institution, size, reference_genome from `schema/ontology/studies.json`).

*This page was processed by **entity-page-writer** on **2026-09-10**.*
