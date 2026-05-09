---
name: Adenoid Cystic Carcinoma — Sanger 2013
studyId: acyc_sanger_2013
institution: Wellcome Sanger Institute / MD Anderson Cancer Center
size: 24
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - affymetrix-snp6
  - fish
  - sanger-sequencing
panels: []
tags:
  - salivary-gland-cancer
  - adenoid-cystic-carcinoma
  - ACYC
  - rare-cancers
  - exome-sequencing
processed_by: crosslinker
processed_at: 2026-05-09
---

# Adenoid Cystic Carcinoma — Sanger 2013

## Overview

Whole-exome sequencing of 24 adenoid cystic carcinoma (ACC; [ACYC](../cancer_types/ACYC.md)) tumor/normal pairs performed by the Wellcome Sanger Institute in collaboration with MD Anderson Cancer Center, published by Stephens et al. 2013 in *Journal of Clinical Investigation*. Includes extension sequencing of [SPEN](../genes/SPEN.md) (42 additional cases) and [FGFR2](../genes/FGFR2.md) (25 additional cases) by Sanger sequencing. Sequence data deposited in the European Genome-phenome Archive (EGA00001064049); SNP6 data in ArrayExpress E-MTAB-1141; expression data in ArrayExpress E-MTAB-1397.

## Composition

- 24 [ACYC](../cancer_types/ACYC.md) cases: 23 pretreatment primary tumors + 1 local-regional lymph-node metastasis, with matched normal salivary-gland parenchyma.
- Histology: roughly equal cribriform and predominantly solid forms; 19/24 MYB-positive.
- Solution-phase exome capture + next-generation sequencing; Affymetrix SNP 6.0 copy-number profiling analyzed with ASCAT v2.1.
- Extension cohorts: targeted Sanger sequencing of SPEN across 42 additional ACC cases and FGFR2 across 25 additional ACC cases.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md)
- [fish](../methods/fish.md)
- [sanger-sequencing](../methods/sanger-sequencing.md)

## Papers using this cohort

- [PMID:23778141](../papers/23778141.md) — Stephens et al. 2013, "Whole exome sequencing of adenoid cystic carcinoma," *Journal of Clinical Investigation*.

## Notable findings derived from this cohort

- 312 somatic mutations across 24 exomes (range 2–35; mean 13/exome) — lower than most adult solid tumors; mutation burden not significantly associated with histology or [MYB](../genes/MYB.md) status [PMID:23778141](../papers/23778141.md).
- Chromatin-biology genes mutated in 12/24 (50%) cases: [ARID1A](../genes/ARID1A.md), [ARID1B](../genes/ARID1B.md), [ARID5B](../genes/ARID5B.md), [CREBBP](../genes/CREBBP.md), [EP300](../genes/EP300.md), [KDM6A](../genes/KDM6A.md), [KDM5A](../genes/KDM5A.md), [KMT2C](../genes/KMT2C.md), [SMARCA2](../genes/SMARCA2.md), [CHD2](../genes/CHD2.md), [BRD2](../genes/BRD2.md) [PMID:23778141](../papers/23778141.md).
- SPEN nominated as a novel ACC cancer gene: 6 truncating mutations in 5 discovery cases (all solid histology) + 2 additional truncating mutations in extension cohort; mechanism is not simple loss-of-function (no consistent LOH) [PMID:23778141](../papers/23778141.md).
- Three likely activating FGFR2 mutations across discovery+extension cohorts (p.Y376C, p.I389_V393>M, p.K642R) nominating FGFR inhibition — e.g. [dovitinib](../drugs/dovitinib.md) — as a therapeutic strategy; NCT01524692 trial cited [PMID:23778141](../papers/23778141.md).
- [NOTCH1](../genes/NOTCH1.md) and [NOTCH2](../genes/NOTCH2.md) mutations identified in 3 cases, co-occurring with SPEN truncations in one tumor, implicating Notch-pathway deregulation [PMID:23778141](../papers/23778141.md).
- Recurrent copy-number losses at 1p36, 6q, 9p, and 12q; MYB-positive cases showed copy-number breakpoints at MYB and [NFIB](../genes/NFIB.md) loci [PMID:23778141](../papers/23778141.md).

## Sources

- [PMID:23778141](../papers/23778141.md)
- EGA: EGA00001064049
- ArrayExpress: E-MTAB-1141 (SNP6), E-MTAB-1397 (expression)

*This page was processed by **crosslinker** on **2026-05-09**.*
