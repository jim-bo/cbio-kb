---
name: Mutational Signatures Analysis (COSMIC)
slug: mutational-signatures
kind: method
canonical_source: corpus
unverified: true
tags: [mutational-signatures, cosmic, somatic-mutation, snv, indel]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Mutational Signatures Analysis (COSMIC)

## Overview

Decomposition of somatic mutation patterns (single-base substitution trinucleotide contexts, doublet substitutions, small indels) into a mixture of known COSMIC mutational signatures. Each COSMIC signature represents a characteristic mutation pattern attributed to a specific biological process (e.g., SBS1 = clock-like CpG deamination, SBS2/13 = APOBEC activity, SBS3 = HRD/BRCA deficiency, SBS4 = tobacco exposure, dMMR signatures). Decomposition is typically performed using non-negative matrix factorization (NMF) or maximum-likelihood fitting of a catalogue of 96 trinucleotide contexts against the COSMIC v2/v3 signature reference.

## Used by

- Applied to WGS data of 28 metastatic neuroendocrine neoplasms ([pog570_bcgsc_2020](../datasets/pog570_bcgsc_2020.md)) using COSMIC v3; identified AID/APOBEC and dMMR/replication-slippage contributions in multiple cases; PN12 showed kataegis; PN2 (germline biallelic [NTHL1](../genes/NTHL1.md) loss) carried a strong dMMR signature; PN19 (11 months prior platinum) exhibited platinum-therapy signatures [PMID:40328872](../papers/40328872.md).
- Five distinct mutational signatures (S1–S5) identified across 167 nccRCC tumors; pRCC dominated by S1+S3, chRCC and renal oncocytoma by S3+S4; kidney cancer subtypes co-clustered by signature [PMID:25401301](../papers/25401301.md)
- Wellcome Trust Sanger Institute NMF-based mutational-signatures framework applied to 243 [HCC](../cancer_types/HCC.md) exomes, identifying 8 signatures (including novel 23 and 24); signature 24 (C>A-rich) linked to aflatoxin B1 exposure in HBV-positive tumors and validated in 452 ICGC-Japan + 198 TCGA exomes. [PMID:25822088](../papers/25822088.md)
- NMF-based mutational signature analysis (Wellcome Trust Sanger Institute framework, Alexandrov 2013) identified three signatures in Sézary syndrome: CpG deamination/aging (C>T at NpCpG), C>A at CpCpN, and C>T at CpCpN/TpCpN [PMID:26551667](../papers/26551667.md).
- Mutational signature decomposition adapted from Alexandrov et al. (30 COSMIC signatures) applied to 28 uveal melanoma samples; identified BRCA/signature-3 in 79% of samples, with no UV signature (COSMIC 7) detected in any sample [PMID:26683228](../papers/26683228.md).
- nsNMF-derived mutational signature analysis of periampullary tumors identified 5 prominent signatures (out of 21); signature #1 (AC/AT>AN) was independently associated with worse overall survival (multivariate Cox p=0.02) [PMID:26804919](../papers/26804919.md)
- COSMIC mutational signatures SBS7a, SBS7b, SBS7c, SBS7d (UVR-associated) and DBS1 (CC>[TT](../cancer_types/TT.md)) were attributed in NanoSeq data from paired pre/post NB-UVB skin biopsies; post-treatment SBS7 increase in buttock skin was significant (P<0.001, Mann-Whitney U) and correlated tightly with DBS1 increase (Pearson r=0.897). [PMID:26950094](../papers/26950094.md)
- Six mutational signatures extracted by NMF from 1,144 [NSCLC](../cancer_types/NSCLC.md) exomes; smoking signature SI4 separated never- vs ever-smokers well in ADC (AUC=0.87) but poorly in SqCC (AUC=0.62) [PMID:27158780](../papers/27158780.md)
- Mutational signature decomposition applied to 151 advanced head and neck tumors; identified APOBEC, tobacco, and UV-light signatures — UV signature present in 86% of [CSCC](../cancer_types/CSCC.md) cases and associated with markedly higher mutation counts (37.9 vs 4.3, P=.008) [PMID:27442865](../papers/27442865.md)
- COSMIC mutational signature decomposition applied to urothelial carcinoma WES data identified four signatures (APOBEC sigs 2/13, age, smoking, ERCC2-associated); post-chemotherapy tumours were enriched for [APOBEC3A](../genes/APOBEC3A.md) YTCA-context mutations (P=1×10⁻⁵). [PMID:27749842](../papers/27749842.md)
- WTSI/Sanger deconstructSigs framework applied over 13 COSMIC breast-cancer signatures to metastatic breast cancer exomes; APOBEC signatures 2+13 contributed 58.8% of mutations in HR+/HER2− mBC vs 31.9% in primary TCGA samples (p<2e-16) [PMID:28027327](../papers/28027327.md).
- Mutation signatures decomposed against the Alexandrov 30-signature catalog (KL-divergence) in 994 high-TMB cases from MSK-IMPACT, tracking aging, APOBEC, smoking, BRCA1/2, MMR, UV, [POLE](../genes/POLE.md), and TMZ signatures [PMID:28481359](../papers/28481359.md)
- Ten COSMIC mutational signatures identified in 489 CCAs (Signatures 1, 5, 8, 16, 17; APOBEC 2/13; MMR-deficient 6/20; aristolochic acid 22); APOBEC enriched in Fluke-Pos and Signature 1 elevated in CpG-island Cluster 1 [PMID:28667006](../papers/28667006.md)
- 24 mutational signatures detected with ≥5% contribution across 491 medulloblastomas; Signature 3 (BRCA-associated) unexpectedly prevalent in Group 3/4; Signatures 18 and 5 enriched in Group 3 (P=4.7×10⁻⁵) and Group 4 (P=1.0×10⁻¹¹) respectively [PMID:28726821](../papers/28726821.md)
- Five APOBEC-dominated mutational signature clusters (MSig1–MSig4) defined from 412 [BLCA](../cancer_types/BLCA.md) tumors; MSig1 (high-APOBEC, high-burden) had best 5-year survival (75%) while MSig2 (low mutation rate) had the worst (22%) [PMID:28988769](../papers/28988769.md)
- Mutational signatures decomposed using deconstructSigs v1.8.0 against COSMIC in 68 paired melanoma WES samples; COSMIC signature 11 (temozolomide/melanoma-related) was enriched in novel on-therapy mutations in progressive-disease patients [PMID:29033130](../papers/29033130.md)
- COSMIC mutational signatures applied to 206 TCGA sarcomas; 90% of mutations attributed to COSMIC5 (53%) and COSMIC1 (37%); APOBEC signatures elevated in DDLPS and [MPNST](../cancer_types/MPNST.md) (p<10⁻⁶) [PMID:29100075](../papers/29100075.md)
- 30 COSMIC mutational signature processes decomposed from SUMMIT basket-trial tumor sequencing; contributed to TMB and genomic context analysis of ERBB2/ERBB3-mutant solid tumors [PMID:29420467](../papers/29420467.md)
- Applied (29 COSMIC signatures, Alexandrov et al. 2013) to bladder cancer organoid lines; APOBEC signature detected in SCBO-4 and SCBO-5, smoking signature in SCBO-6; signatures were stable across passages and xenograft conversion [PMID:29625057](../papers/29625057.md).
- Mutational signatures analysis performed on pediatric cancer WGS data; signatures used to characterize mutational processes contributing to somatic mutations in pediatric tumors [PMID:29670109](../papers/29670109.md)
- Applied to TCGA pan-cancer cohort to characterize signature patterns across cancer types [PMID:29713003](../papers/29713003.md)
- Mutational signature analysis with deconstructSigs (Alexandrov 2013 signature set) applied to MSI-H and MSS subgroups in [ACC](../cancer_types/ACC.md), [CESC](../cancer_types/CESC.md), and [MESO](../cancer_types/MESO.md); no statistically significant differences found after Benjamini-Hochberg correction due to small MSI-H cohort sizes [PMID:29850653](../papers/29850653.md)
- Mutational-signature decomposition used for hypermutated samples (≥10 SNVs) in 189 advanced endometrial cancer patients; combined with MSIsensor to rescue one occult MMR-D case missed by IHC [PMID:30068706](../papers/30068706.md)
- Non-negative matrix factorization applied against COSMIC signatures across 249 MSS ICB-treated tumors; dominant signature (UV in melanoma, smoking in [NSCLC](../cancer_types/NSCLC.md), APOBEC in bladder/HNSCC) correlated with TMB and ITH; in melanoma TMB was non-predictive of ICB response after adjusting for dominant signature [PMID:30150660](../papers/30150660.md)
- Six mutational signatures identified in 292 prostate cancer WGS genomes: clock-like signatures 1 and 5, DNA-repair signatures 3 (BRCAness) and 6, and APOBEC signatures 2 and 13; APOBEC3B-driven kataegis events co-localize with SV breakpoints including TMPRSS2-ERG fusions [PMID:30537516](../papers/30537516.md)
- Three de novo signatures decomposed via [sigprofiler](../methods/sigprofiler.md) in the pan-Asia cHCC-ICC cohort (133 cases): COSMIC 22 (aristolochic acid, 63.5% prevalence), COSMIC 5 (clock-like), and COSMIC 24 (aflatoxin B1, 38.8%); [TP53](../genes/TP53.md) R249S — an AFB1-induced [HCC](../cancer_types/HCC.md) marker — accounted for 25.8% of [TP53](../genes/TP53.md) mutations [PMID:31130341](../papers/31130341.md)
- In the 923-patient glioma cohort ([glioma_mskcc_2019](../datasets/glioma_mskcc_2019.md)), alkylator-induced hypermutation (signature 11 ≥50%) was identified in 38 tumors; therapy-induced hypermutation was more common in IDH-mutant (29% vs. 12%, P=0.004) and MGMT-methylated (30% vs. 10%, P=0.006) patients [PMID:31263031](../papers/31263031.md)
- Dominant mutational signatures identified by hierarchical clustering of cosine similarity in 37 [UTUC](../cancer_types/UTUC.md) tumors: APOBEC (COSMIC 2, 13), defective MMR (COSMIC 6, C>T at CpG), and an ERCC2-like (COSMIC 5) signature [PMID:31278255](../papers/31278255.md)
- COSMIC mutational signature decomposition (via deconstructSigs, ≥40 SNVs threshold) in synchronous DCIS/IDC-NST: aging signatures 1/5 dominant in 63%/58%, HRD signature 3 in 21%/26%, APOBEC signatures 2/13 in 16%/16% [PMID:32220886](../papers/32220886.md)
- Mutational signature decomposition applied to uterine sarcoma MSK-IMPACT samples with ≥10 SNVs; MMR-D signatures identified in two MSI-H uLMS outliers; aging signatures prevalent in uLMS [PMID:32299819](../papers/32299819.md)
- AID/APOBEC Signatures 2+13 and aging/MMR-D signatures confirmed stable across PDX passages in [UTUC](../cancer_types/UTUC.md) models; Signature 2 lost in UCC30 PDX flagged as engraftment-driven genomic drift [PMID:32332851](../papers/32332851.md)
- Computed for 268 [LUAD](../cancer_types/LUAD.md) tumors (44%) with ≥13.8 mut/Mb; SBS2 (SHR 2.07, p=0.021) and SBS13 (SHR 2.27, p=0.005) associated with increased postresection recurrence risk; APOBEC signatures increased with histologic-subtype invasiveness [PMID:32791233](../papers/32791233.md)
- Five [CSCC](../cancer_types/CSCC.md) ([CSCC](../cancer_types/CSCC.md)) molecular subtypes resolved by mutational-signature analysis of 88 tumors: xeroderma pigmentosum (XP), sporadic, immunosuppressed without [azathioprine](../drugs/azathioprine.md), immunosuppressed on azathioprine (high COSMIC signature 32), and RDEB; XP tumors lacked canonical UV signature 7 due to trinucleotide-context differences [PMID:34272401](../papers/34272401.md)
- Mutational signatures extracted from cf-WES data of 5 high-tumor-fraction cf-IMPACT-negative plasma samples; predominant tumor mutational signatures were recoverable from cfDNA WES at average mVAF 11% [PMID:34059130](../papers/34059130.md)
- Used in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS) for somatic variant calling and genomic analysis of the [lung_nci_2022](../datasets/lung_nci_2022.md) cohort [PMID:34493867](../papers/34493867.md)
- Applied genome-wide in [mixed_kunga_msk_2022](../datasets/mixed_kunga_msk_2022.md) cWGTS pipeline: mutational signature analysis identified signatures inaccessible to panel/exome assays as a key value-add of WGS in 114 pediatric/AYA solid tumor patients [PMID:35585047](../papers/35585047.md)
- Mutational signatures decomposed against COSMIC v2 (30 signatures) in 7,494 sarcomas and aggregated into APOBEC, aging, [BRCA](../cancer_types/BRCA.md), MMR, smoking, UV, [POLE](../genes/POLE.md), and alkylating signature classes (dominance threshold ≥0.4); UV signature dominated cutaneous angiosarcoma and ultra-high-TMB cases [PMID:35705558](../papers/35705558.md)
- COSMIC v3 mutational signature extraction applied to MSK-IMPACT sarcoma samples with ≥15 SNVs from 2,138 tumors spanning 45 histological entities [PMID:35705560](../papers/35705560.md)

