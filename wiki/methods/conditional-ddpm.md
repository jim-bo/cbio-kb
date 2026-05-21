---
name: Conditional DDPM
slug: conditional-ddpm
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-synthesis, radiotherapy, imaging]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Conditional DDPM

## Overview

A conditional denoising diffusion probabilistic model (DDPM) for translating cone-beam CT (CBCT) images into synthetic CT (sCT) images with planning-CT-like Hounsfield-unit (HU) accuracy. The model concatenates the CBCT image channel-wise with the noisy sample as static guidance at every reverse diffusion step, enabling stable image-to-image translation. It was developed for online adaptive radiotherapy (ART) workflows where real-time CBCT-based dose calculation is needed without the manual deformable registration of a planning CT.

## Used by

- Applied to paired CBCT and deformably-registered planning CT (dpCT) slices from 41 brain and 47 head-and-neck radiotherapy patients; outperformed four diffusion-based variants (Uncond-1/ILVR, Uncond-2, Adap-Cond-1, Adap-Cond-2) and a Cycle GAN baseline on MAE, PSNR, and NCC; brain MAE improved from 40.63 HU (CBCT) to 25.99 HU (sCT) [PMID:37646491](../papers/37646491.md)

## Notes

- Averaging 10 stochastic reverse-process samples per slice further reduced MAE (brain: 22.31 HU; H&N: 25.99 HU) at the cost of ~2 min per-slice inference time on a 24 [GB](../cancer_types/GB.md) Nvidia RTX 3090.
- The model showed tolerance to inexact paired training data — in heavily metal-artifact-corrupted H&N slices, sCT was less artifact-corrupted than the dpCT training target.
- 2D slice-based architecture; 3D/volumetric coherence and clinical integration remain future work.
- No cancer genomics, molecular data, or cBioPortal-relevant entities in the originating paper — method is included for radiotherapy imaging context only.

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
