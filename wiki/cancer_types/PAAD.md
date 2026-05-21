---
name: Pancreatic Adenocarcinoma
oncotree_code: PAAD
main_type: Pancreatic Cancer
parent: PANCREAS
tags: [pancreas, kras-driven]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Pancreatic Adenocarcinoma (PAAD)

## Overview

OncoTree code for pancreatic adenocarcinoma. In the corpus, PAAD is characterized by near-universal [KRAS](../genes/KRAS.md) mutation with allele-specific biology, recurrent [TP53](../genes/TP53.md) / [CDKN2A](../genes/CDKN2A.md) / [SMAD4](../genes/SMAD4.md) co-alterations, and clinical behavior strongly shaped by stage at resection.

## Cohorts in the corpus

- [msk_chord_2024](../datasets/msk_chord_2024.md) — 3,109 pancreatic cancer patients at MSK in the MSK-CHORD clinicogenomic harmonized real-world dataset [PMID:39506116](../papers/39506116.md).
- [pancreas_msk_2024](../datasets/pancreas_msk_2024.md) — 1,360 consecutive resected PDAC patients at MSK (2004–2019), with [MSK-IMPACT](../methods/msk-impact-panel.md) targeted sequencing on 397, bulk RNA-seq on 100, and [CosMx SMI](../methods/cosmx-smi.md) spatial profiling on 20 [PMID:39214094](../papers/39214094.md).

## Recurrent alterations

