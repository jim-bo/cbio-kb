---
name: Pediatric Precision Sequencing (PIPseq, Columbia, 2017)
studyId: mixed_pipseq_2017
institution: Columbia University Medical Center
size: 101
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-sequencing
  - rna-seq
  - targeted-panel
panels:
  - columbia-comprehensive-cancer-panel
tags:
  - pediatric
  - pan-cancer
  - precision-medicine
  - germline
  - pipseq
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# Pediatric Precision Sequencing (PIPseq, Columbia, 2017)

## Overview

The Precision in Pediatric Sequencing (PIPseq) program at Columbia University Medical Center is a prospective CLIA-certified clinical genomics program for high-risk pediatric hematology-oncology patients. The study enrolled 101 consecutive patients (mean age 9.3 years; range 2 weeks–26 years; sequenced January 2014–April 2016) who met eligibility criteria including <50% estimated 5-year survival, outlier phenotype, rare cancers without standard-of-care, suspected germline predisposition, or relapsed/refractory disease. VCFs, translocations, and gene expression data were released through cBioPortal under CUMC IRB approval.

## Composition

- **101 patients**, 120 samples (85 primary disease, 35 relapse/refractory); 60% male, 41% female.
- **Solid tumors (64%):** sarcoma (n=17), brain tumors (n=16), and other solid histologies across >20 OncoTree codes including [NBL](../cancer_types/NBL.md), [OS](../cancer_types/OS.md), [ES](../cancer_types/ES.md), [ARMS](../cancer_types/ARMS.md), [MBL](../cancer_types/MBL.md), [WT](../cancer_types/WT.md), [RCC](../cancer_types/RCC.md), [LIHB](../cancer_types/LIHB.md), [HCC](../cancer_types/HCC.md), [ATRT](../cancer_types/ATRT.md), [IMT](../cancer_types/IMT.md).
- **Hematologic disease (36%):** [AML](../cancer_types/AML.md), [BLL](../cancer_types/BLL.md), [JMML](../cancer_types/JMML.md), [AMKL](../cancer_types/AMKL.md), [CML](../cancer_types/CML.md), [TLL](../cancer_types/TLL.md), [ALCL](../cancer_types/ALCL.md), [HL](../cancer_types/HL.md), [PTLD](../cancer_types/PTLD.md).
- **Sequencing platforms (n=120):** cancer WES + transcriptome 63 (53%), cancer WES alone 19 (16%), constitutional WES 22 (18%), transcriptome only 3 (2%), targeted 467-gene panel 13 (11%).
- Reads aligned to GRCh37/hg19; WES achieved >150-fold and targeted capture >500-fold average coverage with >98% of coding sequence at ≥10X.

## Assays / panels (linked)

- [whole-exome sequencing](../methods/whole-exome-seq.md) — Agilent SureSelectXT All Exon V5+UTRs on HiSeq2500 (paired-end 125 cycle ×2); paired tumor/normal.
- [RNA-seq](../methods/rna-seq.md) — TruSeq Stranded Total RNA LT kit; fusion detection via [FusionMap](../methods/fusionmap.md); quantification with [TopHat2/Cufflinks](../methods/tophat-cufflinks.md).
- [Columbia Comprehensive Cancer Panel](../methods/columbia-comprehensive-cancer-panel.md) — 467-gene targeted panel (5.59 Mb custom Agilent SureSelectXT library), optimized for FFPE material, >500-fold average coverage.
- CNV inferred from WES via EXCAVATOR v2.2.

## Papers using this cohort

- [PMID:28007021](../papers/28007021.md) — Oberg et al. 2016. First 101 patients in the PIPseq program; comprehensive characterization of actionable somatic findings (38%), germline predisposition variants (14%), and RNA-seq diagnostic/prognostic impact (70% unique clinical contribution in patients with full cWES+RNA-seq).

## Notable findings derived from this cohort

- Potentially actionable somatic alterations identified in 38/101 patients (38%); only 6/38 (16%) received matched targeted therapy, demonstrating the gap between actionability and treatment access [PMID:28007021](../papers/28007021.md).
- Clinically impactful findings (diagnostic, prognostic, pharmacogenomic, or actionable) in 66/101 patients (66%) overall and 75% (45/60) of those with full cWES + RNA-seq [PMID:28007021](../papers/28007021.md).
- RNA-seq uniquely contributed clinical impact in 23/33 patients (70%) through fusion detection, expression-based subtyping, and BCR-ABL1-like signature identification [PMID:28007021](../papers/28007021.md).
- Germline cancer-predisposition variants in 14/90 patients (14%); ACMG secondary findings returned to six patients ([BRCA1](../genes/BRCA1.md) ×2, [TP53](../genes/TP53.md), [TNNT2](../genes/TNNT2.md), [RYR1](../genes/RYR1.md), [VHL](../genes/VHL.md)) [PMID:28007021](../papers/28007021.md).
- Most frequently mutated genes: [TP53](../genes/TP53.md) in solid tumors (n=9, 9%); RAS-pathway genes in hematologic samples ([NRAS](../genes/NRAS.md) n=5, [KRAS](../genes/KRAS.md) n=3) [PMID:28007021](../papers/28007021.md).
- 94% of consented patients opted in to receive ACMG secondary findings, supporting broad return-of-results policies in pediatric oncology [PMID:28007021](../papers/28007021.md).
- Mean mutational load 216.9 variants per patient (SD 829.3, median 69); lower than adult-cancer benchmarks, higher in solid tumors than hematologic conditions [PMID:28007021](../papers/28007021.md).

## Sources

- cBioPortal study: mixed_pipseq_2017
- CUMC IRB-approved data release (VCFs, translocations, gene expression).

*This page was processed by **entity-page-writer** on **2026-05-15**.*
