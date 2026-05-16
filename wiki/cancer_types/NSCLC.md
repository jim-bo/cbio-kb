---
name: Non-Small Cell Lung Cancer
oncotree_code: NSCLC
main_type: Non-Small Cell Lung Cancer
parent: LUNG
tags: [lung, nsclc]
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# Non-Small Cell Lung Cancer (NSCLC)

## Overview

Non-Small Cell Lung Cancer (parent LUNG); encompasses histologies including [LUAD](./LUAD.md) and [LUSC](./LUSC.md).

## Cohorts in the corpus

- [bm_nsclc_mskcc_2023](../datasets/bm_nsclc_mskcc_2023.md): 233 patients with resected NSCLC brain metastasis (BM) profiled by MSK-IMPACT — 180 (77%) [LUAD](../cancer_types/LUAD.md), 23 (10%) [LUSC](../cancer_types/LUSC.md), 30 (13%) other NSCLC. Matched samples: 47 primaries, 42 extracranial metastases. Median age 67; 80% current/former smokers [PMID:37591896](../papers/37591896.md).
- [msk_chord_2024](../datasets/msk_chord_2024.md): 7,809 NSCLC patients in the MSK-CHORD clinicogenomic harmonized real-world dataset at MSK [PMID:39506116](../papers/39506116.md).
- A549 and CALU3 (NSCLC cell lines, [EGFR](../genes/EGFR.md)+/HER2+): preclinical ADC radiosensitization study with C-MMAE and T-MMAE. [PMID:27698471](../papers/27698471.md)
- Commentary cohort: oligometastatic NSCLC patients treated on Gomez et al. Lancet Oncol 2016 RCT (≤3 metastases after first-line systemic therapy) cited as cross-tumor precedent for metastasis-directed local consolidative therapy. [PMID:28045614](../papers/28045614.md)
- [csf_msk_2024](../datasets/csf_msk_2024.md): Lung cancer was the most common primary cancer type in the MSK CSF ctDNA cohort (n=188 patients); NSCLC patients profiled by MSK-IMPACT (IMPACT468/IMPACT505) on CSF samples [PMID:39289779](../papers/39289779.md).
- Aerts 2014 introduced foundational CT [radiomics](../methods/radiomics.md) across NSCLC cohorts Lung1 (n=422, Netherlands Cancer Institute), Lung2 (n=225, MAASTRO Clinic), and Lung3 (n=89, MD Anderson), deriving a 4-feature radiomic signature predictive of overall survival [PMID:24892406](../papers/24892406.md).
- Bakr 2018 published the NSCLC-Radiogenomics Stanford cohort pairing pre-treatment CT imaging with RNA-seq and somatic mutation data in 211 NSCLC patients (135 [LUAD](../cancer_types/LUAD.md), 45 [LUSC](../cancer_types/LUSC.md), 31 other); CT features linked to genomic subtypes [PMID:30325352](../papers/30325352.md).

## Recurrent alterations

