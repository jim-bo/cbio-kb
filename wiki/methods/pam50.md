---
name: PAM50
slug: pam50
kind: method
canonical_source: corpus
unverified: true
tags:
  - breast-cancer
  - gene-expression
  - intrinsic-subtype
  - classifier
processed_by: crosslinker
processed_at: 2026-05-16
---

# PAM50

## Overview

PAM50 is a 50-gene RT-PCR-based expression assay that classifies breast tumors into five intrinsic molecular subtypes: Luminal A, Luminal B, HER2-enriched, Basal-like, and Normal-like. It was developed to provide a reproducible, transcriptomics-based subtyping that captures biologically distinct disease categories beyond immunohistochemical (IHC) surrogates. PAM50 is also used to compute a Prosigna Risk of Recurrence (ROR) score. The assay is commercially available as the Prosigna test (NanoString Technologies).

## Used by

- Applied to 1,980 METABRIC patients with copy-number and gene-expression data (Molecular Dataset subset of n=3,240 total) to assign intrinsic subtypes used alongside IntClust integrative subtypes in a multistate Markov model of breast cancer recurrence trajectories ([brca_metabric](../datasets/brca_metabric.md)) [PMID:30867590](../papers/30867590.md)

## Notes

- PAM50 subtyping at the molecular level captures prognostic information that is partially but not completely overlapping with IHC (ER/HER2 status). The METABRIC study showed that IntClust subtypes provide additional late-relapse discrimination beyond both IHC and PAM50 in ER+/HER2- disease.
- The PAM50 Normal-like subtype is considered a technical artifact by some authors as it may reflect high stromal contamination rather than a distinct biological entity.
- Gene panel ID not found in cBioPortal gene-panels ontology; corpus-grown slug.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
