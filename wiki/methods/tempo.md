---
name: TEMPO
slug: tempo
kind: method
canonical_source: corpus
unverified: true
tags: [analysis-pipeline, whole-exome-seq, msk, somatic-variant-calling]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# TEMPO

## Overview

TEMPO is an MSKCC computational pipeline for processing paired tumor-normal whole-exome sequencing data. It integrates FACETS (allele-specific copy number), MSIsensor (microsatellite instability), OncoKB (variant oncogenicity classification), and COSMIC mutational-signature decomposition into a single workflow.

## Used by

- Ran the MSKCC TEMPO pipeline on paired tumor-normal WES from a rectal cancer cohort, combined with FACETS for allele-specific copy number, MSIsensor for MSI (score threshold ≥10), OncoKB to classify variants as oncogenic, and COSMIC v3 mutational signatures [PMID:40100215](../papers/40100215.md)

## Notes

- Observed as a named MSKCC analysis pipeline rather than a single tool; not yet in cBioPortal's canonical method/panel lists.

## Sources

*This page was processed by **entity-page-writer** on **2026-09-10**.*
