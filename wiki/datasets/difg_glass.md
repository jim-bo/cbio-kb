---
name: "Diffuse Glioma (GLASS International Consortium)"
slug: difg_glass
institution: GLASS International Consortium (multi-institutional)
size: 132
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [bulk-rna-seq, methylation-array, whole-exome-seq, whole-genome-seq]
panels: []
tags:
  - glioma
  - idh-mutant
  - longitudinal
  - methylation
  - glass-consortium
processed_by: crosslinker
processed_at: 2026-04-11
---

# Diffuse Glioma (GLASS International Consortium)

## Overview

Multi-institutional longitudinal glioma cohort from the GLASS International Consortium, comprising matched initial and first recurrent glioma samples profiled by DNA methylation arrays, DNA sequencing, and RNA sequencing. Designed to study epigenetic and genomic evolution across glioma subtypes upon recurrence and treatment. [PMID:38117484](../papers/38117484.md)

## Composition

- 132 patients with matched initial and first recurrent gliomas; 354 total DNA methylation samples. [PMID:38117484](../papers/38117484.md)
- Cancer types: IDH-mutant 1p/19q-codeleted oligodendroglioma ([ODG](../cancer_types/ODG.md); n=13), IDH-mutant astrocytoma ([ASTR](../cancer_types/ASTR.md); n=59), IDH-wildtype glioblastoma ([GB](../cancer_types/GB.md); n=60). [PMID:38117484](../papers/38117484.md)
- 54 patients with RNA-seq, 64 with DNA sequencing (WGS or WES), 49 with all three modalities. [PMID:38117484](../papers/38117484.md)
- Independent validation cohort: GLASS-NL consortium with 100 IDH-mutant astrocytoma patients (36 treated, 64 untreated paired samples). [PMID:38117484](../papers/38117484.md)

## Assays / panels (linked)

- Illumina 450K or EPIC BeadChip methylation arrays. [PMID:38117484](../papers/38117484.md)
- Whole-genome sequencing (WGS) and whole-exome sequencing (WES). [PMID:38117484](../papers/38117484.md)
- RNA sequencing (RNA-seq). [PMID:38117484](../papers/38117484.md)
- ChIP-seq for H3K27ac and H3K4me3 on 17 fresh-frozen GCIMP tumor samples. [PMID:38117484](../papers/38117484.md)

## Papers using this cohort

- [PMID:38117484](../papers/38117484.md) — The Epigenetic Evolution of Glioma Is Determined by the [IDH1](../genes/IDH1.md) Mutation Status and Treatment Regimen.

## Notable findings derived from this cohort

- IDH-wildtype gliomas had a stable epigenome over time; IDH-mutant gliomas showed genome-wide loss of DNA methylation at recurrence (674 CpG probes with >15% difference). [PMID:38117484](../papers/38117484.md)
- 71% (10/14) of IDH-mutant tumors that switched subtypes transitioned from GCIMP-high to GCIMP-low, associated with worse [OS](../cancer_types/OS.md). [PMID:38117484](../papers/38117484.md)
- Treatment ([temozolomide](../drugs/temozolomide.md) and/or radiotherapy) was associated with consistent loss of DNA methylation at recurrence vs. untreated patients. [PMID:38117484](../papers/38117484.md)
- [HOXD13](../genes/HOXD13.md) identified as a master regulator of IDH-mutant astrocytoma progression. [PMID:38117484](../papers/38117484.md)
- Previously treated IDH-mutant patients had worse survival from second surgery (log-rank P=0.0001) despite longer progression-free interval. [PMID:38117484](../papers/38117484.md)

## Sources

- cBioPortal study `difg_glass` [PMID:38117484](../papers/38117484.md).

*This page was processed by **crosslinker** on **2026-04-11**.*
