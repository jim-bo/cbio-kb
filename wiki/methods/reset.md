---
name: RESET
slug: reset
kind: method
canonical_source: corpus
unverified: true
tags: [methylation, epigenomics, driver-annotation]
processed_by: crosslinker
processed_at: 2026-05-16
---

# RESET

## Overview

RESET is a bioinformatic method for calling [CDKN2A](../genes/CDKN2A.md) promoter methylation-driven silencing from Illumina Infinium DNA methylation array data. It uses a specific probe (cg13601799) to classify samples as CDKN2A-promoter-methylated vs unmethylated, enabling quantification of epigenetic CDKN2A inactivation as a mechanism of cell-cycle pathway disruption. The method is applied in the context of the TCGA PanCanAtlas cell-cycle pathway analysis.

## Used by

- Applied to HM450 methylation array data (probe cg13601799) to identify CDKN2A promoter methylation-driven inactivation in 9,125 TCGA PanCanAtlas tumors across 33 cancer types, complementing somatic mutation and copy-number alteration calls for the cell-cycle pathway [PMID:29625050](../papers/29625050.md).

## Notes

- Specifically targets probe cg13601799 in the CDKN2A promoter region on Illumina HM450/EPIC arrays.
- Used to distinguish epigenetic silencing from somatic mutation or deletion as mechanisms of CDKN2A inactivation.
- Part of the TCGA PanCanAtlas driver-annotation suite alongside MutSigCV, GISTIC 2.0, Cancer Hotspots, 3D Hotspots, and OncoKB.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
