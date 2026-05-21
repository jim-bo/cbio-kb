---
name: Endometrial Carcinoma
oncotree_code: UCEC
main_type: Endometrial Cancer
parent: UTERUS
tags: []
processed_by: crosslinker
processed_at: 2026-05-21
---

# Endometrial Carcinoma (UCEC)

## Overview

Endometrial carcinoma (UCEC) is the most common gynecologic malignancy in the United States. On OncoTree it is a child of UTERUS and the parent for uterine serous carcinoma ([USC](../cancer_types/USC.md)), uterine carcinosarcoma ([UCS](../cancer_types/UCS.md)), and other subtypes. TCGA molecular subtypes — POLE-mutant, MSI-H/dMMR, CN-high/TP53abn, and CN-low/NSMP — have prognostic and therapeutic relevance.

## Cohorts in the corpus

- 1,882 prospectively sequenced endometrial carcinoma patients (259 self-identified Black, 1,623 White) at MSK (1/2014--12/2021) using MSK-IMPACT (341--505 gene panel). Dataset: [ucec_ancestry_cds_msk_2023](../datasets/ucec_ancestry_cds_msk_2023.md). [PMID:37651310](../papers/37651310.md)
- 35 patients with recurrent/advanced dMMR/MSI-H or hypermutated endometrial or ovarian cancers enrolled in phase 2 [nivolumab](../drugs/nivolumab.md) trial (NCT03241745). 83% endometrioid histology. Dataset: [ucec_msk_2024](../datasets/ucec_msk_2024.md). [PMID:38653864](../papers/38653864.md)

## Recurrent alterations

