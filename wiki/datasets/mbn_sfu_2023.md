---
name: Mature B-Cell Neoplasms (Simon Fraser University, Blood 2023)
studyId: mbn_sfu_2023
institution: Simon Fraser University
size: 297
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - rna-seq
panels: []
tags:
  - burkitt-lymphoma
  - DLBCL
  - EBV
  - lymphoma
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# Mature B-Cell Neoplasms (Simon Fraser University, Blood 2023)

## Overview

Whole-genome and/or transcriptome sequencing of Burkitt lymphoma ([BL](../cancer_types/BL.md)) and diffuse large B-cell lymphoma ([DLBCLNOS](../cancer_types/DLBCLNOS.md)) cases assembled by Thomas et al. (Simon Fraser University), with cases collected in Uganda, the United States, Brazil, France, Germany and Canada. Name, institution, size (297) and reference genome (hg38) are taken from the cBioPortal study record in `schema/ontology/studies.json`; the study aggregates 281 BL cases (181 pediatric, 100 adult) and additional DLBCL comparator material [PMID:36201743](../papers/36201743.md).

## Composition

- 281 Burkitt lymphomas: 181 pediatric (pBL), 100 adult (aBL); 148 (53%) EBV-positive, 133 (47%) EBV-negative [PMID:36201743](../papers/36201743.md).
- 295 diffuse large B-cell lymphoma ([DLBCLNOS](../cancer_types/DLBCLNOS.md)) tumors used as a comparator group (methods list 280 newly sequenced plus additional cell lines) [PMID:36201743](../papers/36201743.md).
- Core genomic analysis used 230 BL genomes with WGS (118 EBV-positive, 112 EBV-negative); the cBioPortal record lists 297 samples on hg38, which does not map 1:1 onto any single analytic subset described in the paper text [PMID:36201743](../papers/36201743.md).

## Assays / panels (linked)

- [Whole-genome sequencing](../methods/whole-genome-seq.md) (BL reads aligned to GRCh38, DLBCL reads to GRCh37) and [RNA-seq](../methods/rna-seq.md) [PMID:36201743](../papers/36201743.md).

## Papers using this cohort

- [PMID:36201743](../papers/36201743.md) — Thomas et al. (SFU), source publication: EBV-status-driven molecular subgrouping (DGG-BL, IC-BL, Q53-BL) of Burkitt lymphoma via consensus NMF clustering.

## Notable findings derived from this cohort

- Tumor EBV status explained more molecular variation than patient age; only *[ARID1A](../genes/ARID1A.md)* and *[TET2](../genes/TET2.md)* mutation frequencies differed significantly by age [PMID:36201743](../papers/36201743.md).
- Consensus NMF clustering defined three BL-predominant genetic subgroups — DGG-BL (*[DDX3X](../genes/DDX3X.md)*, *[GNA13](../genes/GNA13.md)*, *[GNAI2](../genes/GNAI2.md)*), IC-BL (*[ID3](../genes/ID3.md)*, *[CCND3](../genes/CCND3.md)*), and Q53-BL (genetically quiet, *[TP53](../genes/TP53.md)*-mutated) — that differed in EBV status, sex, mutation burden, aberrant somatic hypermutation, and gene expression [PMID:36201743](../papers/36201743.md).
- An exome-compatible random-forest classifier separated BL from DLBCL with 93.3% accuracy and was validated on 3 published external cohorts [PMID:36201743](../papers/36201743.md).

## Sources

- cBioPortal study record: `mbn_sfu_2023` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:36201743](../papers/36201743.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
