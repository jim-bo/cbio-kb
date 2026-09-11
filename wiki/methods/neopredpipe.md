---
name: NeoPredPipe
slug: neopredpipe
kind: method
canonical_source: corpus
unverified: true
tags: [neoantigen-prediction, immunogenomics, bioinformatics]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# NeoPredPipe

## Overview

A neoantigen prediction pipeline that integrates somatic variant calls with patient HLA class I genotypes and peptide-binding prediction to generate ranked candidate neoantigen lists from tumor exome (or genome) data, typically run downstream of HLA typing and variant calling.

## Used by

- Predicted neoantigens from somatic variant calls in a colorectal cancer whole-exome sequencing cohort, alongside POLYSOLVER HLA typing, LOHHLA for HLA loss of heterozygosity, and an immunoediting score [PMID:35487942](../papers/35487942.md).

## Notes

- Runs downstream of HLA class I genotyping (e.g., POLYSOLVER) and somatic variant calling.
- Commonly paired with HLA-LOH detection (e.g., LOHHLA) and immunoediting quantification in immune-landscape analyses.

## Sources

- [PMID:35487942](../papers/35487942.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
