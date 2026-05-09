---
name: Quantitative Methylation-Specific PCR (qMSP)
slug: qmsp
kind: method
canonical_source: corpus
unverified: true
tags: [methylation, pcr, epigenetics, bisulfite-sequencing]
processed_by: crosslinker
processed_at: 2026-05-09
---

# Quantitative Methylation-Specific PCR (qMSP)

## Overview

Quantitative methylation-specific PCR (qMSP) measures promoter CpG methylation at specific gene loci after bisulfite conversion of DNA. Sodium bisulfite converts unmethylated cytosines to uracil (then thymine after PCR) while methylated cytosines remain unchanged. Separate PCR primer pairs targeting the unmethylated (U) and methylated (M) converted sequences are used in quantitative (real-time) PCR; results are expressed as a ratio of methylated to total signal. Commonly uses the EZ DNA Methylation kit (Zymo Research) or equivalent for bisulfite conversion.

## Used by

- Applied to 23 pancreatic neoplasms with acinar differentiation after EZ bisulfite conversion, with U/M primer pairs targeting [BRCA1](../genes/BRCA1.md) and [MLH1](../genes/MLH1.md) promoters; found 0/23 BRCA1-methylated and 1/23 MLH1-methylated (ACINAR06) tumors — MLH1 methylation did not correlate with MSI status in this cohort [PMID:24293293](../papers/24293293.md).

## Notes

- qMSP is locus-specific and targeted; genome-wide methylation profiling requires RRBS or methylation arrays.
- Sensitivity depends on tumor purity and bisulfite conversion efficiency.
- In the PMID:24293293 acinar carcinoma cohort, MLH1 methylation was detected in only 1/23 tumors and did not explain the MSI phenotype, arguing against promoter silencing as the primary MMR-inactivation mechanism in this tumor type.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
