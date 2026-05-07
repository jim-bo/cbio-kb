---
name: Broad/DFCI Cutaneous Melanoma WGS (skcm_broad_dfarber)
studyId: skcm_broad_dfarber
institution: Broad Institute / Dana-Farber Cancer Institute (DFCI) and multiple contributing institutions
size: 25
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - STRUCTURAL_VARIANT
panels: []
tags:
  - melanoma
  - SKCM
  - WGS
  - PREX2
  - structural rearrangements
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Broad/DFCI Cutaneous Melanoma WGS (skcm_broad_dfarber)

## Overview

The Broad/DFCI melanoma WGS dataset comprises 25 metastatic cutaneous melanomas with matched germline DNA, sequenced at 59-fold tumor and 32-fold normal haploid coverage. Sequencing used Illumina GAIIx (5 cases) and Illumina HiSeq 2000 (20 cases) with paired-end 101-nt reads aligned to hg19 with BWA. An extension cohort of 107 tumor/normal pairs (45 tumors + 62 short-term cultures) was screened by bidirectional Sanger sequencing of 40 [PREX2](../genes/PREX2.md) exons. Data are available at dbGaP (phs000452.v1.p1).

## Composition

- 25 metastatic cutaneous melanoma/germline pairs (discovery)
- 107 tumor/normal pairs (extension cohort; Sanger sequencing of PREX2 exons)
- Cancer type: [SKCM](../cancer_types/SKCM.md) (includes 2 acral and 23 trunk/non-acral melanomas)
- Somatic mutation rates varied nearly 100-fold (acral: 3-14/Mb; trunk: 5-55/Mb; hypermutated: 111/Mb)

## Assays / panels (linked)

- [Whole-genome sequencing](../methods/whole-genome-seq.md)
- [Sanger sequencing](../methods/sanger-sequencing.md) (extension cohort validation)
- [FISH](../methods/fish.md) (copy-number validation)

## Papers using this cohort

- [PMID:22622578](../papers/22622578.md)

## Notable findings derived from this cohort

- PREX2 was recurrently mutated in 11/25 discovery tumors and 14% of the 107-sample extension cohort; truncated and point-mutant PREX2 variants accelerated in vivo tumor formation in PMEL-NRAS* melanocytes [PMID:22622578](../papers/22622578.md)
- [BRAF](../genes/BRAF.md) V600E present in 16/25 tumors (64%); [NRAS](../genes/NRAS.md) mutated in 9/25 (36%); BRAF and NRAS mutations were mutually exclusive [PMID:22622578](../papers/22622578.md)
- Average of 97 structural rearrangements per genome (range 6-420); chromothripsis observed in select tumors; recurrently rearranged genes include [PTEN](../genes/PTEN.md) (4), [FHIT](../genes/FHIT.md) (6), [MACROD2](../genes/MACROD2.md) (5) [PMID:22622578](../papers/22622578.md)
- C>T transitions consistent with UV mutagenesis dominated high-mutation-rate tumors (93% in hypermutated ME009 vs. 36% in acral ME015) [PMID:22622578](../papers/22622578.md)

## Sources

- [PMID:22622578](../papers/22622578.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
