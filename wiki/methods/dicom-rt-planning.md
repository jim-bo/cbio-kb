---
name: DICOM RT planning (RTPLAN/RTDOSE)
slug: dicom-rt-planning
kind: method
canonical_source: corpus
unverified: true
tags: [dicom, radiotherapy, rt-planning, dose, treatment-planning]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# DICOM RT planning (RTPLAN/RTDOSE)

## Overview

DICOM RTPLAN and RTDOSE are the DICOM standard objects that together encode a radiotherapy treatment plan: RTPLAN stores beam geometry, field parameters, fractionation, and dose prescription; RTDOSE stores the computed 3D dose distribution in the patient coordinate system. Both are linked via Frame of Reference UID to the simulation CT and RT-STRUCT contours. Together with [DICOM RT-STRUCT](../methods/dicom-rt-struct.md), these objects form the complete RT planning DICOM triplet used in multi-modal clinical research archives.

**Cross-reference**: [dicom-rt-struct](../methods/dicom-rt-struct.md) stores the spatial contours (gross tumor, organs at risk) referenced by RTPLAN/RTDOSE. Both DICOM objects are part of the same RT planning chain. The distinction: RT-STRUCT defines *where* to treat; RTPLAN/RTDOSE define *how* dose is delivered and *what* dose distribution results.

## Used by

- [PMID:30179230](../papers/30179230.md) — HNSCC imaging archive at MD Anderson includes RTPLAN and RTDOSE files for 215 patients treated with curative-intent radiotherapy; re-exported from Pinnacle v9.6 (Philips Radiation Oncology Systems) after primary clinical use; mean prescribed dose 68.66 Gy (range 56–72 Gy) in 28–40 fractions using techniques spanning 2D RT, IMRT, and volumetric arc therapy; curation required resolving Frame of Reference UID mismatches between RT structure sets and source CTs for 90.7% of cases [PMID:30179230](../papers/30179230.md).

## Notes

- RTPLAN/RTDOSE re-calculation during export from Pinnacle in the MD Anderson archive means the archived dose distributions reflect re-calculated rather than original treatment delivery parameters; users should account for this in dose-volume histogram analyses [PMID:30179230](../papers/30179230.md).
- The HNSCC archive combination of simulation CT + RT-STRUCT + RTPLAN + RTDOSE enables inter-institutional benchmarking of dose-volume relationships and supports modeling of toxicity outcomes from delivered dose distributions [PMID:30179230](../papers/30179230.md).

## Sources

- [PMID:30179230](../papers/30179230.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
