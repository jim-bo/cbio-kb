---
name: Pediatric solid tumor PDXs (UTHSA, Nat Commun 2023)
studyId: pancan_pdx_uthsa_2023
institution: UT Health San Antonio and UT Southwestern
size: 136
reference_genome: hg38
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
panels: []
tags:
  - pediatric
  - patient-derived-xenograft
  - pan-cancer
  - PDX
processed_by: crosslinker
processed_at: 2026-09-11
---

# Pediatric solid tumor PDXs (UTHSA, Nat Commun 2023)

## Overview

A pan-pediatric-cancer patient-derived xenograft (PDX) resource: 68 early-passage subcutaneous PDXs from 65 pediatric solid-tumor patients across 16 cancer types, plus matched patient tumors and germline samples, built by He, Bandyopadhyay and colleagues at UT Health San Antonio and UT Southwestern. Name, institution, size (136 = PDX + matched patient-tumor samples), and reference genome (hg38) are taken from the cBioPortal study record in `schema/ontology/studies.json` [PMID:37990009](../papers/37990009.md).

## Composition

- 68 analyzed PDXs from 65 patients across 16 cancer types: 14 Wilms tumors ([WT](../cancer_types/WT.md)), 13 hepatoblastomas ([LIHB](../cancer_types/LIHB.md)), 12 osteosarcomas ([OS](../cancer_types/OS.md)), 10 germ cell tumors ([GCT](../cancer_types/GCT.md)), and 19 others including clear cell sarcoma ([CCS](../cancer_types/CCS.md)), neuroblastoma ([NBL](../cancer_types/NBL.md)), embryonal rhabdomyosarcoma ([ERMS](../cancer_types/ERMS.md)), pleomorphic sarcoma ([MFH](../cancer_types/MFH.md)), a [BCOR](../genes/BCOR.md)–[CCNB3](../genes/CCNB3.md) Ewing-like sarcoma, and glioblastoma ([GB](../cancer_types/GB.md)) [PMID:37990009](../papers/37990009.md).
- 27 (40%) PDXs had a matched patient tumor and 40 (59%) had germline DNA; all patients were under 18 years (median 6.5) [PMID:37990009](../papers/37990009.md).
- 90 subcutaneous PDXs were generated from 194 implanted fresh tumor samples; engraftment varied by histology (clear cell sarcoma 100%, Wilms tumor 85%, osteosarcoma 67%, neuroblastoma 26%, brain tumors 23%) [PMID:37990009](../papers/37990009.md).

## Assays / panels (linked)

- All 68 PDXs: low-pass [whole-genome sequencing](../methods/whole-genome-seq.md) (~4x), [whole-exome sequencing](../methods/whole-exome-seq.md) (~300x), and [RNA-seq](../methods/rna-seq.md) (~80M reads); reads aligned to GRCh38, mouse reads removed with Disambiguate [PMID:37990009](../papers/37990009.md).

## Papers using this cohort

- [PMID:37990009](../papers/37990009.md) — He, Bandyopadhyay et al. (UT Health San Antonio / UT Southwestern), source publication: builds the PDX resource and characterizes patient-tumor-to-PDX clonal selection.

## Notable findings derived from this cohort

- About 30% of patient-tumor/PDX pairs had low mutational similarity; in those pairs, clonal analysis showed a minor, more-proliferative patient-tumor subclone carrying more clonal neoantigens seeded the dominant PDX clone, consistent with the immunocompetent patient's innate immune system (inflammasome, NK-cell, HLA signals) suppressing that subclone before PDX engraftment in immunodeficient NSG mice [PMID:37990009](../papers/37990009.md).
- Copy-number, ploidy, expression and fusion profiles were well conserved between patient tumors and PDXs; an [LRPAP1](../genes/LRPAP1.md)–[PDGFRA](../genes/PDGFRA.md) fusion was identified in a glioblastoma and a germ cell tumor [PMID:37990009](../papers/37990009.md).

## Sources

- cBioPortal study record: `pancan_pdx_uthsa_2023` (name, institution, size, reference_genome taken from `schema/ontology/studies.json`).
- [PMID:37990009](../papers/37990009.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
