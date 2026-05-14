---
symbol: PPM1D
aliases: []
cancer_types:
  - LUAD
  - BRCA
  - PRAD
tags:
  - clonal-hematopoiesis
  - therapy-related
processed_by: wiki-cli
processed_at: 2026-05-14
---

# PPM1D

## Overview

PPM1D (protein phosphatase Mg2+/Mn2+-dependent 1D, also known as Wip1) encodes a serine/threonine phosphatase that negatively regulates the DNA damage response by dephosphorylating [ATM](../genes/ATM.md), p53, and H2AX. Truncating mutations in exon 6 are a recurrent form of clonal hematopoiesis (CH), particularly enriched after cytotoxic chemotherapy or radiation, and can confound tumor-tissue sequencing when blood-based contamination is not controlled.

## Alterations observed in the corpus

- **Clonal hematopoiesis variant enriched after prior systemic therapy:** PPM1D truncating variants (alongside [CHEK2](../genes/CHEK2.md) variants) are flagged as clonal-hematopoiesis (CH) mutations enriched after prior systemic therapy in a large multi-cancer real-world dataset (MSK-CHORD), encompassing [LUAD](../cancer_types/LUAD.md), [BRCA](../cancer_types/BRCA.md), and [PRAD](../cancer_types/PRAD.md) patients. [PMID:39506116](../papers/39506116.md)
- Single frameshift mutation identified in the sinonasal adenoid cystic carcinoma cohort; PPM1D (Wip1 phosphatase) is a known oncogene that restrains p53 activity [PMID:24418857](../papers/24418857.md)
- PPM1D identified as one of seven significantly mutated genes (SMGs, q<0.1) in the TCGA PTC cohort (n=402 exome-sequenced tumors); DNA-repair SMG co-occurring with MAPK-pathway drivers; DNA-repair mutations associated with higher mutation density (p=0.022) and high-risk patients (p=0.018). [PMID:25417114](../papers/25417114.md)

## Cancer types (linked)

- **[LUAD](../cancer_types/LUAD.md) / [BRCA](../cancer_types/BRCA.md) / [PRAD](../cancer_types/PRAD.md):** PPM1D CH variants appear in tumor-sequencing data from multiple cancer types within MSK-CHORD, reflecting the pan-cancer nature of therapy-related clonal hematopoiesis rather than a somatic tumor driver role. [PMID:39506116](../papers/39506116.md)

## Co-occurrence and mutual exclusivity

- Co-flagged with [CHEK2](../genes/CHEK2.md) as a clonal-hematopoiesis marker enriched in patients who have received prior systemic therapy. [PMID:39506116](../papers/39506116.md)

## Therapeutic relevance

- PPM1D CH variants are a biomarker of prior therapy exposure rather than a therapeutic target in the current corpus. Their enrichment after treatment may complicate interpretation of tumor NGS panels that do not have matched germline comparators.

## Open questions

- The degree to which PPM1D CH variants in MSK-CHORD are tumor-derived versus blood-contamination artifacts remains to be formally quantified; the paper identifies the association but does not resolve the source. [PMID:39506116](../papers/39506116.md)

## Sources

- [PMID:39506116](../papers/39506116.md)

*This page was processed by **crosslinker** on **2026-05-04**.*
- [PMID:24418857](../papers/24418857.md)

*This page was processed by **wiki-cli** on **2026-05-09**.*
- [PMID:25417114](../papers/25417114.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
