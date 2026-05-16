---
name: Waltz
slug: waltz
kind: method
canonical_source: corpus
unverified: true
tags:
  - variant-calling
  - somatic
  - tumor-guided
  - ctdna
  - liquid-biopsy
processed_by: crosslinker
processed_at: 2026-05-16
---

# Waltz

## Overview

Waltz (version 2.0) is a tumor-guided somatic variant caller developed at Memorial Sloan Kettering Cancer Center for ultra-sensitive detection of low-frequency variants in cell-free DNA (cfDNA). The tumor-guided approach uses mutations previously identified in matched tumor tissue to focus calling in plasma, dramatically improving sensitivity relative to tumor-blind de novo approaches. It is part of the MSK cfDNA analysis pipeline and is used in conjunction with high-depth targeted sequencing panels.

## Used by

- Used as the tumor-guided genotyping caller for plasma cfDNA in a 10-patient pediatric retinoblastoma cohort; with a custom hybrid-capture panel (average unique coverage ~1530×), Waltz 2.0 recovered 10/13 expected somatic [RB1](../genes/RB1.md) mutations in 8/10 patients (median VAF 4.9%, range 0.7%–12.6%) [PMID:32633890](../papers/32633890.md)

## Notes

- Tumor-guided genotyping via Waltz achieves higher sensitivity than tumor-blind de novo calling (10/13 vs. 7/13 RB1 mutations recovered in [PMID:32633890](../papers/32633890.md)) at the cost of requiring matched tumor sequencing data.
- Used alongside [VarDict](../methods/vardict.md) (tumor-blind de novo calling) and the [rb1-cfdna-custom-capture-panel](../methods/rb1-cfdna-custom-capture-panel.md) in the retinoblastoma cfDNA study.
- Technical replicates of 5 samples showed Waltz VAF concordance with Pearson r²=0.993.

## Sources

- [PMID:32633890](../papers/32633890.md) — Plasma cfDNA somatic RB1 variant detection in pediatric retinoblastoma; Waltz 2.0 used for tumor-guided genotyping.

*This page was processed by **crosslinker** on **2026-05-16**.*
