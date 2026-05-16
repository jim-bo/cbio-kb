---
name: gnomAD Non-Cancer Controls
slug: gnomad-non-cancer-controls
kind: method
canonical_source: corpus
unverified: true
tags: [population-database, germline, controls]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# gnomAD Non-Cancer Controls

## Overview

The Genome Aggregation Database (gnomAD) non-cancer subset — a curated reference population of individuals without cancer diagnoses derived from the full gnomAD dataset. Commonly used as a control population for germline burden testing in cancer-predisposition studies. gnomAD v3.1.1 covers >76,000 genomes; the non-cancer subset (n ≈ 74,023) excludes participants with known malignancies.

## Used by

- Used as the statistical comparator (n=74,023 healthy adults) for gene-level germline burden testing across 372 pediatric cancer patients; LP/PV frequencies in 25 HBOC genes in cases were compared against allele frequencies in this control set using logistic regression and Fisher's exact tests [PMID:29489754](../papers/29489754.md)
- Used as a population filter (gnomAD allele frequency ≥0.5%) during plasma-only variant calling for MSK-ACCESS; combined with an in-house panel-of-normals filter to remove 14,508 germline and non-specific calls from 24,561 plasma-only variants before matched-WBC germline/CH removal [PMID:34145282](../papers/34145282.md)

## Notes

- A limitation is that non-cancer status at time of enrollment does not exclude future cancer development or pre-symptomatic carriers of predisposition alleles.
- Ascertainment bias: adult controls have survived the pediatric-cancer-risk window, potentially deflating LP/PV frequencies for genes associated specifically with childhood malignancies.
- Version used: gnomAD v3.1.1.

## Sources

- [PMID:29489754](../papers/29489754.md)
- [PMID:34145282](../papers/34145282.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
