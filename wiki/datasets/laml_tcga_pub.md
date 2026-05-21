---
name: Acute Myeloid Leukemia — TCGA (2013)
studyId: laml_tcga_pub
institution: The Cancer Genome Atlas / Washington University
size: 200
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - whole-exome-seq
  - rna-seq
  - 450k-methylation-array
  - affymetrix-snp6
panels: []
tags:
  - AML
  - acute myeloid leukemia
  - TCGA
processed_by: crosslinker
processed_at: 2026-05-21
---

# Acute Myeloid Leukemia — TCGA (2013)

## Overview

The Cancer Genome Atlas comprehensive genomic and epigenomic characterization of 200 clinically annotated adult de novo [AML](../cancer_types/AML.md) cases, published in NEJM 2013. Samples drawn from a single-institution Washington University tissue-banking protocol (Nov 2001–Mar 2010), selected to reflect a real-world distribution of FAB and cytogenetic subtypes. [PMID:23634996](../papers/23634996.md)

## Composition

- 200 adult de novo [AML](../cancer_types/AML.md) cases with matched normal (peripheral blood or skin); selected to reflect a real-world distribution of FAB subtypes and cytogenetic risk groups. [PMID:23634996](../papers/23634996.md)
- 50 cases profiled by whole-genome sequencing (mean coverage 30.54×); 150 by whole-exome sequencing (mean coverage 167.50×); all somatic variants validated by hybridization-capture deep digital sequencing. [PMID:23634996](../papers/23634996.md)
- Multi-platform profiling: RNA-seq (179 samples), microRNA-seq (194 samples), Affymetrix U133 Plus 2 expression (197 samples), Illumina HumanMethylation450 arrays (192 samples), Affymetrix SNP 6.0 copy-number arrays (all 200 patients with matched normal skin). [PMID:23634996](../papers/23634996.md)

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — 50 tumor/normal-skin pairs, mean 30.54× coverage. [PMID:23634996](../papers/23634996.md)
- [whole-exome-seq](../methods/whole-exome-seq.md) — 150 tumor/normal-skin pairs, mean 167.50× coverage. [PMID:23634996](../papers/23634996.md)
- [rna-seq](../methods/rna-seq.md) — 179 samples; NMF consensus clustering identified 7 expression groups mapping onto FAB subtypes. [PMID:23634996](../papers/23634996.md)
- [450k-methylation-array](../methods/450k-methylation-array.md) — Illumina Infinium HumanMethylation450 BeadChip on 192 samples. [PMID:23634996](../papers/23634996.md)
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — somatic copy-number profiling on all 200 tumor and matched normal skin samples. [PMID:23634996](../papers/23634996.md)

## Papers using this cohort

- [PMID:23634996](../papers/23634996.md) — The Cancer Genome Atlas Research Network, "Genomic and Epigenomic Landscapes of Adult De Novo Acute Myeloid Leukemia," *N Engl J Med* 2013.
- [PMID:27959731](../papers/27959731.md) — Welch et al., *N Engl J Med* 2016: Used as comparator to benchmark [TP53](../genes/TP53.md) mutation spectrum and methylation patterns from the WashU [decitabine](../drugs/decitabine.md) trial ([mnm_washu_2016](../datasets/mnm_washu_2016.md)); no TP53-driven methylation signature identifiable in either dataset.

## Notable findings derived from this cohort

