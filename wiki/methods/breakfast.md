---
name: BREAKFAST
slug: breakfast
kind: method
canonical_source: corpus
unverified: true
tags: [fusion-calling, rna-seq, gene-fusion]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# BREAKFAST

## Overview

BREAKFAST is a gene fusion detection tool for RNA-seq data that identifies chimeric transcripts using split-read and discordant-pair evidence. It was developed with a focus on detecting rearrangements in cancer genomes and was used as one of three complementary callers in the TCGA pan-cancer fusion landscape analysis.

## Used by

- One of three RNA-seq fusion callers in the TCGA pan-cancer fusion analysis across 9,624 tumor samples spanning 33 cancer types; used alongside STAR-Fusion and EricScript with 5 kb and 100 kb minimum-distance cutoffs to reduce readthrough artifacts [PMID:29617662](../papers/29617662.md)

## Notes

- Applied with minimum inter-gene distance cutoffs to reduce false-positive readthrough fusions.
- Multi-tool consensus (support from ≥2 callers) increases confidence in reported fusions.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
