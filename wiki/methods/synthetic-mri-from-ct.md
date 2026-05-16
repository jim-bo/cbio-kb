---
name: Synthetic MRI from CT
slug: synthetic-mri-from-ct
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-synthesis, ct-to-mri, radiation-oncology]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Synthetic MRI from CT

## Overview

Synthetic MRI from CT (CT-to-MR synthesis) is a deep learning-based image translation task that generates MRI-equivalent images from CT data. Applications include improving soft-tissue contrast for CT-guided procedures, generating virtual MRI contrasts for radiotherapy planning when MRI acquisition is not feasible, and cross-modality registration tasks.

## Used by

- Covered as part of a systematic review of 111 deep learning studies on inter- and intra-modality medical image synthesis; CT-to-MR synthesis is among the surveyed tasks alongside the more clinically dominant MR-to-CT direction [PMID:33305538](../papers/33305538.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- CT-to-MR synthesis is less clinically driven than MR-to-CT; CT already provides Hounsfield units for dose calculation, so the motivation is soft-tissue visualization or virtual contrast.
- Related pages: [Synthetic CT from MRI](../methods/synthetic-ct-from-mri.md), [CycleGAN](../methods/cyclegan.md), [U-Net](../methods/u-net.md).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
