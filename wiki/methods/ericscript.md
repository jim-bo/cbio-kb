---
name: EricScript
slug: ericscript
kind: method
canonical_source: corpus
unverified: true
tags: [fusion-calling, rna-seq, gene-fusion]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# EricScript

## Overview

EricScript is a computational tool for discovering gene fusions in paired-end RNA-seq data. It uses a probabilistic model to identify chimeric transcripts from discordant and split read evidence. EricScript was used as one of three callers in the TCGA pan-cancer fusion analysis, complementing STAR-Fusion and BREAKFAST.

## Used by

- One of three RNA-seq fusion callers in the TCGA pan-cancer fusion analysis across 9,624 tumor samples spanning 33 cancer types; used alongside STAR-Fusion and BREAKFAST with 5 kb and 100 kb minimum-distance cutoffs; contributed to the multi-tool ensemble producing 25,664 filtered fusions [PMID:29617662](../papers/29617662.md)
- Used alongside STAR-Fusion and BreakFast to detect gene fusions from RNA-Seq data across 9,125 TCGA PanCanAtlas tumors [PMID:29625050](../papers/29625050.md).

## Notes

- Used in combination with STAR-Fusion and BREAKFAST; calls supported by multiple tools have greater confidence.
- Applied with minimum inter-gene distance cutoffs (5 kb and 100 kb) to reduce readthrough/artifact calls.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
