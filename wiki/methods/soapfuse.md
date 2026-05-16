---
name: SOAPfuse
slug: soapfuse
kind: method
canonical_source: corpus
unverified: true
tags: [fusion-calling, rna-seq, bioinformatics]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# SOAPfuse

## Overview

SOAPfuse is a computational tool for detecting gene fusion transcripts from paired-end RNA-seq data. It uses a split-read and spanning-read approach to identify fusion junctions with high sensitivity, and is commonly deployed as part of ensemble fusion-calling pipelines to increase discovery recall. SOAPfuse was developed by BGI and operates on SOAP-aligned reads.

## Used by

- One of four fusion-calling algorithms (alongside [deFuse](../methods/defuse.md), [FusionCatcher](../methods/fusioncatcher.md), and [STAR-Fusion](../methods/star-fusion.md)) applied to 244 RNA-seq PPTC pediatric PDX models; the combined ensemble yielded 925 high-confidence and 92 known oncogenic driver fusions, identifying canonical EWSR1-FLI1, PAX3-FOXO1, BCR-ABL1, and CIC-DUX4 fusions [PMID:31693904](../papers/31693904.md).

## Notes

- Corpus-grown slug; no matching `genePanelId` in cBioPortal ontology.
- Best used in ensemble with other callers (deFuse, FusionCatcher, STAR-Fusion) to reduce false positives and increase sensitivity.
- Requires paired-end RNA-seq data aligned with SOAP2 or equivalent.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-16**.*
