---
name: TCGA Bladder Urothelial Carcinoma (2014)
studyId: blca_tcga_pub
institution: The Cancer Genome Atlas Research Network
size: 131
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - affymetrix-snp6
  - hm450-methylation-array
  - rppa
panels: []
tags:
  - tcga
  - urothelial-carcinoma
  - muscle-invasive-bladder-cancer
  - chromatin-remodeling
  - apobec-mutagenesis
  - multi-platform
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# TCGA Bladder Urothelial Carcinoma (2014)

## Overview

The blca_tcga_pub dataset is the inaugural comprehensive multi-platform molecular characterization of muscle-invasive, high-grade urothelial bladder carcinoma produced by The Cancer Genome Atlas (TCGA) Research Network, published in *Nature* in 2014. It profiled 131 chemotherapy-naive tumors (stages T2–T4a, Nx, Mx) from 19 tissue source sites using six integrated data platforms: whole-exome sequencing, low-pass whole-genome sequencing, RNA-seq, miRNA-seq, DNA methylation arrays, reverse-phase protein arrays (RPPA), and Affymetrix SNP 6.0 copy-number arrays. The study established bladder cancer as the epithelial cancer with the highest frequency of chromatin-regulator mutations and identified potential therapeutic targets in 69% of tumors.

## Composition

- **131 chemotherapy-naive, muscle-invasive, high-grade urothelial bladder carcinomas** (T2–T4a, Nx, Mx); matched peripheral blood (n=118) and/or tumor-adjacent normal bladder tissue (n=23).
- Tumor purity threshold: ≥60% tumor nuclei, ≤20% necrosis, ≤50% variant histology.
- Cancer type: [BLCA](../cancer_types/BLCA.md) (urothelial carcinoma of the bladder).
- Samples from 19 tissue source sites across the United States.
- Mean/median somatic mutation rates: 7.7 / 5.5 mutations per Mb; average 302 exonic mutations, 204 segmental copy-number alterations, and 22 genomic rearrangements per sample.
- 72% of patients had current or past smoking history.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 130 tumor/normal pairs; 186,260 exons across 18,091 genes; mean coverage 100× (≥82% target bases covered ≥30×).
- [whole-genome-seq](../methods/whole-genome-seq.md) — low-pass paired-end sequencing of 114 tumors at 6–8× coverage for structural variant detection.
- [rna-seq](../methods/rna-seq.md) — all tumors (n=129 used for mRNA subtype clustering); also miRNA-seq.
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — somatic copy-number alteration profiling.
- [hm450-methylation-array](../methods/hm450-methylation-array.md) — DNA methylation profiling; identified CIMP subgroup (34% of tumors).
- [rppa](../methods/rppa.md) — protein and phosphoprotein expression profiling.
- Analytic tools: [mutect](../methods/mutect.md) for somatic point mutations, [mutsig](../methods/mutsig.md) (MutSig 1.5) for significantly mutated genes, [gistic](../methods/gistic.md) (GISTIC 2.0) for focal CNAs.

## Papers using this cohort

- [PMID:24476821](../papers/24476821.md) — TCGA Research Network, *Nature* (2014): Comprehensive molecular characterization of urothelial bladder carcinoma.
- [PMID:26901067](../papers/26901067.md) — Al-Ahmadie et al., *Nat Genet* 2016: CDH1 mutations absent in 127 NOS tumors from this cohort; used as comparator for plasmacytoid-variant bladder cancer.
- [PMID:27749842](../papers/27749842.md) — Faltas et al., *Nat Genet* 2016: Used as mutation-frequency benchmark for the Weill Cornell chemotherapy-evolution cohort; clonal enrichment of L1CAM and integrin signaling mutations in post-chemotherapy tumors was compared against this TCGA baseline.
- [PMID:28583311](../papers/28583311.md) — Pietzak et al., *JCO* 2017: 98 TCGA MIBC specimens with no prior history of NMIBC used as a muscle-invasive comparator cohort to contextualize gene-alteration frequencies (e.g., FGFR3, STAG2, TP53/MDM2) and mutational burden in the MSK NMIBC cohort. [PMID:28583311](../papers/28583311.md)

## Notable findings derived from this cohort

