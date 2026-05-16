---
name: VarDict
slug: vardict
kind: method
canonical_source: corpus
unverified: true
tags:
  - variant-calling
  - somatic
  - snv
  - indel
  - ctdna
processed_by: wiki-cli
processed_at: 2026-05-16
---

# VarDict

## Overview

VarDict is an open-source somatic variant caller designed for targeted sequencing data. It calls single-nucleotide variants (SNVs) and insertions/deletions (indels) from matched tumor–normal or tumor-only sequencing. VarDict is optimized for sensitivity at low variant allele frequencies (VAFs), making it suitable for liquid biopsy (cfDNA) applications where tumor-derived variants may be present at sub-1% VAF. It supports multiple output modes and integrates with standard variant-annotation workflows.

## Used by

- Applied as the tumor-blind de novo somatic variant caller for plasma cfDNA in a 10-patient pediatric retinoblastoma cohort; used in conjunction with custom VAF and buffy-coat filters (VAF >0.5%, ≥10 mutant reads, VAF >2× matched buffy coat) to recover 7/13 expected somatic [RB1](../genes/RB1.md) mutations in 6/10 patients without reference to matched tumor data [PMID:32633890](../papers/32633890.md)
- Used alongside [MuTect](../methods/mutect.md) for SNV/indel calling in cfDNA from 681 plasma samples in the MSK-ACCESS pipeline; variant calls from both callers integrated into the MSK-ACCESS bioinformatics workflow [PMID:34145282](../papers/34145282.md)
- Part of the MSK-ACCESS bioinformatics pipeline applied to cfDNA from metastatic solid tumor patients in the tumor-fraction-guided cfDNA triage study [PMID:34059130](../papers/34059130.md)

## Notes

- Used alongside [Waltz 2.0](../methods/waltz.md) (tumor-guided genotyping) and manual review in IGV v2.3.36 in the retinoblastoma cfDNA study.
- At low VAF (sub-1%), VarDict de novo calls require additional filtering against matched buffy coat and a panel of unmatched normals to control false positives; the error floor at sub-1% VAF without unique molecular identifiers (UMIs) was not fully characterized in [PMID:32633890](../papers/32633890.md).

## Sources

- [PMID:32633890](../papers/32633890.md) — Plasma cfDNA somatic RB1 variant detection in pediatric retinoblastoma; VarDict used for tumor-blind de novo calling.

*This page was processed by **crosslinker** on **2026-05-16**.*
- [PMID:34145282](../papers/34145282.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:34059130](../papers/34059130.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
