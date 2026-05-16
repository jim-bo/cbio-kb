---
name: LOHHLA
slug: lohhla
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [hla, loss-of-heterozygosity, immune-evasion, wgs]
processed_by: crosslinker
processed_at: 2026-05-16
---

# LOHHLA

## Overview

LOHHLA (Loss Of Heterozygosity in Human Leukocyte Antigen) is a computational tool that infers allele-specific copy-number at the HLA locus from sequencing data. It detects somatic loss of heterozygosity at HLA class I loci ([HLA-A](../genes/HLA-A.md), [HLA-B](../genes/HLA-B.md), [HLA-C](../genes/HLA-C.md)), which is a mechanism of immune evasion in tumours.

## Used by

- Applied in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS); HLA LOH was enriched in TP53-deficient tumours and RTK-RAS pathway-altered tumours in the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)

## Notes

- HLA LOH is a mechanism by which tumours evade immune surveillance by eliminating neoantigen presentation alleles.
- In the Sherlock-Lung cohort, [BRCA1](../genes/BRCA1.md) LOH was also enriched in the TP53-deficient/MDM2-amplified tumour group alongside HLA LOH.
- Piano tumours with low TMB and rare HLA LOH are predicted to be poor responders to immune checkpoint inhibitors.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
