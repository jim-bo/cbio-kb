---
name: MSK KRASG12C Colorectal Resistance 2022
studyId: coadread_mskresistance_2022
institution: Memorial Sloan Kettering Cancer Center
size: 12
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MSK-IMPACT
  - Guardant360 CDx
  - ctDx FIRST
  - MSK-ACCESS
panels: []
tags:
  - colorectal
  - KRAS
  - resistance
  - ctDNA
processed_by: crosslinker
processed_at: 2026-05-06
---

# MSK KRASG12C Colorectal Resistance 2022

## Overview

A clinical/translational dataset from Memorial Sloan Kettering Cancer Center characterizing the genetic mechanisms of acquired resistance to combined KRASG12C and [EGFR](../genes/EGFR.md) inhibition in KRASG12C-mutant colorectal cancer (CRC). The dataset includes serial ctDNA from 12 patients treated with [sotorasib](../drugs/sotorasib.md) or [adagrasib](../drugs/adagrasib.md) plus anti-EGFR antibodies ([cetuximab](../drugs/cetuximab.md) or [panitumumab](../drugs/panitumumab.md)), as well as cell line and patient-derived xenograft (PDX) models of resistance.

## Composition

- 12 patients with KRASG12C-mutant colorectal cancer treated with combination KRASG12C + EGFR inhibition: adagrasib plus cetuximab (n = 8) or sotorasib plus panitumumab (n = 4).
- Serial ctDNA collected approximately every 6 weeks in 4 patients for longitudinal resistance dynamics.
- 2 KRASG12C-mutant CRC cell lines (C106, RW7213) grown to resistance in sotorasib plus cetuximab.
- 1 KRASG12C-mutant CRC patient-derived xenograft (CLR113) treated with sotorasib plus cetuximab until acquired resistance.
- Cancer type: colorectal adenocarcinoma ([COADREAD](../cancer_types/COADREAD.md)).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) (cell lines, PDX, tissue)
- Guardant360 CDx (patients 1–5, 11)
- ctDx FIRST (patients 6–10)
- MSK-ACCESS (patient 12)

## Papers using this cohort

- [PMID:36355783](../papers/36355783.md) — Characterization of acquired resistance to combined KRASG12C + EGFR inhibition in KRASG12C-mutant CRC; dataset is the primary source.

## Notable findings derived from this cohort

- Resistance to combined KRASG12C + EGFR inhibition was heterogeneous, with multiple low-frequency alterations co-occurring: RAS mutations (58.3%), MAPK pathway (58.3%), RTK activation (75%), PI3K-mTOR (25%), nuclear function (41.7%) [PMID:36355783](../papers/36355783.md).
- KRASG12C amplification (>20 copies) was identified as the only recurrent resistance alteration that increased steadily in proportion to tumor markers across patients; all other resistance alterations appeared and disappeared at low VAF [PMID:36355783](../papers/36355783.md).
- Drug withdrawal induced oncogene-induced senescence in KRASG12C-amplified resistant cells, creating a therapeutic vulnerability to the mTOR-targeting senolytic AZD8055, as validated in patient 12 tissue biopsy showing elevated p16 (2+, 65% cells vs. 5% pretreatment) and p-S6 [PMID:36355783](../papers/36355783.md).

## Sources

- cBioPortal study: `coadread_mskresistance_2022`

*This page was processed by **crosslinker** on **2026-05-06**.*
