---
name: PET Attenuation Correction (DL-based)
slug: pet-attenuation-correction
kind: method
canonical_source: corpus
unverified: true
tags: [deep-learning, image-synthesis, pet-mr, nuclear-medicine, attenuation-correction]
processed_by: crosslinker
processed_at: 2026-05-16
---

# PET Attenuation Correction (DL-based)

## Overview

PET attenuation correction using deep learning generates a synthetic CT (or attenuation map) from MRI data in PET/MR systems, where no CT scan is acquired. This synthetic CT is used to [estimate](../methods/estimate.md) photon attenuation coefficients at 511 keV for quantitative PET reconstruction. Learning-based methods outperform conventional atlas-based or segmentation-based approaches, primarily because they can better reconstruct bone (which has high attenuation and appears dark on MRI).

## Used by

- Reviewed as a specific application of MR-to-CT synthesis (Tables 2 and 6 of the paper) across a corpus of 111 deep learning image synthesis studies; learning-based methods reduced PET bias to ~2% vs ~5% bias with conventional CT-synthesis methods; improvement is attributable to better bone reconstruction; also reviewed for direct synthetic-CT-from-non-attenuation-corrected-PET with bias generally <5% across VOIs [PMID:33305538](../papers/33305538.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- Bone attenuation correction is the dominant error source; bone and air both appear dark on conventional T1/T2 MRI sequences.
- UTE (ultrashort echo time) and ZTE (zero echo time) MRI sequences provide bone contrast but are slow and sacrifice soft-tissue diagnostic value.
- Related pages: [Synthetic CT from MRI](../methods/synthetic-ct-from-mri.md), [Low-Count PET Restoration](../methods/low-count-pet-restoration.md), [U-Net](../methods/u-net.md).

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
