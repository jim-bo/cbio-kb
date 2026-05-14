---
name: Cutaneous T-Cell Lymphoma — Columbia 2015
studyId: ctcl_columbia_2015
institution: Columbia University / Northwestern University / Leiden University Medical Center
size: 42
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - copy-number-array
panels: []
tags:
  - cutaneous-t-cell-lymphoma
  - sezary-syndrome
  - mycosis-fungoides
  - SS
  - MYCF
  - lymphoma
  - epigenetic-regulators
processed_by: crosslinker
processed_at: 2026-05-14
---

# Cutaneous T-Cell Lymphoma — Columbia 2015

## Overview

Whole-exome sequencing of 42 tumor-normal pairs from cutaneous T-cell lymphoma (CTCL) patients — 25 Sézary syndrome ([SS](../cancer_types/SS.md)) and 17 other CTCL including 8 mycosis fungoides ([MYCF](../cancer_types/MYCF.md)) — collected across Northwestern University (Chicago) and Leiden University Medical Center. Raw data deposited in dbGaP under accession phs000994.v1.p1. Reference genome hg19.

## Composition

- 25 Sézary syndrome samples: peripheral-blood [CD4](../genes/CD4.md)+ T cells as tumor; granulocytes or buccal swab as matched normal.
- 17 other CTCL samples (8 mycosis fungoides, 9 other CTCL): skin biopsies as tumor; buccal swab as normal.
- Cancer types: [SS](../cancer_types/SS.md) (Sézary syndrome), [MYCF](../cancer_types/MYCF.md) (mycosis fungoides).
- Agilent SureSelect 50 Mb All Exon kit; Illumina HiSeq2000, paired-end 2×100 bp; mean depth 143.5×, 95.3% of targets covered >30×.
- Copy-number analysis: EXCAVATOR (pooled or somatic mode).
- Variant calling: SAVI Bayesian framework; somatic variants retained at ≥15% VAF, absent in normal.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) (Agilent SureSelect 50 Mb; Illumina HiSeq2000; hg19)
- [bwa](../methods/bwa.md) (v0.5.9 alignment to hg19)
- [mutational-signatures](../methods/mutational-signatures.md) (Alexandrov 2013 NMF framework; three signatures identified)

## Papers using this cohort

- [PMID:26551667](../papers/26551667.md) — da Silva Almeida et al. 2015, "The mutational landscape of cutaneous T-cell lymphoma and Sézary syndrome," *Nature Genetics*.

## Notable findings derived from this cohort

- Sézary syndrome dominated by chromosomal deletions of tumor suppressors: [TP53](../genes/TP53.md) 17p13.1 (52%), [PTEN](../genes/PTEN.md) 10q23.3 (20%), [CDKN1B](../genes/CDKN1B.md) 12p13.1 (20%), [RB1](../genes/RB1.md) 13q14.2 (16%), and [DNMT3A](../genes/DNMT3A.md) 2p23.3 (20%, including two homozygous deletions) [PMID:26551667](../papers/26551667.md).
- Recurrent mutations in epigenetic regulators: [TET2](../genes/TET2.md), [CREBBP](../genes/CREBBP.md), [KMT2D](../genes/KMT2D.md), [KMT2C](../genes/KMT2C.md), [BRD9](../genes/BRD9.md), [SMARCA4](../genes/SMARCA4.md), [CHD3](../genes/CHD3.md) in Sézary syndrome; [SMARCA4](../genes/SMARCA4.md) and KMT2D/KMT2C in mycosis fungoides [PMID:26551667](../papers/26551667.md).
- TCR-signaling effector mutations activating MAPK, NFkB, and NFAT pathways: [MAPK1](../genes/MAPK1.md) p.E322K/A (mycosis fungoides), [BRAF](../genes/BRAF.md) p.K601E, [CARD11](../genes/CARD11.md) linker-domain mutations (p.S615F, p.E626K) as NFkB activators, [PRKG1](../genes/PRKG1.md) N-terminal LoF mutations, [JAK3](../genes/JAK3.md) p.V678L with [SH2B3](../genes/SH2B3.md) LoF [PMID:26551667](../papers/26551667.md).
- Median 39 non-synonymous somatic mutations per Sézary syndrome sample; median 21 CNAs per sample (range 0–56) [PMID:26551667](../papers/26551667.md).
- Three mutational signatures in Sézary syndrome: C>T at NpCpG (CpG deamination/aging), C>A at CpCpN, and C>T at CpCpN/TpCpN [PMID:26551667](../papers/26551667.md).
- CTCL cell lines (HH, HUT78, HUT102, SeAX) broadly sensitive to NFkB inhibition (Mi-2, [bortezomib](../drugs/bortezomib.md)); JAK3-mutant HUT78 line responsive to [tofacitinib](../drugs/tofacitinib.md) and [ruxolitinib](../drugs/ruxolitinib.md) [PMID:26551667](../papers/26551667.md).

## Sources

- [PMID:26551667](../papers/26551667.md)
- dbGaP: phs000994.v1.p1

*This page was processed by **crosslinker** on **2026-05-14**.*