- Included in pan-cancer MSK-IMPACT pathway and metastasis analyses [PMID:39506116](../papers/39506116.md).
- Canonical driver frequencies in the resected MSK cohort (n=397 sequenced): [KRAS](../genes/KRAS.md) 90%, [TP53](../genes/TP53.md) 71%, [CDKN2A](../genes/CDKN2A.md) 24%, [SMAD4](../genes/SMAD4.md) 17%; no significant difference in these frequencies between early- and late-stage disease after multiple-testing correction [PMID:39214094](../papers/39214094.md).
- [KRAS](../genes/KRAS.md) allele distribution: G12D 36.5%, G12V 32.5%, G12R 13.9%, other [KRAS](../genes/KRAS.md) 8.1%, [KRAS](../genes/KRAS.md) wildtype 9.1% [PMID:39214094](../papers/39214094.md).
- [KRAS](../genes/KRAS.md)^G12R^ tumors carry a higher proportion of [CDKN2A](../genes/CDKN2A.md) mutations than [KRAS](../genes/KRAS.md)^G12D^ (40% vs 22.1%, p=0.046) [PMID:39214094](../papers/39214094.md).
- Whole-exome sequencing of 19 pancreatic cystic neoplasms (IPMNs, MCNs, SPNs) identified recurrent somatic mutations in [VHL](../genes/VHL.md), [RNF43](../genes/RNF43.md), and [GNAS](../genes/GNAS.md), linking driver genes to specific PAAD subtypes [PMID:22158988](../papers/22158988.md)
- Whole-exome sequencing of 142 ICGC pancreatic ductal adenocarcinoma tumors revealed [KRAS](../genes/KRAS.md), [TP53](../genes/TP53.md), [SMAD4](../genes/SMAD4.md), and [CDKN2A](../genes/CDKN2A.md) as the most frequently mutated genes, plus novel axon-guidance pathway alterations [PMID:23103869](../papers/23103869.md)
- The [gemcitabine](../drugs/gemcitabine.md) + [saridegib](../drugs/saridegib.md) (Smoothened inhibitor) co-clinical trial in PAAD was halted after interim analysis showed inferior survival in the experimental arm despite positive preclinical signal in Kras-driven GEM models; post-clinical mouse experiments suggested chronic Smoothened targeting induces a more aggressive phenotype, illustrating the risk of short preclinical dosing windows [PMID:23999436](../papers/23999436.md).
- Whole-exome sequencing of 109 microdissected PAAD (plus 11 [PAASC](../cancer_types/PAASC.md), 4 [PAAC](../cancer_types/PAAC.md)) identified 24 SMGs; [KRAS](../genes/KRAS.md) 92%, [TP53](../genes/TP53.md) 50%, [SMAD4](../genes/SMAD4.md) 19%, CDKN2A/B 36%; [MYC](../genes/MYC.md) amplification at 8q24.13 uniquely associates with poor overall survival (P=0.0013) and adenosquamous ([PAASC](../cancer_types/PAASC.md)) subtype; [BRAF](../genes/BRAF.md) V600E (3%) is mutually exclusive with [KRAS](../genes/KRAS.md) and vemurafenib-sensitive in a patient-derived cell line; codon-61 [KRAS](../genes/KRAS.md) alleles confer favourable prognosis vs codon-12 (P=0.01999) [PMID:25855536](../papers/25855536.md)
- Narrative review of nine prospective SBRT trials in locally advanced PAAD: 33 Gy/5-fraction regimen with [gemcitabine](../drugs/gemcitabine.md) (Herman et al., n=49) achieved 79% 1-year local control and 13.9-month median [OS](../cancer_types/OS.md) with only 2% acute and 6% late grade 3+ GI toxicity; SMAD4/DPC4 loss is a candidate biomarker for metastatic propensity and patient selection for local intensification; duodenal dose constraints (V15Gy <9 cc, V20Gy <3 cc, V33Gy <1 cc) are essential [PMID:27826200](../papers/27826200.md).
- In the MSK-IMPACT pan-cancer cohort, [KRAS](../genes/KRAS.md) was mutated in 90% of PAAD — the highest rate of any principal tumor type — with G12 codon variants comprising 80% of all KRAS mutations; KRAS was classified as non-actionable under then-current OncoKB criteria (predating approval of KRAS G12C inhibitors). [PMID:28481359](../papers/28481359.md)
- MC3 pan-cancer mutation-calling project (10,510 TCGA pairs) included PAAD; PAAD recovered only 33% of original PanCan12 MAF calls due to low tumor purity (median ABSOLUTE purity 39.7%), making it the most problematic cancer type for MC3 concordance [PMID:29596782](../papers/29596782.md)
- Pan-cancer fusion study (9,624 TCGA samples) included PAAD; [FGFR2](../genes/FGFR2.md) fusions were detected in PAAD and represent potential therapeutic targets; [FGFR3](../genes/FGFR3.md) druggable target annotation spanned 15 cancer types including PAAD [PMID:29617662](../papers/29617662.md)
- Pan-cancer aneuploidy study placed PAAD in the gastrointestinal arm-level cluster (co-gaining 8q, 13q, chromosome 20 alongside [COAD](../cancer_types/COAD.md), [READ](../cancer_types/READ.md), [STAD](../cancer_types/STAD.md)); leukocyte fraction was most strongly negatively correlated with aneuploidy in PAAD (Spearman ρ = −0.428) [PMID:29622463](../papers/29622463.md)
- Included in TCGA PanCancer Atlas integrative molecular analysis of 9,759 tumors across 33 cancer types [PMID:29625048](../papers/29625048.md)
- KRAS and [TP53](../genes/TP53.md) significantly co-occur in PAAD (contrasting their mutual exclusivity in COAD/READ/LUAD); PAAD context demonstrates tissue-specific driver interactions [PMID:29625049](../papers/29625049.md)
- RTK-RAS alteration rate 78% in PAAD; KRAS hotspot mutations in 72% of PAAD (highest pan-cancer); HER2+MEK inhibitor combination actionable in 7% of PAAD [PMID:29625050](../papers/29625050.md)
- Included in TCGA Pan-Cancer Clinical Data Resource (11,160 patients, 33 cancer types); all four endpoints (OS, PFI, DFI, DSS) recommended without reservation for PAAD [PMID:29625055](../papers/29625055.md)
- PAAD (pancreatic adenocarcinoma) was highlighted as a cancer type where the tumor microenvironment drives drug response; patient-derived tumoroids on 3D bioprinted decellularized scaffolds were proposed as a drug-screening platform for personalized therapy in pancreatic ductal adenocarcinoma. [PMID:30643250](../papers/30643250.md)
- Pancreatic adenocarcinoma (n=4, 5.3%) was among TRK fusion-positive tumor types in the MSK prospective cohort; pancreatic cancers were over-represented in the MSK real-world cohort relative to the pivotal [larotrectinib](../drugs/larotrectinib.md) trial cohort [PMID:31871300](../papers/31871300.md)
- Included in PCAWG pan-cancer WGS cohort (n=2,658 tumors, 38 types); pancreatic adenocarcinoma analyzed for somatic driver landscape including [KRAS](../genes/KRAS.md) (287 PCAWG driver events), [SMAD4](../genes/SMAD4.md), and [ARID1A](../genes/ARID1A.md) alterations [PMID:32025007](../papers/32025007.md).
- MSK-ACCESS cfDNA panel prospectively profiled pancreatic cancer patients (part of 28% group including PAAD/BLCA/PRAD/biliary, n=617 patients total); [KRAS](../genes/KRAS.md) was noted as a gene where cfDNA detection was lower than tissue in pancreatic cancer; matched WBC sequencing removed >10,000 germline/CH confounders that would otherwise appear as false somatic calls in pancreatic cancer plasma [PMID:34145282](../papers/34145282.md).
- CPTAC proteogenomic study of 140 treatment-naive pancreatic tumors (135 PDAC + 5 adenosquamous) found KRAS alterations in 97%, TP53 in 83%, [CDKN2A](../genes/CDKN2A.md) in 48%, and [SMAD4](../genes/SMAD4.md) in 29%; two proteogenomic subtypes (C1 classical, C2 basal-like) showed stronger prognostic separation than Moffitt RNA-only subtypes (HR 3.4 vs 2.3); only ~6% of tumors were immune-hot; dataset [paad_cptac_2021](../datasets/paad_cptac_2021.md) [PMID:34534465](../papers/34534465.md)
- MSK-MET pan-cancer cohort (25,775 patients, 50 tumor types, MSK-IMPACT) characterizes primary vs. metastatic genomic differences; PAAD is among tumor types analyzed for [FGA](../genes/FGA.md), TMB, WGD, and driver-alteration frequency shifts between primary and metastatic specimens [PMID:35120664](../papers/35120664.md)
- Wu et al. pan-cancer Asian cohort ([pan_origimed_2020](../datasets/pan_origimed_2020.md), n=10,194): PAAD comprised 5% of cohort; KRAS GoF in 74% (MEKi Level 3B/4); CDKN2A LoF in 20% (CDK4/6 inhibitor candidate per OncoKB Level 4); abemaciclib/palbociclib/ribociclib actionable strategy proposed [PMID:35871175](../papers/35871175.md)

