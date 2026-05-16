---
symbol: RPP25L
aliases: []
cancer_types: []
tags: [rna-processing, synthetic-lethality, paralogue-dependency]
processed_by: crosslinker
processed_at: 2026-05-16
canonical_source: cbioportal
unverified: false
---

# RPP25L

## Overview

RPP25L encodes a subunit of the RNase P/MRP ribonucleoprotein complex involved in pre-tRNA and pre-rRNA processing. In cancer functional genomics, RPP25L is notable as a paralog-dependency gene: when its paralogue [RPP25](../genes/RPP25.md) is silenced by promoter methylation, cancer cells become dependent on RPP25L expression for survival, establishing a synthetic lethal vulnerability.

## Alterations observed in the corpus

- Identified as a paralog-dependency gene in the Cancer Cell Line Encyclopedia (CCLE) functional genomics dataset (1,070+ lines): promoter methylation/silencing of [RPP25](../genes/RPP25.md) creates synthetic lethality toward RPP25L; the dependent relationship was confirmed across cell lines with concordant RPP25 silencing [PMID:31068700](../papers/31068700.md)

## Cancer types (linked)

- No specific cancer-type-restricted frequency data reported in the current corpus; the dependency is observed across lineages in the CCLE dataset wherever RPP25 is silenced.

## Co-occurrence and mutual exclusivity

- Synthetic lethality partner of [RPP25](../genes/RPP25.md): RPP25L dependence is gated by RPP25 promoter methylation; the relationship parallels the [LDHA](../genes/LDHA.md)/[LDHB](../genes/LDHB.md) reciprocal paralogue dependency [PMID:31068700](../papers/31068700.md)

## Therapeutic relevance

- RPP25 methylation-driven RPP25L dependence is a candidate synthetic lethal vulnerability; therapeutic exploitation requires confirmation in patient tumor models [PMID:31068700](../papers/31068700.md)

## Open questions

- Whether RPP25L dependency translates from cancer cell lines to primary tumors requires in vivo validation.
- The molecular mechanism by which RPP25 loss specifically upregulates RPP25L dependency has not been fully characterized.

## Sources

- [PMID:31068700](../papers/31068700.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
