---
name: Cancer Cell Line Encyclopedia (Broad/Novartis)
studyId: cellline_ccle_broad
institution: Broad Institute / Novartis Institutes for BioMedical Research
size: 947
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [MUTATION_EXTENDED, COPY_NUMBER_ALTERATION, MRNA_EXPRESSION, PROTEOMICS]
panels: []
tags: [cell-line, pharmacogenomics, multi-omic, pan-cancer]
processed_by: entity-page-writer
processed_at: 2026-05-11
---

# Cancer Cell Line Encyclopedia (Broad/Novartis)

## Overview

The Cancer Cell Line Encyclopedia (CCLE) is a large-scale genomic and pharmacologic resource developed jointly by the Broad Institute and Novartis Institutes for BioMedical Research. It profiles 947 human cancer cell lines spanning 36 tumor lineages with multi-omic data — targeted massively parallel sequencing, copy number, gene expression, and mass spectrometric genotyping — coupled with pharmacologic profiling of 24 anticancer drugs across 479-481 lines using 8-point dose-response curves.

## Composition

- 947 cancer cell lines spanning 36 tumor lineages; cancer types include [MEL](../cancer_types/MEL.md), [NBL](../cancer_types/NBL.md), [PCM](../cancer_types/PCM.md), [ES](../cancer_types/ES.md), and many others.
- Pharmacologic profiling: 24 anticancer compounds (including [erlotinib](../drugs/erlotinib.md), [lapatinib](../drugs/lapatinib.md), [panobinostat](../drugs/panobinostat.md), [irinotecan](../drugs/irinotecan.md), [topotecan](../drugs/topotecan.md), [nutlin-3a](../drugs/nutlin-3a.md)) across 479-481 lines.

## Assays / panels (linked)

- Targeted massively parallel sequencing of >1,600 genes.
- OncoMap: mass spectrometric genotyping ([Sequenom genotyping](../methods/sequenom-genotyping.md)) of 492 mutations in 33 cancer genes.
- [Affymetrix SNP 6.0](../methods/affymetrix-snp6.md) copy number arrays.
- Affymetrix U133 Plus 2.0 expression arrays.
- Pharmacologic profiling: 8-point dose-response curves.

## Papers using this cohort

- [PMID:22460905](../papers/22460905.md) — Primary CCLE publication describing the resource and pharmacogenomic findings.
- [PMID:24686850](../papers/24686850.md) — Lin et al. (2014): CCLE cell-line expression data used to cross-reference ZNF750 mRNA expression in the context of ESCC genomic characterization.

## Notable findings derived from this cohort

- [EGFR](../genes/EGFR.md) mutations predict [erlotinib](../drugs/erlotinib.md) sensitivity; [ERBB2](../genes/ERBB2.md) amplification/overexpression predicts [lapatinib](../drugs/lapatinib.md) sensitivity; [BRAF](../genes/BRAF.md) V600E predicts sensitivity to RAF inhibitors PLX4720 and RAF265 [PMID:22460905](../papers/22460905.md).
- [SLFN11](../genes/SLFN11.md) expression is the top correlate of [irinotecan](../drugs/irinotecan.md) and [topotecan](../drugs/topotecan.md) sensitivity across 12 of 16 lineages; all three Ewing sarcoma lines tested were sensitive to irinotecan [PMID:22460905](../papers/22460905.md).
- [AHR](../genes/AHR.md) expression correlates with MEK inhibitor sensitivity in NRAS-mutant cancer cell lines; functional dependency confirmed by shRNA knockdown [PMID:22460905](../papers/22460905.md).
- 12 of 14 multiple myeloma ([PCM](../cancer_types/PCM.md)) cell lines showed enhanced sensitivity to the IGF-1R inhibitor AEW541, with high [IGF1](../genes/IGF1.md) and [IGF1R](../genes/IGF1R.md) expression [PMID:22460905](../papers/22460905.md).
- Hematologic lineages showed preferential sensitivity to [panobinostat](../drugs/panobinostat.md) (HDAC inhibitor) [PMID:22460905](../papers/22460905.md).
- [Elastic net](../methods/elastic-net.md) regression across >50,000 genomic features was used to build predictive models of drug sensitivity [PMID:22460905](../papers/22460905.md).
- [ZNF750](../genes/ZNF750.md) mRNA expression referenced from CCLE cell-line data as part of ESCC tumor-versus-normal expression comparisons [PMID:24686850](../papers/24686850.md).

## Sources

- [PMID:22460905](../papers/22460905.md)
- [PMID:24686850](../papers/24686850.md)

*This page was processed by **entity-page-writer** on **2026-05-11**.*