- [TP53](../genes/TP53.md) — mutations in 72% of Black vs. 42% of White patients (q<0.001); defines the CN-H/TP53abn molecular subtype. [PMID:37651310](../papers/37651310.md)
- [PTEN](../genes/PTEN.md) — mutations in 26% Black vs. 55% White (q<0.001); associated with endometrioid histology. Mutated in 76% of dMMR/MSI-H cohort. [PMID:37651310](../papers/37651310.md) [PMID:38653864](../papers/38653864.md)
- [PIK3CA](../genes/PIK3CA.md) — mutations in 38% Black vs. 46% White (similar frequency, different mechanism); mutated in 48% of dMMR/MSI-H cohort. [PMID:37651310](../papers/37651310.md) [PMID:38653864](../papers/38653864.md)
- [CCNE1](../genes/CCNE1.md) — amplification enriched in Black patients (15% vs. 4%, q<0.001) and in carcinosarcomas (29% vs. 10%). [PMID:37651310](../papers/37651310.md)
- [ERBB2](../genes/ERBB2.md) — amplification enriched in Black patients (12% vs. 3%, q<0.001); therapeutic target for [trastuzumab](../drugs/trastuzumab.md) and T-DXd. [PMID:37651310](../papers/37651310.md)
- [ARID1A](../genes/ARID1A.md) — mutations less frequent in Black patients (19% vs. 47%); mutated in 82% of dMMR/MSI-H cohort. [PMID:37651310](../papers/37651310.md) [PMID:38653864](../papers/38653864.md)
- [MLH1](../genes/MLH1.md) — promoter hypermethylation in 66% of dMMR/MSI-H cohort; somatic/germline mutations in 30%. [PMID:38653864](../papers/38653864.md)
- [SETD1B](../genes/SETD1B.md) — mutations in 58% of [nivolumab](../drugs/nivolumab.md) responders vs. 14% non-responders (P=0.015). [PMID:38653864](../papers/38653864.md)
- [MEGF8](../genes/MEGF8.md) — mutations in 32% of [nivolumab](../drugs/nivolumab.md) responders vs. 0% non-responders (P=0.027). [PMID:38653864](../papers/38653864.md)
- [POLE](../genes/POLE.md) — exonuclease domain mutations rare in Black patients (1.2% vs. 5.8%); favorable prognosis subtype. [PMID:37651310](../papers/37651310.md)
- [KMT2B](../genes/KMT2B.md) — mutations enriched in CN-H/TP53abn ECs (16% vs. 8%) and carcinosarcomas (31% vs. 10%) from Black patients. [PMID:37651310](../papers/37651310.md)
- TCGA integrated analysis of 373 endometrial carcinomas (307 endometrioid, 53 serous, 13 mixed) proposed four molecular subgroups: [POLE](../genes/POLE.md) ultramutated (~7%, improved PFS), MSI hypermutated (~28%), copy-number low (CTNNB1-high), and copy-number high/serous-like ([TP53](../genes/TP53.md) ~90%, worse PFS); 93% of endometrioid tumors had PI3K/AKT alterations [PMID:23636398](../papers/23636398.md)
- Endometrial polyps harbour low-VAF hotspot mutations in canonical UCEC driver genes ([KRAS](../genes/KRAS.md) 26%, [PIK3CA](../genes/PIK3CA.md), [PIK3R1](../genes/PIK3R1.md), [PTEN](../genes/PTEN.md), [ERBB2](../genes/ERBB2.md), [FBXW7](../genes/FBXW7.md)); KEGG pathway analysis flags 'endometrial cancer' as top enriched pathway (FDR p=2.8×10⁻⁵), supporting polyps as potential UCEC precursor lesions [PMID:28445112](../papers/28445112.md)
- In the MSK-IMPACT pan-cancer cohort, [ESR1](../genes/ESR1.md) hotspot mutations were found in UCEC almost exclusively in post-hormone-therapy metastatic tumors; MSI UCEC patients showed responses to immune checkpoint blockade; [POLE](../genes/POLE.md) and MMR mutation signatures were enriched in endometrial lineages. [PMID:28481359](../papers/28481359.md)
- Whole-exome sequencing of 63 clear cell endometrial carcinomas ([UCCC](../cancer_types/UCCC.md)) in the [uccc_nih_2017](../datasets/uccc_nih_2017.md) cohort revealed molecular heterogeneity: 27% serous-like (TP53/PPP2R1A), 20.6% endometrioid-like, 19.1% mixed, and 33.3% with no detectable alteration across the 7-gene + MSI panel; MSI was present in 11.3%; the molecular four-subgroup TCGA UCEC framework (POLE-ultramutated, MSI-hypermutated, copy-number-low, copy-number-high) provides context for CCEC classification. [PMID:28485815](../papers/28485815.md)
- MC3 pan-cancer mutation-calling project (10,510 TCGA pairs) included UCEC; concordance with the legacy PanCan12 MAF exceeded 90% [PMID:29596782](../papers/29596782.md)
- Pan-cancer fusion study (9,624 TCGA samples) included UCEC; [ESR1](../genes/ESR1.md) fusions were among the recurrent events spanning gynecological cancers; druggable fusions annotated across 29 cancer types including UCEC [PMID:29617662](../papers/29617662.md)
- Pan-cancer aneuploidy study included UCEC in the gynecological arm-level cluster (alongside [UCS](../cancer_types/UCS.md)); UCEC is an exception to the positive aneuploidy–mutation-rate correlation due to MSI-high and POLE-mutant cases; copy-number-high serous-like endometrial is a notable exception that clusters outside the typical UCEC pattern [PMID:29622463](../papers/29622463.md)
- Included in TCGA PanCancer Atlas; UCEC dominated iCluster C8; POLE-mutation signature found in hypermutated C8:UCEC; pan-squamous C10/C25/C27 and pan-GI subtypes linked to UCEC molecular patterns [PMID:29625048](../papers/29625048.md)
- TP53-PPP2R1A vs CTNNB1-PTEN-CTCF mutually exclusive driver networks partition UCEC; MSI-high UCEC over-expresses immune effectors [GZMA](../genes/GZMA.md), [PRF1](../genes/PRF1.md), [GZMK](../genes/GZMK.md), [GZMH](../genes/GZMH.md); POLE-mutant UCEC subtype context referenced [PMID:29625049](../papers/29625049.md)
- Non-hypermutated UCEC CN-high shows 86% PI3K pathway alteration rate; CN-low UCEC shows 95%; MSI-H and POLE-mutant UCEC subtypes carry highest mutation burden and pathway alteration frequency; HER2+PI3K combination actionable in 7% of UCEC CN-high [PMID:29625050](../papers/29625050.md)
- Included in TCGA Pan-Cancer Clinical Data Resource (11,160 patients, 33 cancer types); all four endpoints ([OS](../cancer_types/OS.md), PFI, DFI, DSS) recommended without reservation for UCEC [PMID:29625055](../papers/29625055.md)
- MSI-H detected in 31.4% of endometrial carcinoma cases — highest prevalence among all 39 cancer types analyzed by MANTIS WES caller across 11,139 TCGA/TARGET tumors; one of four classic Lynch syndrome-associated cancer types [PMID:29850653](../papers/29850653.md)
- 189 patients / 197 advanced endometrial tumors profiled by MSK-IMPACT (341 or 410 gene panel); 95% advanced disease; PI3K/AKT/mTOR pathway altered in 70%, RTK/RAS/beta-catenin in 65%; 67% had ≥1 actionable alteration; genomic MSI calling rescued one MMR-proficient-by-IHC case; novel CN Cluster C (heterozygous losses) had worse PFS1 (median 9.6 vs 17.0/17.4 months, p=0.006) [PMID:30068706](../papers/30068706.md)
- In PCAWG, ovarian and uterine adenocarcinoma showed SV dominance over point mutations (ovary: 5.8 ± 2.6 SVs vs 1.9 ± 1.0 point mutations, P < 1×10⁻¹⁶) [PMID:32025007](../papers/32025007.md).
- In CCLE proteomics, [RPL22](../genes/RPL22.md) mutation — a hotspot in MSI endometrial cancers — uniquely associated with proteome-level changes in MSI-associated complexes (mismatch repair, SKI complex, H3K4 methyltransferases); only ~50 proteins differentially expressed in MSI vs >1,000 mRNAs [PMID:31978347](../papers/31978347.md).
- CPTAC proteogenomics of 95 endometrial carcinomas (83 endometrioid, 12 serous); four genomic subtypes ([POLE](../genes/POLE.md) n=7, MSI n=25, CNV-low n=43, CNV-high n=20); MSI tumors: [PTEN](../genes/PTEN.md) 92%, [ARID1A](../genes/ARID1A.md) 76%, [RPL22](../genes/RPL22.md) 64%, [JAK1](../genes/JAK1.md) 44%; TMB alone insufficient for ICB selection — APM deficiency (JAK1/STAT1 truncations, reduced TAP1/TAP2/HLA) marks immune-evasion subgroup [PMID:32059776](../papers/32059776.md).
- [PPM1D](../genes/PPM1D.md) CH mutations were found in 7% of endometrial cancer patients (vs <5% in most tumor types) in the MSK-IMPACT CH cohort; among untreated endometrial patients [PPM1D](../genes/PPM1D.md) CH was 0%, indicating the enrichment is almost entirely therapy-driven (platinum/topoisomerase II inhibitors). [PMID:33106634](../papers/33106634.md)
- In 1,417 prostate cancers profiled by MSK-IMPACT, [PIK3R1](../genes/PIK3R1.md) truncating mutations in endometrial cancer (n=1,769 MSS cases compared) clustered in n-SH2/i-SH2 domains — distinct from the c-SH2 domain hotspot seen in prostate cancer — suggesting tumor-type-specific functional consequences [PMID:35670774](../papers/35670774.md).
- In 184 MSI-H endometrial carcinomas profiled by MSK-IMPACT, three distinct MMR-D mechanisms (germline Lynch n=25, somatic n=39, [MLH1](../genes/MLH1.md) promoter hypermethylation n=120) were associated with divergent molecular profiles, TMB (MLH1ph median 32 vs germline 44 vs somatic 48 mt/Mb, p<0.001), and 2-year stage-I/II PFS (70.3% vs 100% vs 100%) [PMID:35849120](../papers/35849120.md).
- MSK cfDNA pilot (N=44 newly diagnosed EC; [ucec_ccr_cfdna_msk_2022](../datasets/ucec_ccr_cfdna_msk_2022.md)): baseline ctDNA detected in 22% (8/36) of evaluable patients, enriched in advanced/high-risk histologies ([USC](../cancer_types/USC.md), [UCS](../cancer_types/UCS.md)); detectable baseline ctDNA associated with reduced PFS (HR 11.14, p<0.001); post-surgical ctDNA associated with reduced PFS (HR 15.56, p=0.014); primary-tumor mutational landscape: [TP53](../genes/TP53.md) 52%, [PTEN](../genes/PTEN.md) 50%, [PIK3CA](../genes/PIK3CA.md) 50%, [ARID1A](../genes/ARID1A.md) 36%, [FBXW7](../genes/FBXW7.md) 29% [PMID:36007103](../papers/36007103.md)
- Wu et al. pan-cancer Asian cohort ([pan_origimed_2020](../datasets/pan_origimed_2020.md), n=10,194): UCEC included among 25 principal tumor types; TP53 (58% pan-cohort), PIK3CA (11%), MSI-H/TMB-H/PD-L1+ IO biomarker positivity profiled across tumor types [PMID:35871175](../papers/35871175.md)

