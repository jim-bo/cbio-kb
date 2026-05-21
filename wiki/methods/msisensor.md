---
name: MSIsensor
slug: msisensor
kind: method
canonical_source: corpus
unverified: true
tags:
  - computational
  - msi
  - msi-calling
  - targeted-sequencing
processed_by: crosslinker
processed_at: 2026-05-21
---

# MSIsensor

## Overview

MSIsensor is a computational tool for detecting microsatellite instability (MSI) from paired tumor-normal next-generation sequencing data. It scans the sequenced genome for microsatellite loci (using the `msisensor scan` sub-command) and computes a per-locus distribution of repeat-unit lengths in tumor vs. normal reads; an overall MSI score (percentage of unstable loci) is computed across all evaluated sites. A threshold of ≥10 is commonly used to classify samples as MSI-H (high instability). MSIsensor is widely deployed in clinical NGS pipelines as the reference standard for MSI calling, including within the MSK-IMPACT clinical sequencing program at Memorial Sloan Kettering Cancer Center.

## Used by

- Used as the reference comparator in the development and validation of [mimsi](../methods/mimsi.md), assessed across a held-out test set (n=317), a prospective validation cohort (n=5,037 with MMR IHC), and a global MSK-IMPACT comparison cohort (n=45,112 samples) [PMID:39746944](../papers/39746944.md).
- Used in the MSK-IMPACT clinical pipeline for MSI inference in 2,336 PDAC patients; cut-off ≥10 for MSI-H classification [PMID:39753968](../papers/39753968.md).
- Used alongside MiMSI and IDYLLA MSI to assess microsatellite instability in 244 [GBC](../cancer_types/GBC.md) samples; identified 6 tumors (3%) as MSI-High [PMID:36228155](../papers/36228155.md)
- Applied to WGS data of 28 metastatic NENs to predict MSI status; classified PN4 (homozygous MSH6/MLH1 loss, TMB ~11 mut/Mb) as MSI-low — illustrating that dMMR does not always predict MSI-high in non-colorectal tumors [PMID:40328872](../papers/40328872.md).
- MSIsensor used to cross-check signature-based MSI calls in the MSK-IMPACT cohort; identified 102 MSI patients across 11 tumor types, 45% previously untested for MMR deficiency [PMID:28481359](../papers/28481359.md)
- MSIsensor used to determine MSI status from targeted sequencing data in 295 metastatic [EGC](../cancer_types/EGC.md) patients (MSI-H threshold ≥10); identified 9/295 (3%) MSI-H tumors [PMID:29122777](../papers/29122777.md)
- MSIsensor score ≥10 used to classify 99 MSI-H/hypermutated (8.7%) and 1,027 MSS (90.6%) cases among 1,134 [COADREAD](../cancer_types/COADREAD.md) tumors; 98.6% concordance with MMR IHC [PMID:29316426](../papers/29316426.md)
- MSIsensor used to assess microsatellite instability in SUMMIT basket-trial patients with ERBB2/ERBB3-mutant solid tumors profiled by MSK-IMPACT; results contributed to TMB and co-mutation analysis [PMID:29420467](../papers/29420467.md)
- Used to quantify MSI status (threshold score >4) across TCGA PanCancer Atlas tumors; 250/1,464 samples with somatic MMR mutations and 18/60 with germline MMR variants reached MSI-high status [PMID:29625049](../papers/29625049.md).
- Applied to MSK-IMPACT targeted sequencing data from 195 cholangiocarcinoma patients; identified 1 MSI-H tumor (0.5%, score 35.1) with MLH1/MSH6 protein loss on IHC [PMID:29848569](../papers/29848569.md)
- MSIsensor v0.2 (threshold ≥10 for MSI-H) applied to 189 advanced endometrial cancer tumors; 29/30 MMR-D/presumed-MMR-D tumors scored MSI-H; one MMR-proficient-by-IHC case was rescued as MSI-H by MSIsensor (occult MMR deficiency) [PMID:30068706](../papers/30068706.md)
- MSIsensor used to call MSI status in 127 advanced [HCC](../cancer_types/HCC.md) tumors (MSI-H threshold ≥10); no MSI-H cases observed and TMB median 4.08 [PMID:30373752](../papers/30373752.md)
- Used to call microsatellite instability status in 37 high-grade [UTUC](../cancer_types/UTUC.md) tumors; mean MSIsensor score in WCM [UTUC](../cancer_types/UTUC.md) and TCGA UCB were both below the MSI-H threshold of 3.5 and indistinguishable, confirming sporadic [UTUC](../cancer_types/UTUC.md) is not microsatellite-unstable despite reduced MMR protein expression [PMID:31278255](../papers/31278255.md)
- Applied to all 1,045 adenoid cystic carcinomas to assess microsatellite status; all cases returned microsatellite-stable, even among the 15/90 MSKCC R/M cases with MLH1/MSH6 germline variants [PMID:31483290](../papers/31483290.md).
- MSIsensor v0.2 applied to 107 uterine sarcoma MSK-IMPACT samples; threshold ≥10 defined MSI-H; 2 uLMS cases scored MSI-H with outlier TMB and IHC-confirmed MMR loss [PMID:32299819](../papers/32299819.md)
- MSIsensor used to [estimate](../methods/estimate.md) microsatellite instability in 83 retinoblastoma specimens; TMB uniformly low (0–3 mutations/Mb) [PMID:33466343](../papers/33466343.md)
- MSIsensor (cutoff ≥10) used for MSI calling in 487 EAC/EGJ patients; 15/487 (3.1%) were MSI-high and excluded from survival analyses [PMID:33795256](../papers/33795256.md)
- Applied to cfDNA plasma samples in the tumor-fraction-guided cfDNA triage study to assess MSI status; one CRPC patient with two failed tumor biopsies was found to be MSI-High by cf-IMPACT, confirmed by later bone biopsy, leading to [pembrolizumab](../drugs/pembrolizumab.md) treatment and durable response [PMID:34059130](../papers/34059130.md)
- Used to classify MSI status in 64 Nigerian CRC tumors; 28.1% (18/64) were MSI-H, significantly higher than TCGA (14.2%) and MSKCC (8.5%) reference cohorts (P<0.001) [PMID:34819518](../papers/34819518.md)
- MSIsensor score ≥10 used to classify MSI-H; 14 MSI-H cases excluded from neoadjuvant response analyses in 237-patient [EGC](../cancer_types/EGC.md) cohort [PMID:35377946](../papers/35377946.md).
- Applied in [lgsoc_mapk_msk_2022](../datasets/lgsoc_mapk_msk_2022.md): all 102 evaluable LGSC cases were microsatellite stable (median MSIsensor score 0.12) [PMID:35443055](../papers/35443055.md)
- Used in the cWGTS pipeline ([mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md)) for microsatellite instability assessment in 114 pediatric/AYA solid tumor patients; MSI signal detected in 7 patients [PMID:35585047](../papers/35585047.md)
- MSIsensor with threshold ≥10 used to classify MSI status in 2,138 sarcomas; only 5/1,893 evaluable samples were MSI-high, confirming MSI rarity in mesenchymal tumors [PMID:35705560](../papers/35705560.md)
- MSIsensor (threshold ≥10 = MSI-H; 3–<10 = indeterminate; <3 = MSS) applied to 184 endometrial cancers; all MLH1ph and somatic MMR-D cases were MSI-H, but 83% of MSH6-germline and 31% of MLH1/PMS2/MSH2-germline cases scored MSS/indeterminate — revealing a sensitivity floor for Lynch syndrome EC [PMID:35849120](../papers/35849120.md)

