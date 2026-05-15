---
name: Amplicon Sequencing
slug: amplicon-sequencing
kind: method
canonical_source: corpus
unverified: true
tags: [sequencing, deep-sequencing, editing-quantification]
processed_by: wiki-cli
processed_at: 2026-05-15
---

# Amplicon Sequencing

## Overview

Amplicon (deep) sequencing is a targeted PCR-amplicon-based next-generation sequencing approach that achieves very high depth (hundreds to thousands of reads) at specific genomic loci. It is commonly used to quantify somatic editing efficiency (Indel rates and HDR frequencies) at CRISPR-Cas9 cut sites, to validate somatic mutations identified by WES/WGS, or to detect rare variants in heterogeneous samples.

## Used by

- Amplicon deep sequencing of AAV-CRISPR-edited genomic loci (Tp53, Nf1, Pik3ca) was used to quantify Indel rates and HDR efficiency in rat mammary tumor models; confirmed ~4.2% whole-gland allelic editing and ~80% allelic editing in Nf1Indel tumors. [PMID:26437033](../papers/26437033.md)
- Ion AmpliSeq 8-gene amplicon panel (TP53, DNMT3A, IDH1, IDH2, ASXL1, SRSF2, U2AF1, SF3B1) applied to 45 AML/MDS patients on decitabine to track serial mutation clearance. [PMID:27959731](../papers/27959731.md)

## Notes

- Typical read depths for editing quantification: 1,000–10,000× per locus.
- Software such as CRISPResso or TIDE used for Indel spectrum analysis from amplicon reads.
- Distinct from targeted hybrid-capture sequencing (e.g., [targeted-dna-seq](../methods/targeted-dna-seq.md)) in that amplicon sequencing uses PCR preamplification rather than hybridization capture, giving higher depth but narrower genomic coverage.

## Sources

- [PMID:26437033](../papers/26437033.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:27959731](../papers/27959731.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