## Subtypes

- CN-H/TP53abn: 69% of Black vs. 35% of White ECs (P<0.001); associated with serous/carcinosarcoma histology, higher chromosomal instability ([FGA](../genes/FGA.md) 30% vs. 10%), and lower actionable alteration frequency. [PMID:37651310](../papers/37651310.md)
- POLE-mutant: 1.2% Black vs. 5.8% White; favorable prognosis. [PMID:37651310](../papers/37651310.md)
- MSI-H/dMMR: 14% Black vs. 25% White; eligible for immune checkpoint therapy. [PMID:37651310](../papers/37651310.md)
- Serous carcinoma ([USC](../cancer_types/USC.md)): 29% Black vs. 13% White (P<0.01). [PMID:37651310](../papers/37651310.md)
- Carcinosarcoma ([UCS](../cancer_types/UCS.md)): 20% Black vs. 11% White (P<0.01). [PMID:37651310](../papers/37651310.md)

## Therapeutic landscape

- Nivolumab in dMMR/MSI-H UCEC: ORR 58.8% (7 CRs, 13 PRs), PFS24 64.7%, median PFS 21.6 months; TMB and PD-L1 were not predictive within dMMR-selected population. [PMID:38653864](../papers/38653864.md)
- T cell functional states (dysfunctional CD8+PD-1+, terminally dysfunctional CD8+PD-1+[TOX](../genes/TOX.md)+) and spatial proximity to PD-L1+ cells predict [nivolumab](../drugs/nivolumab.md) benefit (AUC=0.897, P=0.0007). [PMID:38653864](../papers/38653864.md)
- [ERBB2](../genes/ERBB2.md) amplification in Black patients represents a therapeutic opportunity with [trastuzumab](../drugs/trastuzumab.md) and T-DXd (including low-HER2-expressing carcinosarcomas). [PMID:37651310](../papers/37651310.md)
- [CCNE1](../genes/CCNE1.md) amplification (enriched in Black patients) is a potential target for [WEE1](../genes/WEE1.md) inhibitors, [ATR](../genes/ATR.md) inhibitors, and PKMYT1 kinase inhibitors. [PMID:37651310](../papers/37651310.md)
- Only 22.4% of Black patients had OncoKB Level 1/2/3A actionable alterations vs. 39.7% of White patients (P<0.001), underscoring need for more diverse clinical trials. [PMID:37651310](../papers/37651310.md)

