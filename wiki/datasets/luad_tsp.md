---
name: Lung Adenocarcinoma Tumour Sequencing Project (TSP)
studyId: luad_tsp
institution: Dana-Farber Cancer Institute, MD Anderson Cancer Center, Memorial Sloan-Kettering Cancer Center, University of Michigan, Washington University
size: 188
reference_genome: hg18
canonical_source: cbioportal
unverified: false
assays: [targeted-dna-seq, snp-array, gene-expression-array]
panels: []
tags: [luad, lung-adenocarcinoma, somatic-mutation, smoking, tsp]
processed_by: crosslinker
processed_at: 2026-05-05
---

# Lung Adenocarcinoma Tumour Sequencing Project (TSP)

## Overview

The Tumour Sequencing Project (TSP) [LUAD](../cancer_types/LUAD.md) cohort is a multi-institutional effort that performed targeted sequencing of 623 candidate cancer genes across 188 primary lung adenocarcinoma tumours with matched normals. Samples were contributed by Dana-Farber, MD Anderson, Memorial Sloan-Kettering, University of Michigan, and Washington University. The dataset is publicly available via dbGaP (phs000144.v1.p1) and GEO (GSE12667 for expression data).

## Composition

- 188 primary [LUAD](../cancer_types/LUAD.md) tumours (minimum 70% tumour content), with matched normal tissue.
- Targeted DNA sequencing of 623 candidate cancer genes (all coding exons and splice sites); 247 Mb of tumour DNA analysed per sample.
- SNP array (Affymetrix 250K StyI) copy number data on 383 tumours.
- Gene expression (Affymetrix U133Plus2) on 75 tumours.
- Clinical fields include smoking status, tumour grade, and histological subtype.

## Assays / panels (linked)

- [targeted-dna-seq](../methods/targeted-dna-seq.md) — 623-gene cancer gene panel covering all coding exons and splice sites.
- SNP array (Affymetrix 250K StyI) for copy number analysis.
- Gene expression array (Affymetrix U133Plus2).

## Papers using this cohort

- [PMID:18948947](../papers/18948947.md) — Ding et al. 2008, *Nature*: Somatic mutations affect key pathways in lung adenocarcinoma.

## Notable findings derived from this cohort

- Targeted sequencing of 623 candidate cancer genes across 188 primary LUAD tumours (dbGaP phs000144.v1.p1), identifying 1,013 somatic mutations and 26 significantly mutated genes including [NF1](../genes/NF1.md), [ATM](../genes/ATM.md), [RB1](../genes/RB1.md), [APC](../genes/APC.md), [ERBB4](../genes/ERBB4.md), and [EPHA3](../genes/EPHA3.md) as novel recurrently mutated genes in lung adenocarcinoma [PMID:18948947](../papers/18948947.md).

## Sources

- dbGaP: phs000144.v1.p1
- GEO: GSE12667 (expression data)

*This page was processed by **crosslinker** on **2026-05-05**.*
