---
name: DFCI OncoPanelv2 (DFCI-ONCOPANEL-1)
slug: DFCI-ONCOPANEL-1
kind: targeted_sequencing_panel
canonical_source: cbioportal
unverified: false
tags: [targeted-sequencing, cancer-panel, somatic-mutation, copy-number]
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# DFCI OncoPanelv2 (DFCI-ONCOPANEL-1)

## Overview

DFCI-ONCOPANEL-1 (OncoPanelv2) is a targeted Illumina hybrid-capture sequencing panel covering 504 cancer-associated genes, developed at Dana-Farber Cancer Institute. It detects somatic single-nucleotide variants (SNVs), indels, and copy-number alterations (CNAs) in tumor samples. Sequencing is performed 100 bp paired-end on the HiSeq 2500 platform. The panel is validated for use with FFPE and fresh-frozen tumor material.

## Used by

- [cscc_dfarber_2015](../datasets/cscc_dfarber_2015.md) — targeted sequencing of 29 lymph-node metastases from HPV-negative cutaneous squamous cell carcinoma patients; mean tumor coverage 82× (range 25–166×); variant calling via [mutect](../methods/mutect.md) with OxoG filtering, annotation via [oncotator](../methods/oncotator.md), significance by [mutsig](../methods/mutsig.md), and CNAs by [gistic](../methods/gistic.md) 2.0 [PMID:25589618](../papers/25589618.md)

## Notes

- Covers 504 cancer-associated genes; suitable for tumor-only or paired tumor/normal sequencing.
- Reads aligned to b37 reference genome with Picard/Firehose.
- Typical tumor coverage ~82×; normal ~69× in the cSCC cohort.
- Variant annotation via Oncotator against dbSNP 134 and 1000 Genomes.
- CNA calling with Nexus 7.5 and GISTIC 2.0 (arm-level peel correction; minimum segment size 6).
- HPV status can be independently assessed via hybrid-capture sequencing of HPV E6/E7 sequences.

## Sources

- [PMID:25589618](../papers/25589618.md) — Li et al. 2015, targeted sequencing of metastatic cSCC

*This page was processed by **entity-page-writer** on **2026-05-14**.*
