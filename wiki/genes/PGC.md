---
symbol: PGC
aliases:
  - Progastricsin
  - pepsinogen C
cancer_types:
  - STAD
tags:
  - gastric-lineage
  - non-coding-hotspot
  - stomach-specific
processed_by: crosslinker
processed_at: 2026-05-16
canonical_source: cbioportal
unverified: false
---

# PGC

## Overview

PGC (Progastricsin / Pepsinogen C) is a stomach-lineage gene encoding a gastric aspartic protease expressed at extremely high levels in normal stomach tissue (11,940 TPM in stomach vs. ≤2 TPM in most other tissues). In the context of cancer genomics, PGC has been identified as a recurrent non-coding indel hotspot in gastric cancer, likely reflecting the elevated background mutation rate at [CTCF](../genes/CTCF.md) binding sites (CBS) in stomach-lineage chromatin rather than positive selection for PGC inactivation per se.

## Alterations observed in the corpus

- Second-most-significant non-coding indel hotspot in gastric cancer ([STAD](../cancer_types/STAD.md)); intronic indels identified genome-wide in a TCGA gastric and colorectal cancer non-coding mutation scan; indels were not associated with PGC expression change, suggesting passive accumulation at a high-background CBS locus rather than a driver mechanism [PMID:29670109](../papers/29670109.md)

## Cancer types (linked)

- [STAD](../cancer_types/STAD.md) — non-coding intronic indel hotspot; stomach-specific expression pattern (11,940 TPM stomach vs. ≤2 TPM elsewhere) makes locus susceptible to CBS-associated elevated indel background rate; no expression-level driver effect demonstrated [PMID:29670109](../papers/29670109.md)

## Co-occurrence and mutual exclusivity

- Co-occurs in the same non-coding hotspot landscape as [AFDN](../genes/AFDN.md) (top genome-wide indel hotspot), [MUC6](../genes/MUC6.md), and [LIPF](../genes/LIPF.md) in gastric cancer; all share stomach-lineage open chromatin and CTCF binding site proximity [PMID:29670109](../papers/29670109.md)

## Therapeutic relevance

- No direct therapeutic relevance established; paper explicitly states PGC intronic indels are not associated with expression changes and do not propose treatment implications [PMID:29670109](../papers/29670109.md)

## Open questions

- Whether any PGC locus CBS hotspot indels represent genuine non-coding drivers (as opposed to passenger events at a high-background locus) remains unresolved; the paper proposes a passive accumulation model [PMID:29670109](../papers/29670109.md)

## Sources

- [PMID:29670109](../papers/29670109.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