## Notes

- COSMIC v3 (signatures SBS1–SBS60+) supersedes v2 (30 signatures); results are version-dependent and not always interchangeable.
- Accurate decomposition requires sufficiently large mutation catalogues; small samples or low-TMB tumors may yield unstable fits.
- dMMR ≠ MSI-High in all non-colorectal contexts (illustrated by PMID:40328872 PN4 — biallelic MSH6/MLH1 loss, predicted MSI-low by MSIsensor despite dMMR signatures).
- Tool variants: SigProfilerExtractor, MutationalPatterns, deconstructSigs, SigMA (for HRD).

## Sources

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25401301](../papers/25401301.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:25822088](../papers/25822088.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26551667](../papers/26551667.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26683228](../papers/26683228.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26804919](../papers/26804919.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:26950094](../papers/26950094.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27442865](../papers/27442865.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:27749842](../papers/27749842.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28027327](../papers/28027327.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28481359](../papers/28481359.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28667006](../papers/28667006.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28726821](../papers/28726821.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:28988769](../papers/28988769.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29100075](../papers/29100075.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29420467](../papers/29420467.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29625057](../papers/29625057.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29670109](../papers/29670109.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29713003](../papers/29713003.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:29850653](../papers/29850653.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30068706](../papers/30068706.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30150660](../papers/30150660.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:30537516](../papers/30537516.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31263031](../papers/31263031.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:31278255](../papers/31278255.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32220886](../papers/32220886.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32299819](../papers/32299819.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32332851](../papers/32332851.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32791233](../papers/32791233.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34272401](../papers/34272401.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34059130](../papers/34059130.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:34493867](../papers/34493867.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35705558](../papers/35705558.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35705560](../papers/35705560.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