## Sources

- [PMID:37651310](../papers/37651310.md) — Molecular characterization of endometrial carcinomas in Black and White patients reveals disparate drivers with therapeutic implications (Cancer Discovery, 2023)
- [PMID:38653864](../papers/38653864.md) — Nivolumab for mismatch-repair-deficient or hypermutated gynecologic cancers: a phase 2 trial with biomarker analyses (Nature Medicine, 2024)

- [PMID:23636398](../papers/23636398.md) — Cancer Genome Atlas Research Network. Integrated genomic characterization of endometrial carcinoma. *Nature* 2013.

- [PMID:28445112](../papers/28445112.md) — Reinikka et al. 2025; endometrial polyp WGS/RNA-seq; low-VAF UCEC-driver hotspot mutations in 26% [KRAS](../genes/KRAS.md), [PIK3CA](../genes/PIK3CA.md), [PIK3R1](../genes/PIK3R1.md), [PTEN](../genes/PTEN.md), [ERBB2](../genes/ERBB2.md), [FBXW7](../genes/FBXW7.md).

- [PMID:28481359](../papers/28481359.md)
- [PMID:28485815](../papers/28485815.md)


- [PMID:29596782](../papers/29596782.md)


- [PMID:29617662](../papers/29617662.md)


- [PMID:29622463](../papers/29622463.md)


- [PMID:29625048](../papers/29625048.md)


- [PMID:29625049](../papers/29625049.md)


- [PMID:29625050](../papers/29625050.md)


- [PMID:29625055](../papers/29625055.md)


- [PMID:29850653](../papers/29850653.md)


- [PMID:30068706](../papers/30068706.md)


- [PMID:32025007](../papers/32025007.md)


- [PMID:31978347](../papers/31978347.md)


- [PMID:32059776](../papers/32059776.md)


- [PMID:33106634](../papers/33106634.md)


- [PMID:35670774](../papers/35670774.md)


- [PMID:35849120](../papers/35849120.md)


- [PMID:36007103](../papers/36007103.md)


- [PMID:35871175](../papers/35871175.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
