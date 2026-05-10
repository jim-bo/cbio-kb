---
name: Multiple Myeloma Research Consortium WES/WGS Cohort (Broad, 2014)
studyId: mm_broad
institution: Broad Institute / Multiple Myeloma Research Consortium (MMRC)
size: 203
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - affymetrix-snp6
  - fish
panels: []
tags:
  - multiple-myeloma
  - plasma-cell-myeloma
  - clonal-heterogeneity
  - subclonal-architecture
  - targeted-therapy
  - mapk-pathway
  - copy-number
processed_by: crosslinker
processed_at: 2026-05-09
---

# Multiple Myeloma Research Consortium WES/WGS Cohort (Broad, 2014)

## Overview

The mm_broad dataset comprises 203 multiple myeloma (MM) tumor–normal pairs assembled from the Multiple Myeloma Research Consortium (MMRC) tissue bank. Bone marrow aspirates from MM patients were paired with matched peripheral blood germline. The study, led by Lohr et al. at the Broad Institute, was designed to characterize the somatic mutation landscape and clonal architecture of MM using integrative genomic and copy-number profiling. Data are deposited in dbGaP under accession phs000348.

## Composition

- **203 tumor–normal pairs**: 177 profiled by whole-exome sequencing and 26 by whole-genome sequencing; 153 patients additionally profiled by Affymetrix SNP 6.0 copy-number arrays.
- Cancer type: plasma cell myeloma ([PCM](../cancer_types/PCM.md)).
- Samples from MMRC tissue bank; bone marrow aspirates paired with peripheral blood germline.
- 116 patients classified hyperdiploid and 86 non-hyperdiploid by a WES/WGS-based classifier developed in this study.
- 50 patients had routine clinical [FISH](../methods/fish.md) testing for t(4;14) and t(11;14).
- Mutation validation rate: **90.4%** across 140 mutations re-genotyped.
- 16 of the WES and 23 of the WGS samples were previously reported in Chapman et al. 2011 (PMID:21430775).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 177 patients; Agilent SureSelect v2 + Illumina HiSeq 76 bp PE; average 89× tumor, 88× normal.
- [whole-genome-seq](../methods/whole-genome-seq.md) — 26 patients; average ~30× coverage.
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — 153 patients; Affymetrix SNP 6.0 copy-number arrays.
- [fish](../methods/fish.md) — routine clinical testing for t(4;14) and t(11;14) in 50 patients.
- Analytical stack: [mutsig](../methods/mutsig.md) (MutSigCV) for mutation significance, [gistic](../methods/gistic.md) for focal copy-number peaks, [absolute](../methods/absolute.md) for tumor purity / CCF / LOH estimation, Bayesian CCF clustering for subclonal architecture inference.

## Papers using this cohort

- [PMID:24434212](../papers/24434212.md) — Lohr et al., *Cancer Cell* (2014): Widespread genetic heterogeneity in multiple myeloma: implications for targeted therapy.

## Notable findings derived from this cohort

- **11 significantly mutated genes** at q < 0.1 identified: [KRAS](../genes/KRAS.md), [NRAS](../genes/NRAS.md), [BRAF](../genes/BRAF.md), [TENT5C](../genes/TENT5C.md), [TP53](../genes/TP53.md), [DIS3](../genes/DIS3.md), [TRAF3](../genes/TRAF3.md), [CYLD](../genes/CYLD.md), [RB1](../genes/RB1.md), [PRDM1](../genes/PRDM1.md), plus a recurrent hotspot in [IRF4](../genes/IRF4.md) K123R (3 of 4 IRF4-mutant patients). [PMID:24434212](../papers/24434212.md)
- MM tumors are pervasively subclonal — nearly all patients with tumor purity >0.7 had detectable clonal heterogeneity; most harbored ≥3 subclones; significantly mutated driver genes including [BRAF](../genes/BRAF.md) were frequently subclonal. [PMID:24434212](../papers/24434212.md)
- Recurrent homozygous deletions in 7 regions identified by GISTIC across 153 patients, covering [CDKN2C](../genes/CDKN2C.md), NF-κB regulators [TRAF3](../genes/TRAF3.md) / [BIRC2](../genes/BIRC2.md) / [BIRC3](../genes/BIRC3.md) / [CYLD](../genes/CYLD.md), [PTPRD](../genes/PTPRD.md), and an 8p23.1 peak (including [BLK](../genes/BLK.md), [MSRA](../genes/MSRA.md), [PINX1](../genes/PINX1.md), [SOX7](../genes/SOX7.md)). [PMID:24434212](../papers/24434212.md)
- In vitro modeling showed that [BRAF](../genes/BRAF.md) inhibitors ([dabrafenib](../drugs/dabrafenib.md), [plx4720](../drugs/plx4720.md)) suppress MAPK in BRAF-mutant cells but paradoxically activate MAPK and promote growth in BRAF-WT, KRAS/NRAS-mutant cells — predicting limited efficacy when BRAF mutations are subclonal in MM. [PMID:24434212](../papers/24434212.md)

## Sources

- dbGaP accession: phs000348
- cBioPortal study ID: mm_broad

*This page was processed by **crosslinker** on **2026-05-09**.*
