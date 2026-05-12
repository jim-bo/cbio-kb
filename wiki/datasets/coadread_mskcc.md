---
name: MSKCC Colorectal Adenocarcinoma Triplets
studyId: coadread_mskcc
institution: Memorial Sloan Kettering Cancer Center
size: "69"
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - whole-genome-seq
panels:
  - msk-impact-panel
tags:
  - colorectal-cancer
  - metastasis
  - primary-met-concordance
  - msk-impact
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# MSKCC Colorectal Adenocarcinoma Triplets

## Overview

69 matched patient trios (primary tumor, metastasis, and normal tissue) from microsatellite-stable colorectal cancer patients at Memorial Sloan Kettering Cancer Center. All patients were MSS; 62/69 (90%) presented at stage IV. Raw data deposited in dbGaP phs000790.v1.p1. The cohort was designed to assess primary-vs-metastasis mutation concordance for clinical sequencing decisions.

## Composition

- 69 patient trios; primary tumor location: right colon 28 (40%), left colon 30 (44%), rectum 11 (16%).
- 30 (43.5%) chemonaive prior to resection; 39 (56.5%) prior therapy. No anti-EGFR treatment before resection.
- Cancer type: [COADREAD](../cancer_types/COADREAD.md).
- Assay: [msk-impact-panel](../methods/msk-impact-panel.md) (230-gene custom capture, mean 692× target coverage); WGS validation in 4 trios.

## Assays / panels (linked)

- [msk-impact-panel](../methods/msk-impact-panel.md)
- [whole-genome-seq](../methods/whole-genome-seq.md)

## Papers using this cohort

- [PMID:25164765](../papers/25164765.md)

## Notable findings derived from this cohort

- [KRAS](../genes/KRAS.md), [NRAS](../genes/NRAS.md), and [BRAF](../genes/BRAF.md) mutations were 100% concordant between primary tumor and metastasis across all 69 trios, supporting single-site sequencing for clinical anti-EGFR eligibility decisions [PMID:25164765](../papers/25164765.md).
- 93% overall concordance for recurrent driver mutations; 18 private mutations (discordant) were found in [APC](../genes/APC.md) (n=7), [PIK3CA](../genes/PIK3CA.md) (n=5), [SMAD4](../genes/SMAD4.md) (n=3), and [TP53](../genes/TP53.md) (n=3) [PMID:25164765](../papers/25164765.md).
- Metastasis-private RTK-RAS events ([MAP2K1](../genes/MAP2K1.md) Q56P, [EGFR](../genes/EGFR.md) amplification) were identified in RAS/RAF wild-type cases, demonstrating actionable heterogeneity missed by primary-only sequencing [PMID:25164765](../papers/25164765.md).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-11**.*
