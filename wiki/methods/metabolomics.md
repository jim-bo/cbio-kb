---
name: Metabolomics
slug: metabolomics
kind: method
canonical_source: corpus
unverified: true
tags: [metabolomics, mass-spectrometry, nmr, multi-omics]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Metabolomics

## Overview

Metabolomics is the comprehensive, quantitative profiling of small-molecule metabolites (the metabolome) in biological samples. Platforms include mass spectrometry (LC-MS, GC-MS, CE-MS) and nuclear magnetic resonance (NMR) spectroscopy. Untargeted metabolomics surveys thousands of metabolite features simultaneously; targeted panels focus on predefined metabolic pathways. Metabolomics captures the downstream functional output of genome, transcriptome, and proteome states — metabolite levels reflect integrated enzymatic activity and are therefore sensitive to metabolic reprogramming, nutrient availability, and drug perturbations that upstream layers cannot fully predict.

## Used by

- Reviewed as a core omics modality in multi-omics integration for precision health and precision oncology alongside WGS, WES, RNA-seq, proteomics, DNA methylation, ChIP-seq, ATAC-seq, [lipidomics](../methods/lipidomics.md), and wearable monitoring; Babu and Snyder (2023) emphasize that metabolomics provides mechanistic resolution not available from nucleic-acid or protein measurements alone. [PMID:37119971](../papers/37119971.md)
- The iPOP (integrative personal omics profiling) longitudinal study (54-year-old individual, 20 time points, 14 months) used metabolomics among its omics layers to capture transitions between healthy and insulin-resistant states, establishing a template for longitudinal multi-omics in clinical settings. [PMID:37119971](../papers/37119971.md)

## Notes

- Metabolomics and [lipidomics](../methods/lipidomics.md) are complementary: metabolomics typically covers polar, low-molecular-weight metabolites (amino acids, organic acids, nucleotides, sugars); lipidomics covers lipid species with specialized extraction and ionization.
- No gene-panel ID. Corpus-grown slug. See `schema/ontology/_observed.md`.
- In cancer, metabolomics has been applied to identify Warburg effect metabolites, TCA cycle reprogramming, and amino acid dependency phenotypes; no cBioPortal-hosted metabolomics datasets appear in the current corpus.

## Sources

- [PMID:37119971](../papers/37119971.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
