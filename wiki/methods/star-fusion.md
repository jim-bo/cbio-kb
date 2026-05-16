---
name: STAR-Fusion
slug: star-fusion
kind: method
canonical_source: corpus
unverified: true
tags: [fusion-calling, rna-seq, gene-fusion]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# STAR-Fusion

## Overview

STAR-Fusion is a gene-fusion detection tool that uses the [STAR](../genes/STAR.md) aligner to identify chimeric RNA reads spanning two distinct genomic loci. It applies a series of filters (panel-of-normals, FFPM thresholds, minimum read support) to reduce false-positive fusion calls from RNA-seq data. STAR-Fusion is the dominant caller in multi-tool fusion pipelines due to its sensitivity and integration with the widely-used STAR aligner.

## Used by

- Primary fusion caller in the TCGA pan-cancer fusion analysis across 9,624 tumor samples and 713 normal samples spanning 33 cancer types; run alongside EricScript and BREAKFAST; STAR-Fusion-only calls required FFPM > 0.1 threshold; recovered 95.5% (405/424) of curated TCGA marker-paper fusions; yielded 25,664 filtered fusions with 63.3% WGS validation rate [PMID:29617662](../papers/29617662.md)
- Used alongside EricScript and BreakFast to detect gene fusions from RNA-Seq data across 9,125 TCGA PanCanAtlas tumors in the pan-cancer oncogenic signaling pathway analysis [PMID:29625050](../papers/29625050.md).
- One of four fusion-calling algorithms (alongside deFuse, FusionCatcher, SOAPfuse) applied to 244 RNA-seq PPTC PDX models; the combined ensemble yielded 925 high-confidence and 92 known oncogenic driver fusions, identifying canonical EWSR1-FLI1, PAX3-FOXO1, BCR-ABL1, and CIC-DUX4 fusions [PMID:31693904](../papers/31693904.md).

## Notes

- STAR-Fusion is the dominant caller in this multi-tool pipeline; results inherit STAR-Fusion biases even with multi-tool integration.
- FFPM (Fusion Fragments Per Million) > 0.1 was required for STAR-Fusion-only calls; calls supported by ≥2 tools had relaxed thresholds.
- Paired with STAR-aligner for upstream mapping.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31693904](../papers/31693904.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
