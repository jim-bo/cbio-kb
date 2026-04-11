---
name: "Pleural Mesothelioma"
oncotree_code: PLMESO
parent: PLEURA
tags: []
processed_by: crosslinker
processed_at: 2026-04-11
---

# Pleural Mesothelioma (PLMESO)

## Overview

Diffuse pleural mesothelioma (DPM/PLMESO) is a rare, aggressive malignancy of the pleural lining, most commonly caused by prior asbestos exposure. On OncoTree it sits under PLEURA. Histologic subtypes include epithelioid (most common, better prognosis), biphasic, and sarcomatoid. Classical driver genes include [BAP1](../genes/BAP1.md), CDKN2A/B, and [NF2](../genes/NF2.md).

## Cohorts in the corpus

- 290 diffuse pleural mesothelioma patients profiled by MSK-IMPACT at Memorial Sloan Kettering (1/2014--1/2021); 210 evaluable (72%) for LOH analysis (tumor purity >=20%); 10 GNH cases identified. Additional 105-patient validation cohort sequenced with [IMPACT505](../methods/IMPACT505.md). Dataset: [plmeso_msk_2024](../datasets/plmeso_msk_2024.md). [PMID:38630790](../papers/38630790.md)
- Included as one of 22 cancer site-of-origin classes in the ATLAS RNA classifier; sarcoma lineage scores differentiated epithelioid from biphasic/sarcomatoid mesothelioma (AUC=0.81), prognostic for survival (median 15.0 vs. 23.9 months; log-rank P=0.049). [PMID:27634761](../papers/27634761.md)

## Recurrent alterations

- [BAP1](../genes/BAP1.md) — classical DPM driver; not enriched in genomic near-haploidization (GNH) subset. [PMID:38630790](../papers/38630790.md)
- [CDKN2A](../genes/CDKN2A.md) / [CDKN2B](../genes/CDKN2B.md) — classical DPM drivers; not enriched in GNH subset. [PMID:38630790](../papers/38630790.md)
- [NF2](../genes/NF2.md) — altered in 90% of GNH DPMs (driven by biphasic histology enrichment) and 26.5% of non-GNH DPMs. [PMID:38630790](../papers/38630790.md)
- [SETDB1](../genes/SETDB1.md) — somatic loss-of-function mutations in 8/10 GNH cases; absent in non-GNH DPMs (q=0.0035); validated in 4/4 GNH cases in the validation cohort. Highly specific for GNH DPMs. [PMID:38630790](../papers/38630790.md)
- [TP53](../genes/TP53.md) — alterations significantly more common in GNH DPMs (60% vs. 14%, q=0.0035); early clonal event preceding genome-wide LOH. [PMID:38630790](../papers/38630790.md)
- [MLH1](../genes/MLH1.md) — truncating mutation in one non-GNH hypermutator (31.5 muts/Mb, MSI-high). [PMID:38630790](../papers/38630790.md)

## Subtypes

- Genomic near-haploidization (GNH) subset (~4.8% of evaluable DPMs): younger age (58 vs. 71 years, P=0.008), less asbestos exposure (20% vs. 58%, P=0.02), 80% biphasic histology (vs. 15%, P<0.0001), high TILs (3+ score: 90% vs. 20%), tumor necrosis (90% vs. 24%). Overall survival shorter: 10.9 vs. 25.4 months (P=0.004). [PMID:38630790](../papers/38630790.md)
- Half of GNH cases showed genome duplication resulting in >=2n copy states. Chromosomes 5p and 7p recurrently spared from LOH. [PMID:38630790](../papers/38630790.md)
- Epithelioid vs. biphasic/sarcomatoid distinction captured by RNA expression-based ATLAS sarcoma lineage scores (AUC=0.81). [PMID:27634761](../papers/27634761.md)

## Therapeutic landscape

- GNH DPMs showed preliminary immunotherapy responsiveness: 2/3 GNH patients treated with ipilimumab/nivolumab or [pembrolizumab](../drugs/pembrolizumab.md) achieved partial response (67%) vs. 1/44 (2%) in non-GNH. A clinical trial of [durvalumab](../drugs/durvalumab.md) + platinum-pemetrexed in 3 GNH patients showed tumor shrinkage in all and [OS](../cancer_types/OS.md) >=12 months. [PMID:38630790](../papers/38630790.md)
- [SETDB1](../genes/SETDB1.md) mutations as a molecular marker for GNH subset when detected on panels covering this gene (e.g., IMPACT505). [PMID:38630790](../papers/38630790.md)
- RNA-based mesothelioma subtype classification (epithelioid vs. biphasic/sarcomatoid) is prognostic and may guide treatment decisions. [PMID:27634761](../papers/27634761.md)

## Sources

- [PMID:38630790](../papers/38630790.md) — Diffuse pleural mesotheliomas with genomic near-haploidization: a newly recognized subset (Clinical Cancer Research, 2024)
- [PMID:27634761](../papers/27634761.md) — A platform-independent AI tumor lineage and site (ATLAS) classifier (Communications Biology, 2024)

*This page was processed by **crosslinker** on **2026-04-11**.*
