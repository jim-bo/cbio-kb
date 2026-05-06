---
name: Whole-genome sequencing (WGS)
slug: whole-genome-seq
kind: method
canonical_source: 
unverified: true
tags: [sequencing, wgs]
processed_by: crosslinker
processed_at: 2026-05-05
---

# Whole-genome sequencing (WGS)

## Overview

Unbiased short-read sequencing of the entire tumor (and matched normal) genome, used in the corpus for structural variant detection, mutational signature analysis at non-coding sites, evolutionary timing, and microbiome read mining.

## Used by

- [PMID:35927489](../papers/35927489.md) — 177 WGS samples in the CLL-map cohort; identified 681 SV breakpoints in 141 patients (~4.8/patient), [BCL2](../genes/BCL2.md) translocations predominantly in M-CLL via aberrant V(D)J, and a recurrent 37-Mb chr14 deletion disrupting [ZFP36L1](../genes/ZFP36L1.md) (and [DICER1](../genes/DICER1.md), [TRAF3](../genes/TRAF3.md)) in U-CLL via class-switch recombination. Supported mutational signature analysis (canonical AID SBS84 enriched in U-CLL clustered mutations; non-canonical AID SBS85 enriched in M-CLL, p=1.6×10^-9; plus SBS18) [PMID:35927489](../papers/35927489.md).
- [PMID:36723991](../papers/36723991.md) — WGS on FACS-purified Hodgkin and Reed Sternberg cells from 25 cHL patients with matched intratumoral T cells as germline; established the first comprehensive WGS landscape of cHL, with median post-artifact-removal mutational burden of 5,279 SBS+indels per genome (range 1,880–18,883), prevalent APOBEC mutagenesis (SBS2/SBS13), AID off-target activity, chromothripsis, and timing of WGD as a late event [PMID:36723991](../papers/36723991.md).
- [PMID:37202560](../papers/37202560.md) — tumor WGS in the AC-ICAM colon cancer atlas, used for microbiome read mining alongside 16S rRNA sequencing [PMID:37202560](../papers/37202560.md).
- [PMID:37730754](../papers/37730754.md) — shallow WGS used for CNV assessment from 62 plasma samples (10 patients) in the longitudinal ctDNA arm of the rhabdomyosarcoma progression/relapse study [PMID:37730754](../papers/37730754.md).
- [PMID:38117484](../papers/38117484.md) — WGS on a subset of 64 glioma patients in the GLASS International consortium; integrated with 450K/EPIC methylation arrays and RNA-seq [PMID:38117484](../papers/38117484.md).
- [PMID:38412093](../papers/38412093.md) — WGS on 9 of 141 characterized anaplastic thyroid carcinoma regions (the remaining 132 underwent WES) [PMID:38412093](../papers/38412093.md).
- [PMID:38488813](../papers/38488813.md) — WGS at 30X on 44 prostate cancer PDX models; paired with targeted sequencing (T200.1 panel) and RNA-seq for integrative multi-platform molecular characterization [PMID:38488813](../papers/38488813.md).
- [PMID:39305899](../papers/39305899.md) — WGS (BWA-MEM2, MuSE, Mutect2, SomaticSniper, Strelka2, Battenberg/ASCAT) on a subset of the UCLA sarcoma biobank (194 specimens from 126 patients); used alongside [DFCI-ONCOPANEL-3](../methods/DFCI-ONCOPANEL-3.md) targeted DNA and bulk RNA-seq to characterize 24 bone and soft-tissue sarcoma subtypes; enabled CNV analysis including whole-genome duplications in intra-patient heterogeneity studies and functional-vs-genomic concordance analyses [PMID:39305899](../papers/39305899.md).
- Low-pass WGS (5x) applied to 51 primary and 102 metastatic breast cancer specimens in AURORA cohort; 11 DNA segments more frequently amplified in metastases (q<0.05), including [MYC](../genes/MYC.md) and [MDM4](../genes/MDM4.md) regions [PMID:36585450](../papers/36585450.md)
- Applied to primary tumors from 2 MEC patients (Patient 1: 29x tumor/25x normal; Patient 2: 22x tumor/15x normal; GRCh37/hg19); revealed >30-way biallelic chromoplexy event in MEC1 and double-minute [ELK4](../genes/ELK4.md) amplification in MEC2 [PMID:36577525](../papers/36577525.md)
- Applied to 40 treatment-naive [HGSOC](../cancer_types/HGSOC.md) tumor-normal pairs; mutational signature inference classified tumours into HRD-Dup (n=16), HRD-Del (n=6), and FBI (n=14) subtypes [PMID:36517593](../papers/36517593.md)

## Notes

- Small WGS cohorts in some corpus papers (e.g., n=25 in cHL, 177 in CLL) are repeatedly cited as a limitation for SV and rare-variant inference [PMID:35927489](../papers/35927489.md) [PMID:36723991](../papers/36723991.md).
- HRS-cell WGS in cHL required whole-genome amplification, introducing palindromic SBS artifacts that had to be computationally removed [PMID:36723991](../papers/36723991.md).

## Sources

- [PMID:35927489](../papers/35927489.md)
- [PMID:36723991](../papers/36723991.md)
- [PMID:37202560](../papers/37202560.md)
- [PMID:37730754](../papers/37730754.md)
- [PMID:38117484](../papers/38117484.md)
- [PMID:38412093](../papers/38412093.md)
- [PMID:38488813](../papers/38488813.md)
- [PMID:39305899](../papers/39305899.md)

*This page was processed by **crosslinker** on **2026-05-05**.*
- [PMID:36585450](../papers/36585450.md)

*This page was processed by **crosslinker** on **2026-05-05**.*
- [PMID:36577525](../papers/36577525.md)

*This page was processed by **crosslinker** on **2026-05-05**.*
- [PMID:36517593](../papers/36517593.md)

*This page was processed by **crosslinker** on **2026-05-05**.*
