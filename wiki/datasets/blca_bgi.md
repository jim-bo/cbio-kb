---
name: BGI/UCGC Bladder Cancer 2013 (Guo)
studyId: blca_bgi
institution: BGI (Beijing Genomics Institute) / Urinogenital Cancer Genomics Consortium (UCGC), China
size: 99
reference_genome: hg18
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - sanger-sequencing
  - gistic
  - fish
panels: []
tags:
  - bladder-cancer
  - tcc
  - sister-chromatid-cohesion
  - cohesin-complex
  - fgfr3-tacc3-fusion
  - aneuploidy
  - chromatin-remodeling
processed_by: crosslinker
processed_at: 2026-05-09
---

# BGI/UCGC Bladder Cancer 2013 (Guo)

## Overview

Whole-genome, whole-exome, and transcriptome sequencing study of 99 transitional cell carcinoma (TCC) bladder tumors with matched peripheral blood, assembled by Guo et al. through member institutions of the Urinogenital Cancer Genomics Consortium (UCGC) in China and published in *Nature Genetics* 2013. The study identified frequent loss-of-function alterations in [STAG2](../genes/STAG2.md) and [ESPL1](../genes/ESPL1.md) (cohesin/cohesion genes), a recurrent [FGFR3](../genes/FGFR3.md)–[TACC3](../genes/TACC3.md) in-frame fusion, and confirmed 37 significantly mutated genes. The cBioPortal study identifier is `blca_bgi`.

## Composition

- **Cancer type:** [BLCA](../cancer_types/BLCA.md) — transitional cell carcinoma (TCC) of the bladder.
- **Samples:** 99 individuals; tumors with malignant cell purity >85% selected; recruited through UCGC member institutions in China.
- **Validation cohort:** 50 additional TCC tumor/normal pairs for targeted [STAG2](../genes/STAG2.md) sequencing (exons 3–35) by Sanger.
- Reference genome: hg18 (NCBI human reference). [PMID:24121792](../papers/24121792.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — Illumina HiSeq 2000; Agilent SureSelect Human All Exon 50 Mb capture; tumor/normal pairs. 91% SNV and 74% indel Sanger validation rate.
- [whole-genome-seq](../methods/whole-genome-seq.md) — fourfold mean haploid coverage; tumor/normal pairs; used to confirm FGFR3–TACC3 fusions via junction-spanning and mate-pair reads.
- [rna-seq](../methods/rna-seq.md) — subset of 42 DNA-sequenced tumors plus 16 matched normal bladder tissues; used for fusion transcript detection.
- [sanger-sequencing](../methods/sanger-sequencing.md) — validation of candidate somatic mutations and targeted STAG2 sequencing in extension cohort.
- [gistic](../methods/gistic.md) — reimplemented algorithm on SegSeq copy-number calls; 84 focal amplification regions and 80 focal deletion regions identified.
- [fish](../methods/fish.md) — used to validate [DHFR](../genes/DHFR.md) amplifications at 5q.

## Papers using this cohort

- [PMID:24121792](../papers/24121792.md) — Guo G et al., "Whole-genome and whole-exome sequencing of bladder cancer identifies frequent alterations in genes involved in sister chromatid cohesion and segregation", *Nature Genetics* 2013.

## Notable findings derived from this cohort

- 37 significantly mutated genes identified (P < 0.01 vs background; non-silent mutations in ≥5/99 tumors), confirming known TCC drivers and newly identifying [STAG2](../genes/STAG2.md) as the top novel driver (P = 8×10⁻¹¹). [PMID:24121792](../papers/24121792.md)
- 32% (32/99) of tumors harbored genetic alterations in the sister chromatid cohesion and segregation (SCCS) pathway ([STAG2](../genes/STAG2.md) 16%, [ESPL1](../genes/ESPL1.md) 6%, [TACC3](../genes/TACC3.md) fusion 5%, [NIPBL](../genes/NIPBL.md) 4%, [SMC1A](../genes/SMC1A.md) 3%, [SMC3](../genes/SMC3.md) 2%); SCCS-altered tumors showed significantly higher aneuploidy (P = 0.01). [PMID:24121792](../papers/24121792.md)
- [STAG2](../genes/STAG2.md) alteration (mutation or deletion) in 16% of tumors was associated with significantly worse overall survival (log-rank P < 0.001), persisting within superficial and invasive TCC subtypes. [PMID:24121792](../papers/24121792.md)
- 58% (58/99) of tumors harbored mutations in chromatin-remodeling genes, including [KDM6A](../genes/KDM6A.md)/[UTY](../genes/UTY.md) (30%), [ARID1A](../genes/ARID1A.md) (17%), and histone methyltransferases [KMT2A](../genes/KMT2A.md)/[KMT2C](../genes/KMT2C.md)/[KMT2E](../genes/KMT2E.md) (16%). [PMID:24121792](../papers/24121792.md)
- Recurrent in-frame [FGFR3](../genes/FGFR3.md)–[TACC3](../genes/TACC3.md) gene fusion in 2/42 (5%) RNA-seq tumors; confirmed by WGS junction reads. [PMID:24121792](../papers/24121792.md)
- [DHFR](../genes/DHFR.md) focal amplification at 5q in 14/99 (14%) tumors; flagged as therapeutically relevant given DHFR is the target of antifolate anticancer agents. [PMID:24121792](../papers/24121792.md)
- [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) homozygous focal deletion at 9p21 in 50/99 (50%) of tumors — the most common focal deletion. [PMID:24121792](../papers/24121792.md)

## Sources

- cBioPortal study: `blca_bgi`
- [PMID:24121792](../papers/24121792.md) — primary publication
- EGA accession: not stated in frontmatter (sequencing data deposited via UCGC/BGI)

*This page was processed by **crosslinker** on **2026-05-09**.*
