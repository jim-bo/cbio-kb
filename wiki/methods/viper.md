---
name: VIPER (Virtual Inference of Protein-activity by Enriched Regulon analysis)
slug: viper
kind: method
canonical_source: corpus
unverified: true
tags: [master-regulator, transcription-factor, proteomics, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-09-10
---

# VIPER (Virtual Inference of Protein-activity by Enriched Regulon analysis)

## Overview

VIPER infers the activity of transcription factors and other signaling proteins ("master regulators") from bulk or single-cell gene expression data, using pre-built transcriptional regulatory networks (regulons) from tools such as ARACNe. For each candidate regulator, VIPER computes a normalized enrichment score over the expression signatures of its transcriptional targets, analogous to GSEA. Because mRNA levels of signaling proteins often do not reflect protein activity, VIPER provides a protein-activity estimate from RNA data without direct proteomics measurements.

## Used by

- Applied to RNA-seq profiles of 28 metastatic neuroendocrine neoplasms ([pog570_bcgsc_2020](../datasets/pog570_bcgsc_2020.md)) to perform master-regulator inference; Cluster B NENs showed [MYC](../genes/MYC.md) family activation, and Cluster A showed relative inhibition of [MEN1](../genes/MEN1.md) and [DAXX](../genes/DAXX.md) compared with other clusters [PMID:40328872](../papers/40328872.md).
- VIPER-style regulon analysis applied to 23 candidate transcription factor regulators in 408 BLCA RNA-seq samples; identified GATA3, FOXA1, PPARG as luminal drivers and TP63, EGFR as basal-squamous discriminators; validated in independent Sjödahl 308-sample cohort [PMID:28988769](../papers/28988769.md)
- Used with ARACNe (metaVIPER) for protein-activity inference from snRNA-seq of MYOD1-mutant spindle cell/sclerosing rhabdomyosarcoma, identifying three conserved tumor cell states [PMID:41758938](../papers/41758938.md)

## Notes

- Requires a tissue-matched regulon; pan-cancer regulons (e.g., from TCGA ARACNe networks) may not be optimal for rare tumor types.
- VIPER and metaVIPER (multi-network) are available as the R/Bioconductor package `viper`.
- Commonly combined with clustering or enrichment analyses to identify co-activated transcriptional programs.

## Sources
- [PMID:28988769](../papers/28988769.md)
- [PMID:41758938](../papers/41758938.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