- TMB was higher in BM vs EM (median 8.8 vs 5.8; p=0.00766); [FGA](../genes/FGA.md) was higher in BM vs EM (p=2.77e-06) and vs PT (p=2.27e-07) [PMID:37591896](../papers/37591896.md).
- [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) alterations more frequent in BM (34%) vs PT (13%, p=0.003, q=0.04); cell-cycle pathway alterations 56% BM vs 32% PT (p=0.004, q=0.041) [PMID:37591896](../papers/37591896.md).
- Paired BM–BM samples showed high genomic concordance vs lower concordance in synchronous BM/PT pairs [PMID:37591896](../papers/37591896.md).
- [NF1](../genes/NF1.md) alterations were more frequent in LMD patients (15%) [PMID:37591896](../papers/37591896.md).
- [HLA-B](../genes/HLA-B.md) mutations appeared as private BM events [PMID:37591896](../papers/37591896.md).
- [EGFR](../genes/EGFR.md) mutations and high-level amplification detected in CSF ctDNA from lung cancer patients; acquired resistance mutations including p.T790M, p.C797S, p.L792H, p.L718Q, p.L718V, p.G724S identified in serial CSF samples [PMID:39289779](../papers/39289779.md).
- [KRAS](../genes/KRAS.md) mutations detected in CSF ctDNA from lung cancer patients; also observed as off-target resistance alteration in EGFR-mutant patients [PMID:39289779](../papers/39289779.md).
- [ALK](../genes/ALK.md) [EML4](../genes/EML4.md)::[ALK](../genes/ALK.md) fusions in lung carcinomas; resistance mutations p.G1202R and p.G1269A detected in CSF upon targeted therapy progression [PMID:39289779](../papers/39289779.md).
- [MET](../genes/MET.md) amplification and exon 14 skipping mutations detected in CSF; resistance mutation p.Y1230N emerged on [crizotinib](../drugs/crizotinib.md) [PMID:39289779](../papers/39289779.md).
- [RET](../genes/RET.md) and [ROS1](../genes/ROS1.md) rearrangements with diverse gene partners detected in CSF ctDNA from lung carcinomas [PMID:39289779](../papers/39289779.md).
- [STK11](../genes/STK11.md) and [KEAP1](../genes/KEAP1.md) mutations detected in CSF ctDNA from lung cancer patients [PMID:39289779](../papers/39289779.md).
- [EGFR](../genes/EGFR.md) and [ERBB2](../genes/ERBB2.md) surface expression levels (not mutation status) gate ADC binding and receptor-restricted radiosensitization in NSCLC cell lines (A549, CALU3). Adding [cetuximab](../drugs/cetuximab.md) or [trastuzumab](../drugs/trastuzumab.md) to cytotoxic chemo-RT in NSCLC failed in prior trials; ADC delivery [paradigm](../methods/paradigm.md) proposed as alternative. [PMID:27698471](../papers/27698471.md)
- Oligometastatic NSCLC (≤3 metastases) may have a distinct biology attributable to 14q32-encoded microRNA-mediated attenuation of epithelial-mesenchymal transition; local consolidative therapy in this group prolonged PFS in the Gomez et al. RCT. [PMID:28045614](../papers/28045614.md)
- DyAM multimodal ML framework (n=247 advanced NSCLC at MSK) integrating CT [radiomics](../methods/radiomics.md), PD-L1 IHC texture, and MSK-IMPACT genomics predicted PD-(L)1 blockade response with AUC=0.80 (95% CI 0.74-0.86), significantly outperforming TMB alone (AUC=0.61) and PD-L1 TPS alone (AUC=0.73); [EGFR](../genes/EGFR.md) mutation (8.9%, aHR=2.14, P=0.03) and [STK11](../genes/STK11.md) mutation (17.8%, aHR=2.53, P<0.005) were independent negative predictors of immunotherapy response [PMID:36038778](../papers/36038778.md)
- Orthotopic implantation of resected NSCLC under the renal capsule of NOD-scid mice increased engraftment rates from 30-40% to 90% and enabled drug testing within 6-8 weeks; 11 of 16 evaluable PDX models showed concordant drug response between mouse and patient, with strong concordance particularly for resistance to conventional chemotherapy [PMID:23999436](../papers/23999436.md).
- Whole-exome sequencing of 34 advanced NSCLC patients treated with [pembrolizumab](../drugs/pembrolizumab.md) showed higher nonsynonymous somatic mutation burden significantly associated with objective response, durable clinical benefit, and PFS (pooled Mann-Whitney P=0.0008; PFS HR 0.19, P=0.0004); a candidate cutoff of ≥178 nonsynonymous mutations, molecular smoking signature, neoantigen burden, and deleterious mutations in [POLD1](../genes/POLD1.md)/[POLE](../genes/POLE.md)/[MSH2](../genes/MSH2.md) also correlated with efficacy. [PMID:25765070](../papers/25765070.md)
- Largest NSCLC WES study to date (660 LUAD + 484 LUSC, n=1,144 total; nsclc_tcga_broad_2016): identified 6 genes SMG in both histologies (TP53, RB1, ARID1A, CDKN2A, PIK3CA, NF1), 14 pan-lung SMGs in joint analysis including KLF5 and EP300/CREBBP; ≥5 predicted neoepitopes in 47% of LUAD and 53% of LUSC, supporting broad immunotherapy applicability [PMID:27158780](../papers/27158780.md)
- Narrative review of young-onset NSCLC (YLC, generally defined as age <40–50 years) synthesizing ≥40 studies: targetable alterations present in 57–70% of YLC vs ~52% in older patients (Sacher et al., p<0.001); ALK rearrangements, ROS1 fusions, and EGFR mutations are over-represented while KRAS, BRAF, and MET alterations are under-represented; Indian patients present approximately a decade earlier than the global median [PMID:27346245](../papers/27346245.md).
- Pre-operative ctDNA was detected in 48% (46/96) of early-stage NSCLCs in the TRACERx cohort, with a stark histology difference: 97% of LUSC vs 19% of LUAD; post-operative ctDNA detected relapse in 13/14 (93%) confirmed-relapse cases with a median 70-day lead-time over imaging. [PMID:28445469](../papers/28445469.md)
- In 240 advanced NSCLC patients profiled by MSK-IMPACT and treated with anti-PD-(L)1, targeted-panel TMB correlated with WES at Spearman r=0.86 (p<0.001) and was higher in patients with durable clinical benefit (median 8.5 vs 6.6 SNVs/Mb, p=0.006); TMB and PD-L1 were independent predictors, together yielding 50% DCB rate; EGFR and STK11 mutations associated with lack of benefit [PMID:29337640](../papers/29337640.md)
- In SUMMIT, 26 HER2-mutant NSCLC patients (predominantly LUAD with exon 20 insertions) achieved only 1 RECIST response to neratinib but median PFS 5.5 months with 6 patients on therapy >1 year; HER2 exon 20 insertions are analogous to EGFR exon 20 insertions resistant to first/second-generation TKIs [PMID:29420467](../papers/29420467.md)
- CheckMate-012 WES study (n=75 advanced NSCLC): tumor mutation burden (TMB) is a strong, PD-L1-independent predictor of response to nivolumab + ipilimumab; high TMB (>median 158 mutations) yielded ORR 51% vs 13% (p=0.0005), DCB 65% vs 34%, PFS HR 0.41 (p=0.0024); TMB from MSK-IMPACT 468-gene or FoundationOne 315-gene panels was similarly predictive as WES-derived TMB [PMID:29657128](../papers/29657128.md)
- N=57 in pooled MSS ICB WES cohort; KRAS-mutant smoker-signature tumors are a favorable subgroup for ICB; EGFR-hotspot never-smoker tumors are unfavorable (low TMB, subclonal-skewed mutations, poor response) [PMID:30150660](../papers/30150660.md)
- NSCLC was the largest histology in the ICI-treated MSK-IMPACT cohort (n=350); TMB-high NSCLC patients had improved overall survival, the effect persisted after removing NSCLC and melanoma from the pan-cancer analysis, and PFS/clinical-benefit associations with TMB were specifically reported for this histology. [PMID:30643254](../papers/30643254.md)
- Non-small cell lung cancer (n=41–53 evaluable) was one of three tumor types in a prospective cfDNA+WBC co-sequencing study; cfDNA detected at least one tumor mutation in 76% of NSCLC patients; EGFR T790M resistance mutations were recoverable as subclonal VUSo from cfDNA; MET amplification detected in one case (cfDNA CNV detection limited by low ctDNA fraction) [PMID:31768066](../papers/31768066.md)

