---
name: GATK Somatic Indel Detector
slug: gatk-somatic-indel-detector
kind: somatic_variant_calling
canonical_source: corpus
unverified: true
tags: [variant-calling, indel, somatic, GATK]
processed_by: crosslinker
processed_at: 2026-05-14
---

# GATK Somatic Indel Detector

## Overview

GATK Somatic Indel Detector is a variant-calling tool from the Genome Analysis Toolkit (GATK) designed to detect somatic insertion and deletion (indel) events in paired tumor/normal sequencing data. It identifies candidate somatic indels by comparing allele frequencies between tumor and matched normal samples, with configurable thresholds for minimum allele fraction and read support.

## Used by

- [coad_caseccc_2015](../datasets/coad_caseccc_2015.md) — used alongside [mutect](../methods/mutect.md) and [varscan](../methods/varscan.md) for somatic indel calling in 29 AA CRC discovery exomes (paired tumor/normal); contributed to identification of 20 significantly mutated genes in African American MSS colorectal cancer including [EPHA6](../genes/EPHA6.md) and [FLCN](../genes/FLCN.md) as AA-specific drivers [PMID:25583493](../papers/25583493.md)

## Notes

- Part of the GATK toolkit; intended for use with BWA-aligned BAM files.
- Typically used in combination with other somatic callers (MuTect for SNVs, VarScan for SNVs/indels) for increased sensitivity.
- Superseded in later GATK versions (GATK4+) by Mutect2, which handles both SNVs and indels.

## Sources

- [PMID:25583493](../papers/25583493.md) — Guda et al. 2015, WES of African American MSS CRC

*This page was processed by **crosslinker** on **2026-05-14**.*
