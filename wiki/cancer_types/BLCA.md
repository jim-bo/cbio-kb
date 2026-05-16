---
name: Bladder Urothelial Carcinoma
oncotree_code: BLCA
main_type: Bladder Cancer
parent: BLADDER
tags: [urothelial, fgfr3]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Bladder Urothelial Carcinoma (BLCA)

## Overview

Urothelial carcinoma arising in the bladder; OncoTree code `BLCA` under the bladder/urinary tract lineage. Spans non-muscle-invasive (NMIBC), muscle-invasive (MIBC), and metastatic disease states with distinct genomic landscapes ([PMID:37682528](../papers/37682528.md)).

## Cohorts in the corpus

- [bladder_msk_2023](../datasets/bladder_msk_2023.md) — 1,421 patients / 1,507 urothelial carcinoma tumors sequenced at MSK, including 504 NMIBC and 526 MIBC bladder specimens alongside upper-tract and metastatic cases ([PMID:37682528](../papers/37682528.md)).

## Recurrent alterations

- [FGFR3](../genes/FGFR3.md) — oncogenic alterations in 39% (199/504) of NMIBC and 14% (75/526) of MIBC bladder tumors; S249C is the dominant hotspot, and R248C is less frequent in bladder (11%, 37/333) than upper-tract disease ([PMID:37682528](../papers/37682528.md)).
- [ERBB2](../genes/ERBB2.md) — co-altered in 11% of FGFR3-altered MIBC (vs 2.5% in NMIBC) ([PMID:37682528](../papers/37682528.md)).
- [TP53](../genes/TP53.md), [RB1](../genes/RB1.md) — inversely associated with [FGFR3](../genes/FGFR3.md) alterations in urothelial carcinoma ([PMID:37682528](../papers/37682528.md)).
- [PIK3CA](../genes/PIK3CA.md), [TSC1](../genes/TSC1.md), [AKT1](../genes/AKT1.md) — PI3K pathway co-alterations in 37% of FGFR2/3-altered tumors ([PMID:37682528](../papers/37682528.md)).
- [CDKN2A](../genes/CDKN2A.md), [CDKN2B](../genes/CDKN2B.md), [KDM6A](../genes/KDM6A.md) — frequently co-altered with [FGFR3](../genes/FGFR3.md) ([PMID:37682528](../papers/37682528.md)).
- Bladder cancer patients harboring [FGFR3](../genes/FGFR3.md) alterations showed differential responses to [erdafitinib](../drugs/erdafitinib.md) in a clinical cohort analysis [PMID:36543146](../papers/36543146.md)
- UC-GENOME study (n=218 metastatic urothelial carcinoma) found Stroma-rich molecular subtype enrichment in metastatic vs non-metastatic disease (Mantel-Haenszel p=1.86e-10), [TP53](../genes/TP53.md) E285K hotspot enrichment (10.8% vs 5.9% in TCGA-BLCA), APOBEC SBS13 low similarity predicting worse outcomes on both chemotherapy (HR 2.50, p=0.013) and ICI (HR 2.19, p=0.011), and a 25-predictor elastic net model achieving AUC=0.84 for ICI response prediction vs TMB alone (AUC=0.68, p=0.038) [PMID:36333289](../papers/36333289.md)
- Integrated genomic analysis of 97 high-grade urothelial tumors found 61% carried a potentially actionable alteration; most prevalent somatic mutations were [TP53](../genes/TP53.md) (34%), [PIK3CA](../genes/PIK3CA.md) (18%), and [FGFR3](../genes/FGFR3.md) (13%); RTK-RAS-RAF and PI3K/AKT/mTOR pathway lesions were largely mutually exclusive; [ERBB2](../genes/ERBB2.md) focally amplified in 6.2% with HER2 overexpression [PMID:23897969](../papers/23897969.md).
- Whole-exome/genome sequencing of 99 Chinese transitional cell carcinoma (TCC) cases identified 37 significantly mutated genes including novel driver [STAG2](../genes/STAG2.md) (16% combined mutation/deletion frequency); 32% of tumors harbored alterations in sister chromatid cohesion and segregation genes; [STAG2](../genes/STAG2.md) alterations associated with significantly worse survival and higher aneuploidy; recurrent FGFR3-TACC3 fusion detected in 5% by RNA-seq [PMID:24121792](../papers/24121792.md).
- TCGA multi-platform analysis of 131 muscle-invasive urothelial carcinomas identified 32 significantly mutated genes, chromatin-regulator mutations in 76% of tumors (highest frequency among TCGA epithelial cancers), [APOBEC3B](../genes/APOBEC3B.md) as a dominant mutagen (51% of mutations), and potential therapeutic targets in 69% of cases — including [FGFR3](../genes/FGFR3.md)–[TACC3](../genes/TACC3.md) fusions, [ERBB2](../genes/ERBB2.md) alterations (9%), and PI3K/mTOR pathway activation (42%) [PMID:24476821](../papers/24476821.md).
- [SMARCA4](../genes/SMARCA4.md) inactivating mutations occur in 5–8% of bladder carcinoma (TCGA data) [PMID:24658004](../papers/24658004.md)
- MSK-IMPACT targeted sequencing of 109 high-grade urothelial carcinomas: [PIK3CA](../genes/PIK3CA.md) mutations (21%) associated with improved RFS/CSS post-cystectomy (HR 0.35, P=0.014); [CDKN2A](../genes/CDKN2A.md) alterations independently predict worse outcomes (RFS HR 5.76, P<0.001); [TP53](../genes/TP53.md) mutation (57%) not prognostic after stage adjustment; chromatin-modifying genes mutated in 83% but not prognostic [PMID:25092538](../papers/25092538.md)
- Whole-exome sequencing of 50 muscle-invasive urothelial carcinoma patients (25 [cisplatin](../drugs/cisplatin.md) responders vs 25 non-responders) identified somatic [ERCC2](../genes/ERCC2.md) mutations exclusively in responders (9/25, 36%; q=0.007), proposing [ERCC2](../genes/ERCC2.md) as a predictive biomarker for neoadjuvant cisplatin-based chemotherapy response. [PMID:25096233](../papers/25096233.md)
- [UTUC](../cancer_types/UTUC.md) and BLCA share recurrent [FGFR3](../genes/FGFR3.md) alterations; targeted sequencing of upper-tract urothelial carcinoma cohort identified [FGFR3](../genes/FGFR3.md) mutations in a subset with bladder cancer comparisons [PMID:26278805](../papers/26278805.md)
- Plasmacytoid-variant bladder cancer (SRCBC) arises within the context of urothelial carcinoma; [CDH1](../genes/CDH1.md) truncating mutations are pathognomonic for the plasmacytoid subtype (84% frequency, vs 0% in 127 TCGA urothelial NOS tumors), and E-cadherin loss is universal; co-mutation profile otherwise overlaps with conventional urothelial carcinoma ([TP53](../genes/TP53.md), [RB1](../genes/RB1.md), [ERBB2](../genes/ERBB2.md), [PIK3CA](../genes/PIK3CA.md)) [PMID:26901067](../papers/26901067.md)
- WES of 72 urothelial tumors from 32 patients (16 matched pre/post-chemotherapy sets + 2 rapid autopsies) at Weill Cornell showed only 28.4% of mutations shared between matched pre- and post-chemotherapy samples; post-chemotherapy tumors showed clonal enrichment of L1CAM/integrin-signaling pathway mutations and dominant APOBEC3A mutagenesis, supporting repeat biopsy and L1CAM/FAK inhibition as candidate strategies in chemotherapy-resistant BLCA [PMID:27749842](../papers/27749842.md).
- Single case of EWSR1::BEND2 fusion sarcoma (small round cell) of the urinary bladder; initial misdiagnosis as Ewing sarcoma (CD99+, EWSR1 FISH+) corrected by RNA-seq revealing EWSR1 exon 10::BEND2 exon 2 in-frame fusion; [PTEN](../genes/PTEN.md) loss co-occurring on 10q deletion [PMID:28199314](../papers/28199314.md)
- In the MSK-IMPACT pan-cancer cohort, BLCA had the highest TERT promoter mutation rate of any principal tumor type at 70%; MSI BLCA patients showed responses to immune checkpoint blockade; BLCA was included among 62 principal tumor types in msk_impact_2017. [PMID:28481359](../papers/28481359.md)
- MSK-IMPACT targeted sequencing of 105 nonmuscle invasive bladder cancer (NMIBC) tumors (blca_nmibc_2017) found TERT promoter mutations in 73% across all grade/stage groups; chromatin-modifying gene alterations in 69% (KDM6A 38%, ARID1A 21%); ERBB2 and FGFR3 alterations in 57% of high-grade NMIBC in a mutually exclusive pattern; DDR gene alterations in 30% of high-grade NMIBC; ARID1A mutations associated with 3.14-fold higher BCG-recurrence risk (HR=3.14, 95% CI 1.51-6.51, P=0.002). [PMID:28583311](../papers/28583311.md)
- TCGA expanded comprehensive molecular characterization of 412 chemotherapy-naive muscle-invasive bladder cancers integrating WES, RNA-seq, miRNA-seq, DNA methylation, SNP6, and RPPA; defined five mRNA subtypes (luminal-papillary, luminal-infiltrated, luminal, basal-squamous, neuronal), identified 58 SMGs, and linked APOBEC-dominated mutagenesis (67% of SNVs) paradoxically to best survival [PMID:28988769](../papers/28988769.md)
- In the SUMMIT basket trial (n=16 bladder), HER2-mutant bladder urothelial carcinoma showed no RECIST responses to neratinib despite S310 hotspot predominance, demonstrating lineage-based intrinsic resistance to single-agent pan-HER kinase inhibition [PMID:29420467](../papers/29420467.md)
- MC3 pan-cancer mutation-calling project (10,510 TCGA pairs) included BLCA; BLCA concordance with the legacy PanCan12 MAF exceeded 90% [PMID:29596782](../papers/29596782.md)
- Pan-cancer fusion study (9,624 TCGA samples) identified FGFR3–TACC3 in 2.0% of BLCA samples as a top recurrent intra-cancer fusion; FGFR3 was annotated as a druggable target in BLCA across 15 cancer types [PMID:29617662](../papers/29617662.md)
- Pan-cancer aneuploidy study (10,522 TCGA tumors) included BLCA in the pan-cancer cohort; BLCA was not highlighted as an outlier for aneuploidy score [PMID:29622463](../papers/29622463.md)
- Included in TCGA PanCancer Atlas integrative molecular analysis (9,759 tumors, 33 cancer types); BLCA showed substantial molecular heterogeneity with <50% of samples in any single iCluster and appeared in C27 (pan-squamous, HPV+) [PMID:29625048](../papers/29625048.md)
- Included in TCGA PanCancer Atlas integrative driver/immune analysis (11,000 tumors, 33 cancer types); Notch pathway deregulation highlighted as a tumor-type-anchored druggable axis in BLCA [PMID:29625049](../papers/29625049.md)
- Included in pan-cancer pathway analysis of 9,125 TCGA tumors; ERBB2 alterations reported in BLCA; NRF2/oxidative-stress pathway alteration noted [PMID:29625050](../papers/29625050.md)
- Included in TCGA Pan-Cancer Clinical Data Resource (11,160 patients, 33 cancer types); all four endpoints (OS, PFI, DFI, DSS) recommended without reservation for BLCA [PMID:29625055](../papers/29625055.md)
- 17 of 18 patients in this bladder cancer organoid biobank had urothelial carcinoma (BLCA); organoids recapitulate FGFR3 (60%), epigenetic regulator (73%), and TP53 (33%) mutation rates from the TCGA BLCA landscape; drug responses to trametinib and gemcitabine validated in orthotopic xenografts [PMID:29625057](../papers/29625057.md)

