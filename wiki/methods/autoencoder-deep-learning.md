---
name: Autoencoder (Deep Learning)
slug: autoencoder-deep-learning
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-synthesis, unsupervised-learning, representation-learning, radiation-oncology]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Autoencoder (Deep Learning)

## Overview

An autoencoder is a neural network trained to encode input data into a compact latent representation and then decode it back to reconstruct the original input. In the context of medical image synthesis, autoencoders are used for inter- and intra-modality translation by training the encoder on one modality and the decoder on another. They represent the earliest and simplest of the three major deep learning architectural families used for image synthesis, preceding U-Net and GAN approaches in the medical imaging literature.

## Used by

- Identified as one of three main architectural families (along with U-Net and GAN) in a systematic review of 111 deep learning studies on inter- and intra-modality medical image synthesis (e.g., MR-to-CT, low-dose CT restoration, PET attenuation correction); AE-only studies are a minority compared to U-Net and GAN [PMID:33305538](../papers/33305538.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- Variational autoencoders (VAE) extend AEs with a probabilistic latent space and are used for image generation and augmentation.
- The encoder-decoder backbone of U-Net is architecturally similar to an autoencoder, but U-Net adds skip connections from encoder to decoder.
- In current medical imaging practice, autoencoders are largely superseded by U-Net and GAN architectures for synthesis tasks.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
