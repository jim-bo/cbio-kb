---
name: Prostate Adenocarcinoma
oncotree_code: PRAD
main_type: Prostate Cancer
parent: PROSTATE
tags: [prostate]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Prostate Adenocarcinoma (PRAD)

## Overview

OncoTree code for prostate adenocarcinoma.

## Cohorts in the corpus

- [msk_chord_2024](../datasets/msk_chord_2024.md) — 3,211 prostate cancer patients at MSK in the MSK-CHORD clinicogenomic harmonized real-world dataset [PMID:39506116](../papers/39506116.md).
- Commentary cohort: oligometastatic hormone-sensitive PRAD; synchronous de novo cases estimated at "several thousands" per year in the US; metachronous/oligorecurrent cases potentially the majority of men who progress to metastatic disease. No primary data collected. [PMID:28045614](../papers/28045614.md)
- [prad_msk_mdanderson_2023](../datasets/prad_msk_mdanderson_2023.md) — 44 PDX models from 38 prostate cancer patients at MD Anderson Cancer Center, spanning adenocarcinoma and NEPC, profiled by WGS, T200.1 targeted sequencing, and RNA-seq. [PMID:38488813](../papers/38488813.md)
- [prostate_msk_2024](../datasets/prostate_msk_2024.md) — 2,257 PRAD patients at MSK sequenced by MSK-IMPACT (3,244 tumors); subgroups: 63 MSI-H/dMMR (2.8%), 33 TMB-H/MSS (1.5%). [PMID:38949888](../papers/38949888.md)
- [msk_ctdna_vte_2024](../datasets/msk_ctdna_vte_2024.md) — PRAD comprised 5% of the 4,141-patient liquid biopsy VTE discovery cohort. [PMID:39147831](../papers/39147831.md)
- ATLAS classifier validation — PRAD included in the 22-class site-of-origin model; de-differentiation score distinguishes PRAD from [PRNE](../cancer_types/PRNE.md) (AUC=0.834). [PMID:27634761](../papers/27634761.md)

## Recurrent alterations

