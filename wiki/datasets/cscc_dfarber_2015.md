---
name: Dana-Farber Metastatic Cutaneous SCC Cohort (2015)
studyId: cscc_dfarber_2015
institution: Dana-Farber Cancer Institute / Harvard Medical School
size: 29 patients (26 paired tumor/normal, 3 unpaired) with lymph-node metastatic cSCC
reference_genome: b37
canonical_source: cbioportal
unverified: false
assays:
  - DFCI-ONCOPANEL-1
panels:
  - DFCI-ONCOPANEL-1
tags:
  - cutaneous-squamous-cell-carcinoma
  - metastatic
  - targeted-sequencing
  - hpv-negative
  - uv-mutational-signature
  - oncopanel
  - ras-rtk-pi3k-pathway
  - chromatin-remodeling
processed_by: entity-page-writer
processed_at: 2026-05-14
---

# Dana-Farber Metastatic Cutaneous SCC Cohort (2015)

## Overview

A single-institution cohort from Dana-Farber Cancer Institute profiling 29 lymph-node metastases from patients with cutaneous squamous cell carcinoma (cSCC) — an FDA-orphaned subset with poor prognosis at the metastatic stage. All 29 samples were confirmed HPV-negative by p16 IHC and hybrid-capture sequencing of HPV E6/E7 (Pathogenica). The cohort showed a high UV-associated coding mutation rate (~33 mutations/Mb across the panel) dominated by C>T transitions at pyrimidine dinucleotides. BAM files were submitted to dbGaP. Published in 2015 by Li et al. in *Clinical Cancer Research*.

## Composition

- **n = 29** patients; 19 male / 10 female; median age at metastatic diagnosis 74 (range 48–92); 4 immunocompromised; 12 smokers.
- Primary tumor sites predominantly head and neck; parotid gland the most frequent nodal site.
- 26 samples with matched normal skin; 3 unpaired (the unpaired set showed ~2× the SNV count of paired samples).
- Median progression-free survival 37 months (range 1–130); median overall survival 60 months (range 7–155).
- Cancer type: [CSCC](../cancer_types/CSCC.md).

## Assays / panels (linked)

- [DFCI-ONCOPANEL-1](../methods/DFCI-ONCOPANEL-1.md) — targeted Illumina hybrid-capture of 504 cancer-associated genes, sequenced 100 bp on HiSeq 2500. Mean tumor coverage 82× (range 25–166×); normal mean 69×. Reads aligned to b37 with Picard/Firehose pipeline.
- Variant calling: [mutect](../methods/mutect.md) (SNVs/indels) with OxoG artifact filtering; [oncotator](../methods/oncotator.md) annotation against dbSNP 134 and 1000 Genomes; significance via [mutsig](../methods/mutsig.md) (1.5, 2.0, and CV). CNAs by Nexus 7.5 and [gistic](../methods/gistic.md) 2.0.

## Papers using this cohort

- [PMID:25589618](../papers/25589618.md) — Li et al. (2015). Targeted sequencing of 504 cancer-associated genes on 29 lymph-node metastatic cSCC samples; identified RAS/RTK/PI3K pathway activation and chromatin-remodeling inactivation as independent prognostic markers.

## Notable findings derived from this cohort

- [TP53](../genes/TP53.md) mutated in 23/29 (79%), consistent with HPV-negative status; [CDKN2A](../genes/CDKN2A.md) altered by mutation and homozygous loss in 14/29 (48%). [PMID:25589618](../papers/25589618.md)
- RAS/RTK/PI3K pathway activating mutations present in 11/29 (38%) samples spanning 12 oncogenes ([BRAF](../genes/BRAF.md), [KRAS](../genes/KRAS.md), [HRAS](../genes/HRAS.md), [EGFR](../genes/EGFR.md), [FGFR3](../genes/FGFR3.md), [KIT](../genes/KIT.md), [ERBB4](../genes/ERBB4.md), [MTOR](../genes/MTOR.md), [PIK3CA](../genes/PIK3CA.md), [EZH2](../genes/EZH2.md), [HGF](../genes/HGF.md), [CARD11](../genes/CARD11.md)); events are nearly mutually exclusive. [PMID:25589618](../papers/25589618.md)
- Chromatin-remodeling inactivation ([CREBBP](../genes/CREBBP.md), [EP300](../genes/EP300.md), [KMT2D](../genes/KMT2D.md), [ARID2](../genes/ARID2.md), [ARID1A](../genes/ARID1A.md)) in 48% of samples; independently associated with shorter progression-free survival. [PMID:25589618](../papers/25589618.md)
- Combined RAS/RTK/PI3K activation (excluding EGFR/ERBB4) and chromatin-remodeling inactivation was the strongest prognostic correlate: mean PFS 12 months (pathway-mutated) vs 50 months (non-mutated) vs 79 months (EGFR/ERBB4-mutated). [PMID:25589618](../papers/25589618.md)
- [TP63](../genes/TP63.md) amplified in 7/29 (24%); [MYC](../genes/MYC.md) in 10/29; recurrent 9p21 ([CDKN2A](../genes/CDKN2A.md)/CDKN2B) homozygous deletions in 6/29 (21%). [PMID:25589618](../papers/25589618.md)

## Sources

- [PMID:25589618](../papers/25589618.md)

*This page was processed by **entity-page-writer** on **2026-05-14**.*
