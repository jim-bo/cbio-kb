---
name: Genome MuSiC
slug: genome-music
kind: method
canonical_source: corpus
unverified: true
tags: [significantly-mutated-genes, statistical-analysis, bioinformatics]
processed_by: wiki-cli
processed_at: 2026-05-15
---

# Genome MuSiC

## Overview

Genome MuSiC (Mutation Significance in Cancer) is a computational suite for identifying significantly mutated genes in cancer genome sequencing studies. It accounts for gene length, background mutation rate, and mutation context to distinguish driver from passenger mutations, outputting false-discovery-rate-controlled significance scores.

## Used by

- Applied in ICGC PedBrain pilocytic astrocytoma WGS study (96 cases) for significantly mutated gene analysis (max-FDR 0.05); identified only [BRAF](../genes/BRAF.md), [FGFR1](../genes/FGFR1.md), [KRAS](../genes/KRAS.md), and [NF1](../genes/NF1.md) as significantly mutated genes, confirming pilocytic astrocytoma as a single-pathway (MAPK) disease [PMID:23817572](../papers/23817572.md)
- Applied to Ewing sarcoma WGS data; genome-MuSiC SMG test identified [STAG2](../genes/STAG2.md), [TP53](../genes/TP53.md), and [EZH2](../genes/EZH2.md) as the only significantly mutated genes among 112 tumors [PMID:25223734](../papers/25223734.md)
- Used for significantly mutated gene identification in 29 AA CRC discovery exomes, contributing to the nomination of 20 significantly mutated genes including [EPHA6](../genes/EPHA6.md) and [FLCN](../genes/FLCN.md) as African American-specific CRC drivers [PMID:25583493](../papers/25583493.md)
- MuSiC (Genome MuSiC) used alongside MutSig and drGAP for driver gene detection (FDR<0.1) in 216 metastatic breast cancer exomes [PMID:28027327](../papers/28027327.md).
- GenomeMuSiC used alongside MutSigCV and IntOGen for significantly mutated gene detection across 491 medulloblastoma cases, enabling confident driver assignment to 76% of Group 3 and 82% of Group 4 tumors [PMID:28726821](../papers/28726821.md)
- MuSiC (Genome MuSiC) used for significantly mutated gene analysis in 206 TCGA sarcomas; identified only 3 SMGs (TP53, ATRX, RB1) consistent with the low mutation burden (mean 1.06/Mb) of these tumors [PMID:29100075](../papers/29100075.md)
- Applied alongside MutSig to identify 47 significantly recurrently mutated genes across 1,027 MSS [COADREAD](../cancer_types/COADREAD.md) tumors prospectively sequenced by MSK-IMPACT [PMID:29316426](../papers/29316426.md)

## Notes

- Corpus-grown slug; not found in cBioPortal canonical gene panel ontology.
- Predecessor to tools such as MutSig2CV; developed at the Genome Institute (Washington University).

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25223734](../papers/25223734.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583493](../papers/25583493.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:28027327](../papers/28027327.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28726821](../papers/28726821.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29100075](../papers/29100075.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29316426](../papers/29316426.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
