---
name: DICOM RT-STRUCT
slug: dicom-rt-struct
kind: method
canonical_source: corpus
unverified: true
tags: [dicom, radiotherapy, contour, segmentation, rt-planning]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# DICOM RT-STRUCT

## Overview

DICOM RT-STRUCT (RT Structure Set) is the DICOM standard object for storing 3D contour sets drawn on CT or MRI images for radiotherapy planning and research. Each RT-STRUCT file contains named contours (regions of interest: gross tumor volume, clinical target volume, planning target volume, organs at risk) linked to the source imaging series via Frame of Reference UID. RT-STRUCT files are the standard input for radiotherapy dose calculation and the primary segmentation substrate for [CT radiomics](../methods/ct-radiomics.md) and [radiomics](../methods/radiomics.md) downstream analyses.

**Cross-reference**: [dicom-rt-planning](../methods/dicom-rt-planning.md) stores the RT treatment plan (beam parameters, dose prescription) as a separate DICOM object; both are included in multi-modal RT archives. RT-STRUCT files define the spatial contours; RTPLAN specifies how dose is delivered.

## Used by

- [PMID:38362943](../papers/38362943.md) — RADCURE releases RT-STRUCT files for 3346 HNC patients at Princess Margaret Cancer Centre, containing manually contoured gross primary tumor, gross nodal volumes, and 19 organs at risk; nomenclature was standardized across the cohort to improve interoperability for downstream radiomics analyses [PMID:38362943](../papers/38362943.md).
- [PMID:30179230](../papers/30179230.md) — HNSCC imaging archive at MD Anderson includes RT-STRUCT files (alongside RTPLAN and RTDOSE) as part of the 433,384 DICOM files; 195/215 (90.7%) subjects had series/study inconsistency problems on initial intake requiring 2–6 curation rounds per subject to resolve RTSTRUCT/RTDOSE/RTPLAN mis-linkages [PMID:30179230](../papers/30179230.md).

## Notes

- RT-STRUCT Frame of Reference UID mismatches between structure sets and source CT images were the most common curation error in the MD Anderson HNSCC archive, underscoring the importance of DICOM curation tooling (Posda Tools) before public release [PMID:30179230](../papers/30179230.md).
- RADCURE standardized RT-STRUCT nomenclature as a deliberate step to improve reusability across research groups; non-standardized nomenclature is a known barrier to multi-institutional pooling of RT planning data [PMID:38362943](../papers/38362943.md).

## Sources

- [PMID:38362943](../papers/38362943.md)
- [PMID:30179230](../papers/30179230.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
