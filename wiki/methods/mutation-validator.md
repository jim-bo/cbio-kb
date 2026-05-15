---
name: Mutation Validator
slug: mutation-validator
kind: method
canonical_source: corpus
unverified: true
tags: [validation, somatic-calling, quality-control]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# Mutation Validator

## Overview

Mutation Validator is a tool for cross-validating somatic variant calls using orthogonal sequencing data (e.g., targeted deep sequencing). In the TCGA MC3 context, it was used to assess the accuracy of ensemble MAF calls against targeted-sequencing validation data on 3,128 samples (median 126 validation sites/sample).

## Used by

- Applied within the TCGA MC3 project to validate somatic calls from the ensemble pipeline against TCGA targeted deep-sequencing data on 3,128 samples; validation was performed on the ISB Cancer Genomics Cloud and Broad FireCloud [PMID:29596782](../papers/29596782.md)

## Notes

- Validation sites in MC3 were non-randomly selected by individual TCGA AWGs, biased toward known SMG candidates; false-negative rates for sites missed by all callers cannot be estimated.
- Most validation used the same sequencing chemistry as discovery, limiting its ability to detect systematic errors targeted by filters such as PoN and OxoG.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
