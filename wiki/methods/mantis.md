---
name: MANTIS
slug: mantis
kind: MSI-detector
canonical_source: corpus
unverified: true
tags: [microsatellite-instability, MSI, pan-cancer, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-16
---

# MANTIS

## Overview

MANTIS (Microsatellite Analysis for Normal-Tumor InStability) is a microsatellite instability (MSI) detection algorithm that operates on paired tumor-normal whole-exome or whole-genome sequencing data. It evaluates a set of microsatellite loci (2,530 loci in its original publication) and assigns a step-wise difference score per locus; samples with an average distance score ≥ 0.4 are classified MSI-H. MANTIS was designed for pan-cancer applicability and avoids the Bethesda PCR-panel loci that were shown to perform poorly outside colorectal and endometrial contexts.

## Used by

- Applied to 11,139 paired tumor-normal whole-exome sequencing samples from 39 cancer types (TCGA, TARGET, and external cohorts) in the largest pan-cancer MSI analysis at the time; detected MSI-H in 3.8% of all tumors across 27 of 39 cancer types, including previously underappreciated signal in adrenocortical carcinoma ([ACC](../cancer_types/ACC.md), 4.3%), cervical cancer ([CESC](../cancer_types/CESC.md), 2.6%), and mesothelioma ([MESO](../cancer_types/MESO.md), 2.4%) [PMID:29850653](../papers/29850653.md)

## Notes

- The standard detection threshold used by Bonneville et al. is average distance ≥ 0.4; cancer-type-specific calibration was not explored in the original pan-cancer study.
- Of 2,530 assessed loci, 22 showed consistent MSI-H vs MSS discrimination across ≥5 cohorts (difference > 0.75, ≥50% coverage); neither of the standard Bethesda/Promega PCR-panel loci ranked in the top 22, highlighting heterogeneity of informative loci across cancer types.
- Samples with tumor purity < ~20% may yield indeterminate calls; locus sets were originally designed from exome-flanking regions and are not directly comparable to clinical PCR panels.

## Sources

- [PMID:29850653](../papers/29850653.md) — Bonneville et al. (2018), pan-cancer MSI analysis using MANTIS across 39 cancer types.

*This page was processed by **crosslinker** on **2026-05-16**.*
