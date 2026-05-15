---
name: MC3 (Mutation Dataset)
slug: mc3
kind: method
canonical_source: corpus
unverified: true
tags: [somatic-mutation, tcga, pan-cancer, dataset]
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# MC3 (Mutation Dataset)

## Overview

The MC3 (Multi-Center Mutation Calling in Multiple Cancers) dataset refers to the canonical somatic mutation annotation file (MAF) produced by the TCGA MC3 project (Ellrott et al., 2018). The open-access PASS-filtered MAF contains 3,600,963 variants from 10,295 TCGA tumors across 33 cancer types and serves as the reference somatic mutation resource for PanCancer Atlas analyses. This entry refers to the dataset/resource itself, as distinct from the [mc3-pipeline](../methods/mc3-pipeline.md) used to produce it.

## Used by

- MC3 Public MAF used as the source of driver-gene mutation calls for integration with fusion data across 8,955 TCGA patients; enabled quantification of fusion-only vs. mutation-only vs. dual-driver samples [PMID:29617662](../papers/29617662.md)

## Notes

- Controlled-access MAF: 22,485,627 variants; open-access PASS MAF: 3,600,963 variants.
- Hosted at the NCI GDC: https://gdc.cancer.gov/about-data/publications/mc3-2017.
- See [mc3-pipeline](../methods/mc3-pipeline.md) for the workflow that produced this resource.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
