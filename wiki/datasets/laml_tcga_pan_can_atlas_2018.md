---
name: Acute Myeloid Leukemia (TCGA, PanCancer Atlas 2018)
studyId: laml_tcga_pan_can_atlas_2018
institution: The Cancer Genome Atlas (TCGA)
size: 200
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - WES
  - RNA-seq
  - SNP array
panels: []
tags:
  - laml
  - aml
  - leukemia
  - TCGA
  - pan-cancer
  - pan-can-atlas
processed_by: crosslinker
processed_at: 2026-05-15
---

# Acute Myeloid Leukemia (TCGA, PanCancer Atlas 2018)

## Overview

The TCGA [AML](../cancer_types/AML.md) PanCancer Atlas 2018 cohort is the acute myeloid leukemia arm of the TCGA PanCancer Atlas, available in cBioPortal as `laml_tcga_pan_can_atlas_2018`. It encompasses TCGA [LAML](../cancer_types/LAML.md) samples with uniformly reprocessed mutation calls (MC3 pipeline), copy-number profiles, and RNA-seq expression. LAML presents unique analytical challenges in the MC3 pipeline because the "normal" skin biopsies frequently contain blood enriched with tumor cells, leading to conservative misclassification of somatic calls as germline.

## Composition

- Cancer type: Acute Myeloid Leukemia ([AML](../cancer_types/AML.md)), OncoTree code AML.
- Approximately 200 tumor samples.
- Data modalities: WES, RNA-seq, SNP array.
- Somatic mutations from MC3 ensemble pipeline; LAML recovered only 44% of legacy AWG calls due to tumor-in-normal contamination artifact.
- Copy-number from Affymetrix SNP 6.0 / ABSOLUTE.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)

## Papers using this cohort

- [PMID:29617662](../papers/29617662.md) — Pan-cancer fusion catalog (Gao et al., 2018)

## Notable findings derived from this cohort

- Pan-cancer RNA-seq fusion analysis (9,624 TCGA tumors) identified a distinct LAML fusion landscape: 14.0% of LAML tumors had fusions but no driver-gene point mutations ("fusion-only" tumors), including classic leukemic fusions [CBFB](../genes/CBFB.md)-[MYH11](../genes/MYH11.md) (n=3), [BCR](../genes/BCR.md)-[ABL1](../genes/ABL1.md) (n=2), [PML](../genes/PML.md)-[RARA](../genes/RARA.md) (n=2), and [NUP98](../genes/NUP98.md)-[NSD1](../genes/NSD1.md) (n=2); [PML](../genes/PML.md)-[RARA](../genes/RARA.md) is a druggable target in 16 LAML samples per DEPO annotation [PMID:29617662](../papers/29617662.md).
- [CBFB](../genes/CBFB.md) is fused but rarely mutated in LAML, representing an alternative mechanism of inactivation for this transcriptional regulator; strict mutual exclusivity between [CBFB](../genes/CBFB.md) fusions and CBFB point mutations observed [PMID:29617662](../papers/29617662.md).
- LAML has among the lowest aneuploidy scores in the pan-cancer cohort (mean 1.6), consistent with the known biology of leukemia as a predominantly mutation/fusion-driven rather than chromosomal-instability-driven disease [PMID:29617662](../papers/29617662.md).

## Sources

- cBioPortal study: `laml_tcga_pan_can_atlas_2018`
- [PMID:29617662](../papers/29617662.md)

*This page was processed by **crosslinker** on **2026-05-15**.*
