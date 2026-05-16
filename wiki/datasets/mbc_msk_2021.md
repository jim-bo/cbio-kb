---
name: MSK Metaplastic Breast Cancer Cohort (MSK, npj Breast Cancer 2021)
studyId: mbc_msk_2021
institution: Memorial Sloan Kettering Cancer Center
size: 19
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - msk-impact-panel
panels:
  - IMPACT341
  - IMPACT468
tags:
  - metaplastic-breast-cancer
  - triple-negative
  - TERT-promoter
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Metaplastic Breast Cancer Cohort (MSK, npj Breast Cancer 2021)

## Overview

Sequencing dataset of 19 previously unreported primary [metaplastic breast cancers](../cancer_types/MBC.md) ([MBCs](../cancer_types/MBC.md)) from Memorial Sloan Kettering Cancer Center, released as part of a study characterizing TERT somatic alterations across 60 MBCs in total. The 19 newly reported cases consist of 5 whole-exome sequencing (WES) samples and 14 MSK-IMPACT targeted panel samples; 3 of the MSK-IMPACT cases were previously reported in [msk_impact_2017](../datasets/msk_impact_2017.md). This dataset was released to enable community-wide access to genomic data from this rare and aggressive breast cancer subtype. [PMID:33863915](../papers/33863915.md)

## Composition

- Cancer type: metaplastic breast cancer ([MBC](../cancer_types/MBC.md)); 95% triple-negative phenotype, 92% histologic grade 3.
- 19 newly reported MBC cases: 5 WES + 14 MSK-IMPACT targeted sequencing.
- Histologic subtypes across the broader 60-sample cohort: squamous 23% (14/60), spindle cell 27% (16/60), osseous 8% (5/60), chondroid 42% (25/60).
- Combined with 41 previously published MBCs for analysis totaling 60 primary tumors; median patient age 57 (range 34–85). [PMID:33863915](../papers/33863915.md)

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md) (WES, n=5): reads aligned with [BWA](../methods/bwa.md) v0.7.15 to GRCh37; variants called with [MuTect](../methods/mutect.md), [Strelka](../methods/strelka.md), VarScan2, Platypus, Lancet, Scalpel.
- [MSK-IMPACT](../methods/msk-impact-panel.md) 341–468-gene targeted panel (n=14): CCFs computed with [ABSOLUTE](../methods/absolute.md); CNAs/LOH via [FACETS](../methods/facets.md).
- Mutational signatures analyzed with [SigMA](../methods/sigma-mutational-signatures.md) and [DeconstructSigs](../methods/deconstructsigs.md). [PMID:33863915](../papers/33863915.md)

## Papers using this cohort

- [PMID:33863915](../papers/33863915.md) — da Silva et al., *npj Breast Cancer* 2021: Characterized TERT promoter hotspot mutations and gene amplification in 60 primary MBCs; TERT alterations found in 17% (10/60), significantly less frequent in chondroid-predominant MBCs (0/25) than other subtypes (p=0.005); mutually exclusive with TP53 (p<0.001) and co-occurring with PIK3CA hotspots (p=0.001). [PMID:33863915](../papers/33863915.md)

## Notable findings derived from this cohort

- TERT promoter hotspot C228T detected in 9/60 MBCs (15%) and TERT gene amplification in 1/60 (2%); all TERT-altered cases were triple-negative. [PMID:33863915](../papers/33863915.md)
- TERT alterations were significantly less frequent in chondroid-predominant MBCs (0/25) vs other subtypes (10/35; p=0.005, Fisher's exact). [PMID:33863915](../papers/33863915.md)
- TERT alterations were mutually exclusive with [TP53](../genes/TP53.md) mutations (CoMEt p<0.001) and significantly co-occurred with clonal [PIK3CA](../genes/PIK3CA.md) hotspot mutations (83% vs 13%; p=0.001). [PMID:33863915](../papers/33863915.md)
- TERT-altered MBCs had significantly lower fraction genome altered (median 22% vs 54%; p=0.002); no significant TMB difference (p=0.72). [PMID:33863915](../papers/33863915.md)
- 60% of MBCs displayed dominant HRD-associated COSMIC signatures 3 and 8; 34% showed aging signatures 1/5. [PMID:33863915](../papers/33863915.md)

## Sources

- cBioPortal study `mbc_msk_2021`.
- da Silva EM, et al. *TERT promoter hotspot mutations and gene amplification in metaplastic breast cancer.* npj Breast Cancer. 2021. [PMID:33863915](../papers/33863915.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
