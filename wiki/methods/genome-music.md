---
name: Genome MuSiC
slug: genome-music
kind: method
canonical_source: corpus
unverified: true
tags: [significantly-mutated-genes, statistical-analysis, bioinformatics]
processed_by: crosslinker
processed_at: 2026-05-14
---

# Genome MuSiC

## Overview

Genome MuSiC (Mutation Significance in Cancer) is a computational suite for identifying significantly mutated genes in cancer genome sequencing studies. It accounts for gene length, background mutation rate, and mutation context to distinguish driver from passenger mutations, outputting false-discovery-rate-controlled significance scores.

## Used by

- Applied in ICGC PedBrain pilocytic astrocytoma WGS study (96 cases) for significantly mutated gene analysis (max-FDR 0.05); identified only [BRAF](../genes/BRAF.md), [FGFR1](../genes/FGFR1.md), [KRAS](../genes/KRAS.md), and [NF1](../genes/NF1.md) as significantly mutated genes, confirming pilocytic astrocytoma as a single-pathway (MAPK) disease [PMID:23817572](../papers/23817572.md)
- Applied to Ewing sarcoma WGS data; genome-MuSiC SMG test identified [STAG2](../genes/STAG2.md), [TP53](../genes/TP53.md), and [EZH2](../genes/EZH2.md) as the only significantly mutated genes among 112 tumors [PMID:25223734](../papers/25223734.md)
- Used for significantly mutated gene identification in 29 AA CRC discovery exomes, contributing to the nomination of 20 significantly mutated genes including [EPHA6](../genes/EPHA6.md) and [FLCN](../genes/FLCN.md) as African American-specific CRC drivers [PMID:25583493](../papers/25583493.md)

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Predecessor to tools such as MutSig2CV; developed at the Genome Institute (Washington University).

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25223734](../papers/25223734.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583493](../papers/25583493.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
