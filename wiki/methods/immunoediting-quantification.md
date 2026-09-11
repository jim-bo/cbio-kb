---
name: Immunoediting quantification
slug: immunoediting-quantification
kind: method
canonical_source: 
unverified: true
tags: [neoantigen, immune, computational]
processed_by: wiki-cli
processed_at: 2026-09-10
---

# Immunoediting quantification

## Overview

Computational scoring of genetic immunoediting based on the ratio of observed to expected neoantigens in a tumor; values below 1 indicate negative selection of neoantigen-bearing clones [PMID:37202560](../papers/37202560.md).

## Used by

- [PMID:37202560](../papers/37202560.md) — applied in the AC-ICAM colon cancer atlas; quantifying genetic immunoediting (fewer observed neoantigens than expected) refined the prognostic value of the ICR signature [PMID:37202560](../papers/37202560.md).
- Used (following Rooney et al.) to quantify immunoediting from whole-exome-sequenced colorectal cancer neoantigen calls [PMID:35487942](../papers/35487942.md).

## Notes

- Immunoediting quantification depends on neoantigen prediction pipelines, which carry known noise [PMID:37202560](../papers/37202560.md).

## Sources

- [PMID:37202560](../papers/37202560.md)
- [PMID:35487942](../papers/35487942.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
