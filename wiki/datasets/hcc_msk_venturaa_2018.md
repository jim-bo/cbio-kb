---
name: Liver Hepatocellular Adenoma and Carcinomas (MSK, PLOS One 2018)
studyId: hcc_msk_venturaa_2018
institution: Memorial Sloan Kettering Cancer Center
size: 21
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-panel
  - mirna-seq
  - immunohistochemistry
panels:
  - IMPACT341
tags:
  - hcc
  - hepatocellular-carcinoma
  - hepatocellular-adenoma
  - liad
  - msk
  - ventura-lab
processed_by: crosslinker
processed_at: 2026-05-16
---

# Liver Hepatocellular Adenoma and Carcinomas (MSK, PLOS One 2018)

## Overview

A pilot study cohort of 21 patients — 11 hepatocellular adenomas (HCA/[LIAD](../cancer_types/LIAD.md)) and 10 hepatocellular carcinomas ([HCC](../cancer_types/HCC.md)) — resected at Memorial Sloan Kettering Cancer Center between 1999 and 2013. Patients were explicitly selected without underlying viral hepatitis, prior liver-directed therapy, or cirrhosis, excluding the carcinogenic field effect common in hepatitis-associated [HCC](../cancer_types/HCC.md). Assembled by Zheng, Sadot, and colleagues in the Ventura lab (MSK) to characterize miRNA and DNA mutation differences between benign HCA and malignant HCC.

## Composition

- 11 HCA ([LIAD](../cancer_types/LIAD.md)): median age 40 (range 24–56), 91% female, 64% with oral contraceptive use history. Subtypes: inflammatory I-HCA n=6 (54%), steatotic H-HCA n=4 (37%), β-catenin B-HCA n=1 (9%).
- 10 HCC ([HCC](../cancer_types/HCC.md)): median age 73 (range 63–81), 40% female; median AFP 15 ng/mL (range 1.9–92,881).
- 9 HCA + 10 HCC underwent MSK-IMPACT 341-gene targeted DNA sequencing (HCA1 and HCA9 lacked sufficient tissue for IMPACT).
- All 21 samples underwent small RNA sequencing (Illumina HiSeq, TruSeq Small RNA kit, ~11.5M reads/sample, aligned with BWA-MEM to hg19/b37).
- IHC for β-catenin, LFABP, SAA, CRP, and glutamine synthetase performed for HCA subtype classification.

## Assays / panels (linked)

- [IMPACT341](../methods/IMPACT341.md) — targeted DNA sequencing of 341 cancer-relevant genes; matched tumor/normal pairs; ~735× mean coverage.
- [mirna-seq](../methods/mirna-seq.md) — small RNA sequencing for microRNA profiling.
- [immunohistochemistry](../methods/immunohistochemistry.md) — HCA subtype classification (β-catenin, LFABP, SAA, CRP, glutamine synthetase).
- [bwa](../methods/bwa.md) — read alignment to hg19/b37; GATK realignment for variant calling.

## Papers using this cohort

- [PMID:30052636](../papers/30052636.md) — Zheng et al. PLOS ONE 2018: "Characterization of hepatocellular adenoma and carcinoma using microRNA profiling and targeted gene sequencing."

## Notable findings derived from this cohort

- [HNF1A](../genes/HNF1A.md) was the most frequently mutated gene in HCA (3/9 IMPACT-sequenced), all in steatotic H-HCA with LFABP loss by IHC; [TERT](../genes/TERT.md) promoter mutations dominated HCC (7/10) and were absent in all HCA [PMID:30052636](../papers/30052636.md).
- [CTNNB1](../genes/CTNNB1.md) mutations occurred in 1/9 HCA (B-HCA subtype) and 2/10 HCC; both HCC CTNNB1-mutant cases co-carried [TERT](../genes/TERT.md) promoter mutations, supporting [CTNNB1](../genes/CTNNB1.md) as an early event and [TERT](../genes/TERT.md) as a late malignant-transformation step [PMID:30052636](../papers/30052636.md).
- Six miRNAs (miR-200a, miR-429, miR-490-3p down; miR-452, miR-766, miR-1180 up) are concordantly deregulated in both HCA and HCC vs. adjacent normal liver, proposed as candidate adenoma-carcinoma-sequence biomarkers [PMID:30052636](../papers/30052636.md).
- C19MC cluster members (miR-515-5p, miR-517a, miR-518b, miR-520c-3p) are 3–4 fold higher in HCC than in HCA or normal liver, proposed as a malignant-transformation marker; chr19q13.41 is not covered by [IMPACT341](../methods/IMPACT341.md), so copy-number drivers could not be assessed [PMID:30052636](../papers/30052636.md).

## Sources

- cBioPortal study: `hcc_msk_venturaa_2018`
- Citation: Zheng et al. PLOS ONE 2018; DOI: 10.1371/journal.pone.0200776

*This page was processed by **crosslinker** on **2026-05-16**.*
