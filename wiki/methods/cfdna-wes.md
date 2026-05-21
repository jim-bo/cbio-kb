---
name: cfDNA Whole-Exome Sequencing
slug: cfdna-wes
kind: method
canonical_source: corpus
unverified: true
tags: [liquid-biopsy, cfDNA, whole-exome-seq, ctDNA]
processed_by: crosslinker
processed_at: 2026-05-21
---

# cfDNA Whole-Exome Sequencing

## Overview

Cell-free DNA whole-exome sequencing (cfDNA-WES) is a liquid-biopsy approach that applies whole-exome capture to circulating cell-free DNA extracted from plasma, enabling genome-wide detection of somatic alterations (SNVs, indels, copy-number alterations) without requiring a fresh tumor biopsy. Plasma is typically sequenced at high depth (e.g., 100× mean depth) using standard exome capture kits (Agilent SureSelect, Twist, etc.). cfDNA-WES can detect actionable alterations across the exome, including mutations missed in targeted panels, and is particularly valuable when re-biopsy is not feasible. Sensitivity for SNVs is generally around 5% variant allele frequency threshold; CNA calling requires higher ctDNA fractions (~20%).

## Used by

- MAPPYACTS precision-oncology trial (NCT02613962): plasma WES at 100× depth attempted in 234 extracerebral pediatric solid-tumor patients; 128/190 (67%) analyzable with paired tumor WES — 76% of tumor actionable SNVs also detected in plasma; 14 patients had 35 additional actionable SNVs detected only by cfDNA-WES, including an [ALK](../genes/ALK.md) p.Arg1275Gln detected only in plasma [PMID:35292802](../papers/35292802.md).

## Notes

- cfDNA-WES sensitivity is higher in high-ctDNA-fraction tumors (e.g., neuroblastoma median 35% vs 16% in other pediatric cancers in MAPPYACTS).
- cfDNA-WES success rate was 67% in patients with paired tumor WES success; lower in localized disease (47%) vs metastatic disease (66%).
- CNA calling from cfDNA-WES is limited by lower allelic fraction thresholds (~20%) compared to SNV calling (~5%).
- Different capture kits between tumor and plasma can complicate CNA calling comparisons.
- Salvage application: cfDNA-WES succeeded in 11/35 (34%) patients where tumor WES failed, identifying actionable findings in 5.
- Corpus-grown slug; not in cBioPortal gene-panel ontology.

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
