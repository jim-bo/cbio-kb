---
name: "Endometrial Carcinoma cfDNA (MSK, Clin Cancer Res 2022)"
studyId: ucec_ccr_cfdna_msk_2022
institution: "Memorial Sloan Kettering Cancer Center"
size: 44
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-ngs
  - liquid-biopsy
panels:
  - IMPACT468
  - ACCESS129
tags:
  - UCEC
  - endometrial-cancer
  - cfDNA
  - ctDNA
  - liquid-biopsy
  - MRD
  - longitudinal
  - MSK-ACCESS
  - MSK-IMPACT
processed_by: crosslinker
processed_at: 2026-05-21
---

# Endometrial Carcinoma cfDNA (MSK, Clin Cancer Res 2022)

## Overview

`ucec_ccr_cfdna_msk_2022` is a prospective proof-of-principle liquid-biopsy study from Memorial Sloan Kettering testing whether high-sensitivity, UMI-based cell-free DNA (cfDNA) sequencing can capture the mutational repertoire of primary endometrial cancer and enable longitudinal disease monitoring. It enrolled 44 newly diagnosed endometrial cancer patients with serial pre- and post-surgical plasma collections over 24 months. Primary tumors were profiled by MSK-IMPACT (468 genes) and matched cfDNA by MSK-ACCESS (129-gene high-depth, molecular-barcoded assay). The dataset is notable as one of the first systematic longitudinal ctDNA monitoring studies in endometrial cancer with both tissue and plasma profiling on matched patients.

## Composition

- **44 prospectively accrued, biopsy-confirmed newly diagnosed [endometrial cancer (UCEC)](../cancer_types/UCEC.md) patients** consented at MSK between 09/2017 and 07/2018 [PMID:36007103](../papers/36007103.md).
- **Stage:** FIGO stage I in 34/44 (77%); advanced stage III/IV in 10/44 (23%).
- **Histology:** Endometrioid ([UEC](../cancer_types/UEC.md)) 24/44 (55%); serous carcinoma ([USC](../cancer_types/USC.md)) 7/44 (16%); carcinosarcoma ([UCS](../cancer_types/UCS.md)) 6/44 (14%); remaining cases include high-grade carcinomas and adenosarcoma.
- **Tissue NGS:** 42 primary ECs profiled with [MSK-IMPACT 468-gene panel](../methods/IMPACT468.md) (median tumor depth 618×, range 101–1,030×; matched normal 504×). Six stage III/IV cases had extra-uterine sites sequenced (sentinel lymph nodes, peritoneal implants, fallopian tube).
- **cfDNA NGS:** 36 patients with adequate plasma input (10–20 ng cfDNA) sequenced on [MSK-ACCESS](../methods/ACCESS129.md), a 129-gene UMI-based liquid-biopsy assay (median raw coverage 25,611×; median duplex coverage 1,340× post-collapsing).
- **Longitudinal:** Blood drawn at baseline (pre-op), post-op (median 22 days, range 9–57), and every 6 months to 24 months; 229/258 (89%) intended draws collected despite COVID-19 disruption. Serial samples from 25 patients sequenced.
- **Follow-up:** Median 33 months (range 0.3–44); 11 patients had recurrent or persistent disease.
- TCGA molecular subtypes: 10/42 (24%) MSI; 12/42 (29%) copy-number low; 20/42 (48%) copy-number high.

## Assays / panels (linked)

- [MSK-IMPACT 468-gene panel](../methods/IMPACT468.md) — primary tumor tissue sequencing, 468 cancer-related genes; tumor-normal paired.
- [MSK-ACCESS](../methods/ACCESS129.md) — 129-gene UMI-based cfDNA assay with molecular barcoding; tumor-informed genotyping via Waltz (≥2 duplex consensus reads required); supports variant detection at ~0.1% tumor-informed / ~0.5% de novo allele frequency.

## Papers using this cohort

- [PMID:36007103](../papers/36007103.md) — Ashley et al., Clin Cancer Res 2022/2023: primary publication establishing the prospective cfDNA monitoring framework in newly diagnosed endometrial cancer and demonstrating prognostic utility of baseline and post-surgery ctDNA.

## Notable findings derived from this cohort

- Baseline ctDNA detected in 8/36 (22%) patients sequenced; 6/8 had stage III/IV disease; no low-grade stage I endometrioid patients had detectable baseline ctDNA; 92% (35/38) of primary-tumor mutations covered by MSK-ACCESS were detected in baseline plasma [PMID:36007103](../papers/36007103.md).
- Detectable baseline ctDNA was significantly associated with worse progression-free survival: **HR 11.14 (95% CI 2.72–45.59, p<0.001)**; detectable post-surgical ctDNA was also strongly prognostic: **HR 15.56 (95% CI 2.16–112.16, p=0.014)** in landmark analysis [PMID:36007103](../papers/36007103.md).
- Serial ctDNA tracked imaging-confirmed disease progression and response in 6/25 patients with longitudinal sampling; rising ctDNA preceded imaging-detected recurrence by up to 6 months and elevated serum CA125 by 5.8–17 months in selected cases [PMID:36007103](../papers/36007103.md).
- Primary tumor mutational landscape recapitulated TCGA: most frequently mutated genes were [TP53](../genes/TP53.md) (52%), [PTEN](../genes/PTEN.md) (50%), [PIK3CA](../genes/PIK3CA.md) (50%), [ARID1A](../genes/ARID1A.md) (36%), [FBXW7](../genes/FBXW7.md) (29%) [PMID:36007103](../papers/36007103.md).
- Tumor–lymph node spatial heterogeneity was documented in stage III/IV cases: mutations subclonal in the primary (e.g., [ARID1A](../genes/ARID1A.md), [PIK3CA](../genes/PIK3CA.md), [KRAS](../genes/KRAS.md)) became clonal in sentinel lymph nodes, and some mutations were restricted to nodal compartments; baseline cfDNA more faithfully captured primary-tumor mutations than lymph-node-private mutations [PMID:36007103](../papers/36007103.md).

## Sources

- cBioPortal study: `ucec_ccr_cfdna_msk_2022`

*This page was processed by **crosslinker** on **2026-05-21**.*
