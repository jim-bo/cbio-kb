---
name: TCGA Head and Neck Squamous Cell Carcinoma (2015)
studyId: hnsc_tcga_pub
institution: The Cancer Genome Atlas Network (multi-institutional)
size: 279 head and neck squamous cell carcinomas with complete multi-platform data
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - mirna-seq
  - affymetrix-snp6
  - hm450-methylation-array
  - rppa
panels: []
tags:
  - tcga
  - head-neck
  - squamous
  - hpv
  - smoking
  - oral-cavity
  - oropharynx
  - larynx
  - multi-platform
  - apobec-mutagenesis
  - chromatin-remodeling
  - notch-signaling
  - wnt-signaling
  - pi3k-akt-mtor
processed_by: crosslinker
processed_at: 2026-05-14
---

# TCGA Head and Neck Squamous Cell Carcinoma (2015)

## Overview

The Cancer Genome Atlas (TCGA) multi-platform genomic characterization of 279 head and neck squamous cell carcinomas (HNSCC), published in *Nature* in 2015. The study profiled tumors from oral cavity (62%), larynx (26%), and oropharynx (12%) with whole-exome sequencing (mean coverage 95×), supplemented by low-pass whole-genome sequencing (n=29), RNA-seq, miRNA-seq, DNA methylation (HM450), RPPA, and SNP6.0 arrays. The cohort defines two major disease biologies based on HPV status: HPV-positive (n=36) and HPV-negative (n=243) tumors, with distinct mutational landscapes, copy-number profiles, and mRNA expression subtypes.

## Composition

- **n=279** HNSCC with complete multi-platform data (drawn from a larger 500-tumour TCGA target).
- Anatomic sites: oral cavity 172 (62%), larynx 72 (26%), oropharynx 33 (12%), plus rare hypopharynx cases.
- Predominantly male (73%) and heavy smokers (mean 51 pack-years).
- HPV status by RNA-seq E6/E7 mapping (threshold >1,000 reads): 36 HPV(+), 243 HPV(−). 64% of oropharyngeal tumours HPV(+) vs 6% of non-oropharyngeal tumours.
- Cancer types: [HNSC](../cancer_types/HNSC.md), [OCSC](../cancer_types/OCSC.md), [OPHSC](../cancer_types/OPHSC.md), [LXSC](../cancer_types/LXSC.md), [HPHSC](../cancer_types/HPHSC.md).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — mean 95× coverage, 82% of target bases ≥30×; all 279 tumors.
- [whole-genome-seq](../methods/whole-genome-seq.md) — high-coverage, n=29 tumors for structural-variant detection.
- [rna-seq](../methods/rna-seq.md) — mRNA expression and HPV integration detection.
- [mirna-seq](../methods/mirna-seq.md) — miRNA profiling.
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — copy-number alteration calls.
- [hm450-methylation-array](../methods/hm450-methylation-array.md) — DNA methylation profiling.
- [rppa](../methods/rppa.md) — reverse-phase protein array.
- Analytic tools: [mutsig](../methods/mutsig.md) (MutSigCV) for significantly mutated genes; [gistic](../methods/gistic.md) for focal CNAs.

## Papers using this cohort

- [PMID:25631445](../papers/25631445.md) — TCGA Network (2015). Comprehensive genomic characterization of 279 HNSCCs; identified 11 significantly mutated genes (MutSigCV q < 0.1), HPV(+)/HPV(−) biologic dichotomy, four mRNA subtypes, and candidate therapeutic alterations in most tumors.

## Notable findings derived from this cohort

- Eleven significantly mutated genes (MutSigCV q < 0.1): [TP53](../genes/TP53.md) 72%, [FAT1](../genes/FAT1.md) 23%, [CDKN2A](../genes/CDKN2A.md) 22%, [PIK3CA](../genes/PIK3CA.md) 21%, [NOTCH1](../genes/NOTCH1.md) 19%, [KMT2D](../genes/KMT2D.md) 18%, [NSD1](../genes/NSD1.md) 10%, [CASP8](../genes/CASP8.md) 9%, [AJUBA](../genes/AJUBA.md) 6%, [NFE2L2](../genes/NFE2L2.md) 6%, [HLA-A](../genes/HLA-A.md) 3%. [PMID:25631445](../papers/25631445.md)
- [TP53](../genes/TP53.md) mutated in 86% of HPV(−) tumors but only 1/36 HPV(+) cases; [PIK3CA](../genes/PIK3CA.md) mutated in 56% of HPV(+) vs 34% of HPV(−), with helical-domain enrichment in HPV(+). [PMID:25631445](../papers/25631445.md)
- Novel recurrent inactivation of [TRAF3](../genes/TRAF3.md) in HPV(+) tumors (deletions 14%, truncating mutations 8%), representing the first link between [TRAF3](../genes/TRAF3.md) loss and HPV-associated carcinoma. [PMID:25631445](../papers/25631445.md)
- [NSD1](../genes/NSD1.md) inactivated in 33 tumors (10%) by mutations or focal homozygous deletions; associated with DNA hypomethylation. [PMID:25631445](../papers/25631445.md)
- Four mRNA expression subtypes confirmed (atypical 24%, mesenchymal 27%, basal 31%, classical 18%), each with distinct co-occurring genomic features; classical subtype resembles lung squamous cell carcinoma ([LUSC](../cancer_types/LUSC.md)) with tobacco and oxidative-stress signatures. [PMID:25631445](../papers/25631445.md)
- Favourable outcomes in HPV(+) and HPV(−)/TP53-wild-type tumors vs poor outcomes in TP53-mutant and 11q13/[CCND1](../genes/CCND1.md)-amplified tumors; co-amplification of 11q13 ([CCND1](../genes/CCND1.md), [FADD](../genes/FADD.md), [CTTN](../genes/CTTN.md)) and 11q22 ([BIRC2](../genes/BIRC2.md), [YAP1](../genes/YAP1.md)) in 31% of HPV(−) tumors. [PMID:25631445](../papers/25631445.md)
- Oral-cavity CNA-low "M class" subset defined by activating [HRAS](../genes/HRAS.md) + inactivating [CASP8](../genes/CASP8.md) + wild-type [TP53](../genes/TP53.md); favourable clinical outcome. [PMID:25631445](../papers/25631445.md)

## Sources

- [PMID:25631445](../papers/25631445.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