## Notes

- Operates on paired tumor-normal BAM files; evaluates loci generated by `msisensor scan v0.2`.
- Threshold ≥10 for MSI-H in the MSK-IMPACT clinical deployment [PMID:39753968](../papers/39753968.md).
- Sensitivity 0.67 and auROC 0.907 on a held-out test set enriched for difficult (low-purity, low-coverage) cases — substantially lower than [mimsi](../methods/mimsi.md) (sensitivity 0.895, auROC 0.971) [PMID:39746944](../papers/39746944.md).
- Indeterminate rate of 3.8% (n=1,724 of 45,112 MSK-IMPACT samples) vs. 0.47% for MiMSI [PMID:39746944](../papers/39746944.md).
- Fails to report in 118 of 5,037 prospective cohort cases (2.3%) due to low coverage or purity [PMID:39746944](../papers/39746944.md).
- 96% concordance with MiMSI for definitive MSS/MSI-H calls [PMID:39746944](../papers/39746944.md).

## Sources

- [PMID:39746944](../papers/39746944.md) — Ziegler et al. benchmarked MSIsensor against MiMSI across multiple cohorts; MSIsensor sensitivity 0.67 vs. MiMSI 0.895 on held-out test set (317 samples), with particular underperformance in low-purity cases (<30% purity: MSIsensor 72.8% vs MiMSI 85.1%, McNemar's P=8.244×10⁻⁷); indeterminate rate 3.8% across 45,112 MSK-IMPACT samples [PMID:39746944](../papers/39746944.md).
- [PMID:39753968](../papers/39753968.md) — MSIsensor (cutoff ≥10) used for MSI inference in the 2,336-patient MSK PDAC cohort sequenced with MSK-IMPACT; MSI was one of the OncoKB level 1 biomarkers tracked in the actionability landscape analysis [PMID:39753968](../papers/39753968.md).

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:36228155](../papers/36228155.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:40328872](../papers/40328872.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28481359](../papers/28481359.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29122777](../papers/29122777.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29316426](../papers/29316426.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29420467](../papers/29420467.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29848569](../papers/29848569.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30068706](../papers/30068706.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30373752](../papers/30373752.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31278255](../papers/31278255.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31483290](../papers/31483290.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32299819](../papers/32299819.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33466343](../papers/33466343.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33795256](../papers/33795256.md)

- [PMID:34059130](../papers/34059130.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34819518](../papers/34819518.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35377946](../papers/35377946.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35443055](../papers/35443055.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35705560](../papers/35705560.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35849120](../papers/35849120.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
