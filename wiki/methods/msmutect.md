---
name: MSMuTect
slug: msmutect
kind: method
canonical_source: corpus
unverified: true
tags:
  - somatic-mutation
  - microsatellite
  - indel
  - msi
  - bioinformatics
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSMuTect

## Overview

MSMuTect is a computational tool for accurate detection of somatic microsatellite (MS) insertions and deletions (INDELs) from paired tumor-normal sequencing data. It uses a probabilistic model of MS locus behavior to call somatic changes in repeat-unit count, enabling comprehensive profiling of the MS mutation landscape — which is especially relevant for microsatellite-unstable (MSI-H) tumors. MSMuTect was used in the CPTAC colon cancer proteogenomic study to characterize the bimodal distribution of MS INDEL counts that separates MSI-H from MSS tumors.

## Used by

- Used to identify 6,186 somatic microsatellite INDELs across 106 CPTAC colon cancer tumors ([coad_cptac_2019](../datasets/coad_cptac_2019.md)); MS INDEL count showed a bimodal distribution partitioning 24 MSI-H from 82 MSS tumors; MSI-H tumors showed increased A>G/T>C transitions and were enriched for mismatch-repair-pathway and BRAF/POLE mutations [PMID:31031003](../papers/31031003.md)

## Notes

- Complements standard SNV/INDEL callers (e.g., MuTect2) by focusing specifically on microsatellite loci where short-read aligners may miscall repeat-expansion events.
- Results in the CPTAC study were 100% concordant with PCR-based MSI testing ([msi-pcr-pentaplex](../methods/msi-pcr-pentaplex.md)) on 85 overlapping samples.
- Not in cBioPortal gene-panels ontology; corpus-grown slug.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
