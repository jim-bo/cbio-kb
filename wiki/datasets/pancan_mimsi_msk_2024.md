---
name: Pan-Cancer MSK MiMSI MSI Cohort (2024)
studyId: pancan_mimsi_msk_2024
institution: Memorial Sloan Kettering Cancer Center
size: 5037
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays: [targeted-sequencing]
panels: [IMPACT468]
tags:
  - pan-cancer
  - microsatellite-instability
  - MSI
  - MMR
  - deep-learning
  - MiMSI
processed_by: crosslinker
processed_at: 2026-04-30
---

# Pan-Cancer MSK MiMSI MSI Cohort (2024)

## Overview

Prospective secondary cohort of 5,037 MSK-IMPACT–sequenced tumors with paired mismatch repair (MMR) immunohistochemistry (IHC) used to validate the MiMSI deep multiple-instance learning MSI classifier. Spans 42 cancer types. The training/test microsatellite vectors and somatic alteration data are released as cBioPortal study `pancan_mimsi_msk_2024` [PMID:39746944](../papers/39746944.md).

## Composition

- 5,037 samples from 42 cancer types with paired MMR IHC; 4,195 MMR-proficient and 842 MMR-deficient (580 [MLH1](../genes/MLH1.md) loss, 166 [MSH2](../genes/MSH2.md) loss, 60 [MSH6](../genes/MSH6.md) loss, 36 [PMS2](../genes/PMS2.md) loss) [PMID:39746944](../papers/39746944.md).
- Cancer types most represented: [COAD](../cancer_types/COAD.md) (n=2,448), [UCEC](../cancer_types/UCEC.md) (n=1,212), esophagogastric carcinoma (n=475), cancer of unknown primary (n=114), [BLCA](../cancer_types/BLCA.md) (n=73), small bowel cancer (n=60), [PRAD](../cancer_types/PRAD.md) (n=55) [PMID:39746944](../papers/39746944.md).
- Orthogonal MMR ground-truth: MMR IHC confirmed by board-certified pathologist; MSI-PCR for training/test cohort [PMID:39746944](../papers/39746944.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) ([IMPACT468](../methods/IMPACT468.md)) — targeted hybridization-capture sequencing; typical mean coverage ~600×; microsatellite locus list: 1,755 loci covered by MSK-IMPACT (generated using [msisensor](../methods/msisensor.md) scan v0.2) [PMID:39746944](../papers/39746944.md).

## Papers using this cohort

- [PMID:39746944](../papers/39746944.md) — Ziegler et al. 2025: MiMSI, a deep multiple-instance learning MSI classifier trained on 741 MSK-IMPACT cases and validated prospectively. MiMSI achieved sensitivity 0.895 and auROC 0.971 on held-out test samples, outperforming MSISensor (sensitivity 0.67, auROC 0.907), with the largest advantage in tumors with <30% purity (MiMSI 85.1% vs MSISensor 72.8%).

## Notable findings derived from this cohort

- MMR-deficient (MMR-D) tumors had significantly higher TMB than MMR-proficient (median 39 vs 5.27 mut/Mb, Mann-Whitney P<2.2×10⁻¹⁶); [MSH2](../genes/MSH2.md) loss had higher TMB than [MLH1](../genes/MLH1.md) loss (median 46.5 vs 37.7, P=0.0013) [PMID:39746944](../papers/39746944.md).
- Median indel/SNV ratio 0.18 in MMR-P vs 0.5 in MMR-D; [MSH6](../genes/MSH6.md) loss had the lowest (0.09) and [MLH1](../genes/MLH1.md) loss the highest (0.57) among MMR-D subgroups [PMID:39746944](../papers/39746944.md).
- MiMSI sensitivity in this prospective cohort: 91.6% (95% CI 89.5–93.4%) vs MSISensor 86.1% (83.3–88.6%); MiMSI correctly classified 226/247 (91%) MSISensor-indeterminate cases [PMID:39746944](../papers/39746944.md).
- MiMSI advantage over MSISensor was most marked in tumors with <30% purity (85.1% vs 72.8%, McNemar's chi-squared P=8.244×10⁻⁷) [PMID:39746944](../papers/39746944.md).
- Per-cancer-type sensitivity advantage for MiMSI in small bowel cancer (100% vs 94.1%), [PRAD](../cancer_types/PRAD.md) (93.8% vs 85.7%), and [UCEC](../cancer_types/UCEC.md) (89.7% vs 79%) [PMID:39746944](../papers/39746944.md).

## Sources

- cBioPortal study `pancan_mimsi_msk_2024`. Note: raw sequencing reads are not available (patient-consent restrictions); only precomputed microsatellite vectors and somatic alteration data are public. Ziegler et al. *MiMSI: A deep learning classifier to detect microsatellite instability in next generation sequencing data.* 2025. [PMID:39746944](../papers/39746944.md).

*This page was processed by **crosslinker** on **2026-04-30**.*
