---
name: U-Net
slug: u-net
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-synthesis, segmentation, convolutional-neural-network, radiation-oncology]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# U-Net

## Overview

U-Net is a convolutional neural network architecture originally developed for biomedical image segmentation, characterized by a symmetric encoder-decoder structure with skip connections between corresponding encoder and decoder levels. The skip connections preserve spatial detail lost during downsampling. U-Net is widely used for both segmentation and image-to-image translation (synthesis) tasks in medical imaging.

## Used by

- Identified as one of the two dominant architectures (alongside GAN) in a systematic review of 111 deep learning studies on inter- and intra-modality medical image synthesis; U-net and GAN studies together account for ~90% of the reviewed articles, with U-Net widely applied for MR-to-CT synthesis, low-dose CT restoration, and intra-modality MR synthesis [PMID:33305538](../papers/33305538.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- Original architecture by Ronneberger et al. (2015) from ISBI cell-tracking challenge.
- For 3D data, 3D U-Net variants are used; 2D slice-based U-Net is more common due to GPU memory constraints.
- Typically trained with pixel-wise loss functions (MAE, MSE) and optionally perceptual or adversarial losses.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