## Subtypes

- [KRAS](../genes/KRAS.md)^G12R^-mutant PDAC is a distinct clinical subset: enriched in stage I disease (23% vs 11% in stage II–III, p=0.022), more often node-negative (47% vs 26% for [KRAS](../genes/KRAS.md)^G12D^, p=0.019), with improved [OS](../cancer_types/OS.md) and decreased distant recurrence compared to [KRAS](../genes/KRAS.md)^G12D^; also associated with family history of pancreatic cancer (16.4% vs 4.2%, p=0.003) [PMID:39214094](../papers/39214094.md).
- Transcriptional programs diverge by KRAS allele: KRAS^G12D^ tumors show enhanced KRAS signaling and EMT; KRAS^G12R^ tumors show increased TNF/NF-κB signaling by both bulk RNA-seq and [CosMx SMI](../methods/cosmx-smi.md) spatial profiling [PMID:39214094](../papers/39214094.md).

## Therapeutic landscape

- NLP-augmented integrated survival-prediction models outperformed stage- or genomics-only models [PMID:39506116](../papers/39506116.md).
- KRAS^G12R^ resected PDAC was enriched among patients who received neoadjuvant [fluorouracil](../drugs/fluorouracil.md)-based chemotherapy (most frequently FOLFIRINOX with [irinotecan](../drugs/irinotecan.md) and [oxaliplatin](../drugs/oxaliplatin.md)), consistent with higher response likelihood rather than borderline-resectable selection [PMID:39214094](../papers/39214094.md).
- Allele-specific transcriptional divergence (NF-κB vs KRAS/EMT) suggests divergent actionable dependencies across KRAS-mutant PDAC rather than a single pan-KRAS strategy [PMID:39214094](../papers/39214094.md).
- [BRAF](../genes/BRAF.md) fusions detected in PAAD at low frequency: [SND1](../genes/SND1.md) was the dominant 5' fusion partner in PAAD [BRAF](../genes/BRAF.md) fusions (56%); acinar cell carcinoma of the pancreas had >=5% [BRAF](../genes/BRAF.md) fusion prevalence. [PMID:38922339](../papers/38922339.md)
- PAAD comprised 10% of the 4,141-patient liquid biopsy VTE discovery cohort; ctDNA detection was associated with higher VTE rates across pan-cancer including PAAD. [PMID:39147831](../papers/39147831.md)
- ROBIN METEOR center (U54 CA274318; Washington University) METEOR-CRATR MCT (NCT05975593) has enrolled 12 pancreatic cancer patients with 10 tumor samples (3 with serial biopsies). Preliminary data: SBRT altered cDC1 infiltration in human and murine pancreatic tumors and produced an impaired antigen-presenting-cell ([APC](../genes/APC.md)) phenotype with altered cDC1/cDC2 ratios in draining lymph nodes; myeloid-derived immunosuppressive remodeling of the TME is the working mechanistic hypothesis. CBCT delta-radiomics and ctDNA analyses are underway. [PMID:41941260](../papers/41941260.md)

## Sources

- [PMID:34145282](../papers/34145282.md)
- [PMID:38922339](../papers/38922339.md)
- [PMID:39147831](../papers/39147831.md)
- [PMID:39214094](../papers/39214094.md)
- [PMID:39506116](../papers/39506116.md)
- [PMID:41941260](../papers/41941260.md)


- [PMID:22158988](../papers/22158988.md)

- [PMID:23103869](../papers/23103869.md)

- [PMID:23999436](../papers/23999436.md)

- [PMID:25855536](../papers/25855536.md)

- [PMID:27826200](../papers/27826200.md)

- [PMID:28481359](../papers/28481359.md)

- [PMID:29596782](../papers/29596782.md)

- [PMID:29617662](../papers/29617662.md)

- [PMID:29622463](../papers/29622463.md)

- [PMID:29625048](../papers/29625048.md)

- [PMID:29625049](../papers/29625049.md)

- [PMID:29625050](../papers/29625050.md)

- [PMID:29625055](../papers/29625055.md)

- [PMID:30643250](../papers/30643250.md)

- [PMID:31871300](../papers/31871300.md)

- [PMID:32025007](../papers/32025007.md)

- [PMID:34534465](../papers/34534465.md)

- [PMID:35120664](../papers/35120664.md)


- [PMID:35871175](../papers/35871175.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
