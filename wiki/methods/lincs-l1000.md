---
name: LINCS L1000
slug: lincs-l1000
kind: method
canonical_source: corpus
unverified: true
tags: [drug-connectivity, perturbation-database, transcriptomics, drug-repurposing]
processed_by: crosslinker
processed_at: 2026-05-16
---

# LINCS L1000

## Overview

LINCS L1000 is a high-throughput gene expression profiling platform and perturbation database (part of the NIH Library of Integrated Network-Based Cellular Signatures program). It measures ~1000 landmark genes after compound or genetic perturbations in human cell lines, enabling connectivity mapping: matching a query transcriptomic signature against thousands of drug perturbation profiles to identify compounds that may reverse or mimic the query.

## Used by

- Used in a drug-connectivity analysis comparing HGG vs [LGG](../cancer_types/LGG.md) RNA and phosphoproteomic signatures in pediatric brain tumors (N=218, [brain_cptac_2020](../datasets/brain_cptac_2020.md)); CDK inhibitors were predicted (from RNA + phosphoproteomic evidence) to reverse the HGG-aggressiveness signature, and MEK, proteasome, and HDAC inhibitors were predicted from RNA data alone [PMID:33242424](../papers/33242424.md)

## Notes

- Corpus-grown slug; not in cBioPortal gene-panel ontology.
- L1000 assay measures ~1000 landmark genes via Luminex bead-based platform; the remaining ~21,000 genes are computationally inferred.
- Queries are typically submitted as up/down gene sets; connectivity score is based on Kolmogorov–Smirnov-style enrichment.
- The P100 phosphoproteomic platform (96 phosphopeptides) is a related LINCS perturbation assay.

## Sources

*This page was processed by **crosslinker** on **2026-05-16**.*
