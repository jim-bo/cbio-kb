---
name: gGnome
slug: ggnome
kind: method
canonical_source: corpus
unverified: true
tags: [genome-graph, structural-variants, chromoplexy]
processed_by: crosslinker
processed_at: 2026-09-11
---

# gGnome

## Overview

gGnome is a genome-graph R package used to represent and query complex structural-variant (SV) architectures. In the corpus it was used via its "gWalk" function to confirm chained or closed-loop rearrangement patterns (chromoplexy) from breakpoint calls.

## Used by

- Used (gWalk function) to confirm open-chain and closed-loop chromoplexy structures from DELLY-called structural variants in 277 EWSR1-rearranged small blue round cell tumors (Ewing sarcoma and [EWSR1](../genes/EWSR1.md)::[WT1](../genes/WT1.md) [DSRCT](../cancer_types/DSRCT.md)) [PMID:38335254](../papers/38335254.md).

## Notes

- Applied downstream of DELLY SV calls; chromoplexy in this study was defined as more than one SV in the same sample sharing at least one gene partner.

## Sources

- [PMID:38335254](../papers/38335254.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
