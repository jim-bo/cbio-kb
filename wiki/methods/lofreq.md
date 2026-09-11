---
name: LoFreq
slug: lofreq
kind: method
canonical_source: corpus
unverified: true
tags: [variant-calling, computational, somatic-mutations]
processed_by: crosslinker
processed_at: 2026-09-11
---

# LoFreq

## Overview

LoFreq is a sensitive somatic variant caller designed to detect low-frequency single-nucleotide variants from next-generation sequencing data, using a statistical model of sequencing error to distinguish true low-VAF variants from noise.

## Used by

- Used alongside Strelka for somatic variant calling from whole-exome sequencing data in a study of molecular correlates of response to [atezolizumab](../drugs/atezolizumab.md), with or without [bevacizumab](../drugs/bevacizumab.md), versus [sunitinib](../drugs/sunitinib.md) in renal cell carcinoma [PMID:29867230](../papers/29867230.md).

## Notes

- Corpus-grown slug; not in the cBioPortal gene-panel or molecular-profile ontology.
- Used as a complementary caller to Strelka in this cohort, likely to increase sensitivity for low-VAF somatic variants.

## Sources

- [PMID:29867230](../papers/29867230.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
