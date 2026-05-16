---
name: Selected Reaction Monitoring (SRM/MRM)
slug: selected-reaction-monitoring
kind: method
canonical_source: corpus
unverified: true
tags:
  - proteomics
  - mass-spectrometry
  - targeted-proteomics
  - validation
  - srm
  - mrm
processed_by: crosslinker
processed_at: 2026-05-16
---

# Selected Reaction Monitoring (SRM/MRM)

## Overview

Selected Reaction Monitoring (SRM), also known as Multiple Reaction Monitoring (MRM), is a targeted mass spectrometry technique for highly sensitive and precise quantification of specific proteins or peptides. Unlike discovery proteomics (shotgun/LC-MS/MS), SRM preselects parent-ion/fragment-ion pairs (transitions) for proteins of interest and monitors them across samples, enabling [absolute](../methods/absolute.md) quantification with high reproducibility and sensitivity. SRM is commonly used to validate findings from discovery proteomics experiments.

## Used by

- Used for targeted validation of [CD8A](../genes/CD8A.md), [SLC2A3](../genes/SLC2A3.md) (GLUT3), and [PKM](../genes/PKM.md) isoforms in the CPTAC colon cancer proteogenomic study ([coad_cptac_2019](../datasets/coad_cptac_2019.md), n=110); confirmed SLC2A3 was 1.85-fold elevated (p=0.007) and PKM2 was 1.4-fold elevated (p=0.003) in MSI vs other unified molecular subtype tumors; demonstrated PKM2, not PKM1, is the predominant pyruvate kinase isoform in colon cancer [PMID:31031003](../papers/31031003.md)

## Notes

- SRM validation in the CPTAC study corroborated discovery-phase findings linking glycolytic protein overexpression to reduced CD8 T-cell infiltration in MSI-H colon tumors (median glycolytic-enzyme vs CD8 infiltration Spearman rho = -0.61, p=0.02).
- SRM transitions can be designed to distinguish protein isoforms (e.g., PKM1 vs PKM2) at the peptide level, which is challenging with antibody-based methods.
- Not in cBioPortal gene-panels or molecular-profiles ontologies; corpus-grown slug.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
