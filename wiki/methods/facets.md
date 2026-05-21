---
name: FACETS
slug: facets
kind: method
canonical_source: 
unverified: true
tags: [copy-number, clonality, computational]
processed_by: crosslinker
processed_at: 2026-05-21
---

# FACETS

## Overview

Allele-specific copy-number and clonality inference tool for tumor/normal NGS data.

## Used by

- [PMID:36493333](../papers/36493333.md) — used to assess clonality in the appendiceal adenocarcinoma MSK-IMPACT cohort, supporting the molecular subtyping of mucinous appendiceal adenocarcinoma into RAS-mut, GNAS-mut, and TP53-mut predominant lineages [PMID:36493333](../papers/36493333.md).
- [PMID:37682528](../papers/37682528.md) — used to derive allele-specific copy-number calls from MSK-IMPACT in 1,507 urothelial carcinoma tumors, supporting assessment of [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) co-alteration patterns in [FGFR3](../genes/FGFR3.md)-altered disease [PMID:37682528](../papers/37682528.md).
- [PMID:37651310](../papers/37651310.md) — FACETS used for copy-number analysis in 1,882 endometrial carcinoma patients sequenced by MSK-IMPACT; supported identification of CN-H/TP53abn molecular subtype enriched in Black patients [PMID:37651310](../papers/37651310.md).
- [PMID:38630790](../papers/38630790.md) — FACETS used to assess tumor purity and detect genomic near-haploidization (LOH >80%) in 210 evaluable diffuse pleural mesothelioma patients from MSK-IMPACT sequencing [PMID:38630790](../papers/38630790.md).
- [PMID:38758238](../papers/38758238.md) — FACETS v0.5.6 used for allele-specific copy-number and LOH inference in pituitary neuroendocrine tumors; identified rcLOH pattern in 11/14 treatment-refractory corticotroph PitNETs [PMID:38758238](../papers/38758238.md).
- [PMID:38949888](../papers/38949888.md) — FACETS v0.5.6 used for copy-number analysis in 3,244 prostate cancer tumors from 2,257 patients sequenced by MSK-IMPACT [PMID:38949888](../papers/38949888.md).
- [PMID:39753968](../papers/39753968.md) — FACETS v0.5.14 used in a two-step pipeline for allele-specific copy-number inference in 2,336 PDAC patients sequenced with MSK-IMPACT; 1,555 of 2,322 tumors passed copy-number QC; FACETS output enabled classification of [KRAS](../genes/KRAS.md) allelic imbalance events (focal/arm amplifications, gains, CNLOH, LOH, post-WGD loss) and showed that [KRAS](../genes/KRAS.md) mutant-allele dosage gains independently predict shorter [OS](../cancer_types/OS.md) across all clinical stages [PMID:39753968](../papers/39753968.md).
- Used to assess tumor purity (>=25% threshold) in 22 primary-metastasis WES pairs for bladder cancer clonal evolution analysis [PMID:36543146](../papers/36543146.md)
- FACETS used for allele-specific copy-number estimation and clonality assessment in 151 advanced head and neck tumors sequenced with MSK-IMPACT; identified whole-genome duplication in 25% of [HNSC](../cancer_types/HNSC.md) cases and quantified 3p deletions enriched in recurrent HPV-positive disease [PMID:27442865](../papers/27442865.md)
- Applied FACETS algorithm to infer somatic copy number alterations and tumor purity/ploidy from sequencing data [PMID:28336552](../papers/28336552.md)
- Used to [estimate](../methods/estimate.md) cancer cell fraction and clonality of alterations in MSK-IMPACT-sequenced prostate cancer tumors (504 tumors from 451 patients); identified [TP53](../genes/TP53.md) and [BRCA2](../genes/BRCA2.md) somatic alterations as early truncal clonal events in patients who later developed metastasis [PMID:28825054](../papers/28825054.md)
- FACETS v0.5.0 used for allele-specific copy-number analysis from WES in 68 melanoma biopsies; identified focal [CDKN2A](../genes/CDKN2A.md) loss emerging on-therapy in 4 progressive-disease patients [PMID:29033130](../papers/29033130.md)
- FACETS used for allele-specific copy-number estimation and tumor purity calculation in 295 metastatic [EGC](../cancer_types/EGC.md) samples; [ERBB2](../genes/ERBB2.md) amplification level by FACETS-based NGS predicted [trastuzumab](../drugs/trastuzumab.md) PFS better than IHC/FISH [PMID:29122777](../papers/29122777.md)
- FACETS v0.3.9 used to [estimate](../methods/estimate.md) copy number, purity, and ploidy in SUMMIT basket-trial patients; integrated with ABSOLUTE v1.0.6 for HER2 mutation clonality estimates (95% of HER2 mutations were clonal) [PMID:29420467](../papers/29420467.md)
- FACETS v0.5.10 applied to 1,013 prostate tumor/normal pairs for allele-specific copy number, purity, ploidy, and clonality (cancer-cell fraction) estimation [PMID:29610475](../papers/29610475.md)
- FACETS v0.5.6 (cval=100) used to derive allele-specific copy-number profiles for 189 advanced endometrial cancer tumors; hierarchical clustering of FACETS profiles identified a novel Cluster C (heterozygous losses) with median PFS 9.6 vs 17 months (p=0.006) [PMID:30068706](../papers/30068706.md)
- FACETS algorithm applied for allele-specific copy-number inference and tumor purity estimation in 1,918 prospectively sequenced breast tumors [PMID:30205045](../papers/30205045.md)
- FACETS used for somatic copy-number calling on CSF ctDNA and matched tumor tissue from 85 glioma patients; identified focal amplifications ([EGFR](../genes/EGFR.md), [PDGFRA](../genes/PDGFRA.md), [CDK4](../genes/CDK4.md), [MYC](../genes/MYC.md), [KIT](../genes/KIT.md), [MET](../genes/MET.md)) and homozygous deletions (CDKN2A/B) tracked through serial CSF sampling to document convergent evolution [PMID:30675060](../papers/30675060.md)
- Used for allele-specific copy-number analysis and LOH quantification on 95 of 96 panNET samples ([panet_msk_2018](../datasets/panet_msk_2018.md)); part of the MSK-IMPACT bioinformatics pipeline [PMID:30687805](../papers/30687805.md)
- Used for allele-specific copy-number estimation (v0.3.9) in 837 paired tumor-normal MSK-IMPACT glioma samples; 1p/19q codeletion called at 75% threshold, chr7 gain / chr10 loss at 90% threshold; [BRAF](../genes/BRAF.md) V600 clonality estimated from FACETS purity-corrected CCF [PMID:31263031](../papers/31263031.md)
- Used to infer clonality and intratumor heterogeneity in 1,045 adenoid cystic carcinoma cases; allele-specific copy-number analysis identified BRCA1/2 germline variants as monoallelic (no LOH) and confirmed 4 molecular subgroups by purity/ploidy estimates [PMID:31483290](../papers/31483290.md).
- Run sequentially (purity at critical value 100, then sensitivity 50) on [IMPACT468](../methods/IMPACT468.md) panel data from 12 prostate cancer patients to call allele-specific [PTEN](../genes/PTEN.md) copy number; homozygous [PTEN](../genes/PTEN.md) loss in 2 ROIs tracked with the highest hyperpolarized lactate signal (P=0.059) [PMID:31564440](../papers/31564440.md).
- Used alongside ABSOLUTE and PyClone to infer allele-specific copy number and whole-genome doubling in 56-sample DCIS/IDC-NST WES cohort [PMID:32220886](../papers/32220886.md)
- Applied (with tumor purity ≤20% excluded) for allele-specific copy-number and clonality inference in 424 mCSPC MSK-IMPACT-sequenced tumors [PMID:32220891](../papers/32220891.md)
- v0.5.6 applied for allele-specific copy number, purity, and ploidy estimation in 107 uterine sarcoma MSK-IMPACT samples [PMID:32299819](../papers/32299819.md)
- Used for allele-specific copy-number and clonality inference in 26,743 MSK-IMPACT pan-cancer cohort; CDK12-Bi prostate cancer showed higher fraction of genome gain and more breakpoints consistent with tandem duplicator phenotype [PMID:32317181](../papers/32317181.md)
- Applied for allele-specific copy number and LOH analysis in 430 MSS mCRC patients; large state transitions (LST) computed as ≥10 Mb breaks per chromosome arm to assess HRD [PMID:32730818](../papers/32730818.md)
- Used for copy-number and fraction-genome-altered ([FGA](../genes/FGA.md)) calculations across 604 [LUAD](../cancer_types/LUAD.md) patients; [FGA](../genes/FGA.md) correlated with histologic-subtype invasiveness (LEP 0.174, ACI/PAP 0.222, MIP/SOL 0.304) [PMID:32791233](../papers/32791233.md)
- Applied for allele-specific copy number and cancer cell fraction (CCF) analysis in the [breast_alpelisib_2020](../datasets/breast_alpelisib_2020.md) cohort; identified [PTEN](../genes/PTEN.md) homozygous deletion in ctDNA of resistant HR+ [MBC](../cancer_types/MBC.md) patients [PMID:32864625](../papers/32864625.md)
- FACETS v0.5.14 applied to 74 matched retinoblastoma specimens for copy-number and clonality calling; 69 yielded evaluable arm-level CNA profiles [PMID:33466343](../papers/33466343.md)
- FACETS allele-specific copy-number tool applied to 428 melanoma samples (of 696 total) with adequate quality; 92% had only clonal driver alterations [PMID:33509808](../papers/33509808.md)
- FACETS used for copy-number purity/ploidy correction in 487 EAC/EGJ tumor samples sequenced with MSK-IMPACT [PMID:33795256](../papers/33795256.md)
- Used to call copy-number alterations and LOH in WES and MSK-IMPACT data from 44 metaplastic breast cancers ([MBC](../cancer_types/MBC.md)); TERT-altered MBCs had significantly lower fraction of genome altered (median 22%) than TERT-WT MBCs (median 54%; p=0.002) [PMID:33863915](../papers/33863915.md)
- Used for tumor clonality estimation (CCF) in plasma cf-IMPACT samples from 118 metastatic solid tumor patients; tumor purity from FACETS did not differ between concordant and discordant plasma-tissue sample pairs (p=0.812) [PMID:34059130](../papers/34059130.md)
- Applied for tumor purity estimation in the MSK-ACCESS clinical deployment pipeline; tumor purity did not significantly differ between concordant and tissue/plasma-discordant sample groups [PMID:34145282](../papers/34145282.md)
- Used in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for somatic variant calling and genomic analysis of the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)
- Applied to a subset of 17,224 MSK-MET samples for allele-specific copy-number analysis, deriving purity/ploidy-adjusted [FGA](../genes/FGA.md), whole-genome doubling (WGD) status, and clonality estimates [PMID:35120664](../papers/35120664.md)
- FACETS used to assess copy number, tumor purity, ploidy, and bi-allelic status in 237 esophageal/GEJ adenocarcinoma patients sequenced with MSK-IMPACT [PMID:35377946](../papers/35377946.md).
- FACETS used for clonality and allelic imbalance analysis in 43 dual-driver CRC cases; identified that 21% had both drivers clonal, 40% one clonal/one subclonal [PMID:35235413](../papers/35235413.md).
- FACETS used for copy-number analysis of 42 [SCLC](../cancer_types/SCLC.md) PDX/CDX and 26 clinical samples in the MSK PDX resource; higher CNA density in PDXs attributed to greater tumor purity from murine stromal replacement [PMID:35440124](../papers/35440124.md).
- Used in [lgsoc_mapk_msk_2022](../datasets/lgsoc_mapk_msk_2022.md) to infer loss of heterozygosity at germline mutation loci in 119 LGSC patients sequenced by MSK-IMPACT; LOH assessed in 7 pathogenic germline mutation carriers [PMID:35443055](../papers/35443055.md)
- Used in [prostate_pcbm_swiss_2019](../datasets/prostate_pcbm_swiss_2019.md) for allele-specific copy-number analysis of 168 prostate cancer brain metastasis samples; identified [AR](../genes/AR.md) amplifications in 32/51 (63%) patients and [PTEN](../genes/PTEN.md) loss/deletion in 33/51 (65%) [PMID:35504881](../papers/35504881.md)
- Used in [hcc_meric_2021](../datasets/hcc_meric_2021.md) for allele-specific copy-number analysis of 122 [HCC](../cancer_types/HCC.md) biopsies (114 patients), enabling identification of recurrent focal CNAs subsequently analyzed by GISTIC 2.0 [PMID:35508466](../papers/35508466.md)
- FACETS used for allelic copy-number estimation and clonality calls in 2,735 MSK-IMPACT prostate cancer samples; 1,417 passed QC (samples with low purity were excluded as 'copy-number quiet') [PMID:35670774](../papers/35670774.md)
- FACETS used for allele-specific copy number and whole-genome-doubling calls across 2,138 MSK-IMPACT sarcomas; WGD frequency ranged from ~50% in osteosarcoma/UPS to lower rates in translocation-driven subtypes [PMID:35705560](../papers/35705560.md)
- FACETS used for copy-number and loss-of-heterozygosity analysis in 184 MSI-H/MMR-D endometrial cancers sequenced by MSK-IMPACT [PMID:35849120](../papers/35849120.md)

