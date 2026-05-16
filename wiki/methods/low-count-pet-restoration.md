---
name: Low-Count PET Restoration
slug: low-count-pet-restoration
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-restoration, pet, dose-reduction, nuclear-medicine]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Low-Count PET Restoration

## Overview

Low-count PET restoration uses deep learning to recover full-count-equivalent PET images from PET acquisitions obtained with reduced radiotracer dose or shortened acquisition time. GAN and CycleGAN architectures are commonly used. Adding MRI as a second input channel has been shown to improve clinical uptake-status classification accuracy.

## Used by

- Reviewed as one of the image synthesis tasks (Table 10 of the paper) across a corpus of 111 deep learning image synthesis studies; GAN/CycleGAN can restore full-count PET from as little as 1/100 of full counts (Chen et al. 2019, brain; Ouyang et al. 2019); PSNR ~24–41 dB depending on count fraction and anatomical site; adding MR as a second input improved uptake-status reading accuracy from 83% to 89% [PMID:33305538](../papers/33305538.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- Clinically motivated for pediatric PET imaging (ALARA principle) and for response-evaluation PET where repeat scanning is needed.
- MR-guided PET restoration leverages the complementary soft-tissue information in MRI to constrain the denoising problem.
- Related pages: [PET Attenuation Correction](../methods/pet-attenuation-correction.md), [Generative Adversarial Network](../methods/generative-adversarial-network.md), [CycleGAN](../methods/cyclegan.md).

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
