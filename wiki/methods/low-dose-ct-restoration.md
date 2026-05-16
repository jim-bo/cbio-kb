---
name: Low-Dose CT Restoration
slug: low-dose-ct-restoration
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-restoration, ct, dose-reduction, radiation-oncology]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Low-Dose CT Restoration

## Overview

Low-dose CT restoration uses deep learning (primarily U-Net and GAN architectures) to recover diagnostic image quality from CT acquisitions obtained at reduced radiation dose (low mAs or sparse-view protocols). The trained model takes a noisy/artifact-laden low-dose CT as input and outputs an image approximating full-dose quality, enabling dose reduction without sacrificing diagnostic value.

## Used by

- Reviewed as one of the intra-modality synthesis tasks (Table 7 of the paper) across a corpus of 111 deep learning image synthesis studies; learning-based methods restore PSNR to ~36–44 dB at 1/4 dose; learning-based restoration preserved fine texture better than total-variation (TV) iterative methods that tend to over-smooth; double-blinded reader studies validated learning-based restoration in two studies (Yang et al. 2018; Shan et al. 2019) [PMID:33305538](../papers/33305538.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- Especially relevant for pediatric CT and repeat scanning (e.g., surveillance in cancer patients).
- 3D models outperform 2D slice-based models in preserving inter-slice texture but require more training data.
- Related pages: [U-Net](../methods/u-net.md), [Generative Adversarial Network](../methods/generative-adversarial-network.md), [Low-Count PET Restoration](../methods/low-count-pet-restoration.md).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
