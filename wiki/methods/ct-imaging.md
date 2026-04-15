---
name: CT imaging
slug: ct-imaging
kind: method
canonical_source: corpus
unverified: true
tags: [imaging, ct, computed-tomography, radiology]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# CT imaging

## Overview

Computed tomography (CT) imaging: X-ray-based cross-sectional imaging producing 3D volumetric data in Hounsfield units. In oncology research CT is used for staging, radiotherapy simulation (RT planning CT), response assessment, and as the primary input for [CT radiomics](../methods/ct-radiomics.md) feature extraction. CT imaging is a broader umbrella term; specialized uses include [fdg-pet-ct](../methods/fdg-pet-ct.md) (metabolic imaging) and [ct-radiomics](../methods/ct-radiomics.md) (quantitative feature extraction).

**Cross-reference**: [ct-radiomics](../methods/ct-radiomics.md) describes quantitative feature extraction from CT; [dicom-rt-struct](../methods/dicom-rt-struct.md) describes the DICOM format for contours drawn on CT images.

## Used by

- [PMID:38362943](../papers/38362943.md) — RT simulation CT scans from 3346 HNC patients at Princess Margaret Cancer Centre, acquired on three scanner manufacturers under standard clinical protocols; released as the [RADCURE](../datasets/radcure.md) dataset for [radiomics](radiomics.md) and machine-learning research [PMID:38362943](../papers/38362943.md).
- [PMID:30179230](../papers/30179230.md) — multi-modality imaging archive for 215 HNSCC patients at MD Anderson Cancer Center, including diagnostic CT, PET-CT, MRI, and RT simulation CT; 433,384 DICOM files across 3,225 series; released as the [TCIA HNSCC collection](../datasets/tcia-hnscc.md) [PMID:30179230](../papers/30179230.md).
- [PMID:37397861](../papers/37397861.md) — pretreatment contrast-enhanced CT from 2,552 HNSC patients at Princess Margaret Cancer Centre was the primary imaging input for the RADCURE prognostic challenge; CT-derived primary tumor volume was the single most informative imaging feature, included in the top-performing MTLR model (AUROC 0.823 on internal test); CT radiomics did not improve on EMR+volume models [PMID:37397861](../papers/37397861.md).

## Notes

- CT acquisition parameters (slice thickness, kVp, mA, reconstruction kernel) vary substantially across institutions and scanner generations; this heterogeneity is a known source of radiomic feature instability [PMID:38362943](../papers/38362943.md).
- CT-derived body-composition measurements (skeletal muscle and adipose cross-sectional area at L3) are a specialized downstream use in the HNSCC archive [PMID:30179230](../papers/30179230.md); see [body-composition-ct](../methods/body-composition-ct.md).

## Sources

- [PMID:38362943](../papers/38362943.md)
- [PMID:30179230](../papers/30179230.md)
- [PMID:37397861](../papers/37397861.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
