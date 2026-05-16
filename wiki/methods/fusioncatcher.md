---
name: FusionCatcher
slug: fusioncatcher
kind: method
canonical_source: corpus
unverified: true
tags: [fusion-calling, rna-seq, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-16
---

# FusionCatcher

## Overview

FusionCatcher is an open-source computational pipeline for detecting somatic gene fusions from paired-end RNA-seq data. It integrates multiple alignment and filtering strategies, including [STAR](../genes/STAR.md) and BLAT alignments, to identify chimeric transcripts with high specificity. FusionCatcher is widely used in pediatric oncology and cancer genomics studies as part of ensemble fusion-calling workflows.

## Used by

- One of four fusion-calling algorithms (alongside [deFuse](../methods/defuse.md), [SOAPfuse](../methods/soapfuse.md), and [STAR-Fusion](../methods/star-fusion.md)) applied to 244 RNA-seq PPTC pediatric PDX models; the combined ensemble yielded 925 high-confidence and 92 known oncogenic driver fusions [PMID:31693904](../papers/31693904.md).

## Notes

- Corpus-grown slug; no matching `genePanelId` in cBioPortal ontology.
- Designed for sensitivity in detecting known and novel fusion transcripts from tumor RNA-seq.
- Commonly paired with other callers (deFuse, STAR-Fusion, SOAPfuse) in ensemble pipelines to maximize recall while filtering artifacts.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
