---
name: Ewing Sarcoma (MSK, Cancer Research 2024)
studyId: es_dsrct_msk_2023
institution: Memorial Sloan Kettering Cancer Center
size: 290
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - targeted-rna-seq
panels: []
tags:
  - ewing-sarcoma
  - dsrct
  - ewsr1-rearrangement
  - chromoplexy
  - structural-variants
processed_by: crosslinker
processed_at: 2026-09-11
---

# Ewing Sarcoma (MSK, Cancer Research 2024)

## Overview

An MSK-IMPACT database cohort of 277 EWSR1-rearranged small blue round cell tumors — Ewing sarcoma and desmoplastic small round cell tumor ([DSRCT](../cancer_types/DSRCT.md)) — used to characterize [EWSR1](../genes/EWSR1.md) chromoplexy-associated structural rearrangements, with fusions confirmed by targeted DNA (MSK-IMPACT) or RNA (MSK-Archer) sequencing. cBioPortal study record: 290 samples, hg19. Note: the paper's discovery cohort is described as 277 tumors; the cBioPortal record lists 290 samples. [PMID:38335254](../papers/38335254.md)

## Composition

- Discovery cohort: 173 [Ewing sarcoma (ES)](../cancer_types/ES.md) (147 EWSR1::[FLI1](../genes/FLI1.md), 26 EWSR1::[ERG](../genes/ERG.md)) and 104 [DSRCT](../cancer_types/DSRCT.md) (EWSR1::[WT1](../genes/WT1.md)). [PMID:38335254](../papers/38335254.md)
- Control cohort (not part of this dataset): 50 [TMPRSS2](../genes/TMPRSS2.md)::ERG-fused [PRAD](../cancer_types/PRAD.md) samples, checked for non-canonical structural variants. [PMID:38335254](../papers/38335254.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) matched tumor-normal hybridization-capture DNA panel (specific panel version not stated); ≥100X coverage per exon in ≥98% of targeted exons; SNVs/indels via [MuTect](../methods/mutect.md) and [VarDict](../methods/vardict.md). [PMID:38335254](../papers/38335254.md)
- MSK-Archer, a 123-gene anchored multiplex-PCR RNA fusion panel ([Archer FusionPlex](../methods/archer-fusionplex.md)). [PMID:38335254](../papers/38335254.md)

## Papers using this cohort

- [PMID:38335254](../papers/38335254.md) — source publication for this cohort (*Cancer Research*, 2024).

## Notable findings derived from this cohort

## Sources

- cBioPortal study ID: es_dsrct_msk_2023 (name, institution, size, reference_genome from `schema/ontology/studies.json`).

*This page was processed by **crosslinker** on **2026-09-11**.*
