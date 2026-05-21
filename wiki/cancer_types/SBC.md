---
name: Small Bowel Cancer
oncotree_code: SBC
main_type: Small Bowel Cancer
parent: BOWEL
tags:
  - small-bowel
  - MSI
  - MMR
processed_by: crosslinker
processed_at: 2026-05-21
---

# Small Bowel Cancer (SBC)

## Overview

Small bowel cancer encompasses malignancies of the small intestine including adenocarcinomas, neuroendocrine tumors, and stromal tumors. It is classified under Small Bowel Cancer in OncoTree (parent: BOWEL). Small bowel adenocarcinoma has a relatively high frequency of mismatch repair deficiency (MMR-D)/MSI-H compared to colorectal cancer.

## Cohorts in the corpus

- [pancan_mimsi_msk_2024](../datasets/pancan_mimsi_msk_2024.md): 60 SBC samples in the prospective MMR IHC secondary cohort used to benchmark the MiMSI MSI classifier (pan-cancer MSK-IMPACT cohort, n=5,037 across 42 cancer types). [PMID:39746944](../papers/39746944.md)

## Recurrent alterations

- [MLH1](../genes/MLH1.md), [MSH2](../genes/MSH2.md), [MSH6](../genes/MSH6.md), [PMS2](../genes/PMS2.md): MMR protein loss detected by IHC as the reference standard for MSI-H classification in the MiMSI study; relative proportions among MMR-D SBC tumors not specifically reported. [PMID:39746944](../papers/39746944.md)
- 10.3% of 174 colitis-associated cancer cases arose in the small intestine; small bowel CAC shared the molecular signature of the broader CAC series (TP53-dominant, low [APC](../genes/APC.md), Wnt-independent) and [IDH1](../genes/IDH1.md) mutations were specifically noted in ileal CAC with functional 2-HG production [PMID:36611031](../papers/36611031.md)

## Subtypes

- Small bowel adenocarcinoma (most common; duodenal, jejunal, ileal)
- Small bowel neuroendocrine tumor
- Gastrointestinal stromal tumor ([GIST](../cancer_types/GIST.md)) — distinct entity often classified separately

## Therapeutic landscape

- **MSI-H detection**: MiMSI achieved 100% sensitivity for MSI-H detection in SBC (vs 94.1% for MSISensor), the highest per-cancer sensitivity advantage in the prospective cohort analysis. [PMID:39746944](../papers/39746944.md)
- Immune checkpoint blockade is FDA-approved for MSI-H/dMMR tumors regardless of histology ([pembrolizumab](../drugs/pembrolizumab.md)); high MMR-D frequency makes SBC a relevant indication.

## Sources

- [PMID:39746944](../papers/39746944.md) — Ziegler et al. *Nature Cancer* 2024. MiMSI deep-learning MSI classifier.

- [PMID:36611031](../papers/36611031.md)

*This page was processed by **crosslinker** on **2026-05-21**.*

*This page was processed by **crosslinker** on **2026-05-21**.*
