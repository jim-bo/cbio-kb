---
name: TRACERx 100 NSCLC Cohort (UCL/CRUK, Nature 2017)
studyId: nsclc_tracerx_2017
institution: University College London / Cancer Research UK
size: 100
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - amplicon-sequencing
  - ctDNA-multiplex-pcr-ngs
  - pet-ct-imaging
panels: []
tags:
  - tracerx
  - nsclc
  - lung-cancer
  - clonal-evolution
  - ctdna
  - multi-region-sequencing
  - prospective
processed_by: crosslinker
processed_at: 2026-05-15
---

# TRACERx 100 NSCLC Cohort (UCL/CRUK, Nature 2017)

## Overview

The TRACERx (TRAcking Cancer Evolution through therapy (Rx)) study is a prospective longitudinal cohort study of non-small cell lung cancer ([NSCLC](../cancer_types/NSCLC.md)) led by the Cancer Research UK Lung Cancer Centre of Excellence at University College London. The nsclc_tracerx_2017 dataset encompasses the first 100 surgically resected early-stage NSCLC patients enrolled in TRACERx (NCT01888601), paired with bespoke multiplex-PCR ctDNA profiling. Multi-region whole-exome sequencing of 327 spatially separated primary tumor regions (plus 4 metastatic biopsies) enables reconstruction of clonal and subclonal tumor architecture, which is then tracked longitudinally in plasma via patient-specific ctDNA panels (precursor to the Signatera assay, designed by Natera). This foundational dataset established that ctDNA can detect NSCLC relapse with a median 70-day lead-time over CT imaging.

## Composition

- **100 patients**, 96 evaluable for pre-operative ctDNA; 24-patient longitudinal sub-cohort with pre- and post-surgical plasma profiling.
- **Histologies:** 58 [LUAD](../cancer_types/LUAD.md), 31 [LUSC](../cancer_types/LUSC.md), 7 other NSCLC.
- **Tumor genomics:** 327 spatially separated primary tumor regions + 4 metastatic biopsies; whole-exome sequencing (Illumina); copy number / purity / ploidy via ASCAT; subclonal deconvolution via PyClone; phylogenetic tree reconstruction with CITUP.
- **ctDNA:** Bespoke patient-specific multiplex-PCR NGS panels (median 18 SNVs pre-operative; expanded to median 28 SNVs for LUAD longitudinal phase), sequenced to ~40,000× target depth on Illumina HiSeq 2500. Analytical sensitivity >99% at VAF ≥0.1%; specificity 99.6% per SNV.
- **Imaging:** Pre-operative PET/CT in 92/96 patients; 3D tumor volume measured via CT.
- **Data deposition:** EGA accessions EGAS00001002247 (primary) and EGAS00001002415 (metastatic).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — multi-region tumor exome sequencing.
- [multiregion-exome-seq](../methods/multiregion-exome-seq.md) — TRACERx M-Seq pipeline.
- [amplicon-sequencing](../methods/amplicon-sequencing.md) — bespoke ctDNA panels.
- [ascat](../methods/ascat.md) — copy-number / purity / ploidy.
- [pyclone](../methods/pyclone.md) — subclonal deconvolution.
- [phylogenetic-tree-reconstruction](../methods/phylogenetic-tree-reconstruction.md) — CITUP + manual.
- [pet-ct-imaging](../methods/pet-ct-imaging.md) — pre-operative staging.

## Papers using this cohort

- [PMID:28445469](../papers/28445469.md) — Abbosh et al., *Nature* 2017: First ctDNA analysis from TRACERx; bespoke multiplex-PCR plasma profiling of 96 early-stage NSCLC patients detected relapse with 93% sensitivity and a median 70-day lead-time over imaging; established histology (LUSC vs LUAD) as the dominant predictor of pre-operative ctDNA detectability. [PMID:28445469](../papers/28445469.md)

## Notable findings derived from this cohort

- Pre-operative ctDNA detection rate is strongly histology-dependent: 97% (30/31) of LUSC vs 19% (11/58) of LUAD; independent predictors include non-adenocarcinoma histology, lymphovascular invasion, and high Ki67. [PMID:28445469](../papers/28445469.md)
- Tumor volume correlates linearly with mean clonal plasma VAF (Spearman's ρ = 0.63, P<0.001, n=37); a 10 cm³ primary tumor predicts a mean clonal VAF of 0.1%. [PMID:28445469](../papers/28445469.md)
- Post-operative ctDNA detected confirmed NSCLC relapse in 13/14 (93%) patients, with a median lead-time of 70 days (range 10–346 days) over CT-confirmed relapse. [PMID:28445469](../papers/28445469.md)
- Phylogenetic ctDNA tracking resolved clonal architecture of metastatic seeding; a subclone harboring an [ERBB2](../genes/ERBB2.md) amplification (>15 copies) was identified as driving relapse in patient CRUK0004. [PMID:28445469](../papers/28445469.md)
- An expanded 103-SNV panel detected ctDNA in a post-mortem case 189 days earlier than the 19-SNV panel, demonstrating that panel breadth substantially improves MRD sensitivity. [PMID:28445469](../papers/28445469.md)

## Sources

- cBioPortal study `nsclc_tracerx_2017`.
- Abbosh C, et al. *Phylogenetic ctDNA analysis depicts early-stage lung cancer evolution.* Nature. 2017;545:446–451. [PMID:28445469](../papers/28445469.md)

*This page was processed by **crosslinker** on **2026-05-15**.*
