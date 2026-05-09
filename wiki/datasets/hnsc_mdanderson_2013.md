---
name: Oral Squamous Cell Carcinoma — MD Anderson (Pickering 2013)
studyId: hnsc_mdanderson_2013
institution: MD Anderson Cancer Center
size: 40
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - affymetrix-snp6
  - 450k-methylation-array
  - rna-seq
panels: []
tags:
  - HNSC
  - OSCC
  - oral squamous cell carcinoma
  - head and neck
processed_by: crosslinker
processed_at: 2026-05-09
---

# Oral Squamous Cell Carcinoma — MD Anderson (Pickering 2013)

## Overview

Multi-platform integrated genomic study of 40 oral squamous cell carcinomas (OSCC) from patients treated at MD Anderson Cancer Center, by Pickering et al. (Cancer Discovery 2013). Expression and methylation data deposited in GEO under accession GSE41117. [PMID:23619168](../papers/23619168.md)

## Composition

- 40 OSCC patients at MD Anderson Cancer Center; fresh-frozen surgically-resected tumors with matched non-malignant adjacent tissue; >60% tumor nuclei content required. [PMID:23619168](../papers/23619168.md)
- Cancer type: oral squamous cell carcinoma ([OCSC](../cancer_types/OCSC.md)), a subset of head and neck squamous cell carcinoma ([HNSC](../cancer_types/HNSC.md)). [PMID:23619168](../papers/23619168.md)
- Copy-number profiling available for 38/40 tumors; exome sequencing on all 40; methylation and expression on all 40. [PMID:23619168](../papers/23619168.md)

## Assays / panels (linked)

- [affymetrix-snp6](../methods/affymetrix-snp6.md) — SNP arrays on 38 tumors; ASCAT for allele-specific copy number; [gistic](../methods/gistic.md) v2.0.12 for significance. [PMID:23619168](../papers/23619168.md)
- [whole-exome-seq](../methods/whole-exome-seq.md) — Nimblegen capture with SOLiD or Illumina sequencing. [PMID:23619168](../papers/23619168.md)
- [450k-methylation-array](../methods/450k-methylation-array.md) — Illumina HumanMethylation450 arrays. [PMID:23619168](../papers/23619168.md)
- Affymetrix Human Exon 1.0ST mRNA arrays and Agilent Human microRNA microarrays rel12.0. [PMID:23619168](../papers/23619168.md)
- [sanger-sequencing](../methods/sanger-sequencing.md) — validation of [NOTCH1](../genes/NOTCH1.md) and [CASP8](../genes/CASP8.md) alterations in 44 HNSCC cell lines. [PMID:23619168](../papers/23619168.md)

## Papers using this cohort

- [PMID:23619168](../papers/23619168.md) — Pickering et al., "Integrative genomic characterization of oral squamous cell carcinoma identifies frequent somatic drivers," *Cancer Discov* 2013.

## Notable findings derived from this cohort

- Notch pathway altered in 66% (23/35) of tumors; [NOTCH1](../genes/NOTCH1.md) mutated in 9% of primary tumors and functions as tumor suppressor — activated NOTCH1 (ICN1) caused G1 arrest, p21 induction, senescence, and suppressed xenograft growth. [PMID:23619168](../papers/23619168.md)
- [CASP8](../genes/CASP8.md) mutations in 10% (4/40) define a molecular subtype with fewer copy-number alterations and frequent co-occurrence of [HRAS](../genes/HRAS.md) mutations (3/4 CASP8-mutant tumors had [HRAS](../genes/HRAS.md) mutation; p=0.0016); validated in TCGA HNSCC. [PMID:23619168](../papers/23619168.md)
- [FAT1](../genes/FAT1.md) inactivation (mutation or deletion) in 46% of tumors; [TP53](../genes/TP53.md) mutations in 60%, with splice-site mutations markedly enriched (13% vs. 2% baseline across tumor types). [PMID:23619168](../papers/23619168.md)
- Cell-cycle pathway altered in 94% of tumors via [CCND1](../genes/CCND1.md) amplification and/or [CDKN2A](../genes/CDKN2A.md) loss; mitogenic signaling altered in 63%. [PMID:23619168](../papers/23619168.md)
- 80% (28/35) of tumors harbored at least one targetable alteration, 54% had ≥2; top targets include SRC-family kinases (29%), PI3K signaling (34%), and [TNK2](../genes/TNK2.md) (17%). [PMID:23619168](../papers/23619168.md)
- A CIMP-like methylation subgroup identified with higher methylation frequency and fewer CNAs, associated with non-tobacco use. [PMID:23619168](../papers/23619168.md)

## Sources

- GEO: GSE41117 (expression and methylation)
- DOI: 10.1158/2159-8290.CD-12-0537

*This page was processed by **crosslinker** on **2026-05-09**.*
