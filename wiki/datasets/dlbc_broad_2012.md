---
name: Diffuse Large B-Cell Lymphoma (Broad, 2012)
studyId: dlbc_broad_2012
institution: Broad Institute / Dana-Farber Cancer Institute
size: 55
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [MUTATION_EXTENDED]
panels: []
tags: [DLBCL, lymphoma, WES, MutSig]
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Diffuse Large B-Cell Lymphoma (Broad, 2012)

## Overview

This cohort was generated at the Broad Institute in collaboration with Dana-Farber Cancer Institute, Mayo Clinic, University of Iowa, and Instituto Nacional de Medicina Genomica (Mexico). It comprises 55 primary DLBCL tumor samples with matched germline DNA profiled by [whole-exome sequencing](../methods/whole-exome-seq.md) at 150-fold mean coverage. Statistical significance testing with [MutSig](../methods/mutsig.md) identified 58 significantly mutated genes, including newly implicated drivers such as [MEF2B](../genes/MEF2B.md), [KMT2D](../genes/KMT2D.md), [BTG1](../genes/BTG1.md), [GNA13](../genes/GNA13.md), [ACTB](../genes/ACTB.md), [P2RY8](../genes/P2RY8.md), PCLO, and [TNFRSF14](../genes/TNFRSF14.md).

## Composition

- 55 paired tumor (lymph node biopsy) and germline (peripheral blood) samples; 49 passed QC after excluding 6 with extensive stromal contamination.
- Cancer type: [DLBCLNOS](../cancer_types/DLBCLNOS.md).
- Multi-institution enrollment across US and Mexico.

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md): 150-fold mean coverage; 97% of bases covered per patient (range 91-98%).
- [MutSig](../methods/mutsig.md): statistical framework for identifying genes mutated at rates exceeding background.
- Targeted resequencing for validation: 47 of 47 variants confirmed (97.9% validation rate).

## Papers using this cohort

- [PMID:22343534](../papers/22343534.md) — Primary WES study identifying 58 significantly mutated genes in DLBCL.

## Notable findings derived from this cohort

- MutSig identified 58 significantly mutated genes (FDR q <= 0.1), confirming known drivers ([MYD88](../genes/MYD88.md), [CARD11](../genes/CARD11.md), [EZH2](../genes/EZH2.md), [CREBBP](../genes/CREBBP.md), [CD79B](../genes/CD79B.md), [TP53](../genes/TP53.md)) and uncovering novel ones (MEF2B, KMT2D, BTG1, GNA13, ACTB, P2RY8) [PMID:22343534](../papers/22343534.md).
- [BCL2](../genes/BCL2.md) point mutations in patients with BCL2/IgH translocations arise from AID-mediated somatic hypermutation and are subject to purifying selection preserving anti-apoptotic function [PMID:22343534](../papers/22343534.md).
- Mean nonsynonymous mutation rate was 3.2 mutations per megabase (range 0.6-8.7), higher than CLL and multiple myeloma [PMID:22343534](../papers/22343534.md).
- Histone H1 family proteins were mutated in 69% of patients (59 nonsynonymous mutations across 34 patients) [PMID:22343534](../papers/22343534.md).

## Sources

- [PMID:22343534](../papers/22343534.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
