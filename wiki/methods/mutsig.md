---
name: MutSig
slug: mutsig
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [statistical-method, somatic-mutation, cancer-genomics, significance-testing]
processed_by: wiki-cli
processed_at: 2026-05-14
---

# MutSig

## Overview

MutSig (Mutation Significance) is a statistical algorithm developed at the Broad Institute to identify genes mutated at rates significantly above the background mutation rate in cancer. It accounts for context-specific mutation rates (nucleotide context, gene expression, replication timing) and gene-specific variability to compute q-values for each gene. MutSig is widely used in WES-based cancer genome studies to distinguish driver genes from passenger mutations.

## Used by

- Applied to 55 DLBCL WES samples in the [dlbc_broad_2012](../datasets/dlbc_broad_2012.md) cohort; identified 58 significantly mutated genes at FDR q <= 0.1, with a 97.9% validation rate by targeted resequencing [PMID:22343534](../papers/22343534.md).
- MutSig applied to identify statistically significant driver genes ([SPOP](../genes/SPOP.md), [FOXA1](../genes/FOXA1.md), [MED12](../genes/MED12.md)) in 112 prostate adenocarcinoma WES samples [PMID:22610119](../papers/22610119.md)
- Applied to 103 breast cancer tumor WES data (Broad cohort, [brca_broad](../datasets/brca_broad.md)) to identify significantly mutated genes including [PIK3CA](../genes/PIK3CA.md), [TP53](../genes/TP53.md), and [AKT1](../genes/AKT1.md) [PMID:22722202](../papers/22722202.md)
- MutSig applied to somatic mutation data from 224 TCGA colorectal carcinoma exomes to identify 24 significantly mutated genes including novel candidates [ARID1A](../genes/ARID1A.md), [SOX9](../genes/SOX9.md), [AMER1](../genes/AMER1.md) [PMID:22810696](../papers/22810696.md)
- InVEx permutation framework (related to MutSig) applied to 121 melanoma exomes; leverages intronic mutation rates to control for high UV-induced mutation background; identified 11 significantly mutated genes [PMID:22817889](../papers/22817889.md)
- MutSig applied to 92 medulloblastoma exomes (Broad) to identify 12 significantly mutated genes (q<0.1) including novel candidates [DDX3X](../genes/DDX3X.md), [GPS2](../genes/GPS2.md), [BCOR](../genes/BCOR.md), [LDB1](../genes/LDB1.md) [PMID:22820256](../papers/22820256.md)
- Applied to TCGA [LUSC](../cancer_types/LUSC.md) cohort (178 tumors) to identify significantly mutated genes including [CDKN2A](../genes/CDKN2A.md), [TP53](../genes/TP53.md), [KEAP1](../genes/KEAP1.md), [NFE2L2](../genes/NFE2L2.md), and MLL2 [PMID:22960745](../papers/22960745.md)
- Applied to Broad [LUAD](../cancer_types/LUAD.md) cohort (183 tumors) to identify significantly mutated genes; nominated [RBM10](../genes/RBM10.md), [U2AF1](../genes/U2AF1.md), and [ARID1A](../genes/ARID1A.md) as novel drivers alongside [EGFR](../genes/EGFR.md), [KRAS](../genes/KRAS.md), and [STK11](../genes/STK11.md) [PMID:22980975](../papers/22980975.md)
- MutSig applied to neuroblastoma WES data to identify significantly mutated genes; [ALK](../genes/ALK.md), [PTPN11](../genes/PTPN11.md), and [ATRX](../genes/ATRX.md) passed significance thresholds [PMID:23334666](../papers/23334666.md)
- MutSig analysis of 160 CLL exomes identified [SF3B1](../genes/SF3B1.md), [NOTCH1](../genes/NOTCH1.md), [DDX3X](../genes/DDX3X.md), and [POT1](../genes/POT1.md) as significantly mutated genes beyond background rates [PMID:23415222](../papers/23415222.md)
- MutSig significance algorithm identified 26 significantly mutated genes (FDR q<0.1) in 145 esophageal adenocarcinomas, including [TP53](../genes/TP53.md), [CDKN2A](../genes/CDKN2A.md), [SMAD4](../genes/SMAD4.md), [PIK3CA](../genes/PIK3CA.md), and novel candidates [ELMO1](../genes/ELMO1.md), [DOCK2](../genes/DOCK2.md), and [SPART](../genes/SPART.md) [PMID:23525077](../papers/23525077.md)
- Used together with InVEx to identify 71 significantly mutated genes in 291 [GBM](../cancer_types/GBM.md) exomes, including known drivers ([PTEN](../genes/PTEN.md), [TP53](../genes/TP53.md), [EGFR](../genes/EGFR.md), [PIK3CA](../genes/PIK3CA.md), [NF1](../genes/NF1.md)) and novel [LZTR1](../genes/LZTR1.md) [PMID:24120142](../papers/24120142.md)
- MutSigCV applied to 177 WES + 26 WGS multiple myeloma samples; identified 11 significantly mutated genes at q<0.1 including [KRAS](../genes/KRAS.md), [NRAS](../genes/NRAS.md), [BRAF](../genes/BRAF.md), FAM46C/TENT5C, [TP53](../genes/TP53.md), [DIS3](../genes/DIS3.md), [TRAF3](../genes/TRAF3.md), [CYLD](../genes/CYLD.md), [RB1](../genes/RB1.md), [PRDM1](../genes/PRDM1.md), and [IRF4](../genes/IRF4.md) [PMID:24434212](../papers/24434212.md)
- Applied to the Illumina WES arm of 147 rhabdomyosarcoma tumor/normal pairs; identified significantly mutated genes including [HRAS](../genes/HRAS.md), [KRAS](../genes/KRAS.md), [NRAS](../genes/NRAS.md), [FGFR4](../genes/FGFR4.md), [PIK3CA](../genes/PIK3CA.md), [NF1](../genes/NF1.md), [FBXW7](../genes/FBXW7.md), and [BCOR](../genes/BCOR.md); combined with GATK UnifiedGenotyper for the SOLiD arm [PMID:24436047](../papers/24436047.md)
- MutSig 1.5 applied to TCGA bladder carcinoma WES data (n=130); identified 32 significantly mutated genes at FDR<0.1, including 9 not previously reported as significantly mutated in any cancer ([CDKN1A](../genes/CDKN1A.md), [ERCC2](../genes/ERCC2.md), [RXRA](../genes/RXRA.md), [ELF3](../genes/ELF3.md), [KLF5](../genes/KLF5.md), [FOXQ1](../genes/FOXQ1.md), [RHOB](../genes/RHOB.md), [PAIP1](../genes/PAIP1.md), [BTG2](../genes/BTG2.md)) [PMID:24476821](../papers/24476821.md)
- MutSigCV applied to [ESCC](../cancer_types/ESCC.md) cohort (139 paired tumor/normal samples) to identify 13 significantly mutated genes at FDR q < 0.2, including novel drivers [FAT1](../genes/FAT1.md), [FAT2](../genes/FAT2.md), [ZNF750](../genes/ZNF750.md), and [KMT2D](../genes/KMT2D.md) [PMID:24686850](../papers/24686850.md)
- MutSigCV applied to 215 non-hypermutated gastric adenocarcinomas ([stad_tcga_pub](../datasets/stad_tcga_pub.md)) identified 25 significantly mutated genes including [TP53](../genes/TP53.md), [ARID1A](../genes/ARID1A.md), [KRAS](../genes/KRAS.md), [PIK3CA](../genes/PIK3CA.md), [RNF43](../genes/RNF43.md), [APC](../genes/APC.md), [CTNNB1](../genes/CTNNB1.md), [SMAD4](../genes/SMAD4.md); expanded analysis including indels added [RNF43](../genes/RNF43.md), [B2M](../genes/B2M.md), [NF1](../genes/NF1.md) [PMID:25079317](../papers/25079317.md)
- MutSig2CV applied to 412 lung adenocarcinomas ([luad_tcga_pub](../datasets/luad_tcga_pub.md), 230 TCGA + 182 published) identified 18 significantly mutated genes; newly identified [RIT1](../genes/RIT1.md) activating mutations and [MGA](../genes/MGA.md) loss-of-function (mutually exclusive with [MYC](../genes/MYC.md) amplification) [PMID:25079552](../papers/25079552.md)
- MutSigCV applied to 50 muscle-invasive urothelial carcinoma tumors; identified [ERCC2](../genes/ERCC2.md), [TP53](../genes/TP53.md), [RB1](../genes/RB1.md), [KDM6A](../genes/KDM6A.md), and [ARID1A](../genes/ARID1A.md) as significantly mutated genes. [PMID:25096233](../papers/25096233.md)
- Used in the TCGA ChRCC study to identify significantly mutated genes in 66 tumors; nominated [TP53](../genes/TP53.md) (32%) and [PTEN](../genes/PTEN.md) (9%) as the only statistically significant drivers. [PMID:25155756](../papers/25155756.md)
- MutSig CV v1.4 applied to aggressive cSCC WES (39 tumors) despite extreme UV-driven mutation burden (median 61.2 mutations/Mb); identified 11 significant driver genes at q<0.1, including [TP53](../genes/TP53.md), [CDKN2A](../genes/CDKN2A.md), [NOTCH1](../genes/NOTCH1.md), [NOTCH2](../genes/NOTCH2.md), [AJUBA](../genes/AJUBA.md), [HRAS](../genes/HRAS.md), [CASP8](../genes/CASP8.md) [PMID:25303977](../papers/25303977.md)
- Identified 7 significantly mutated genes (q<0.1) in 402 papillary thyroid carcinomas: [BRAF](../genes/BRAF.md), [NRAS](../genes/NRAS.md), [HRAS](../genes/HRAS.md), [KRAS](../genes/KRAS.md), [EIF1AX](../genes/EIF1AX.md), [PPM1D](../genes/PPM1D.md), [CHEK2](../genes/CHEK2.md); [EIF1AX](../genes/EIF1AX.md) was a novel PTC driver (q=5.3×10⁻⁸) [PMID:25417114](../papers/25417114.md)
- MutSigCV identified 16 significantly mutated genes (q<0.2) in 78 gastric adenocarcinomas, including [TP53](../genes/TP53.md), [ARID1A](../genes/ARID1A.md), [CDH1](../genes/CDH1.md), [APC](../genes/APC.md), [RHOA](../genes/RHOA.md), [PIK3CA](../genes/PIK3CA.md), [SMAD4](../genes/SMAD4.md), [MYC](../genes/MYC.md), and [KRAS](../genes/KRAS.md); 13 were mutated in ≥5% of tumors [PMID:25583476](../papers/25583476.md)
- Applied (versions 1.5, 2.0, and CV; most significant of three taken) to identify recurrently mutated genes in 29 metastatic cSCC tumors from [DFCI-ONCOPANEL-1](../methods/DFCI-ONCOPANEL-1.md) sequencing; identified [TP53](../genes/TP53.md) (79%), [CDKN2A](../genes/CDKN2A.md) (48%), NOTCH1/2/4, and chromatin-remodeling genes as significantly mutated [PMID:25589618](../papers/25589618.md)
- MutSigCV applied to TCGA [HNSC](../cancer_types/HNSC.md) WES data (n=279); identified 11 significantly mutated genes at q<0.1 including [TP53](../genes/TP53.md), [CDKN2A](../genes/CDKN2A.md), [FAT1](../genes/FAT1.md), [PIK3CA](../genes/PIK3CA.md), [NOTCH1](../genes/NOTCH1.md), [KMT2D](../genes/KMT2D.md), [NSD1](../genes/NSD1.md), [CASP8](../genes/CASP8.md), [AJUBA](../genes/AJUBA.md), [NFE2L2](../genes/NFE2L2.md), and [HLA-A](../genes/HLA-A.md); additional trend-significant genes at q<1 [PMID:25631445](../papers/25631445.md)
- MutSigCV used to identify 14 significantly mutated genes (q < 0.05) in 243 [HCC](../cancer_types/HCC.md) exomes including [TP53](../genes/TP53.md), [CTNNB1](../genes/CTNNB1.md), [AXIN1](../genes/AXIN1.md), and TERT-pathway genes. [PMID:25822088](../papers/25822088.md)
- MutSigCV applied to 109 microdissected PDA exomes identifying 24 significantly mutated genes at ≥3.5% frequency; meta-analysis with 99-case ICGC cohort (208-case total) added [ATM](../genes/ATM.md), [ARID2](../genes/ARID2.md), [TGFBR2](../genes/TGFBR2.md), [ACVR1B](../genes/ACVR1B.md). [PMID:25855536](../papers/25855536.md)
- MutSig used to assess recurrence of somatic mutations in 150 mCRPC cases, identifying TP53 as most selectively enriched versus primary prostate cancer (q<0.001). [PMID:26000489](../papers/26000489.md)
- MutSig (Q < 0.1) and InVEx (Bonferroni p < 0.05) together called 42 and 13 significantly mutated genes respectively in 318 melanoma WES cases, including novel SMGs [RAC1](../genes/RAC1.md), [DDX3X](../genes/DDX3X.md), [MRPS31](../genes/MRPS31.md), and [RPS27](../genes/RPS27.md). [PMID:26091043](../papers/26091043.md)
- Applied to the TCGA breast ILC/IDC cohort (n=817) for significantly mutated gene discovery; identified ILC-enriched drivers [CDH1](../genes/CDH1.md), [TBX3](../genes/TBX3.md), [RUNX1](../genes/RUNX1.md), [PIK3CA](../genes/PIK3CA.md), and [FOXA1](../genes/FOXA1.md), plus IDC-enriched TP53 and [MYC](../genes/MYC.md) amplification [PMID:26451490](../papers/26451490.md)
- Used to identify 44 recurrently mutated genes across 538 CLL whole-exomes (CLL8 trial), achieving 94%/61% power at 3%/2% mutation frequency; discovered novel drivers [RPS15](../genes/RPS15.md), [IKZF3](../genes/IKZF3.md), [MGA](../genes/MGA.md), [BRAF](../genes/BRAF.md) (non-V600E), and [MAP2K1](../genes/MAP2K1.md) [PMID:26466571](../papers/26466571.md)
- Applied as MutSigCV to identify 13 significantly mutated genes (q < 0.1) in 333 primary prostate adenocarcinomas including [SPOP](../genes/SPOP.md), TP53, [FOXA1](../genes/FOXA1.md), [PTEN](../genes/PTEN.md), [MED12](../genes/MED12.md), [CDKN1B](../genes/CDKN1B.md), and newly identified [BRAF](../genes/BRAF.md), [HRAS](../genes/HRAS.md), [AKT1](../genes/AKT1.md), [CTNNB1](../genes/CTNNB1.md), [ATM](../genes/ATM.md), [ZMYM3](../genes/ZMYM3.md), [NKX3-1](../genes/NKX3-1.md) [PMID:26544944](../papers/26544944.md).
- MutSig-CV identified 19 significantly mutated genes in periampullary tumors (ampullary, distal bile-duct, duodenal adenocarcinoma), plus 3 additional genes (PBRM1, RECQL4, KDM6A) by inactivation-bias test; MSI cases excluded [PMID:26804919](../papers/26804919.md)
- MutSigCV identified 75 significantly mutated genes in 1,122 diffuse gliomas, 45 of which were novel glioma associations; applied within the TCGA pan-glioma study [PMID:26824661](../papers/26824661.md)
- Used to identify significantly mutated genes in 114 metastatic CRPC biopsies; confirmed TP53 and RB1 as top altered genes differentiating CRPC-NE from CRPC-Adeno [PMID:26855148](../papers/26855148.md)
- MutSigCV applied to 488 non-hypermutated CRCs, identifying 90 significantly mutated genes (73 novel for CRC); hypermutator threshold = 12 mutations/Mb [PMID:27149842](../papers/27149842.md)
- MutSig2CV applied to 660 lung ADC and 484 lung SqCC exomes; identified 38 SMGs in ADC and 20 in SqCC (q < 0.1); 14 additional SMGs in the pan-lung joint analysis [PMID:27158780](../papers/27158780.md)

