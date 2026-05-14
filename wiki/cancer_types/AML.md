---
name: Acute Myeloid Leukemia
oncotree_code: AML
main_type: Leukemia
parent: MNM
tags: []
processed_by: crosslinker
processed_at: 2026-05-09
---

# Acute Myeloid Leukemia (AML)

## Overview

Acute Myeloid Leukemia (AML) is a hematologic malignancy arising from myeloid progenitor cells, classified under the Leukemia main type in OncoTree (parent node MNM). Adult AML genomes are mutation-sparse (mean ~13 coding mutations per sample) yet nearly every tumor harbors at least one driver event across nine recognized functional gene categories: transcription-factor fusions, [NPM1](../genes/NPM1.md) mutations, tumor suppressors, DNA-methylation genes, activated signaling, chromatin modifiers, myeloid transcription factors, cohesin complex, and spliceosome genes.

## Cohorts in the corpus

- [laml_tcga_pub](../datasets/laml_tcga_pub.md) — 200 adult de novo AML cases (50 WGS, 150 WES) from Washington University tissue banking (Nov 2001–Mar 2010); complemented by RNA-seq, microRNA-seq, 450k methylation, and SNP arrays. [PMID:23634996](../papers/23634996.md)

## Recurrent alterations

- TCGA WGS/WES of 200 adult de novo AML cases identified 23 significantly mutated genes (FDR <0.05 by MuSiC); near-universal driver coverage: transcription-factor fusions (18%), [NPM1](../genes/NPM1.md) (27%), tumor suppressors (16%), DNA-methylation genes (44%), activated signaling (59%), chromatin modifiers (30%), myeloid transcription factors (22%), cohesin complex (13%), spliceosome (14%); a novel NPM1 + [DNMT3A](../genes/DNMT3A.md) + [FLT3](../genes/FLT3.md) co-occurring triplet defined a putative epigenetic AML subtype with distinct mRNA, miRNA, and CpG-sparse methylation signatures [PMID:23634996](../papers/23634996.md)
- In a Sanger sequencing screen of 1,345 hematologic cancers for [CALR](../genes/CALR.md) exon 9 mutations, AML cases showed no CALR mutations, confirming that CALR indels are restricted to the MPN/MDS disease spectrum and are absent from acute myeloid leukemia. [PMID:24325359](../papers/24325359.md)

## Subtypes

- **[POLE](../genes/POLE.md) ultramutated / FAB-based stratification.** RNA-seq NMF consensus clustering identified 7 mRNA groups and 5 miRNA groups mapping onto FAB subtypes (M1, M3, M4, M5). [PMID:23634996](../papers/23634996.md)
- **Transcription-factor fusion-driven (PML-RARA, RUNX1-RUNX1T1, MYH11-CBFB, [KMT2A](../genes/KMT2A.md) fusions):** favorable-risk; carry the fewest cooperating mutations (MLL-fused mean 2.09 vs. 5.24 overall, P=0.002). [PMID:23634996](../papers/23634996.md)
- **NPM1 + [DNMT3A](../genes/DNMT3A.md) + [FLT3](../genes/FLT3.md) triple-mutant:** putative novel intermediate-risk subtype with methylation loss in CpG-sparse regions and distinct miRNA signature (high miR-10a, low miR-424). [PMID:23634996](../papers/23634996.md)
- **TP53-mutant unfavorable-risk:** mean 7.00 tier-1 mutations; mutually exclusive of FLT3 and NPM1; associated with complex cytogenetics. [PMID:23634996](../papers/23634996.md)

## Therapeutic landscape

- No drug treatments were administered or evaluated in the TCGA AML study; the dataset ([laml_tcga_pub](../datasets/laml_tcga_pub.md)) was released as a public resource for risk-stratification and pathogenesis research. [PMID:23634996](../papers/23634996.md)
- Authors argue that DNMT3A, IDH1/IDH2, and [TET2](../genes/TET2.md) add prognostic value for intermediate-risk classification beyond the then-current markers (FLT3, NPM1, [CEBPA](../genes/CEBPA.md), [KIT](../genes/KIT.md)). [PMID:23634996](../papers/23634996.md)

## Sources

- [PMID:23634996](../papers/23634996.md) — TCGA Research Network. Genomic and epigenomic landscapes of adult de novo acute myeloid leukemia. *N Engl J Med* 2013.

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:24325359](../papers/24325359.md)

*This page was processed by **crosslinker** on **2026-05-09**.*