## Notes

- In the appendiceal cohort, FACETS-derived clonality was paired with aneuploidy scoring (segment-length-weighted copy-number deviation from diploid), where TP53-mut predominant tumors were highly aneuploid and aneuploidy was independently associated with poor prognosis (P=.001) [PMID:36493333](../papers/36493333.md).

## Sources

- [PMID:36493333](../papers/36493333.md)
- [PMID:37682528](../papers/37682528.md)
- [PMID:37651310](../papers/37651310.md)
- [PMID:38630790](../papers/38630790.md)
- [PMID:38758238](../papers/38758238.md)
- [PMID:38949888](../papers/38949888.md)
- [PMID:39753968](../papers/39753968.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:36543146](../papers/36543146.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27442865](../papers/27442865.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28336552](../papers/28336552.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28825054](../papers/28825054.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29122777](../papers/29122777.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29420467](../papers/29420467.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29610475](../papers/29610475.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30068706](../papers/30068706.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30205045](../papers/30205045.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30675060](../papers/30675060.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30687805](../papers/30687805.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31263031](../papers/31263031.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31483290](../papers/31483290.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31564440](../papers/31564440.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32220886](../papers/32220886.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32220891](../papers/32220891.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32299819](../papers/32299819.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32317181](../papers/32317181.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32730818](../papers/32730818.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32791233](../papers/32791233.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32864625](../papers/32864625.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33466343](../papers/33466343.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33509808](../papers/33509808.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33795256](../papers/33795256.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:33863915](../papers/33863915.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34059130](../papers/34059130.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34145282](../papers/34145282.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34493867](../papers/34493867.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35120664](../papers/35120664.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35377946](../papers/35377946.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35235413](../papers/35235413.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35440124](../papers/35440124.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35443055](../papers/35443055.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35504881](../papers/35504881.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35508466](../papers/35508466.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35670774](../papers/35670774.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35705560](../papers/35705560.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35849120](../papers/35849120.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
