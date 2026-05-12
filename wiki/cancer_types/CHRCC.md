---
name: Chromophobe Renal Cell Carcinoma
oncotree_code: CHRCC
main_type: Renal Cell Carcinoma
parent: NCCRCC
tags:
  - kidney
  - renal
  - chromophobe
  - mitochondria
  - tert
processed_by: wiki-cli
processed_at: 2026-05-12
---

# Chromophobe Renal Cell Carcinoma (CHRCC)

## Overview

Chromophobe renal cell carcinoma is a distinct subtype of renal cell carcinoma arising from the distal nephron (intercalated cells of the collecting duct), in contrast to clear cell RCC (CCRCC), which originates from the proximal tubule. ChRCC accounts for ~5% of all RCC. Genomically it is characterized by a low somatic mutation rate (~0.4 mutations/Mb, ~3-fold below ccRCC), near-universal whole-chromosome losses (chromosomes 1, 2, 6, 10, 13, 17 in ~86% of cases), and an activated oxidative phosphorylation metabolism — counter to the Warburg phenotype of ccRCC. Classic and eosinophilic histologic subtypes have distinct genomic correlates.

## Cohorts in the corpus

- [kich_tcga_pub](../datasets/kich_tcga_pub.md) — 66 primary ChRCC tumors with matched normal tissue/blood; TCGA multi-platform study including WES (n=66), WGS (n=50), mtDNA sequencing (n=61), RNA-seq, miRNA-seq, HM450 methylation, and SNP6 copy-number arrays. [PMID:25155756](../papers/25155756.md)

## Recurrent alterations

- [TP53](../genes/TP53.md) — somatic mutation in 21/66 (32%); only MutSig-significant nuclear gene; mutations correlate with decreased p53 target expression. [PMID:25155756](../papers/25155756.md)
- [PTEN](../genes/PTEN.md) — nonsilent mutation in 6/66 (9%) plus 2 homozygous deletions; MutSig q<0.1; germline PTEN mutations underlie Cowden syndrome (predisposes to ChRCC). [PMID:25155756](../papers/25155756.md)
- [TERT](../genes/TERT.md) — recurrent genomic rearrangement breakpoints within ~10 kb upstream of the TSS in 6/50 ChRCC by WGS; associated with massively elevated TERT expression (>500 units vs ~1 unit in C228T point-mutation cases); novel TERT-upregulation mechanism distinct from promoter point mutations or amplification. [PMID:25155756](../papers/25155756.md)
- mTOR pathway — [MTOR](../genes/MTOR.md) (2/66), [TSC1](../genes/TSC1.md)/[TSC2](../genes/TSC2.md) (4/66 combined), [NRAS](../genes/NRAS.md) activating mutation (1/66); total mTOR-pathway alterations in 15/66 (23%) cases. [PMID:25155756](../papers/25155756.md)
- [CDKN2A](../genes/CDKN2A.md) — epigenetically silenced in 4/66 cases. [PMID:25155756](../papers/25155756.md)
- Whole-chromosome losses of chr 1, 2, 6, 10, 13, 17 in 86% (57/66) of ChRCC; pattern is universal in classic subtype (47/47) but present in only 10/19 eosinophilic cases. [PMID:25155756](../papers/25155756.md)
- Mitochondrial DNA mutations — 35 somatic mtDNA events at >50% heteroplasmy across 27 cases; MT-ND5 (Complex I) most frequently mutated (6/61, predominantly eosinophilic subtype); elevated [PPARGC1A](../genes/PPARGC1A.md) and ~4× mtDNA copy number indicate increased mitochondrial biogenesis. [PMID:25155756](../papers/25155756.md)
- Integrated exome/RNA-seq/CNV profiling of 49 chromophobe RCCs identified TP53, PTEN, PDHB, PRKAG2, and FAAH2 as significantly mutated genes; TP53 mutations significantly enriched in the classic chRCC subtype (P=2.3×10⁻⁵); combined PRKAG2+PDHB mutations define a metabolic subtype; TSC1/TSC2/MTOR mutations nominate mTORC1 inhibitors [PMID:25401301](../papers/25401301.md)

## Subtypes

- **Classic ChRCC** — pale cytoplasm; universal whole-chromosome losses (47/47 in TCGA cohort); no Complex I mtDNA enrichment.
- **Eosinophilic ChRCC** — granular pink cytoplasm; only ~53% (10/19) show canonical chromosome losses; 4/19 have no CNAs; enriched for MT-ND5 mutations (5/6 MT-ND5-mutated cases were eosinophilic; p<0.01). [PMID:25155756](../papers/25155756.md)

## Therapeutic landscape

- mTOR-pathway alterations in 23% of cases (PTEN, MTOR, TSC1/2, NRAS) suggest a subpopulation potentially amenable to mTOR-directed therapy; no direct drug trial data from corpus. [PMID:25155756](../papers/25155756.md)

## Sources

- [PMID:25155756](../papers/25155756.md) — TCGA comprehensive molecular characterization of chromophobe renal cell carcinoma (Cancer Cell 2015).

*This page was processed by **entity-page-writer** on **2026-05-11**.*
- [PMID:25401301](../papers/25401301.md)

*This page was processed by **wiki-cli** on **2026-05-12**.*