- **32 significantly mutated genes** by MutSig 1.5 (FDR < 0.1), including 9 not previously reported as significantly mutated in any cancer: [CDKN1A](../genes/CDKN1A.md), [ERCC2](../genes/ERCC2.md), [RXRA](../genes/RXRA.md), [ELF3](../genes/ELF3.md), [KLF5](../genes/KLF5.md), [FOXQ1](../genes/FOXQ1.md), [RHOB](../genes/RHOB.md), [PAIP1](../genes/PAIP1.md), and [BTG2](../genes/BTG2.md). [PMID:24476821](../papers/24476821.md)
- [TP53](../genes/TP53.md) mutated in 49%; [TP53](../genes/TP53.md) pathway inactivated (mutation + [MDM2](../genes/MDM2.md) amplification or overexpression) in 76% of tumors. [PMID:24476821](../papers/24476821.md)
- **76% of tumors** (99/131) had an inactivating mutation in at least one chromatin regulatory gene; 41% had at least two. Four epigenetic regulators were MutSig-significant: [KMT2D](../genes/KMT2D.md), [ARID1A](../genes/ARID1A.md), [KDM6A](../genes/KDM6A.md), [EP300](../genes/EP300.md). [KMT2D](../genes/KMT2D.md) and [KDM6A](../genes/KDM6A.md) mutations were mutually exclusive. [PMID:24476821](../papers/24476821.md)
- Recurrent in-frame activating [FGFR3](../genes/FGFR3.md)–[TACC3](../genes/TACC3.md) fusions identified in 3 of 114 WGS tumors; enriched in the papillary-like mRNA subtype (cluster I). [PMID:24476821](../papers/24476821.md)
- Four mRNA expression subtypes defined (n=129): papillary-like (cluster I, enriched for [FGFR3](../genes/FGFR3.md) mutation/amplification), basal/squamous-like (cluster III, expressing KRT14/KRT5/KRT6A and [EGFR](../genes/EGFR.md)), and two luminal-like clusters resembling luminal A breast cancer with high [GATA3](../genes/GATA3.md) and [FOXA1](../genes/FOXA1.md). [PMID:24476821](../papers/24476821.md)
- **APOBEC mutagenesis**: 51% of all mutations were TpC → (T/G), attributed to [APOBEC3B](../genes/APOBEC3B.md) activity; [APOBEC3B](../genes/APOBEC3B.md) was highly expressed across all tumors. [PMID:24476821](../papers/24476821.md)
- Potential therapeutic targets identified in **69% of tumors**: 42% in PI(3)K/AKT/mTOR pathway (including [PIK3CA](../genes/PIK3CA.md) 17%, [TSC1](../genes/TSC1.md)/[TSC2](../genes/TSC2.md) 9%); 45% in RTK/MAPK pathway (including [FGFR3](../genes/FGFR3.md) 17%, [ERBB2](../genes/ERBB2.md) 9%). [PMID:24476821](../papers/24476821.md)
- [CDKN2A](../genes/CDKN2A.md) focal deletion in 47% of samples (most common focal deletion); [RXRA](../genes/RXRA.md) S427 hotspot mutations in 7 of 12 RXRA-mutant tumors (5 S427F, 2 S427Y) associated with elevated adipogenesis/lipid-metabolism gene expression. [PMID:24476821](../papers/24476821.md)
- Comprehensive molecular characterization of 131 muscle-invasive urothelial carcinomas revealed APOBEC mutagenesis, chromatin remodeling alterations, and immune pathway enrichment [PMID:25096233](../papers/25096233.md)
- Used as comparator for plasmacytoid-variant bladder cancer: CDH1 truncating mutations were absent in 127 urothelial carcinoma NOS tumors from this cohort, establishing CDH1 mutation as specific to the plasmacytoid variant [PMID:26901067](../papers/26901067.md)
- Used as mutation-frequency benchmark for matched pre/post-chemotherapy WES of 72 UC tumors from 32 patients at Weill Cornell; copy-number landscape stability and APOBEC mutagenesis prevalence in this cohort provided the reference distribution for evolution analyses in the Cornell dataset [PMID:27749842](../papers/27749842.md)
- Used as MIBC comparator in the MSK NMIBC NGS study: [FGFR3](../genes/FGFR3.md) alteration rates in this TCGA MIBC cohort (16%) vs LGTa NMIBC (83%) supported the interpretation that FGFR3 alterations decrease progressively with stage; [STAG2](../genes/STAG2.md) truncating mutation rate (15% in TCGA MIBC) confirmed enrichment of STAG2 truncations in low-grade NMIBC (39%) vs advanced disease [PMID:28583311](../papers/28583311.md)

## Sources

- TCGA data portal / GDC
- cBioPortal study ID: blca_tcga_pub

*This page was processed by **entity-page-writer** on **2026-05-15**.*
