---
name: Breast Ductal Carcinoma In Situ
oncotree_code: DCIS
main_type: Breast Cancer
parent: BREAST
tags:
  - breast
  - ductal
  - in-situ
  - pre-invasive
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Breast Ductal Carcinoma In Situ (DCIS)

## Overview

Breast Ductal Carcinoma In Situ (DCIS) is a pre-invasive neoplasm in which malignant epithelial cells proliferate within the ductal system of the breast without breaching the basement membrane. It sits at OncoTree level 2 under the BREAST parent node. DCIS represents a heterogeneous entity with variable risk of progression to invasive ductal carcinoma ([IDC](../cancer_types/IDC.md)); understanding the molecular events that drive this transition is a central clinical question.

## Cohorts in the corpus

- [brca_metabric](../datasets/brca_metabric.md) and [brca_tcga_pub](../datasets/brca_tcga_pub.md) include primary invasive breast tumors used as human comparators in modeling studies; DCIS-specific cohorts are referenced indirectly via the rat somatic editing platform [PMID:26437033](../papers/26437033.md).

## Recurrent alterations

- [NF1](../genes/NF1.md) Indel editing alone in rat mammary gland produced DCIS histology in 12/13 cases (92%) — all ER+/PR+/Ki67+, at a median 4-week latency — establishing Nf1 biallelic loss as sufficient to initiate DCIS-like lesions in a preclinical model [PMID:26437033](../papers/26437033.md).
- Addition of [TP53](../genes/TP53.md) Indel to Nf1 loss converted the DCIS phenotype to invasive ductal carcinoma, implicating combined NF1/TP53 inactivation in the DCIS-to-invasive transition [PMID:26437033](../papers/26437033.md).
- Synchronous DCIS (n=27) displayed somatic mutations and CNAs indistinguishable from paired IDC-NSTs (n=26): TP53 52%, PIK3CA 41%, GATA3 26%; 92% clonally related to their matched invasive carcinoma; pure DCIS (n=7) lacked PIK3CA mutations entirely (0% vs 41%), suggesting a molecularly less advanced state [PMID:32220886](../papers/32220886.md)

## Subtypes

- DCIS produced in the Nf1Indel rat model is uniformly hormone-receptor-positive (ER+/PR+), mirroring the most common human DCIS subtype and distinct from the ER-negative metaplastic DCIS seen in mouse models under identical genetic editing [PMID:26437033](../papers/26437033.md).

## Therapeutic landscape

- Nf1Indel DCIS rat tumors regressed completely under ovariectomy (3/3 rats) and [fulvestrant](../drugs/fulvestrant.md) (4/4 rats), supporting endocrine sensitivity of NF1-loss-driven ER+ DCIS [PMID:26437033](../papers/26437033.md).

## Sources

- [PMID:26437033](../papers/26437033.md) — Bu et al., *Rat somatic genome editing enables ER+ breast cancer modeling*, bioRxiv 2025.

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:32220886](../papers/32220886.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
