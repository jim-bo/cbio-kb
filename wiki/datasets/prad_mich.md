---
name: Prostate Cancer — Michigan WES (prad_mich)
studyId: prad_mich
institution: University of Michigan
size: 112
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
  - STRUCTURAL_VARIANT
panels: []
tags:
  - prostate-cancer
  - wes
  - crpc
  - metastatic
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Prostate Cancer — Michigan WES (prad_mich)

## Overview

A cohort assembled by the University of Michigan comprising 50 lethal metastatic castration-resistant prostate cancers (CRPCs) obtained at rapid autopsy (heavily pretreated, including 3 foci from the same patient) and 11 treatment-naive high-grade localized prostate cancers. An additional screening cohort of 101 localized and 46 CRPCs (total n=147) was used for [FOXA1](../genes/FOXA1.md) analysis. [CHD1](../genes/CHD1.md) findings were validated across 13 independent DNA and RNA-based studies totaling 954 prostate cancers. Methods included whole-exome sequencing, array CGH, gene expression profiling, and transcriptome sequencing.

## Composition

- 50 metastatic CRPC tumors (rapid autopsy, heavily pretreated).
- 11 treatment-naive high-grade localized prostate cancers.
- Extended cohort: 147 total for FOXA1 analysis; 954 across 13 studies for CHD1 validation.
- Cancer type: [PRAD](../cancer_types/PRAD.md) (prostate adenocarcinoma).
- Key clinical fields: ETS fusion status, castration resistance, CHD1 deletion status.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — primary mutation discovery.
- Array CGH — copy-number profiling.
- Transcriptome sequencing — fusion gene detection.
- Gene expression profiling — [AR](../genes/AR.md) pathway activity.

## Papers using this cohort

- [PMID:22722839](../papers/22722839.md) — Integrative clinical genomics of advanced prostate cancer (Grasso et al., 2012).

## Notable findings derived from this cohort

- Nine significantly mutated genes identified (FDR ≤ 0.10): [TP53](../genes/TP53.md), [AR](../genes/AR.md), [ZFHX3](../genes/ZFHX3.md), [RB1](../genes/RB1.md), [PTEN](../genes/PTEN.md), [APC](../genes/APC.md), [KMT2D](../genes/KMT2D.md), [OR5L1](../genes/OR5L1.md), [CDK12](../genes/CDK12.md) [PMID:22722839](../papers/22722839.md).
- [CHD1](../genes/CHD1.md) focal deletion/mutation in 8% of prostate cancers; 96% of CHD1-deleted cases were ETS fusion-negative (p<0.0001 across 954 tumors) [PMID:22722839](../papers/22722839.md).
- [FOXA1](../genes/FOXA1.md) mutations (3.4% of cases) cluster in the C-terminal transactivation domain, repressing the AR transcriptional program and increasing xenograft tumor growth [PMID:22722839](../papers/22722839.md).
- [TMPRSS2](../genes/TMPRSS2.md):[ERG](../genes/ERG.md) fusion present in the majority of ETS+ cases; [ETS2](../genes/ETS2.md) deleted in ~1/3 of CRPCs [PMID:22722839](../papers/22722839.md).
- Overall mutation rate in CRPC is low (2.00/Mb), confirming monoclonal origin; genomic complexity arises primarily from copy-number alterations and rearrangements [PMID:22722839](../papers/22722839.md).

## Sources

- [PMID:22722839](../papers/22722839.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
