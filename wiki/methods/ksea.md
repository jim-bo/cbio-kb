---
name: KSEA (Kinase-Substrate Enrichment Analysis)
slug: ksea
kind: method
canonical_source: corpus
unverified: true
tags: [proteomics, phosphoproteomics, kinase-activity, enrichment-analysis]
processed_by: crosslinker
processed_at: 2026-05-21
---

# KSEA (Kinase-Substrate Enrichment Analysis)

## Overview

Kinase-Substrate Enrichment Analysis (KSEA) infers kinase activity from phosphoproteomic data by aggregating phosphorylation changes across known kinase-substrate relationships. Using curated kinase-substrate databases (e.g., PhosphoSitePlus), KSEA calculates an enrichment score reflecting whether a kinase's known substrates are collectively hyper- or hypo-phosphorylated relative to a reference condition. This enables systems-level assessment of kinase signaling activity without directly measuring kinase protein levels.

## Used by

- Applied to phosphoproteomic data from 51 [HCC](../cancer_types/HCC.md) biopsies ([hcc_meric_2021](../datasets/hcc_meric_2021.md)), revealing increased activity of [AURKA](../genes/AURKA.md), CDK1/2/5/7, ERK1/2 (MAPK1/3), and [PLK1](../genes/PLK1.md), and decreased activity of PKACA/G, PKCA/Z, and [SGK1](../genes/SGK1.md) in [HCC](../cancer_types/HCC.md) vs normal liver [PMID:35508466](../papers/35508466.md)

## Notes

- Requires a curated kinase-substrate database; PhosphoSitePlus and OmniPath are commonly used.
- Enrichment significance is typically assessed by permutation testing or z-score relative to the global phosphoproteome distribution.
- KSEA complements differential phosphorylation analysis by revealing upstream signaling context.

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
