---
name: HotMAPS
slug: hotmaps
kind: method
canonical_source: corpus
unverified: true
tags: [driver-discovery, mutation-clustering, protein-structure]
processed_by: entity-page-writer
processed_at: 2026-09-10
---

# HotMAPS

## Overview

HotMAPS (Hotspot Missense mutation Areas in Protein Structures) identifies significantly mutated genes by testing for 3D spatial clustering of missense mutations on protein structures, complementing linear hotspot- and background-mutation-rate-based significance callers.

## Used by

- Used (with dNdScv, MutSig2CV and OncodriveFML) as one of four significance callers to define significantly mutated genes in whole-genome-sequenced Burkitt lymphoma and DLBCL genomes; a gene was called significant if at least 2 of the 4 tools called it [PMID:36201743](../papers/36201743.md).

## Notes

- In this corpus, HotMAPS was used strictly as part of a consensus (>=2-of-4-tool) significantly-mutated-gene calling procedure, not reported standalone.

## Sources

- [PMID:36201743](../papers/36201743.md)

*This page was processed by **entity-page-writer** on **2026-09-10**.*
