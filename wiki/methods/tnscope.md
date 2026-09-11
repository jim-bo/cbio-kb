---
name: TNscope
slug: tnscope
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [somatic-variant-calling, wgs, tumour-normal]
processed_by: wiki-cli
processed_at: 2026-09-10
---

# TNscope

## Overview

TNscope is a somatic variant caller developed by Sentieon that detects SNVs, indels, and structural variants from tumour-normal paired WGS or WES data. It uses a haplotype-based approach similar to HaplotypeCaller and is optimised for high sensitivity at low allele fractions.

## Used by

- Applied in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for somatic SNV and indel detection in paired tumour-normal WGS (mean tumour coverage 85×, normal 31×) for the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)
- One of three somatic callers (with Mutect2 and VarScan2) requiring agreement from at least 2 of 3 for SNV/indel calls, filtered to VAF at least 8%, depth at least 8, and at least 2 supporting reads [PMID:35487942](../papers/35487942.md)

## Notes

- TNscope was part of a multi-caller consensus pipeline alongside MuTect and Strelka in the Sherlock-Lung study.
- High-coverage WGS (mean 85×) allows sensitive detection of subclonal somatic variants with allele fractions below 10%.
- Sentieon TNscope is commercially available and is commonly used in clinical WGS pipelines due to its speed and sensitivity.

## Sources
- [PMID:35487942](../papers/35487942.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
