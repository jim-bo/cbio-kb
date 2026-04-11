---
name: LymphGen
slug: lymphgen
kind: method
canonical_source: corpus
unverified: true
tags: [classification, dlbcl, computational, lymphoma]
processed_by: entity-page-writer
processed_at: 2026-04-11
---

# LymphGen

## Overview

LymphGen is a probabilistic classification algorithm that assigns diffuse large B-cell lymphoma (DLBCL) cases to one of six molecular subtypes (MCD, BN2, EZB, A53, ST2, N1) based on SNVs, small INDELs, copy number alterations, and FISH translocation data [PMID:38497151](../papers/38497151.md).

## Used by

- [PMID:38497151](../papers/38497151.md) — LymphGen was applied to SNV/INDEL/CNA data from MSK-IMPACT Heme (400-gene panel) plus BCL2/BCL6 [FISH](../methods/fish.md) translocation data in 396 DLBCL cases; achieved 92% overall accuracy (sensitivity 86%, specificity 98%) vs. the comprehensive NCI panel ground truth; 55% of MSK cases were classified, with EZB (22%) as the most common subtype; removing CNA input reduced accuracy to 81% [PMID:38497151](../papers/38497151.md).

## Notes

- LymphGen can be applied to clinical-grade 400-gene targeted sequencing panels with acceptable sensitivity/specificity; CNA data is required for A53 subtype classification [PMID:38497151](../papers/38497151.md).
- Restricting to Core predictions (>90% probability threshold) improves accuracy to 96% [PMID:38497151](../papers/38497151.md).
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:38497151](../papers/38497151.md)

*This page was processed by **entity-page-writer** on **2026-04-11**.*
