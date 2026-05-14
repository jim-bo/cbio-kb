---
name: VariantDx
slug: variantdx
kind: method
canonical_source: corpus
unverified: true
tags: [variant-calling, somatic-mutations, matched-tumor-normal, wgs]
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# VariantDx

## Overview

VariantDx is a custom somatic mutation-calling pipeline developed for matched tumor/normal whole-genome or whole-exome sequencing. It applies paired-sample variant detection with filtering steps to distinguish somatic variants from germline polymorphisms and sequencing artifacts. Designed for use with hg19/GRCh37 reference genome, VariantDx was applied in the Johns Hopkins adenoid cystic carcinoma (ACC) WGS study for high-specificity somatic SNV and indel detection.

## Used by

- VariantDx custom somatic-mutation caller used for matched tumor/normal variant detection in 25 ACC WGS samples (hg19 reference); identified 396 somatic mutations in 372 genes (median 14/tumor, range 2–36) and supported discovery of recurrent mutations in Rho-GTPase, axon-guidance, chromatin-regulator, and Notch pathways [PMID:26862087](../papers/26862087.md)

## Notes

- Custom pipeline; not widely distributed as a standalone public tool.
- Applied to matched tumor/normal WGS data for somatic SNV and indel calling.
- Results were supplemented by TopHat-Fusion for fusion detection and snpEff for functional annotation in the same study.
- Neoplastic cellularity ≥60% was required for input samples to reduce stromal contamination artifacts.

## Sources

- [PMID:26862087](../papers/26862087.md)

*This page was processed by **entity-page-writer** on **2026-05-14**.*
