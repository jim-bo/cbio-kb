---
name: ContEst
slug: contest
kind: method
canonical_source: corpus
unverified: true
tags: [quality-control, contamination, sequencing]
processed_by: crosslinker
processed_at: 2026-05-15
---

# ContEst

## Overview

ContEst (Contamination Estimation) is a tool developed at the Broad Institute for estimating cross-sample contamination in tumor/normal sequencing pairs. It models the fraction of reads derived from a contaminating sample using SNP genotype likelihoods. Samples exceeding a contamination threshold are excluded from downstream somatic variant calling.

## Used by

- Applied as a quality-control step in the TCGA MC3 pipeline; samples with ContEst contamination > 4% were excluded (12 rules applied total); run by Broad Firehose alongside MuTect and Indelocator [PMID:29596782](../papers/29596782.md)
- Applied in the [prad_p1000](../datasets/prad_p1000.md) prostate cancer WES pipeline (ContEst < 5% threshold; mean contamination 0.6%) [PMID:29610475](../papers/29610475.md)

## Notes

- Contamination [estimate](../methods/estimate.md) > 4–5% is the typical exclusion threshold used in TCGA-affiliated pipelines.
- Run at Broad Firehose as part of the MC3 Broad pipeline arm.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