- Included in pan-cancer MSK-IMPACT pathway and metastasis analyses [PMID:39506116](../papers/39506116.md).
- 91% of PDX models harbored oncogenic alterations in at least one of [AR](../genes/AR.md), [RB1](../genes/RB1.md), [TP53](../genes/TP53.md), or [PTEN](../genes/PTEN.md). [PMID:38488813](../papers/38488813.md)
- [TMPRSS2](../genes/TMPRSS2.md)-[ERG](../genes/ERG.md) fusion detected in 13/44 PDX models; correlated with [ERG](../genes/ERG.md) overexpression in AR-expressing models. [PMID:38488813](../papers/38488813.md)
- [CDK12](../genes/CDK12.md) biallelic loss via dual mutations or structural variation in 4 PDX models; CDK12-loss-associated focal copy-number gains observed. [PMID:38488813](../papers/38488813.md)
- 63 (2.8%) patients had MSI-H/dMMR tumors, 33 (1.5%) had TMB-H/MSS tumors among 2,257 PRAD patients. MSI-H/dMMR had significantly higher TMB than TMB-H/MSS (median 41 vs. 15 mut/Mb, P<0.01). [PMID:38949888](../papers/38949888.md)
- [BRAF](../genes/BRAF.md) fusions in PRAD: [SND1](../genes/SND1.md) was the dominant 5' fusion partner in prostate adenocarcinoma [BRAF](../genes/BRAF.md) fusions (21% of PRAD [BRAF](../genes/BRAF.md) fusions). [PMID:38922339](../papers/38922339.md)
- No specific gene-level alterations identified for the oligometastatic hormone-sensitive state; genetic and transcriptomic profiling of hormone-sensitive localized and metastatic castration-resistant PRAD has been described but a hormone-sensitive oligometastatic data set was noted as "still unavailable." [PMID:28045614](../papers/28045614.md)
- [MSH2](../genes/MSH2.md), [MSH6](../genes/MSH6.md), [MLH1](../genes/MLH1.md), [PMS2](../genes/PMS2.md) — deleterious MMR gene alterations in 75% of MSI-H/dMMR PRAD patients. [PMID:38949888](../papers/38949888.md)
- Integrative genomic profiling of 218 PRAD tumors (MSKCC cohort) identified recurrent copy-number alterations and somatic mutations via SNP arrays and whole-exome sequencing [PMID:20579941](../papers/20579941.md)
- WES of 112 prostate adenocarcinoma tumors identified [SPOP](../genes/SPOP.md), [FOXA1](../genes/FOXA1.md), and [MED12](../genes/MED12.md) as recurrent driver genes [PMID:22610119](../papers/22610119.md)
- WES of 112 prostate tumors (Michigan cohort, [prad_mich](../datasets/prad_mich.md)) identified recurrent ETS family fusions and [SPOP](../genes/SPOP.md) mutations as key drivers of prostate adenocarcinoma [PMID:22722839](../papers/22722839.md)
- WGS of 55 treatment-naïve primary PRAD identified chromoplexy (chains of ≥5 interdependent rearrangements) in 88% of tumors; TMPRSS2-ERG fusion arose within chromoplexy chains in 58% of [ERG](../genes/ERG.md)+ cases; recurrent SCNA burden tracks with Gleason grade (p=0.0059) [PMID:23622249](../papers/23622249.md)
- CNA burden (fraction of autosomal genome with copy-number alterations) predicts biochemical recurrence (HR 1.09 per 1%, P<0.001) and metastasis in two independent prostatectomy cohorts (n=168 and n=104); prognostic independent of PSA, Gleason score, and the Stephenson nomogram, and measurable from FFPE needle biopsies by low-pass WGS [PMID:25024180](../papers/25024180.md)
- Seven patient-derived 3D organoid lines from metastatic CRPC recapitulated the molecular landscape of advanced prostate cancer, including [PTEN](../genes/PTEN.md) biallelic loss (6/7 lines), [TP53](../genes/TP53.md) inactivation (4/7), [CHD1](../genes/CHD1.md) deletion (3/7), [SPOP](../genes/SPOP.md) F133L hotspot (1/7, first in vitro model), and diverse [AR](../genes/AR.md) status; AR-amplified MSK-PCa2 was sensitive to [enzalutamide](../drugs/enzalutamide.md) and [everolimus](../drugs/everolimus.md) in vitro and in xenografts. [PMID:25201530](../papers/25201530.md)
- Prospective WES + transcriptome sequencing of 150 mCRPC bone/soft-tissue biopsies (SU2C-PCF Dream Team; dataset: [prad_su2c_2015](../datasets/prad_su2c_2015.md)): [AR](../genes/AR.md) altered in 62.7%, ETS fusions 56.7%, [TP53](../genes/TP53.md) 53.3%, [PTEN](../genes/PTEN.md) 40.7%; DNA-repair pathway (BRCA2/BRCA1/ATM) aberrations in 19.3% — substantially higher than primary PRAD; 89% of patients harbored a clinically actionable alteration; 8% had pathogenic germline variants; novel recurrent focal homozygous deletion of [ZBTB16](../genes/ZBTB16.md) at chr11q23 in 5% of cases [PMID:26000489](../papers/26000489.md)
- Prostate adenocarcinoma (PRAD) multi-omic profiling identified subtypes defined by ETS fusions, SPOP/FOXA1/IDH1 mutations, and distinct epigenetic signatures [PMID:26544944](../papers/26544944.md)
- Beltran et al. profiled 114 metastatic biopsies from 81 castration-resistant prostate cancer patients (51 CRPC-Adeno, 30 CRPC-NE); concurrent [RB1](../genes/RB1.md)+[TP53](../genes/TP53.md) loss hallmarks neuroendocrine transdifferentiation (53.3% CRPC-NE vs 13.7% CRPC-Adeno); [CYLD](../genes/CYLD.md) deleted in 51% CRPC-NE; 70-gene NEPC classifier (precision/recall >0.99) detects CRPC-NE in up to 8% of metastatic cases across external cohorts [PMID:26855148](../papers/26855148.md)
- WES + array-CGH + expression microarray on 176 tumors from 63 men with mCRPC (rapid autopsy cohort) showed high intra-individual metastatic concordance for key drivers ([AR](../genes/AR.md) amplification/mutation 63%, [TMPRSS2](../genes/TMPRSS2.md)-[ERG](../genes/ERG.md) 100% concordant); somatic FA-pathway or [ATM](../genes/ATM.md) defects predicted longer [carboplatin](../drugs/carboplatin.md) response (log-rank P=0.02) [PMID:26928463](../papers/26928463.md)
- [TRMT10A](../genes/TRMT10A.md) overexpressed in prostate cancer/mCRPC vs normal tissue (TCGA [prad_tcga](../datasets/prad_tcga.md); n=500 tumor, n=52 normal); high TRMT10A IHC associated with shorter [OS](../cancer_types/OS.md) (P=0.014, log-rank) in 54 mCRPC patients; TRMT10A loss sensitizes BRCA1/2-WT mCRPC cells to PARPi ([olaparib](../drugs/olaparib.md)) by impairing ATM-dependent [BRCA1](../genes/BRCA1.md) recruitment; [USP10](../genes/USP10.md) inhibitor [spautin-1](../drugs/spautin-1.md) degrades TRMT10A and synergizes with olaparib in 22Rv1 CDX and two mCRPC PDX models [PMID:28068672](../papers/28068672.md)
- In the MSK-IMPACT pan-cancer cohort (n=10,945 tumors), [AR](../genes/AR.md) was mutated in 18% of metastatic PRAD vs 1% in TCGA primary tumors; recurrent acquired-resistance hotspots L702H and H875Y were observed in 10 patients each; TP53 was significantly enriched vs TCGA in metastatic prostate cancer; TMPRSS2-ERG was the most common rearrangement (n=151) with 23 cryptic [TMPRSS2](../genes/TMPRSS2.md) rearrangements consistent with chromoplexy; MSI-detected prostate cancer (n=1) responded to anti-PD-L1 therapy. [PMID:28481359](../papers/28481359.md)
- MET500 metastatic cohort: prostate adenocarcinoma was the largest lineage represented (93/500, 18.6%); AR alterations (12.6%) were lineage-restricted (predominantly PRAD); mutation burden was significantly elevated vs TCGA primaries with the largest increase in prostate cancer; germline pathogenic variants in [HOXB13](../genes/HOXB13.md) (3 carriers, prostate-susceptibility allele) observed. [PMID:28783718](../papers/28783718.md)
- MSK-IMPACT targeted profiling of 504 tumors from 451 PRAD patients spanning locoregional to mCRPC: actionable alterations in 36%, 22% somatic HR-gene alterations, 19% germline pathogenic variants in 221 tested ([BRCA2](../genes/BRCA2.md) 9%, [CHEK2](../genes/CHEK2.md) 4%, [ATM](../genes/ATM.md) 2%); AR, TP53, [PTEN](../genes/PTEN.md), RB1, ATM frequencies escalate with castration resistance; TP53 and BRCA2 alterations are early clonal events. [PMID:28825054](../papers/28825054.md)
- SNPs-seq screen of 374 PRAD GWAS loci nominated rs4519489 ([NOL10](../genes/NOL10.md) intron, 2p25) as functional: A allele drives higher NOL10 expression via [USF1](../genes/USF1.md) binding; elevated NOL10 tracks with advanced stage, lymph-node metastasis, Gleason score, [BCR](../genes/BCR.md), and shorter OS across CPGEA, TCGA PRAD, and multiple validation cohorts (meta-analysis BCR HR=2.49, P=1.81e-9). [PMID:28927585](../papers/28927585.md)
- WES meta-analysis of 1,013 prostate tumor/normal pairs (680 primary, 333 metastatic castration-resistant) identified 97 SMGs; novel drivers include [CUL3](../genes/CUL3.md) (1.3%, SPOP-like), [SPEN](../genes/SPEN.md) (2.4%, metastasis-enriched AR-pathway), SF3B1/U2AF1 spliceosome pathway (4%), [PIK3R2](../genes/PIK3R2.md) p.Asp557Tyr, [CDK12](../genes/CDK12.md) biallelic inactivation, [MRE11](../genes/MRE11.md), and [PALB2](../genes/PALB2.md); TMPRSS2–[ERG](../genes/ERG.md) fusions define the dominant fusion subtype [PMID:29610475](../papers/29610475.md)
- Pan-cancer fusion study (9,624 TCGA samples) identified TMPRSS2–ERG as the most recurrent single-cancer fusion (38.2% of PRAD, 205 samples); 205 PRAD samples were annotated as druggable via TMPRSS2, making it the largest druggable-fusion group in the pan-cancer cohort [PMID:29617662](../papers/29617662.md)
- Included in TCGA PanCancer Atlas; PRAD dominated iCluster C16; PRAD showed high cell-of-origin molecular homogeneity [PMID:29625048](../papers/29625048.md)
- Included in pan-cancer pathway analysis of 9,125 TCGA tumors across 33 cancer types [PMID:29625050](../papers/29625050.md)
- Included in TCGA Pan-Cancer Clinical Data Resource (11,160 patients, 33 cancer types); TCGA-CDR advises against using OS/DSS for PRAD due to short follow-up; PFI/DFI recommended instead [PMID:29625055](../papers/29625055.md)
- PRAD (prostate adenocarcinoma) was the cancer type studied in 292 whole-genome-profiled cases (203 EOPC, 89 LOPC) from the [prostate_dkfz_2018](../datasets/prostate_dkfz_2018.md) dataset; recurrent SVs included TMPRSS2-ERG fusions (70% of EOPC), 8p [NKX3-1](../genes/NKX3-1.md) loss (37%), 3p14 [FOXP1](../genes/FOXP1.md) loss (30%), 13q22 [KLF5](../genes/KLF5.md) loss (27%), and 8q22 [ESRP1](../genes/ESRP1.md) duplications (17%); APOBEC3B-driven kataegis was the dominant mutational mechanism at SV breakpoints. [PMID:30537516](../papers/30537516.md)
- SU2C mCRPC cohort expanded to 429 patients (444 tumors) profiled by WES and RNA-seq; RB1 alteration is the dominant independent prognostic biomarker (multivariate RR 3.31 OS, RR 6.56 time on ARSI); AR-V7 tumor-tissue detection is not prognostic; 10.5% of post-ARSI tumors show neuroendocrine histologic features [PMID:31061129](../papers/31061129.md).
- HP [1-13C] pyruvate MRI in 12 PRAD patients: Lac_max significantly higher in tumor vs normal prostate (p=0.0001 Gleason 3, p<0.0001 Gleason ≥4) and rose with grade; MCT1 ([SLC16A1](../genes/SLC16A1.md)) identified as rate-limiting lactate transporter by IHC; homozygous PTEN loss trended with highest Lac_max (p=0.059); TMPRSS2-ERG fusion did not segregate lactate signal [PMID:31564440](../papers/31564440.md).
- Castration-resistant prostate cancer (CRPC, n=44–55 evaluable) was one of three tumor types in a prospective cfDNA+WBC co-sequencing study; cfDNA detected at least one tumor mutation in 82% of CRPC patients; AR mutations were recoverable as subclonal VUSo; one MSI-H CRPC patient identified solely from cfDNA had rapid sustained response to anti-PD-L1 therapy [PMID:31768066](../papers/31768066.md)
- In PCAWG, prostate adenocarcinoma showed chromoplexy as a prominent mutational process and [TP53](../genes/TP53.md) association with chromothripsis (OR=2.6); chromothripsis was clonal and early in prostate cancer [PMID:32025007](../papers/32025007.md).
- Prospective MSK-IMPACT sequencing of 424 mCSPC patients showed CDK12 alterations 6.7 pp more frequent in de-novo metastatic vs recurrent disease (FDR 0.037); AR, TP53, cell-cycle, and [MYC](../genes/MYC.md) pathway alterations associated with shorter time to castration resistance; 50% of mCSPC tumors harbored at least one OncoKB-actionable alteration [PMID:32220891](../papers/32220891.md)
- CDK12 alterations in 100/1,875 (5.3%) of prostate cancers sequenced by MSK-IMPACT (highest among 25 solid tumor types); CDK12-biallelic (CDK12-Bi) cases showed tandem duplicator phenotype, fewer TMPRSS2-ERG fusions and TP53 mutations, and shorter OS from metastatic diagnosis (median 64.4 vs 74.9 mo; aHR 1.80, 95% CI 1.12-2.89; p=0.024) [PMID:32317181](../papers/32317181.md)
- cf-IMPACT targeted cfDNA panel (410 genes) identified somatic mutations in prostate cancer patients in the 118-patient metastatic solid-tumor cohort at MSKCC; [BRCA2](../genes/BRCA2.md) OncoKB level 1 alterations identified in plasma of PRAD patients supporting [olaparib](../drugs/olaparib.md) eligibility; sub-clonal [AR](../genes/AR.md) p.H875Y resistance allele detected by plasma cfDNA below the calling threshold of tumor MSK-IMPACT; an MSI-H mCRPC patient identified from cf-IMPACT received [pembrolizumab](../drugs/pembrolizumab.md) with durable PSA response [PMID:34059130](../papers/34059130.md).
- MSK-ACCESS cfDNA panel prospectively profiled prostate cancer patients (part of the 28% NSCLC/PRAD/BLCA/PAAD/biliary group, n=617 patients total); [AR](../genes/AR.md) mutations enriched in cfDNA vs MSK-IMPACT in prostate cancer; OncoKB level 1 actionable alterations detected in 48% of [BLCA](../cancer_types/BLCA.md), 37% of [BRCA](../cancer_types/BRCA.md), and 33% of [NSCLC](../cancer_types/NSCLC.md) samples; PRAD was the second most common cancer type in the cohort; matched WBC sequencing removed >10,000 germline/CH confounders [PMID:34145282](../papers/34145282.md).
- MSK-IMPACT cohort of 2,069 prostate adenocarcinoma patients (1,841 White, 165 Black, 63 Asian; [prad_msk_stopsack_2021](../datasets/prad_msk_stopsack_2021.md)) revealed race-associated somatic differences: [AR](../genes/AR.md) alterations enriched in Black men (adjusted +5 pp vs White); [FOXA1](../genes/FOXA1.md) class-1 forkhead-domain mutations in 21% vs 8% of Asian vs White men; [TP53](../genes/TP53.md) less frequent in Black men (19% vs 30%; adjusted −10 pp); chr8q gain (enriched for [MYC](../genes/MYC.md)) in 49% Black vs 37% White (adjusted +11 pp), independently prognostic for death (HR 2.00 Black, 1.61 White); area-level income independently associated with chr8q gain, arguing against purely germline interpretation [PMID:34667026](../papers/34667026.md)
- MSK-MET pan-cancer cohort (25,775 patients, 50 tumor types, MSK-IMPACT) characterizes primary vs. metastatic genomic differences; PRAD is among tumor types analyzed for [FGA](../genes/FGA.md), TMB, WGD, and driver-alteration frequency shifts between primary and metastatic specimens [PMID:35120664](../papers/35120664.md)
- Prostate cancer brain metastases (PCBM) from 51 Swiss patients profiled by multi-region whole-exome sequencing (168 samples; [prostate_pcbm_swiss_2019](../datasets/prostate_pcbm_swiss_2019.md)); PCBM showed elevated mutation burden vs matched primaries and non-brain mCRPC; 10/51 (19.6%) met PROfound HRR criteria, 5/51 (9.8%) had pathogenic BRCA1/2 alterations [PMID:35504881](../papers/35504881.md)
- ATAC-seq + RNA-seq of 40 metastatic CRPC models (organoids, PDXs, cell lines) defined four chromatin subtypes: CRPC-AR, CRPC-NE, CRPC-WNT, and novel CRPC-SCL (AP-1/YAP/TAZ-driven, ~28% of 366 patients in SU2C/WCM cohorts); CRPC-SCL associated with shorter time on enzalutamide/abiraterone [PMID:35617398](../papers/35617398.md)

