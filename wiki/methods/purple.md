---
name: PURPLE (purity and ploidy estimator)
slug: purple
kind: method
canonical_source: corpus
unverified: true
tags: [cnv, purity-ploidy, wgs, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-21
---

# PURPLE (purity and ploidy estimator)

## Overview

PURPLE is an open-source tumor purity and ploidy estimation tool developed by the Hartwig Medical Foundation. It integrates read-depth ratios (from WGS coverage), B-allele frequencies (BAF) from germline heterozygous SNPs, and structural variants (from GRIDSS) to [estimate](../methods/estimate.md) tumor cellularity and ploidy, and to produce allele-specific copy-number profiles. PURPLE is the second component of the Hartwig WGS pipeline (GRIDSS → PURPLE → LINX) and enables high-resolution somatic CNV calling genome-wide.

## Used by

- Used for purity/ploidy estimation and CNV profiling in WGS of 25 metastatic [CSCC](../cancer_types/CSCC.md) lymph node specimens alongside GRIDSS and LINX; produced the allele-specific CN landscape including focal [PTPRD](../genes/PTPRD.md) deletion (24% of samples), [CDKN2A](../genes/CDKN2A.md) deletion, [MYC](../genes/MYC.md) amplification, and co-amplification of CCND1/FGF3 in two cases [PMID:35982973](../papers/35982973.md)

## Notes

- Inputs: WGS coverage (read-depth ratios), germline BAF, and GRIDSS SVs.
- Outputs: tumor purity, ploidy, and allele-specific copy-number segments.
- Developed by Hartwig Medical Foundation; widely used in WGS-based cancer research.

## Sources

- [PMID:35982973](../papers/35982973.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