## Subtypes

- NMIBC vs MIBC disease states show markedly different [FGFR3](../genes/FGFR3.md) alteration frequencies (39% vs 14%), supporting distinct molecular biology ([PMID:37682528](../papers/37682528.md)).
- FGFR3-fusion tumors carry lower TMB than FGFR3-mutant tumors (median 5 vs 9 mut/Mb, p=0.0006) ([PMID:37682528](../papers/37682528.md)).

## Therapeutic landscape

- [erdafitinib](../drugs/erdafitinib.md) — real-world ORR 40%, median PFS 2.8 months, [OS](../cancer_types/OS.md) 6.6 months in 32 metastatic FGFR3-altered urothelial carcinoma patients; tolerability-limited with 38% dose reductions ([PMID:37682528](../papers/37682528.md)).
- Immune checkpoint blockade outcomes did not differ by [FGFR3](../genes/FGFR3.md) status (n=26 altered vs 155 wildtype) ([PMID:37682528](../papers/37682528.md)).
- [BRAF](../genes/BRAF.md) fusions were identified as acquired resistance mechanisms to [EGFR](../genes/EGFR.md) TKIs in BLCA patients [PMID:38922339](../papers/38922339.md).
- ctDNA detection (MSK-ACCESS) was associated with higher VTE risk in BLCA patients, though the association was not significant for BLCA specifically [PMID:39147831](../papers/39147831.md).
- [enfortumab-vedotin](../drugs/enfortumab-vedotin.md) and next-generation FGFR3-selective inhibitors (e.g., TYRA300, LOXO435) cited as alternative options given [erdafitinib](../drugs/erdafitinib.md)'s modest durability ([PMID:37682528](../papers/37682528.md)).
- ROBIN GenRad center (U54 CA274513; Cleveland Clinic and Emory University) RAD-SG trial (NCT05833867) evaluates RT + [sacituzumab-govitecan](../drugs/sacituzumab-govitecan.md) for bladder preservation in locally advanced muscle-invasive BLCA (MIBC); preliminary results show feasibility with only grade-1 toxicities. Flow cytometry-based immune profiling demonstrates extensive myeloid-lineage accumulation during RT+ADC treatment, with distinct profiles from ICI-treated patients. Comprehensive genomics, serum proteomics, imaging, and ctDNA analyses are underway. [PMID:41941260](../papers/41941260.md)

