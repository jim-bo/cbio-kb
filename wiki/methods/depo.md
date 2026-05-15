---
name: DEPO (Database of Evidence for Precision Oncology)
slug: depo
kind: method
canonical_source: corpus
unverified: true
tags: [druggability, precision-oncology, annotation, database]
processed_by: crosslinker
processed_at: 2026-05-15
---

# DEPO (Database of Evidence for Precision Oncology)

## Overview

DEPO (Database of Evidence for Precision Oncology) is a curated resource that maps genomic alterations (mutations, fusions, copy-number changes) to targeted therapies with supporting clinical evidence. It allows off-label drug-alteration associations and is used to assess whether a given genomic event in a tumor is potentially "druggable" — i.e., targetable by an approved or investigational agent. In the TCGA fusion analysis, DEPO was the druggability annotation oracle.

## Used by

- Used to annotate druggability of gene fusions across 9,624 TCGA tumor samples; identified 574 samples (6.0%) across 29 cancer types as harboring at least one druggable fusion (off-label inclusion permitted); major recurrent druggable targets included [TMPRSS2](../genes/TMPRSS2.md) in [PRAD](../cancer_types/PRAD.md), [RET](../genes/RET.md) in [THCA](../cancer_types/THCA.md), PML-RARA in [LAML](../cancer_types/LAML.md), and [FGFR3](../genes/FGFR3.md) across 15 cancer types [PMID:29617662](../papers/29617662.md)

## Notes

- Off-label inclusion may overstate true clinical actionability; DEPO annotations do not account for co-occurring resistance alterations.
- The 6.0% druggable-fusion rate in the TCGA pan-cancer cohort should be interpreted as an upper bound of potential actionability, not confirmed therapeutic utility.
- DEPO is a curated database; updates to its content will change druggability classifications for the same events.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
