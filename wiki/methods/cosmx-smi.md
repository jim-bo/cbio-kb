---
name: NanoString CosMx SMI
slug: cosmx-smi
kind: method
canonical_source: 
unverified: true
tags: [spatial-transcriptomics, imaging, nanostring, high-plex, tma]
processed_by: crosslinker
processed_at: 2026-04-11
---

# NanoString CosMx SMI

## Overview

NanoString CosMx Spatial Molecular Imager (SMI) is a high-plex in situ single-cell spatial profiling platform that measures RNA (and optionally protein) expression directly on formalin-fixed paraffin-embedded tissue sections, including tissue microarrays, at subcellular resolution [PMID:39214094](../papers/39214094.md).

## Used by

- [PMID:39214094](../papers/39214094.md) — applied to a tissue microarray of 20 [PAAD](../cancer_types/PAAD.md) patients (14 tumors, 6 normal pancreas) to profile allele-specific transcriptional programs in [KRAS](../genes/KRAS.md)-mutant PDAC, identifying enriched [KRAS](../genes/KRAS.md) signaling and EMT in [KRAS](../genes/KRAS.md)^G12D^ tumors versus increased TNF/NF-κB signaling in KRAS^G12R^ tumors [PMID:39214094](../papers/39214094.md).

## Notes

- High-plex in situ RNA profiling on FFPE / TMA sections; used here as the spatial complement to bulk RNA-seq on 100 tumors [PMID:39214094](../papers/39214094.md).
- Corpus-grown slug; not present in canonical `schema/ontology/gene_panels.json` (CosMx is an imaging platform, not a targeted DNA panel), so marked `unverified: true`.

## Sources

- [PMID:39214094](../papers/39214094.md)

*This page was processed by **crosslinker** on **2026-04-11**.*