## Subtypes

- Among [LUAD](../cancer_types/LUAD.md) BM patients: LMD patients had more [EGFR](../genes/EGFR.md) alterations (45% vs 21%, p=0.044); local progressors had more [RB1](../genes/RB1.md) loss (24% vs 6%, p=0.022); multifocal regional progressors had [MYC](../genes/MYC.md) amplifications in 22% vs 0% (p=0.023) [PMID:37591896](../papers/37591896.md).

## Therapeutic landscape

- Non-canonical [EGFR](../genes/EGFR.md) mutations (L861Q, G719A/S, A755G, N771_H773dup) in BM may identify patients at elevated risk for LMD and partial resistance to [osimertinib](../drugs/osimertinib.md); persistence despite TKI therapy noted [PMID:37591896](../papers/37591896.md).
- Cell-cycle/[CDKN2A](../genes/CDKN2A.md)-B loss enrichment in BM suggests a rationale for CDK4/6-directed strategies in CNS-tropic NSCLC, not tested here [PMID:37591896](../papers/37591896.md).
- Leptomeningeal involvement was a strong predictor of CSF ctDNA positivity in NSCLC (OR 20.17, 95% CI 9.65-42.16, p < 0.0001). CSF ctDNA had greater sensitivity than positive cytology for leptomeningeal disease (85.4% vs. 61.7%) and greater negative predictive value (80% vs. 66%) [PMID:39289779](../papers/39289779.md).
- Lung carcinomas had the highest rate of level 1 OncoKB actionable alterations among all tumor types in the CSF ctDNA cohort; 50.7% of ctDNA-positive samples carried a level 1 actionable alteration [PMID:39289779](../papers/39289779.md).
- Serial CSF ctDNA profiling identified clonal evolution and emergence of resistance mechanisms ([EGFR](../genes/EGFR.md) gatekeeper mutations, [ALK](../genes/ALK.md) resistance mutations, [MET](../genes/MET.md) resistance mutations), directly informing treatment changes [PMID:39289779](../papers/39289779.md).
- ATLAS RNA-expression classifier achieved 91.4% site-of-origin accuracy; NSCLC distinguished from [SCLC](../cancer_types/SCLC.md) by lineage de-differentiation score (AUC=0.963); classifier can identify neuroendocrine transformation. [PMID:27634761](../papers/27634761.md)
- EGFR-directed (C-MMAE) and HER2-directed (T-MMAE) ADCs selectively radiosensitize receptor-expressing NSCLC lines without off-target toxicity, in contrast to [cetuximab](../drugs/cetuximab.md) or free MMAE. [PMID:27698471](../papers/27698471.md)
- Local consolidative therapy (e.g., SABR) in oligometastatic NSCLC (≤5 lesions, primarily ≤3 by clinical definition) may alter natural history; self-seeding biology and microRNA-driven attenuation of EMT provide a mechanistic rationale for metastasis-directed ablation. [PMID:28045614](../papers/28045614.md)
- ctDNA detection independently associated with higher VTE rates in advanced NSCLC (HR=2.49, 95% CI 1.99--3.11); NSCLC comprised 34% of the 4,141-patient discovery cohort. The international generalizability cohort (n=463) specifically comprised advanced NSCLC patients (ctDX Lung panel); c-index 0.67 for ctDNA-based VTE prediction. [PMID:39147831](../papers/39147831.md)

## Sources

- [PMID:27634761](../papers/27634761.md)
- [PMID:37591896](../papers/37591896.md)
- [PMID:39147831](../papers/39147831.md)
- [PMID:39289779](../papers/39289779.md)
- [PMID:39506116](../papers/39506116.md)
- [PMID:27698471](../papers/27698471.md)
- [PMID:28045614](../papers/28045614.md)
- [PMID:24892406](../papers/24892406.md)
- [PMID:30325352](../papers/30325352.md)

- [PMID:36038778](../papers/36038778.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23999436](../papers/23999436.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25765070](../papers/25765070.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:27346245](../papers/27346245.md) — Tansir et al. 2025, narrative review of young-onset NSCLC molecular landscape, epidemiology, and therapy.

- [PMID:28445469](../papers/28445469.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29337640](../papers/29337640.md)
- [PMID:29420467](../papers/29420467.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29657128](../papers/29657128.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30150660](../papers/30150660.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30643254](../papers/30643254.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31768066](../papers/31768066.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
