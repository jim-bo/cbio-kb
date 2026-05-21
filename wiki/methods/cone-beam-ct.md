---
name: Cone-Beam CT
slug: cone-beam-ct
kind: method
canonical_source: corpus
unverified: true
tags: [imaging, radiotherapy, CT]
processed_by: entity-page-writer
processed_at: 2026-05-21
---

# Cone-Beam CT

## Overview

Cone-beam computed tomography (CBCT) is an imaging modality used in radiation therapy for daily patient positioning and online adaptive radiotherapy (ART). Unlike planning CT, CBCT is acquired on the treatment machine (e.g., Varian TrueBeam at 100 kVp) immediately before or during treatment, allowing real-time anatomic verification. However, CBCT images suffer from beam-hardening, scatter, and metal artifacts that degrade Hounsfield-unit (HU) accuracy, limiting their direct use for dose calculation. Synthetic CT (sCT) generation from CBCT via deep learning is an active research area to overcome these limitations.

## Used by

- CBCT images from 41 brain and 47 head-and-neck radiotherapy patients served as input to a conditional DDPM model for synthetic CT generation; raw CBCT MAE was 40.63 HU (brain) and 38.99 HU (H&N) vs planning CT reference, reduced to 25.99 HU and 32.56 HU respectively by the sCT model [PMID:37646491](../papers/37646491.md)

## Notes

- CBCT scans acquired on Varian TrueBeam (100 kVp); voxel size 1.0 × 1.0 × 1.0 mm³.
- Beam-hardening artifacts (brain) and streaking/metal artifacts (H&N) are characteristic limitations.
- Direct CBCT-based dose calculation is the goal for online ART; sCT generation is the current workaround.
- No cancer genomics or molecular data in the originating paper — included for radiotherapy imaging context only.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-21**.*
