---
name: 18F-FDG PET/CT
slug: fdg-pet-ct
kind: method
canonical_source: corpus
unverified: true
tags: [imaging, pet-ct, nuclear-medicine, fdg, metabolic-imaging]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# 18F-FDG PET/CT

## Overview

Whole-body 18F-fluorodeoxyglucose (FDG) positron emission tomography combined with computed tomography (PET/CT). FDG uptake in tumor tissue reflects glucose metabolism; CT provides anatomical co-registration and attenuation correction. FDG PET/CT is used preoperatively for staging, post-treatment response assessment, and as a data layer in radiogenomic studies linking metabolic imaging phenotypes to molecular biomarkers. See also [pet-ct-imaging](../methods/pet-ct-imaging.md) for the generic PET-CT acquisition modality.

## Used by

- [PMID:30325352](../papers/30325352.md) — FDG PET/CT acquired in 201 of 211 NSCLC subjects in the [nsclc-radiogenomics-stanford](../datasets/nsclc-radiogenomics-stanford.md) dataset; CT-based attenuation correction with iterative OSEM reconstruction; FDG dose 138.90–572.25 MBq (mean 309.26 MBq); uptake time 23.08–128.90 min (mean 66.58 min); tumor segmentations on co-registered CT were used for semantic annotation by one experienced radiologist [PMID:30325352](../papers/30325352.md).

## Notes

- PET/CT variability (FDG dose, uptake time, scanner model) in the NSCLC radiogenomics dataset was not harmonized; this heterogeneity is flagged by the authors as a limitation for radiomic analyses across the dataset [PMID:30325352](../papers/30325352.md).
- FDG PET/CT is also used in the [tcia-hnscc](../datasets/tcia-hnscc.md) collection for HNSCC patients (see [pet-ct-imaging](../methods/pet-ct-imaging.md)).

## Sources

- [PMID:30325352](../papers/30325352.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
