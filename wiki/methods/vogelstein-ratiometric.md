---
name: Vogelstein 20/20 Ratiometric Driver Discovery
slug: vogelstein-ratiometric
kind: method
canonical_source: corpus
unverified: true
tags: [driver-discovery, oncogene-tsg-classification, statistical-genetics]
processed_by: crosslinker
processed_at: 2026-05-14
---

# Vogelstein 20/20 Ratiometric Driver Discovery

## Overview

The Vogelstein 20/20 ratiometric scheme is a rule-based statistical method for classifying cancer driver genes as oncogenes or tumor suppressors, originally described in Vogelstein et al. (2013, *Science*). A gene is classified as a driver if it exceeds a minimum recurrence threshold (≥5 recurrent or inactivating mutations) and meets either the oncogene criterion (≥20% of mutations are recurrent missense at known hotspots, ONC ≥ 20%) or the tumor-suppressor criterion (≥20% of mutations are inactivating with oncogenic fraction ≤5%, TSG ≥ 20%, ONC ≤ 5%). The method is applied per cancer type or molecular subtype (e.g., ER+ vs ER-) and can identify both oncogenes (enriched for recurrent gain-of-function missense mutations) and tumor suppressors (enriched for loss-of-function events).

## Used by

- [Pereira et al. 2016 — METABRIC breast cancer landscape](../papers/27161491.md): Applied with ER-stratified cutoffs to 2,433 primary breast tumours from the METABRIC cohort (173-gene targeted panel); identified 40 Mut-driver genes (22 ER+ only, 3 ER- only, 15 shared); only 6 of 40 qualified as oncogenes under the ratiometric criteria; the scheme revealed TSG-enriched genes including [MAP3K1](../genes/MAP3K1.md), [KMT2C](../genes/KMT2C.md), [GATA3](../genes/GATA3.md), and [SMAD4](../genes/SMAD4.md) as well as oncogene [PIK3CA](../genes/PIK3CA.md) [PMID:27161491](../papers/27161491.md).

## Notes

- The 20/20 rule is intentionally conservative; it requires strong enrichment of a single mutation class and thus may miss genes with mixed mutation patterns.
- ER-stratification (applied in the METABRIC study) increases sensitivity for subtype-restricted drivers that would be diluted in an unstratified analysis.
- Minimum recurrence threshold of ≥5 mutations limits detection in small cohorts; the METABRIC n=2,433 was specifically assembled to overcome this.
- The method does not use statistical background mutation rate modeling (unlike MutSig); it relies on mutation-type composition ratios.

## Sources

- Vogelstein B et al. (2013) Cancer genome landscapes. *Science* 339:1546–1558.
- [PMID:27161491](../papers/27161491.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
