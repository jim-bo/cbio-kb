---
symbol: IGH
aliases: []
cancer_types:
  - DLBCL
tags:
  - immunoglobulin
  - gene-fusion
  - tcga-pancan
  - lymphoma
processed_by: wiki-cli
processed_at: 2026-09-10
---

# IGH

## Overview

IGH (Immunoglobulin Heavy locus) encodes the immunoglobulin heavy chain gene cluster on chromosome 14q32. In B-cell malignancies, IGH locus rearrangements are among the most clinically important structural variants: translocation of IGH with [MYC](../genes/MYC.md) (t(8;14)) is the hallmark of Burkitt lymphoma; IGH-BCL2 t(14;18) drives follicular lymphoma and diffuse large B-cell lymphoma (DLBCL); and IGH-BCL1/CCND1 t(11;14) defines mantle cell lymphoma. These translocations place oncogenes under the control of the strong IGH enhancer, driving aberrant expression.

## Alterations observed in the corpus

- IGH catalogued as a gene entity in the TCGA pan-cancer fusion atlas (9,624 samples, 33 cancer types including DLBCL), which systematically surveyed gene fusions across RNA-seq data from all major TCGA cancer types. [PMID:29617662](../papers/29617662.md)
- MYC translocation partner in 79% of MYC-translocated Burkitt lymphomas; IGH breakpoints were CSR-type in EBV-negative BL and SHM-type in EBV-positive BL. [PMID:36201743](../papers/36201743.md)

## Cancer types (linked)

- **DLBCL (diffuse large B-cell lymphoma):** IGH translocations are a defining feature of several B-cell lymphoma subtypes in the TCGA pan-cancer cohort. [PMID:29617662](../papers/29617662.md)

## Co-occurrence and mutual exclusivity

- No specific co-mutation pattern reported for IGH in the corpus.

## Therapeutic relevance

- No specific therapeutic annotation for IGH fusions reported in the corpus; IGH-partner oncogenes (MYC, [BCL2](../genes/BCL2.md), [CCND1](../genes/CCND1.md)) are the therapeutic targets in B-cell lymphoma.

## Open questions

- The pan-cancer fusion atlas (PMID:29617662) does not report detailed frequency or partner-gene breakdown for IGH fusions; comprehensive fusion calling in DLBCL and other B-cell malignancies requires specialized RNA-seq or WGS approaches tailored to immunoglobulin locus complexity. [PMID:29617662](../papers/29617662.md)

## Sources

- [PMID:29617662](../papers/29617662.md)
- [PMID:36201743](../papers/36201743.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
