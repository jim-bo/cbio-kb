---
name: OxoG Filter
slug: oxog-filter
kind: method
canonical_source: corpus
unverified: true
tags: [quality-control, artifact-filtering, sequencing]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# OxoG Filter

## Overview

The OxoG filter removes oxidative DNA damage artifacts from somatic variant calls, specifically C>A transversions arising from 8-oxoguanine (OxoG) lesions introduced during DNA extraction or library preparation. These artifacts can masquerade as somatic mutations, particularly in samples with older or FFPE-derived DNA. The filter operates on variant allele frequencies and strand bias signals.

## Used by

- Applied as one of eight named filters in the TCGA MC3 pipeline; run on the ISB Cancer Genomics Cloud and Broad FireCloud; targeted low-VAF G>T strand-biased artifacts particularly prevalent in WashU samples [PMID:29596782](../papers/29596782.md)
- OxoG orientation-bias filter applied to remove FFPE/oxidative artifacts in 304 DLBCLs; 55% of samples were FFPE-derived and 55% lacked patient-matched normals, requiring extensive tumor-only filtering [PMID:29713087](../papers/29713087.md)

## Notes

- Primarily targets C>A (G>T) transversions with strand bias — a hallmark of oxidative damage.
- Especially important for fresh-frozen samples with any degradation and for high-throughput pipelines where many samples are processed together.
- Part of the standard Broad Institute variant-calling quality-control suite.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29713087](../papers/29713087.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