## Notes

- MutSig relies on a background mutation model; covariates include expression levels, replication timing, and trinucleotide context.
- At a q <= 0.1 threshold in the DLBCL study, confirmed known drivers ([MYD88](../genes/MYD88.md), [CARD11](../genes/CARD11.md), [EZH2](../genes/EZH2.md), [CREBBP](../genes/CREBBP.md), [CD79B](../genes/CD79B.md), [TP53](../genes/TP53.md)) and identified novel candidates ([MEF2B](../genes/MEF2B.md), [KMT2D](../genes/KMT2D.md), [BTG1](../genes/BTG1.md), [GNA13](../genes/GNA13.md), [ACTB](../genes/ACTB.md), [P2RY8](../genes/P2RY8.md), [TNFRSF14](../genes/TNFRSF14.md)) [PMID:22343534](../papers/22343534.md).
- A complementary rare-driver analysis using mutational clustering and evolutionary conservation identified [KRAS](../genes/KRAS.md), [BRAF](../genes/BRAF.md), [NOTCH1](../genes/NOTCH1.md), and [SYK](../genes/SYK.md) as likely drivers not captured by MutSig alone [PMID:22343534](../papers/22343534.md).
- Not a sequencing panel; lacks a cBioPortal genePanelId.

## Sources

- [PMID:22343534](../papers/22343534.md) — DLBCL WES study where MutSig identified 58 significantly mutated genes.

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22610119](../papers/22610119.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22722202](../papers/22722202.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22810696](../papers/22810696.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22817889](../papers/22817889.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22820256](../papers/22820256.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22960745](../papers/22960745.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:22980975](../papers/22980975.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23334666](../papers/23334666.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23415222](../papers/23415222.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23525077](../papers/23525077.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24120142](../papers/24120142.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24434212](../papers/24434212.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24436047](../papers/24436047.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24476821](../papers/24476821.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24686850](../papers/24686850.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25079317](../papers/25079317.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25079552](../papers/25079552.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25096233](../papers/25096233.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25155756](../papers/25155756.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25303977](../papers/25303977.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25417114](../papers/25417114.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583476](../papers/25583476.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25589618](../papers/25589618.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25631445](../papers/25631445.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25822088](../papers/25822088.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25855536](../papers/25855536.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26000489](../papers/26000489.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26091043](../papers/26091043.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26451490](../papers/26451490.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26466571](../papers/26466571.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26544944](../papers/26544944.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:26804919](../papers/26804919.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26824661](../papers/26824661.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:26855148](../papers/26855148.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:27149842](../papers/27149842.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
