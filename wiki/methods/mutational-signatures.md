---
name: Mutational Signatures Analysis (COSMIC)
slug: mutational-signatures
kind: method
canonical_source: corpus
unverified: true
tags: [mutational-signatures, cosmic, somatic-mutation, snv, indel]
processed_by: wiki-cli
processed_at: 2026-05-15
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
- COSMIC mutational signatures SBS7a, SBS7b, SBS7c, SBS7d (UVR-associated) and DBS1 (CC>TT) were attributed in NanoSeq data from paired pre/post NB-UVB skin biopsies; post-treatment SBS7 increase in buttock skin was significant (P<0.001, Mann-Whitney U) and correlated tightly with DBS1 increase (Pearson r=0.897). [PMID:26950094](../papers/26950094.md)
- Six mutational signatures extracted by NMF from 1,144 NSCLC exomes; smoking signature SI4 separated never- vs ever-smokers well in ADC (AUC=0.87) but poorly in SqCC (AUC=0.62) [PMID:27158780](../papers/27158780.md)
- Mutational signature decomposition applied to 151 advanced head and neck tumors; identified APOBEC, tobacco, and UV-light signatures — UV signature present in 86% of CSCC cases and associated with markedly higher mutation counts (37.9 vs 4.3, P=.008) [PMID:27442865](../papers/27442865.md)
- COSMIC mutational signature decomposition applied to urothelial carcinoma WES data identified four signatures (APOBEC sigs 2/13, age, smoking, ERCC2-associated); post-chemotherapy tumours were enriched for APOBEC3A YTCA-context mutations (P=1×10⁻⁵). [PMID:27749842](../papers/27749842.md)
- WTSI/Sanger deconstructSigs framework applied over 13 COSMIC breast-cancer signatures to metastatic breast cancer exomes; APOBEC signatures 2+13 contributed 58.8% of mutations in HR+/HER2− mBC vs 31.9% in primary TCGA samples (p<2e-16) [PMID:28027327](../papers/28027327.md).
- Mutation signatures decomposed against the Alexandrov 30-signature catalog (KL-divergence) in 994 high-TMB cases from MSK-IMPACT, tracking aging, APOBEC, smoking, BRCA1/2, MMR, UV, POLE, and TMZ signatures [PMID:28481359](../papers/28481359.md)
- Ten COSMIC mutational signatures identified in 489 CCAs (Signatures 1, 5, 8, 16, 17; APOBEC 2/13; MMR-deficient 6/20; aristolochic acid 22); APOBEC enriched in Fluke-Pos and Signature 1 elevated in CpG-island Cluster 1 [PMID:28667006](../papers/28667006.md)
- 24 mutational signatures detected with ≥5% contribution across 491 medulloblastomas; Signature 3 (BRCA-associated) unexpectedly prevalent in Group 3/4; Signatures 18 and 5 enriched in Group 3 (P=4.7×10⁻⁵) and Group 4 (P=1.0×10⁻¹¹) respectively [PMID:28726821](../papers/28726821.md)
- Five APOBEC-dominated mutational signature clusters (MSig1–MSig4) defined from 412 BLCA tumors; MSig1 (high-APOBEC, high-burden) had best 5-year survival (75%) while MSig2 (low mutation rate) had the worst (22%) [PMID:28988769](../papers/28988769.md)
- Mutational signatures decomposed using deconstructSigs v1.8.0 against COSMIC in 68 paired melanoma WES samples; COSMIC signature 11 (temozolomide/melanoma-related) was enriched in novel on-therapy mutations in progressive-disease patients [PMID:29033130](../papers/29033130.md)
- COSMIC mutational signatures applied to 206 TCGA sarcomas; 90% of mutations attributed to COSMIC5 (53%) and COSMIC1 (37%); APOBEC signatures elevated in DDLPS and MPNST (p<10⁻⁶) [PMID:29100075](../papers/29100075.md)
- 30 COSMIC mutational signature processes decomposed from SUMMIT basket-trial tumor sequencing; contributed to TMB and genomic context analysis of ERBB2/ERBB3-mutant solid tumors [PMID:29420467](../papers/29420467.md)

## Notes

- COSMIC v3 (signatures SBS1–SBS60+) supersedes v2 (30 signatures); results are version-dependent and not always interchangeable.
- Accurate decomposition requires sufficiently large mutation catalogues; small samples or low-TMB tumors may yield unstable fits.
- dMMR ≠ MSI-High in all non-colorectal contexts (illustrated by PMID:40328872 PN4 — biallelic MSH6/MLH1 loss, predicted MSI-low by MSIsensor despite dMMR signatures).
- Tool variants: SigProfilerExtractor, MutationalPatterns, deconstructSigs, SigMA (for HRD).

## Sources

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25401301](../papers/25401301.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25822088](../papers/25822088.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26551667](../papers/26551667.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26683228](../papers/26683228.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26804919](../papers/26804919.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:26950094](../papers/26950094.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27442865](../papers/27442865.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27749842](../papers/27749842.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28027327](../papers/28027327.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28481359](../papers/28481359.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28667006](../papers/28667006.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28726821](../papers/28726821.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28988769](../papers/28988769.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29033130](../papers/29033130.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29100075](../papers/29100075.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29420467](../papers/29420467.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
