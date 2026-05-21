---
name: MiMSI
slug: mimsi
kind: method
canonical_source: corpus
unverified: true
tags:
  - computational
  - msi
  - msi-calling
  - deep-learning
  - multiple-instance-learning
  - targeted-sequencing
processed_by: crosslinker
processed_at: 2026-05-21
---

# MiMSI

## Overview

MiMSI (Multiple Instance learning for MicroSatellite Instability) is a deep learning classifier that detects microsatellite instability (MSI) from targeted next-generation sequencing reads at microsatellite loci. It uses a ResNet-style convolutional neural network feature extractor followed by multiple-instance learning (MIL) pooling (mean or attention-based) and a sigmoid classifier. Input is a three-dimensional vector of per-microsatellite-locus read distributions; confident calls are produced by aggregating 10 random downsampling runs and computing the 95% confidence interval relative to a threshold of 0.4. MiMSI is released under GPLv3 at https://github.com/mskcc/mimsi (Zenodo DOI 10.5281/zenodo.13357948).

## Used by

- Developed, trained, and validated at Memorial Sloan Kettering Cancer Center (MSK) using [MSK-IMPACT](../methods/msk-impact-panel.md) ([IMPACT468](../methods/IMPACT468.md)) targeted panel sequencing data across training (n=741), held-out test (n=317), prospective validation (n=5,037 with MMR IHC), and global comparison (n=45,112) cohorts [PMID:39746944](../papers/39746944.md).
- Used alongside [MSIsensor](../methods/msisensor.md) to orthogonally confirm microsatellite stability in 1,045 adenoid cystic carcinomas; all cases MSS, including 15/90 MSKCC R/M cases with germline MLH1/MSH6 variants [PMID:31483290](../papers/31483290.md).
- Applied for MSI classification in aSCLC; the single MSI-H case (A20) harbored somatic [MLH1](../genes/MLH1.md) homozygous deletion with dual MLH1/PMS2 IHC loss; MiMSI used alongside MSIsensor as orthogonal MSI calling methods [PMID:39185963](../papers/39185963.md)

## Notes

- Input: per-microsatellite-locus read distributions from targeted or WES NGS; 1,755 loci covered by MSK-IMPACT generated using [msisensor](../methods/msisensor.md) scan v0.2.
- Architecture: PyTorch, Adam optimizer, ResNet CNN → MIL pooling → sigmoid; threshold 0.4; 95% CI from 10 random downsamples for indeterminate flagging.
- Outperforms [msisensor](../methods/msisensor.md) in sensitivity (0.895 vs 0.67, auROC 0.971 vs 0.907) on a held-out test set enriched for difficult cases (low purity, low coverage) [PMID:39746944](../papers/39746944.md).
- Reduces indeterminate rate from 3.8% to 0.47% in 45,112 prospectively sequenced MSK-IMPACT tumors; 96% concordance with MSIsensor for definitive calls [PMID:39746944](../papers/39746944.md).
- Advantage over MSIsensor is largest for tumors with <30% tumor purity: 85.1% vs 72.8% sensitivity (McNemar's P=8.244×10⁻⁷) [PMID:39746944](../papers/39746944.md).
- Generalizes to whole-exome sequencing without retraining (98.6% concordance on n=582 WES libraries) [PMID:39746944](../papers/39746944.md).
- Tumor-only mode requires pooled normal comparator and mean (non-attention) pooling; attention pooling with unrelated normal over-calls MSI-H [PMID:39746944](../papers/39746944.md).
- Training data and secondary cohort somatic alterations released as cBioPortal study [pancan_mimsi_msk_2024](../datasets/pancan_mimsi_msk_2024.md) [PMID:39746944](../papers/39746944.md).

## Sources

- [PMID:39746944](../papers/39746944.md) — Ziegler et al. developed and validated MiMSI on 1,058 training/test samples enriched for difficult MSI-calling cases plus a 5,037-sample prospective cohort with orthogonal MMR IHC; MiMSI sensitivity 0.895 vs MSISensor 0.67 on the held-out test set, with the advantage concentrated in low-purity tumors (<30%); global comparison across 45,112 MSK-IMPACT tumors showed 96% concordance with MSIsensor and a 3.33-fold reduction in indeterminate calls [PMID:39746944](../papers/39746944.md).

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31483290](../papers/31483290.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:39185963](../papers/39185963.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
