---
name: Conditional DDPM synthetic CT generation
slug: conditional-ddpm-sct
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, diffusion-model, synthetic-ct, adaptive-radiotherapy, imaging]
processed_by: crosslinker
processed_at: 2026-05-03
---

# Conditional DDPM synthetic CT generation

## Overview

A conditional denoising diffusion probabilistic model (DDPM) that translates cone-beam CT (CBCT) images into synthetic CT (sCT) images with accurate Hounsfield unit values, enabling CBCT-based dose calculation for online adaptive radiotherapy. The CBCT is concatenated as static guidance into each reverse-diffusion step of a time-embedded U-Net (T=1000 steps; β linearly scheduled 1e-4 to 0.02). Averaging over 10 stochastic inference samples further reduces posterior variance.

## Used by

- [PMID:37646491](../papers/37646491.md) — trained on 4,682 brain and 4,314 H&N paired CBCT/deformed-planning-CT slices from 41 brain and 47 H&N patients; on 500 held-out test slices per site, reduced MAE from 40.63 HU to 25.99 HU (brain) and 38.99 HU to 32.56 HU (H&N); outperformed four alternative diffusion schemes and a supervised [Cycle GAN sCT](../methods/cycle-gan-sct.md) on MAE, PSNR, and NCC; throughput ~2 min/slice on a 24 [GB](../cancer_types/GB.md) Nvidia RTX 3090, flagged as too slow for online ART [PMID:37646491](../papers/37646491.md).

## Notes

- Inference speed (~2 min/slice, ~1000 forward passes) is incompatible with online adaptive radiotherapy workflows; authors defer acceleration (DDIM, DPM-Solver, knowledge distillation) to future work.
- The model demonstrated robustness to metal-implant streaking artifacts; sCT was less artifact-laden than the deformed-planning-CT training target in heavily corrupted H&N cases.
- 2D slice-wise architecture; no 3D context or patch-based modeling; no genomic or cancer-type data involved.
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:37646491](../papers/37646491.md)

*This page was processed by **crosslinker** on **2026-05-03**.*