## Subtypes

- MSI-H/dMMR (2.8%) vs. TMB-H/MSS (1.5%) vs. TMB-L/MSS (95.7%) distinct subgroups by immunogenicity; both MSI-H and TMB-H/MSS are more commonly Gleason grade group 5 (62% and 59% vs. 40%, P<0.001). [PMID:38949888](../papers/38949888.md)
- Oligometastatic PRAD (≤5 radiographically visible metastatic lesions) operationalized as a clinically defined intermediate state on the metastatic spectrum; working definition endorsed pending a biologic/genomic definition. [PMID:28045614](../papers/28045614.md)
- NEPC/PRNE: defined by [AR](../genes/AR.md) expression loss, [RB1](../genes/RB1.md) enrichment; DDR pathway transcriptomically upregulated. ATLAS RNA classifier distinguishes PRAD from [PRNE](../cancer_types/PRNE.md) with AUC=0.834. [PMID:38488813](../papers/38488813.md) [PMID:27634761](../papers/27634761.md)

## Therapeutic landscape

- NLP-augmented integrated models outperformed stage- or genomics-only models for overall-survival prediction [PMID:39506116](../papers/39506116.md).
- MSI-H/dMMR PRAD: 45% RECIST ORR and 65% PSA50 response with immune checkpoint blockade (n=27 treated); MSI-H/dMMR patients should receive somatic tumor testing per NCCN recommendations. [PMID:38949888](../papers/38949888.md)
- TMB-H/MSS PRAD: 0% RECIST response with ICB despite FDA approval of [pembrolizumab](../drugs/pembrolizumab.md) for TMB-H tumors; TMB alone is an insufficient biomarker in PRAD. [PMID:38949888](../papers/38949888.md)
- [FGFR1](../genes/FGFR1.md) downstream signature (NRP2, LRP4, TGFBI) stratifies patients for FGFR-targeted therapy in bone-metastatic CRPC; PARP inhibition investigated in NEPC. [PMID:38488813](../papers/38488813.md)
- ctDNA detection associated with higher VTE rates in PRAD patients (5% of pan-cancer cohort); anticoagulation associated with lower VTE in ctDNA-positive patients (adjusted HR=0.50). [PMID:39147831](../papers/39147831.md)
- ATLAS lineage de-differentiation score prognostic for prostate cancer survival and neuroendocrine transformation detection. [PMID:27634761](../papers/27634761.md)
- ROBIN OligoMET center (U54 CA273956; UMB, Weill Cornell Medicine, Thomas Jefferson University) conducts parallel co-clinical studies in oligometastatic PRAD: the TERPS Phase II RCT (NCT05223803) of metastasis-directed SABR had enrolled 47 patients (80+ screened) as of writing; digital-pathology multimodal AI, plasma proteomics, and T-cell receptor repertoire analyses yielded preliminary SABR-benefit signatures. Preclinical dietary interventions showed low-fat/calorie-restricted diets enhanced radiosensitivity while ketogenic diets promoted radio-resistance. These findings catalyzed the biomarker-designed KNIGHTS integral-biomarker RCT (NCT06212583). OligoMET also explicitly investigates molecular drivers of poorer outcomes in African-American patients. [PMID:41941260](../papers/41941260.md)
- Local metastasis-directed therapies (e.g., SABR) in oligometastatic hormone-sensitive PRAD may alter natural history by ablating macroscopic metastases acting as "communal sanctuaries" seeded by circulating tumor cells from multiple sites (self-seeding model); current standard of care remains systemic ADT and any local therapies should be implemented in a clinical trial. [PMID:28045614](../papers/28045614.md)
- 14q32-encoded microRNA signatures and blood-based biomarkers proposed as candidate oligometastatic biomarkers in PRAD, analogous to [NSCLC](../cancer_types/NSCLC.md), but none are clinically validated. [PMID:28045614](../papers/28045614.md)

