---
name: Ampullary Carcinoma (Baylor College of Medicine, Cell Reports 2016)
studyId: ampca_bcm_2016
institution: Baylor College of Medicine / Australian Pancreatic Cancer Genome Initiative (APGI) / MD Anderson / TU Dresden
size: 160
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - targeted-deep-amplicon-seq
  - snp-array
  - rna-seq
panels: []
tags:
  - ampullary-carcinoma
  - periampullary
  - AMPCA
  - cholangiocarcinoma
  - duodenal-adenocarcinoma
  - WNT
  - MSI
processed_by: crosslinker
processed_at: 2026-05-14
---

# Ampullary Carcinoma (Baylor College of Medicine, Cell Reports 2016)

## Overview

Multi-institutional cohort of 160 periampullary tumors collected by the Australian Pancreatic Cancer Genome Initiative (APGI), Baylor College of Medicine, MD Anderson, and TU Dresden. All patients underwent curative-intent pancreatoduodenectomy. The cohort encompasses three anatomically distinct but biologically related tumor types arising at the junction of the pancreatic duct, common bile duct, and duodenum: 98 ampullary adenocarcinomas ([AMPCA](../cancer_types/AMPCA.md)), 44 distal bile duct / cholangiocarcinomas (CAC), and 18 duodenal adenocarcinomas (DUOAC). Sequence data are deposited in dbGaP under accession PRJNA280134. [PMID:26804919](../papers/26804919.md)

## Composition

- 98 ampullary adenocarcinomas ([AMPCA](../cancer_types/AMPCA.md)): 51% pancreatobiliary IHC subtype, 34% intestinal, remainder mixed.
- 44 distal bile duct / cholangiocarcinomas ([EHCH](../cancer_types/EHCH.md)): 86% pancreatobiliary, 11% intestinal.
- 18 duodenal adenocarcinomas ([DA](../cancer_types/DA.md)): 44% intestinal, 22% pancreatobiliary.
- All samples from patients undergoing curative-intent surgery; no recurrent or metastatic biopsies. [PMID:26804919](../papers/26804919.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md): Illumina HiSeq 2000 at ~120× average coverage on 152 samples.
- [targeted-deep-amplicon-seq](../methods/targeted-deep-amplicon-seq.md): 71-gene panel for an 8-sample addendum; ultra-deep validation of all called mutations.
- SNP arrays: Illumina HumanOmni2.5-8 for copy-number profiling.
- [rna-seq](../methods/rna-seq.md): TruSeq Stranded Total RNA, 100 bp paired-end, ≥50 M reads, on 28/98 AMPAC and 2/18 DUOAC samples.
- Reference genome: hg19 (GRCh37). [PMID:26804919](../papers/26804919.md)

## Papers using this cohort

- [PMID:26804919](../papers/26804919.md) — Gingras et al. 2016, *Cell Reports*: Primary study; molecular taxonomy of 160 periampullary tumors revealing WNT-pathway dominance and [ELF3](../genes/ELF3.md) as a novel tumor suppressor.

## Notable findings derived from this cohort

- [ELF3](../genes/ELF3.md) mutated in 10.6% of periampullary tumors with predominantly inactivating frameshift/nonsense mutations — approximately 3× higher than any other cancer in cBioPortal at the time. [PMID:26804919](../papers/26804919.md)
- WNT pathway mutated in 46% of all periampullary tumors; rates differ significantly by site: DUOAC 72%, AMPAC 49%, CAC 30% (ChiSq p<0.05); intestinal IHC subtype 67% WNT-altered vs 30% pancreatobiliary. [PMID:26804919](../papers/26804919.md)
- MSI present in 12/160 patients (8% overall); all 6 MSI-AMPCA patients alive 2–8 years post-diagnosis (p=0.04); MSI associated with dramatically elevated mutation rates (median 68–127 mutations/Mb vs 3.8–4.7/Mb MSS). [PMID:26804919](../papers/26804919.md)
- [PMS2](../genes/PMS2.md) mutated in half of MSI patients — markedly higher than the <5% frequency in the general Lynch-syndrome population. [PMID:26804919](../papers/26804919.md)
- TGF-β pathway mutations independently predicted better [OS](../cancer_types/OS.md) (HR=0.42, p=0.0059); PI3K pathway mutations similarly predicted better OS (HR=0.43, p=0.036). [PMID:26804919](../papers/26804919.md)
- Five mutational signatures prominent; signature #1 (C>T at CpG) independently associated with worse outcome (multivariate Cox p=0.02). [PMID:26804919](../papers/26804919.md)

## Sources

- cBioPortal study: `ampca_bcm_2016` — https://www.cbioportal.org/study/summary?id=ampca_bcm_2016
- dbGaP accession: PRJNA280134
- [PMID:26804919](../papers/26804919.md) — Gingras et al. 2016, *Cell Reports*, DOI 10.1016/j.celrep.2015.12.005.

*This page was processed by **crosslinker** on **2026-05-14**.*
