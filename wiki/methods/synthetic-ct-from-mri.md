---
name: Synthetic CT from MRI
slug: synthetic-ct-from-mri
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-synthesis, radiation-therapy, mri-only-planning, pet-attenuation-correction]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Synthetic CT from MRI

## Overview

Synthetic CT from MRI (sCT or pseudo-CT) is a deep learning-based image synthesis task that generates CT-equivalent images from MRI data. The primary applications are MR-only radiotherapy planning (eliminating the duplicate CT simulation scan) and PET attenuation correction in PET/MR scanners (where CT-based attenuation maps are unavailable). The most common architectures are U-Net and GAN (including CycleGAN).

## Used by

- Reviewed as the most-studied synthesis task (Table 1 of the reviewed paper) across a corpus of 111 deep learning image synthesis studies; within-body MAE typically 40–70 HU; dose differences for photon VMAT plans are typically <1%; PET attenuation bias reduced from ~5% (conventional) to ~2% (learning-based) [PMID:33305538](../papers/33305538.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- Bone is the hardest tissue to synthesize from MRI because both bone and air appear dark on T1/T2; UTE and ZTE sequences improve bone contrast.
- Multi-channel MRI input (e.g., Dixon water/fat + UTE) consistently outperforms single-channel input.
- Proton therapy is more sensitive to sCT HU errors than photon therapy due to Bragg-peak sensitivity.
- Related pages: [CycleGAN](../methods/cyclegan.md), [U-Net](../methods/u-net.md), [PET Attenuation Correction](../methods/pet-attenuation-correction.md).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
