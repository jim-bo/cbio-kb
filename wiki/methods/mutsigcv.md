---
name: MutSigCV
slug: mutsigcv
kind: method
canonical_source: corpus
unverified: true
tags:
  - significantly-mutated-genes
  - somatic-mutation
  - bioinformatics
  - cancer-genomics
processed_by: crosslinker
processed_at: 2026-05-16
---

# MutSigCV

## Overview

MutSigCV is a statistical method for identifying significantly mutated genes (SMGs) in cancer cohorts. It extends the MutSig framework by correcting for covariates of local mutation rate — including gene expression level, DNA replication timing, and chromatin accessibility — that cause many apparent mutations to be background events. MutSigCV uses negative binomial regression to model these covariates and computes per-gene p-values and q-values (FDR-corrected) for the null hypothesis that a gene's mutation rate does not exceed background. It is one of the standard SMG discovery methods in TCGA and large pan-cancer analyses.

## Used by

- Applied to 106 colon cancer WXS profiles ([coad_cptac_2019](../datasets/coad_cptac_2019.md)) in the CPTAC proteogenomic study; identified 8 SMGs in the non-hypermutated group (all previously reported in TCGA) and 9 in the hypermutated/MSI-H group, including four novel SMGs ([CASP5](../genes/CASP5.md), [RNF43](../genes/RNF43.md), [LTN1](../genes/LTN1.md), [BMPR2](../genes/BMPR2.md)) mutated in >50% of MSI-H samples [PMID:31031003](../papers/31031003.md)

## Notes

- MutSigCV is particularly important for exome-scale cohorts where local mutation-rate variation (e.g., in late-replicating, low-expression gene regions) can produce false positives if not corrected.
- The four novel hypermutated SMGs identified in the CPTAC colon study (CASP5, RNF43, LTN1, BMPR2) were not reported in the original TCGA colorectal analysis, possibly due to the MSI-H enrichment of the CPTAC prospective cohort.
- Not in cBioPortal gene-panels ontology; corpus-grown slug.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