- Adult [AML](../cancer_types/AML.md) genomes are mutation-sparse (mean 13 coding mutations per sample); 23 significantly mutated genes at FDR<0.05 including [DNMT3A](../genes/DNMT3A.md), [FLT3](../genes/FLT3.md), [NPM1](../genes/NPM1.md), [IDH1](../genes/IDH1.md), [IDH2](../genes/IDH2.md), [CEBPA](../genes/CEBPA.md), [U2AF1](../genes/U2AF1.md), [EZH2](../genes/EZH2.md), [SMC1A](../genes/SMC1A.md), and [SMC3](../genes/SMC3.md). [PMID:23634996](../papers/23634996.md)
- Nearly every sample (199/200) harbored at least one driver in one of nine functional categories: transcription-factor fusions (18%), [NPM1](../genes/NPM1.md) (27%), tumor suppressors (16%), DNA-methylation genes (44%), activated signaling (59%), chromatin modifiers (30%), myeloid transcription factors (22%), cohesin-complex (13%), and spliceosome (14%). [PMID:23634996](../papers/23634996.md)
- Novel co-occurring triplet of [NPM1](../genes/NPM1.md) + [DNMT3A](../genes/DNMT3A.md) + [FLT3](../genes/FLT3.md) mutations defines a distinct epigenetic [AML](../cancer_types/AML.md) subtype by mRNA, miRNA, and DNA-methylation clustering, with extensive methylation loss. [PMID:23634996](../papers/23634996.md)
- [IDH1](../genes/IDH1.md)/[IDH2](../genes/IDH2.md)-mutant samples showed extensive methylation gains; [KMT2A](../genes/KMT2A.md) fusions and the triple-mutant group showed extensive methylation loss; 160,519 CpG loci differentially methylated (67% gain, 33% loss). [PMID:23634996](../papers/23634996.md)
- Deep digital sequencing enabled VAF-based clonal architecture reconstruction: >50% of WGS tumors had a founding clone plus ≥1 subclone; minimal aneuploidy (median 1 somatic SCNV per genome) and no chromothripsis. [PMID:23634996](../papers/23634996.md)
- 118 gene fusions identified in 80/179 samples by de novo RNA-seq assembly; recurrent in-frame fusions included [PML](../genes/PML.md)–[RARA](../genes/RARA.md), [MYH11](../genes/MYH11.md)–[CBFB](../genes/CBFB.md), [RUNX1](../genes/RUNX1.md)–[RUNX1T1](../genes/RUNX1T1.md), and [NUP98](../genes/NUP98.md)–[NSD1](../genes/NSD1.md). [PMID:23634996](../papers/23634996.md)
- Used as an independent validation cohort to replicate 11 [AML](../cancer_types/AML.md) genomic subgroups (chromatin–spliceosome, [TP53](../genes/TP53.md)–aneuploidy, [IDH2](../genes/IDH2.md) R172, etc.) identified in 1540 AMLSG trial patients; subgroup structure and prognostic associations were confirmed in this TCGA AML dataset. [PMID:27276561](../papers/27276561.md)
- [TP53](../genes/TP53.md) mutation spectrum (missense-dominant, hotspot distribution) in the WashU [decitabine](../drugs/decitabine.md) trial cohort was indistinguishable from that in this TCGA AML dataset; no TP53-driven CpG methylation signature was detectable in either cohort, arguing against a methylation-based mechanism for TP53-decitabine sensitivity. [PMID:27959731](../papers/27959731.md)
- 200 de novo AMLs from this cohort served as a reference cohort for genomic comparison against GCT-associated hematologic malignancies, establishing the absence of canonical myeloid drivers ([FLT3](../genes/FLT3.md), [DNMT3A](../genes/DNMT3A.md), [TET2](../genes/TET2.md), [NPM1](../genes/NPM1.md)) in the GCT-associated cases — [PMID:32897884](../papers/32897884.md)
- Served as an independent validation cohort for [PEAR1](../genes/PEAR1.md) as a prognostic biomarker: elevated [PEAR1](../genes/PEAR1.md) expression was significantly associated with shortened overall survival in TCGA [LAML](../cancer_types/LAML.md), replicating the Beat AML functional-genomic study findings [PMID:35868306](../papers/35868306.md)

## Sources

- DOI: 10.1056/NEJMoa1301689
- Washington University tissue-banking protocol (Nov 2001–Mar 2010)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:32897884](../papers/32897884.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35868306](../papers/35868306.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