## Sources

- [PMID:37682528](../papers/37682528.md) — Guercio et al., Clinical Cancer Research 2023.
- [PMID:38922339](../papers/38922339.md)
- [PMID:39147831](../papers/39147831.md)
- [PMID:41941260](../papers/41941260.md)

- [PMID:36543146](../papers/36543146.md)
- [PMID:36333289](../papers/36333289.md)
- [PMID:23897969](../papers/23897969.md)
- [PMID:24121792](../papers/24121792.md)
- [PMID:24476821](../papers/24476821.md)

- [PMID:24658004](../papers/24658004.md)
- [PMID:25092538](../papers/25092538.md)
- [PMID:25096233](../papers/25096233.md)
- [PMID:26278805](../papers/26278805.md)
- [PMID:26901067](../papers/26901067.md) — Al-Ahmadie et al., plasmacytoid-variant bladder cancer WES; CDH1 truncating mutations pathognomonic for the SRCBC subtype

- [PMID:27749842](../papers/27749842.md)
- [PMID:28199314](../papers/28199314.md) — Halava et al. 2025; EWSR1::BEND2 fusion sarcoma of the urinary bladder initially misdiagnosed as Ewing sarcoma.

- [PMID:28481359](../papers/28481359.md)
- [PMID:28583311](../papers/28583311.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28988769](../papers/28988769.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29420467](../papers/29420467.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29596782](../papers/29596782.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29617662](../papers/29617662.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29622463](../papers/29622463.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29625048](../papers/29625048.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625049](../papers/29625049.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625050](../papers/29625050.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625055](../papers/29625055.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:29625057](../papers/29625057.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
