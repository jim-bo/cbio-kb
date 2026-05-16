---
name: Generative Adversarial Network (GAN)
slug: generative-adversarial-network
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-synthesis, generative-model, radiation-oncology]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Generative Adversarial Network (GAN)

## Overview

A Generative Adversarial Network (GAN) is a deep learning framework in which two networks — a generator and a discriminator — are trained adversarially. The generator learns to produce realistic synthetic outputs (e.g., synthetic CT from MRI), while the discriminator learns to distinguish generated outputs from real ones. The adversarial loss encourages perceptually sharper, more realistic outputs compared to purely pixel-wise loss functions. GANs underlie many image-synthesis architectures including pix2pix, CycleGAN, and DCGAN.

## Used by

- Identified as one of the two dominant architectures (alongside U-Net) in a systematic review of 111 deep learning studies on inter- and intra-modality medical image synthesis; GAN use is rising faster than U-Net since 2017 and is applied across MR-to-CT, CT-to-MR, CBCT-to-CT, low-dose CT restoration, and low-count PET restoration tasks [PMID:33305538](../papers/33305538.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- Training instability (mode collapse, vanishing gradients) is a known limitation; Wasserstein GAN (WGAN) and spectral normalization partially address this.
- Conditional GANs (cGAN) take an input image as a conditioning signal, enabling image-to-image translation.
- Related pages: [CycleGAN](../methods/cyclegan.md), [U-Net](../methods/u-net.md).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
