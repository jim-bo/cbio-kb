---
name: Synthetic CT from CBCT (CBCT Correction)
slug: synthetic-cbct-correction
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-synthesis, adaptive-radiotherapy, cone-beam-ct]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Synthetic CT from CBCT (CBCT Correction)

## Overview

Synthetic CT from cone-beam CT (CBCT) is a deep learning-based image translation task that improves the image quality of on-board CBCT by generating a planning-CT-quality synthetic CT. On-board CBCT is used for daily patient positioning and adaptive radiotherapy but suffers from scatter artifacts, truncated field of view, and poor Hounsfield-unit accuracy. Learning-based correction produces synthetic CTs suitable for daily dose recalculation.

## Used by

- Reviewed as one of the inter-modality synthesis tasks (Table 5 of the paper) across a corpus of 111 deep learning image synthesis studies; CycleGAN-based synthetic CTs from on-board CBCT recover HU accuracy sufficient for adaptive radiotherapy dose recalculation; reported MAE ranges ~40–110 HU depending on anatomical site [PMID:33305538](../papers/33305538.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- Also referred to as CBCT-to-CT synthesis or CBCT scatter correction.
- CycleGAN is particularly suited because paired (same-day) CBCT-planning CT registration is imperfect due to patient motion and organ filling differences.
- Clinical use case: enable daily online dose recalculation and adaptive treatment modification without re-CT simulation.
- Related pages: [CycleGAN](../methods/cyclegan.md), [Generative Adversarial Network](../methods/generative-adversarial-network.md).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
