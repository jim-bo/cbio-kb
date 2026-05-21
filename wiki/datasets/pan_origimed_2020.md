---
name: "China Pan-cancer (OrigiMed, Nature 2022)"
studyId: pan_origimed_2020
institution: "OrigiMed / Multiple Chinese cancer centers"
size: 10194
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-ngs
panels:
  - csys-450-gene-panel
tags:
  - pan-cancer
  - Chinese
  - Asian
  - NSCLC
  - actionability
  - TMB
  - MSI
  - OncoKB
processed_by: crosslinker
processed_at: 2026-05-21
---

# China Pan-cancer (OrigiMed, Nature 2022)

## Overview

`pan_origimed_2020` is the largest pan-cancer genomic landscape study of an Asian (predominantly Chinese, 92% Han) population to date. Conducted under CLIA/CAP-certified conditions at OrigiMed, it profiled 10,194 solid-tumor patients across 25 principal tumor types using the OrigiMed CSYS 450-gene NGS panel (~2.6 Mb coding exons + [TERT](../genes/TERT.md) promoter + 39 fusion-prone gene introns). The dataset enables systematic comparison of mutation spectrum, TMB, MSI, fusions, and actionable variants between Chinese and Western (MSK-IMPACT 2017 comparator) solid-tumor cohorts. Data were deposited on cBioPortal as `pan_origimed_2020`.

## Composition

- **10,194 tumor + matched-blood pairs** (88% of 11,553 screened; remainder excluded for insufficient tumor content, low DNA yield, or sequencing failure) [PMID:35871175](../papers/35871175.md).
- **25 principal tumor types, >100 subtypes;** 31 ethnicities (92% Han Chinese).
- Geography: 41% East China, 29% South China.
- Stage: 55% advanced (III/IV), 35% early (pre-cancer or stage I/II).
- Treatment status: 76% treatment-naive, 16% pretreated, 8% unknown.
- Top tumor types: [NSCLC](../cancer_types/NSCLC.md) 20%, [COADREAD](../cancer_types/COADREAD.md) 12%, [LIHC](../cancer_types/LIHC.md) 11%, [STAD](../cancer_types/STAD.md) 8%, [ESCA](../cancer_types/ESCA.md) 6%, [STS](../cancer_types/STS.md) 6%, [IHCH](../cancer_types/IHCH.md) 5%, [PAAD](../cancer_types/PAAD.md) 5%.
- **Sequencing:** Illumina NextSeq 500 / NovaSeq 6000; median tumor unique coverage 1,202×; matched normal mean unique coverage 300×.
- **Variant calling:** SNVs via MuTect, InDels via Pindel, CNVs via EXCAVATOR, fusions via in-house algorithm; all variants manually reviewed in IGV.

## Assays / panels (linked)

- OrigiMed CSYS 450-gene NGS panel — targets ~2.6 Mb of coding exons of 450 cancer-related genes plus TERT promoter and [select](../methods/select.md) introns of 39 rearrangement-prone genes; CLIA-certified, CAP-accredited.
- PD-L1 IHC with anti-PD-L1 clone 28-8 (Abcam ab205921, 1:300); TPS ≥1% positive.

## Papers using this cohort

- [PMID:35871175](../papers/35871175.md) — Wu et al., Nature 2022: primary publication describing the pan-cancer landscape, propensity-matched comparison with [msk_impact_2017](../datasets/msk_impact_2017.md), and OncoKB actionability analysis.

## Notable findings derived from this cohort

- 80,703 SNVs/InDels, 19,192 truncations, 17,779 gene amplifications, 1,688 homozygous deletions, and 3,111 gene fusions/rearrangements were catalogued; top altered genes pan-cohort were [TP53](../genes/TP53.md) (58%), [KRAS](../genes/KRAS.md) (18%), [TERT](../genes/TERT.md) (14%), [EGFR](../genes/EGFR.md) (13%), [APC](../genes/APC.md) (13%), [CDKN2A](../genes/CDKN2A.md) (12%), [PIK3CA](../genes/PIK3CA.md) (11%) [PMID:35871175](../papers/35871175.md).
- Propensity-score-matched comparison with [msk_impact_2017](../datasets/msk_impact_2017.md) (n=2,820 per arm, 15 tumor types, 266 shared genes) found only 12 significantly different tumor-type:gene pairs (FDR<0.05), with the largest differences being [EGFR](../genes/EGFR.md) enrichment in Chinese [LUAD](../cancer_types/LUAD.md) and [KEAP1](../genes/KEAP1.md) depletion in Chinese [LUAD](../cancer_types/LUAD.md) vs Western [PMID:35871175](../papers/35871175.md).
- 64% of patients (n=6,498) harbored at least one OncoKB Level 1–4 actionable variant including TMB-H; 513 fusion events detected spanning 31 driver genes, with novel partner genes identified for [ROS1](../genes/ROS1.md), [BRAF](../genes/BRAF.md), [MET](../genes/MET.md), [NTRK3](../genes/NTRK3.md), and [ALK](../genes/ALK.md) [PMID:35871175](../papers/35871175.md).
- Combined IO biomarker positivity (MSI-H OR TMB-H OR PD-L1 TPS≥1%) in 30.3% (824/2,723) of evaluable tumors; MSI-H in ~2% (186/~10,194), with 55% of MSI-H cases in [COADREAD](../cancer_types/COADREAD.md) [PMID:35871175](../papers/35871175.md).
- Unusual co-occurrence of [EGFR](../genes/EGFR.md) and [KRAS](../genes/KRAS.md) at SNV/InDel and CNV level in [NSCLC](../cancer_types/NSCLC.md) — atypical relative to canonical mutual exclusivity in Western [LUAD](../cancer_types/LUAD.md) — was flagged as a potential subclonal [admixture](../methods/admixture.md) or ethnic-selection artifact requiring single-cell resolution [PMID:35871175](../papers/35871175.md).

## Sources

- cBioPortal study: `pan_origimed_2020`

*This page was processed by **crosslinker** on **2026-05-21**.*
