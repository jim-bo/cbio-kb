---
name: "HTAN Human Tumor Atlas — Colorectal Polyp / CRC Atlas (COLON MAP, 2021)"
studyId: crc_hta11_htan_2021
institution: "Vanderbilt University Medical Center / HTAN (NCI U2CCA233291)"
size: 62
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - scrna-seq
  - whole-exome-seq
  - targeted-dna-seq
  - rna-seq
  - multiplexed-immunofluorescence
  - immunohistochemistry
panels: []
tags:
  - colorectal-cancer
  - pre-malignant
  - polyps
  - adenoma
  - serrated-polyps
  - sessile-serrated-lesion
  - single-cell
  - htan
  - tumor-microenvironment
  - msi-h
  - mss
processed_by: crosslinker
processed_at: 2026-05-16
---

# HTAN Human Tumor Atlas — Colorectal Polyp / CRC Atlas (COLON MAP, 2021)

## Overview

Multi-omic pre-cancer atlas of human colorectal polyps and CRC generated through the COLON MAP study at Vanderbilt University Medical Center as part of the NCI Human Tumor Atlas Network (HTAN). The study integrates single-cell RNA-seq, whole-exome and targeted DNA sequencing, bulk RNA-seq, and multiplex imaging across 62 polyp/tumor participants (128 scRNA-seq datasets, 142,065 cells). The atlas spans conventional adenomas (tubular TA, tubulovillous TVA) and serrated polyps (hyperplastic HP, sessile serrated lesion SSL) and early CRC. Data are deposited in cBioPortal and on the HTAN data portal. [PMID:34910928](../papers/34910928.md)

## Composition

- 62 polyp/tumor participants from the COLON MAP study at Vanderbilt University Medical Center; 128 scRNA-seq datasets, 142,065 total single cells. [PMID:34910928](../papers/34910928.md)
- Discovery set: 65 specimens (30 tumors); Validation set: 63 specimens (32 tumors); each specimen bisected for multi-assay analysis, collected ~1 year apart. [PMID:34910928](../papers/34910928.md)
- Cancer/pre-cancer types: [COAD](../cancer_types/COAD.md) and [COADREAD](../cancer_types/COADREAD.md); adenoma subtypes (TA, TVA) and serrated subtypes (GCHP, MVHP, SSL). [PMID:34910928](../papers/34910928.md)
- Orthogonal bulk cohorts: bulk RNA-seq on 66 polyps and targeted DNA-seq on 281 polyps (Tennessee Colorectal Polyp Study); 63 TCGA CRC bulk RNA-seq datasets for external validation. [PMID:34910928](../papers/34910928.md)
- CRC validation: 7 fresh CRCs (2 MSI-H, 5 MSS), 26 CRC whole-tumor blocks (14 MSI-H, 12 MSS), 54-individual CRC TMA, and 60-sample external Broad scRNA-seq CRC cohort. [PMID:34910928](../papers/34910928.md)

## Assays / panels (linked)

- [scRNA-seq](../methods/scrna-seq.md) — inDrop/TruDrop platform with dropkick QC; 142,065 cells across 128 datasets.
- [Whole-exome-seq](../methods/whole-exome-seq.md) — FFPE polyps and CRCs; BWA hg19, GATK4 Mutect2 paired tumor-normal calling.
- [Targeted-dna-seq](../methods/targeted-dna-seq.md) — custom literature-derived panel at 500× on 281 polyps from TCPS.
- [Bulk RNA-seq](../methods/rna-seq.md) — 66 polyps from TCPS.
- [Multiplexed immunofluorescence](../methods/multiplexed-immunofluorescence.md) — Cell DIVE platform (MxIF).
- [Immunohistochemistry](../methods/immunohistochemistry.md) — iterative-chromogen multiplex IHC (MxIHC) on TMA.
- [CMS-classifier](../methods/cms-classifier.md) — consensus molecular subtype scoring.

## Papers using this cohort

- [PMID:34910928](../papers/34910928.md) — Chen et al. (2021) — primary study building the HTAN CRC pre-cancer multi-omic atlas.

## Notable findings derived from this cohort

- Two distinct neoplastic cell populations identified: adenoma-specific cells (ASC) enriched in TA/TVA, and serrated-specific cells (SSC) enriched in SSLs/HPs; these arise from mechanistically separate cell-of-origin programs. [PMID:34910928](../papers/34910928.md)
- Conventional adenomas arise from [APC](../genes/APC.md)-truncation-driven WNT-pathway expansion of [LGR5](../genes/LGR5.md)+ crypt-base stem cells; serrated polyps arise from differentiated luminal-surface cells through [BRAF](../genes/BRAF.md) V600E-driven gastric-type metaplasia ([MUC5AC](../genes/MUC5AC.md)+, CDX2-low). [PMID:34910928](../papers/34910928.md)
- Metaplastic serrated lesions are accompanied by a cytotoxic CD8+ T-cell microenvironment that precedes hypermutation; MSI-H CRCs retain spatially heterogeneous metaplastic vs. stem-like regions in which cytotoxic immune cells are selectively depleted from stem-like compartments. [PMID:34910928](../papers/34910928.md)

## Sources

- cBioPortal study: `crc_hta11_htan_2021`
- Raw data: HTAN data portal (https://data.humantumoratlas.org/), HTAN grant U2CCA233291
- Primary publication: [PMID:34910928](../papers/34910928.md) · DOI: 10.1016/j.cell.2021.11.031 · *Cell* (2021)

*This page was processed by **crosslinker** on **2026-05-16**.*
