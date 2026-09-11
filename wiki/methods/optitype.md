---
name: OptiType
slug: optitype
kind: method
canonical_source: corpus
unverified: true
tags: [hla-typing, neoantigen-prediction, bioinformatics]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# OptiType

## Overview

An HLA class I genotyping tool that uses integer linear programming over exome or RNA-seq reads aligned to an HLA reference to call four-digit HLA-A/B/C alleles, commonly run as the first step of a neoantigen prediction pipeline.

## Used by

- OptiType HLA typing fed pVACseq (with NetMHCpan, PickPocket, SMM and SMMPMBEC) to predict neoantigens, keeping peptides with best mutant-allele IC50 <=500 nM, in a gastric cancer PDX/patient-tumor comparison [PMID:37990009](../papers/37990009.md).

## Notes

- Produces four-digit HLA class I genotypes used to seed downstream peptide-binding prediction (e.g., NetMHCpan, pVACseq).

## Sources

- [PMID:37990009](../papers/37990009.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
