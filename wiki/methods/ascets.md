---
name: ASCETS (Arm-level Somatic Copy-number Events in Targeted Sequencing)
slug: ascets
kind: method
canonical_source: corpus
unverified: true
tags: [copy-number, targeted-sequencing, aneuploidy, arm-level, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-16
---

# ASCETS (Arm-level Somatic Copy-number Events in Targeted Sequencing)

## Overview

ASCETS is a computational tool that infers chromosome arm-level somatic copy-number alterations (SCNAs) from targeted hybrid-capture sequencing data (such as MSK-IMPACT), where whole-genome or whole-exome coverage is unavailable. It uses the gene-level integer copy-number calls produced by FACETS to classify each chromosome arm as gained, lost, or neutral relative to the sample ploidy. This enables arm-level aneuploidy scoring — comparable to TCGA-style chromosome arm aneuploidy scores derived from SNP arrays — directly from targeted panel sequencing without requiring SNP-array or WGS data.

## Used by

- Arm-level CNAs in 2,069 MSK-IMPACT-profiled prostate cancer patients (1,841 White, 165 Black, 63 Asian) were called with ASCETS; chr8q gain was enriched in Black men (49%) vs White men (37%, adjusted difference +11 pp, 95% CI 4–18) and was independently prognostic for [OS](../cancer_types/OS.md) (HR 2.00, 95% CI 1.00–4.01 in Black men) [PMID:34667026](../papers/34667026.md)

## Notes

- ASCETS is designed as a downstream post-processor of FACETS allele-specific integer copy-number segments mapped to chromosome arms.
- Enables aneuploidy analyses in large institutional targeted-sequencing cohorts where whole-genome data are not available, bridging the gap between SNP-array-derived TCGA arm scores and clinical NGS panels.
- Requires reliable tumor purity and ploidy estimation (typically from FACETS) for accurate arm classification.

## Sources

- [PMID:34667026](../papers/34667026.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
