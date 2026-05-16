---
name: TMT global proteomics
slug: tmt-proteomics
kind: method
canonical_source: corpus
unverified: true
tags:
  - proteomics
  - mass-spectrometry
  - tandem-mass-tag
  - quantitative-proteomics
  - multi-omics
processed_by: crosslinker
processed_at: 2026-05-16
---

# TMT global proteomics

## Overview

Tandem mass tag (TMT) global proteomics is an isobaric chemical labeling approach for multiplexed, quantitative protein abundance measurement by mass spectrometry. Peptides from up to 16 samples are labeled with isotopically distinct TMT reagents, combined, and analyzed together; quantitation relies on reporter-ion intensities in the MS2 or MS3 spectrum. TMT proteomics enables direct comparison of protein levels across multiple tumor and normal-adjacent tissue (NAT) samples within a single LC-MS/MS run, reducing inter-batch variability. In the CPTAC program, TMT10-plex or TMT11-plex is routinely applied to tumor cohorts to generate global protein abundance matrices.

## Used by

- Applied to 96 tumor/NAT pairs from the prospective CPTAC colon cancer cohort ([coad_cptac_2019](../datasets/coad_cptac_2019.md), n=110 total) alongside label-free and TMT phosphoproteomics; quantified 6,422 proteins in >=50% of samples; 2,217 (35%) were significantly increased and 2,527 (39%) significantly decreased in tumors vs NATs (adj. p<0.01); 31 proteins increased >2-fold including [DDX21](../genes/DDX21.md), [S100A11](../genes/S100A11.md), and [S100P](../genes/S100P.md) (each in 97–100% of pairs) [PMID:31031003](../papers/31031003.md)

## Notes

- TMT global proteomics revealed a protein-level Warburg effect (glycolytic enzyme upregulation + TCA-cycle decrease) in MSI-H tumors not visible at the mRNA level — demonstrating the added value of proteomics over transcriptomics alone.
- Cis-effects of somatic copy-number alterations on protein were found to be stronger than on mRNA in the CPTAC colon cohort, highlighting the importance of protein-level readouts for driver prioritization.
- Not in cBioPortal gene-panels or molecular-profiles ontologies; corpus-grown slug.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
