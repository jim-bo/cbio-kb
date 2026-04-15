---
name: CBCT delta radiomics
slug: cbct-delta-radiomics
kind: method
canonical_source: corpus
unverified: true
tags: [radiomics, imaging, cbct, adaptive-rt, on-treatment]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# CBCT delta radiomics

## Overview

CBCT (Cone-Beam CT) delta radiomics is an imaging-based method that extracts quantitative radiomic features from serial on-treatment cone-beam CT scans acquired during a radiation therapy course, then computes the delta (change) between time points. The approach enables high-temporal-resolution monitoring of treatment response without requiring additional dedicated imaging sessions, since CBCT is routinely acquired for patient positioning at each treatment fraction.

## Used by

- [PMID:41941260](../papers/41941260.md) — CBCT delta radiomics is being standardized across ROBIN consortium institutions by the CBCT Working Group (CBCT WG), which harmonizes Cone-Beam CT acquisition protocols to enable cross-center integrative analysis; deployed within the METEOR center (Washington University, St. Louis) for on-treatment adaptive imaging in locally advanced cervical and pancreatic cancer patients on trial NCT05975593 [PMID:41941260](../papers/41941260.md).

## Notes

- Corpus-grown slug; not present in canonical ontology.
- The ROBIN CBCT WG explicitly flags the need for harmonized acquisition protocols and artifact correction before cross-center delta-radiomics analyses are robust.
- Longitudinal CBCT data are archived as DICOM-RT plans; METEOR-CRATR (NCT05975593) had 126 DICOM-RT plans archived at time of writing.
- Complements molecular biomarker assays (ctDNA, spatial transcriptomics) in the METEOR center's multimodal treatment-response monitoring strategy.

## Sources

- [PMID:41941260](../papers/41941260.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*

*This page was processed by **crosslinker** on **2026-04-15**.*
