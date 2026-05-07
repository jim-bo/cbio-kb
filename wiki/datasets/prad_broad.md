---
name: Broad Prostate Adenocarcinoma WES (prad_broad)
studyId: prad_broad
institution: Broad Institute; American and Australian clinical sites
size: 112
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
panels: []
tags:
  - prostate cancer
  - WES
  - SPOP
  - FOXA1
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Broad Prostate Adenocarcinoma WES (prad_broad)

## Overview

The Broad prostate adenocarcinoma WES dataset comprises 112 prostate adenocarcinoma/normal pairs from treatment-naive radical prostatectomy specimens sourced from American and Australian patients. Mean exome coverage was 118x (89.2% of targets at ≥20x). Copy-number profiling was performed on 169 tumors via Affymetrix SNP 6.0 arrays. RNA-seq was conducted on 22 exome-sequenced tumors and 41 independent samples. Additional validation cohorts covered >300 primary tumors and metastases from Weill Cornell Medical College, University of Michigan, Uropath, and University of Washington.

## Composition

- 112 prostate adenocarcinoma/normal pairs (radical prostatectomy, treatment-naive)
- Cancer type: [PRAD](../cancer_types/PRAD.md)
- 5,764 somatic mutations identified; median 30 non-silent mutations per tumor (~1.4 per Mb)
- Copy-number profiling on 169 tumors (Affymetrix SNP 6.0)
- RNA-seq on 22 exome-sequenced and 41 independent samples

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md)
- [Affymetrix SNP 6.0](../methods/affymetrix-snp6.md)
- [RNA sequencing](../methods/rna-seq.md)
- [Sanger sequencing](../methods/sanger-sequencing.md) (validation)
- [FISH](../methods/fish.md) (copy-number validation)
- [MutSig](../methods/mutsig.md) (driver gene identification)
- [GISTIC](../methods/gistic.md) (copy-number analysis)
- [Sequenom genotyping](../methods/sequenom-genotyping.md) (mutation validation)

## Papers using this cohort

- [PMID:22610119](../papers/22610119.md)

## Notable findings derived from this cohort

- [SPOP](../genes/SPOP.md) was the most frequently mutated gene at 13% (15/111 exomes); all mutations affect conserved residues in the substrate-binding cleft [PMID:22610119](../papers/22610119.md)
- SPOP mutations and ETS rearrangements (TMPRSS2-ERG fusion) were mutually exclusive (P < 0.001, Fisher's exact test) [PMID:22610119](../papers/22610119.md)
- [FOXA1](../genes/FOXA1.md) and [MED12](../genes/MED12.md) identified as additional recurrent driver genes [PMID:22610119](../papers/22610119.md)
- SPOP-mutant tumors enriched for 5q21 deletions ([CHD1](../genes/CHD1.md); P = 1.4e-11) and 6q21 deletions ([FOXO3](../genes/FOXO3.md), [PRDM1](../genes/PRDM1.md); P = 3.4e-7) [PMID:22610119](../papers/22610119.md)
- 12 genes significantly enriched for mutations at q < 0.1 by MutSig analysis [PMID:22610119](../papers/22610119.md)

## Sources

- [PMID:22610119](../papers/22610119.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
