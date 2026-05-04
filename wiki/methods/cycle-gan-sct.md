---
name: Cycle GAN synthetic CT
slug: cycle-gan-sct
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, gan, synthetic-ct, adaptive-radiotherapy, imaging]
processed_by: entity-page-writer
processed_at: 2026-05-03
---

# Cycle GAN synthetic CT

## Overview

A supervised CycleGAN-based approach for CBCT-to-CT image synthesis used in adaptive radiotherapy planning. CycleGAN learns paired or unpaired image-to-image translations using cycle-consistency loss, allowing conversion of cone-beam CT images to synthetic planning-CT images with improved Hounsfield unit accuracy and reduced artifacts.

## Used by

- [PMID:37646491](../papers/37646491.md) — served as a supervised baseline comparator to the proposed [conditional DDPM sCT](../methods/conditional-ddpm-sct.md) model; on brain and head-and-neck test slices, the Cycle GAN sCT was outperformed by the conditional DDPM on MAE, PSNR, and NCC, and showed structural distortion, residual artifacts, or hallucinated low-contrast features relative to the DDPM output [PMID:37646491](../papers/37646491.md).

## Notes

- Used as a supervised comparison, not the primary method in the corpus study.
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:37646491](../papers/37646491.md)

*This page was processed by **entity-page-writer** on **2026-05-03**.*
