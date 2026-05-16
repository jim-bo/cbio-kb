---
name: SELECT
slug: select
kind: method
canonical_source: corpus
unverified: true
tags: [statistics, mutual-exclusivity, co-occurrence, driver-analysis]
processed_by: crosslinker
processed_at: 2026-05-16
---

# SELECT

## Overview

SELECT is a statistical method for testing mutual exclusivity and co-occurrence of somatic alterations across a cancer cohort. It accounts for differences in alteration frequencies across tumor types and samples when assessing whether pairs of alterations appear together or are mutually exclusive more often than expected by chance. The method is applied in pan-cancer analyses to identify functionally interpretable alteration pairs (e.g., within-pathway exclusivity indicating functional redundancy, cross-pathway co-occurrence indicating synergistic dependencies).

## Used by

- Applied to 416 oncogenic alterations in 9,125 TCGA PanCanAtlas tumors to identify significant mutual exclusivity and co-occurrence pairs; yielded 152 mutually exclusive pairs and 116 co-occurring pairs (Table S5); [EGFR](../genes/EGFR.md) was involved in the most significant SELECT pairs of any gene [PMID:29625050](../papers/29625050.md).

## Notes

- Accounts for tumor-type-specific alteration frequencies, which is essential for pan-cancer cohorts where marginal mutation rates differ substantially by cancer type.
- Mutual exclusivity within a pathway suggests functional redundancy (one alteration is sufficient); co-occurrence across pathways can nominate combination-therapy targets.
- Notable results in the PanCanAtlas: RTK activation mutually exclusive with downstream RAS/PI3K alterations; FGFR2/FGFR3 exceptionally co-occurred with PI3K-pathway alterations despite typical RTK–PI3K exclusivity.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
