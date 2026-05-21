---
name: Cycle GAN
slug: cycle-gan
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-synthesis, generative-adversarial-network, radiotherapy]
processed_by: entity-page-writer
processed_at: 2026-05-21
---

# Cycle GAN

## Overview

Cycle GAN (Cycle-Consistent Generative Adversarial Network) is an unsupervised image-to-image translation framework that learns mappings between two image domains without paired training examples, enforcing cycle-consistency to regularize the mapping. In radiotherapy imaging, Cycle GAN has been applied for CBCT-to-CT synthetic image translation to improve Hounsfield-unit accuracy for dose calculation. Supervised variants using paired data are also used as baselines in method comparisons.

## Used by

- Served as the supervised baseline in a CBCT-to-synthetic-CT translation study; the proposed conditional DDPM outperformed Cycle GAN on MAE, PSNR, and NCC in both brain and head-and-neck radiotherapy cohorts [PMID:37646491](../papers/37646491.md)

## Notes

- Cycle GAN is the established baseline for unpaired image-to-image translation; supervised variants use paired CBCT/pCT data.
- Outperformed by conditional DDPM on HU accuracy metrics in the 41-brain + 47-H&N patient study.
- No cancer genomics or molecular data in the originating paper — included for radiotherapy imaging context only.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-21**.*
