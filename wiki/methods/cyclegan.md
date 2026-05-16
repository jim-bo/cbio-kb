---
name: CycleGAN
slug: cyclegan
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-synthesis, generative-model, unpaired-training, radiation-oncology]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# CycleGAN

## Overview

CycleGAN is an unsupervised image-to-image translation framework that learns mappings between two image domains (e.g., MRI and CT) without requiring paired training examples. It uses two generators and two discriminators with a cycle-consistency loss that enforces forward-and-back translation to be an identity operation. CycleGAN is particularly suited for inter-modality medical image synthesis where perfect spatial registration of paired training data is impractical.

## Used by

- Reviewed as a major unsupervised architecture for inter-modality synthesis in a systematic review of 111 deep learning studies; noted for tolerating training-pair misalignment via cycle-consistency loss; a CycleGAN-based approach reduced landmark registration error from 9.8±3.1 mm to 6.0±2.1 mm (head/neck, McKenzie et al. 2019) by using synthetic CT as a bridge for MR-CT deformable registration; also applied for CBCT-to-CT synthesis achieving MAE ~40–110 HU and for low-count PET restoration to as little as 1/100 of full counts [PMID:33305538](../papers/33305538.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- Introduced by Zhu et al. (2017); uses two paired generators (G: X→Y, F: Y→X) and two discriminators.
- Cycle-consistency constraint: F(G(x)) ≈ x and G(F(y)) ≈ y.
- Only 3 of 111 reviewed studies used unpaired (unsupervised) training; the majority still use paired data with conventional or pixel-wise losses.
- Related pages: [Generative Adversarial Network](../methods/generative-adversarial-network.md), [Synthetic CT from MRI](../methods/synthetic-ct-from-mri.md).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
