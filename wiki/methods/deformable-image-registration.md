---
name: Deformable image registration (DIR)
slug: deformable-image-registration
kind: method
canonical_source: corpus
unverified: true
tags: [image-registration, adaptive-radiotherapy, imaging]
processed_by: entity-page-writer
processed_at: 2026-05-03
---

# Deformable image registration (DIR)

## Overview

Deformable image registration (DIR) maps one medical image to another by estimating a non-rigid spatial transformation field, accommodating soft-tissue deformation between imaging sessions. In adaptive radiotherapy, DIR is used to warp a reference planning CT to match the anatomy observed on a current on-board image (e.g., CBCT), producing a deformed planning CT (dpCT) that serves as a pseudo-ground truth or as a training target for image synthesis models.

## Used by

- [PMID:37646491](../papers/37646491.md) — deformable image registration performed in Velocity AI 3.2.1 to generate deformed planning CT (dpCT) from paired planning CT and CBCT acquisitions in 41 brain and 47 H&N patients; dpCT served as the supervisory ground truth for training and evaluating the [conditional DDPM sCT](../methods/conditional-ddpm-sct.md) model; residual mismatch between dpCT and CBCT due to inter-fraction anatomy change was noted as a limitation affecting MAE/PSNR estimates [PMID:37646491](../papers/37646491.md).

## Notes

- The imperfection of dpCT as a ground truth (inter-fraction anatomy change remains) is a known limitation; in some cases the conditional DDPM sCT was less artifact-laden than the dpCT target.
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:37646491](../papers/37646491.md)

*This page was processed by **entity-page-writer** on **2026-05-03**.*
