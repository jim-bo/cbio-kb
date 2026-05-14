---
name: Ingenuity Pathway Analysis
slug: ingenuity-pathway-analysis
kind: method
canonical_source: corpus
unverified: true
tags: [pathway-analysis, gene-set-enrichment, functional-annotation, commercial]
processed_by: crosslinker
processed_at: 2026-05-14
---

# Ingenuity Pathway Analysis

## Overview

Ingenuity Pathway Analysis (IPA) is a commercial bioinformatics platform (Qiagen) that performs pathway enrichment, network analysis, and functional annotation of gene lists derived from sequencing, expression, or proteomics studies. IPA maps input gene sets to curated canonical pathways, disease annotations, and regulatory networks from the Ingenuity Knowledge Base, computing statistical enrichment scores (Fisher's exact test or similar) to identify significantly represented biological processes. It supports both upstream regulator analysis (predicting activated/inhibited upstream transcription factors or kinases) and downstream effect prediction.

## Used by

- Used for pathway enrichment analysis of somatically mutated genes in 25 adenoid cystic carcinomas (ACCs) from whole-genome sequencing; identified Rho-family GTPase signaling (44% of tumors, p=3.9×10⁻⁶) and axon-guidance signaling (56%, p=8.3×10⁻⁵) as significantly enriched pathways, nominating these as candidate therapeutic targets in [ACYC](../cancer_types/ACYC.md) [PMID:26862087](../papers/26862087.md)

## Notes

- Requires a valid IPA license; not open-source.
- Input is typically a gene list with optional fold-change or p-value annotations.
- Canonical pathway enrichment uses Fisher's exact test; significance threshold typically set at p<0.05 with Benjamini-Hochberg correction.
- Upstream regulator analysis predicts which transcription factors or signaling molecules are likely activated or inhibited based on downstream gene expression changes.
- IPA results are context-dependent on the version of the Ingenuity Knowledge Base used; results may differ across IPA releases.

## Sources

- [PMID:26862087](../papers/26862087.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
