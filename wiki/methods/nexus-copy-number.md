---
name: Nexus Copy Number
slug: nexus-copy-number
kind: copy_number_analysis
canonical_source: corpus
unverified: true
tags: []
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# Nexus Copy Number

## Overview

Nexus Copy Number (BioDiscovery) is a commercial software platform for copy-number alteration (CNA) analysis from sequencing and array data. For WES-based analyses it applies the ngCGH module and RankSegmentation algorithm to produce segmented copy-number calls. Results are typically used in combination with allele-specific tools such as [sequenza](../methods/sequenza.md) for LOH inference.

## Used by

- Nexus v7.5 ngCGH module with RankSegmentation used to call copy-number alterations in 15 Korean vulvar SCC paired tumor/normal WES samples; LOH events then inferred with [sequenza](../methods/sequenza.md) and manually curated [PMID:29422544](../papers/29422544.md)

## Notes

- Corpus-grown slug; not listed as a `genePanelId` in cBioPortal gene panels or as a `molecularAlterationType` in cBioPortal molecular profiles.
- Commercial platform (BioDiscovery); commonly used for both array-CGH and next-generation sequencing CNA profiling.
- The ngCGH module adapts array-CGH algorithms to sequencing read-depth data.

## Sources

- [PMID:29422544](../papers/29422544.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
