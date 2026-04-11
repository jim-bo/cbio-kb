---
name: Volumetric MRI segmentation
slug: volumetric-mri-segmentation
kind: method
canonical_source: 
unverified: true
tags: [imaging, mri, segmentation, tumor-volume]
processed_by: entity-page-writer
processed_at: 2026-04-08
---

# Volumetric MRI segmentation

## Overview

Manual 3D volumetric segmentation of tumor on MRI (typically T2/FLAIR abnormality) to derive tumor volume measurements, used as a quantitative imaging biomarker for tumor growth kinetics during active surveillance.

## Used by

- [PMID:37910594](../papers/37910594.md) — manual 3D volumetric segmentation of T2/FLAIR abnormality performed on serial MRIs (median 8 scans/patient) of 128 IDH-mutant Grade 2 gliomas under active surveillance at MSKCC, using TeraRecon iNtuition 4.4.13 with VASARI feature annotation, to compute tumor volume growth rate (TVGR) and doubling time [PMID:37910594](../papers/37910594.md).

## Notes

- Heterogeneous scan parameters across ~22 years of imaging (varying slice thickness, interslice gap, scanner type) may bias volume estimates [PMID:37910594](../papers/37910594.md).
- Manual segmentation, although blinded and expert-reviewed, may include edema or post-surgical changes indistinguishable from tumor on MRI [PMID:37910594](../papers/37910594.md).
- Automated/AI-assisted segmentation is called out as a prospective next step [PMID:37910594](../papers/37910594.md).

## Sources

- [PMID:37910594](../papers/37910594.md)

*This page was processed by **entity-page-writer** on **2026-04-08**.*