## Sources

- [PMID:27634761](../papers/27634761.md)
- [PMID:34059130](../papers/34059130.md)
- [PMID:34145282](../papers/34145282.md)
- [PMID:38488813](../papers/38488813.md)
- [PMID:38922339](../papers/38922339.md)
- [PMID:38949888](../papers/38949888.md)
- [PMID:39147831](../papers/39147831.md)
- [PMID:39506116](../papers/39506116.md)
- [PMID:41941260](../papers/41941260.md)
- [PMID:28045614](../papers/28045614.md)
- [PMID:20579941](../papers/20579941.md)
- [PMID:22610119](../papers/22610119.md)
- [PMID:22722839](../papers/22722839.md)
- [PMID:23622249](../papers/23622249.md) — Baca et al. Punctuated evolution of prostate cancer genomes. *Cell* 2013.
- [PMID:25024180](../papers/25024180.md)
- [PMID:25201530](../papers/25201530.md)
- [PMID:26000489](../papers/26000489.md)
- [PMID:26544944](../papers/26544944.md)
- [PMID:26855148](../papers/26855148.md)

- [PMID:26928463](../papers/26928463.md)
- [PMID:28068672](../papers/28068672.md)
- [PMID:28481359](../papers/28481359.md)
- [PMID:28783718](../papers/28783718.md)
- [PMID:28825054](../papers/28825054.md)
- [PMID:28927585](../papers/28927585.md)

- [PMID:29610475](../papers/29610475.md)
- [PMID:29617662](../papers/29617662.md)
- [PMID:29625048](../papers/29625048.md)
- [PMID:29625050](../papers/29625050.md)
- [PMID:29625055](../papers/29625055.md)
- [PMID:30537516](../papers/30537516.md)
- [PMID:31061129](../papers/31061129.md) — Abida et al. SU2C mCRPC cohort N=429 (PNAS 2019).
- [PMID:31564440](../papers/31564440.md)
- [PMID:31768066](../papers/31768066.md)
- [PMID:32025007](../papers/32025007.md)
- [PMID:32220891](../papers/32220891.md)
- [PMID:32317181](../papers/32317181.md)
- [PMID:34667026](../papers/34667026.md)

- [PMID:35120664](../papers/35120664.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35504881](../papers/35504881.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35617398](../papers/35617398.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
