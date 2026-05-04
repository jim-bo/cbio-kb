---
name: Cone-beam CT (CBCT) imaging
slug: cbct-imaging
kind: method
canonical_source: corpus
unverified: true
tags: [imaging, radiotherapy, cone-beam-ct, igrt]
processed_by: entity-page-writer
processed_at: 2026-05-03
---

# Cone-beam CT (CBCT) imaging

## Overview

Cone-beam computed tomography (CBCT) is an on-board X-ray imaging modality used during image-guided radiotherapy (IGRT) to verify patient positioning and anatomy immediately prior to or during treatment. CBCT images suffer from reduced soft-tissue contrast, beam-hardening artifacts, scatter, and Hounsfield unit (HU) inaccuracies relative to diagnostic CT, which limit their direct use for dose calculation and organ segmentation in adaptive radiotherapy.

## Used by

- [PMID:37646491](../papers/37646491.md) — CBCT acquired on Varian TrueBeam at 100 kVp served as the input to the [conditional DDPM sCT](../methods/conditional-ddpm-sct.md) model; 41 brain and 47 H&N patient CBCT scans used for training and testing; the method's goal was to synthesize planning-CT–quality images from CBCT to enable online adaptive radiotherapy; baseline MAE of CBCT vs. deformed planning CT was 40.63 HU (brain) and 38.99 HU (H&N) [PMID:37646491](../papers/37646491.md).

## Notes

- Voxel size was 1.0 × 1.0 × 1.0 mm³ for both CBCT and planning CT in the corpus study.
- Metal implant artifacts (beam-hardening, streaking) are a known limitation, particularly in head-and-neck patients with dental implants.
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:37646491](../papers/37646491.md)

*This page was processed by **entity-page-writer** on **2026-05-03**.*
