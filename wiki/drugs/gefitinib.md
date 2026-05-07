---
name: gefitinib
targets: [EGFR]
drug_class: EGFR tyrosine kinase inhibitor (first-generation)
canonical_source: corpus
unverified: true
tags:
  - targeted-therapy
  - egfr-inhibitor
  - sarcoma
  - functional-precision-medicine
processed_by: wiki-cli
processed_at: 2026-05-06
---

# gefitinib

## Overview

Gefitinib (Iressa) is a first-generation, reversible [EGFR](../genes/EGFR.md) tyrosine kinase inhibitor (TKI) with FDA approval for first-line treatment of metastatic [NSCLC](../cancer_types/NSCLC.md) harboring [EGFR](../genes/EGFR.md) exon 19 deletions or exon 21 (L858R) substitution mutations. It competes with [erlotinib](../drugs/erlotinib.md) and was largely superseded in clinical practice by third-generation [osimertinib](../drugs/osimertinib.md) for EGFR-mutant [NSCLC](../cancer_types/NSCLC.md).

## Evidence in the corpus

- Mutually exclusive [EGFR](../genes/EGFR.md) and [KRAS](../genes/KRAS.md) mutations in [LUAD](../cancer_types/LUAD.md) (n=188, P<1e-7) support independent treatment stratification: EGFR-mutant tumours (enriched in never-smokers, P=0.0046) are the primary target population for gefitinib and related EGFR TKIs. [PMID:18948947](../papers/18948947.md)
- In a PDTO functional screen of 92 sarcoma specimens, PDTOs from patients with progressive disease at follow-up were more resistant to gefitinib (p=0.048) than those from patients with stable or responding disease, suggesting EGFR pathway dependence may be diminished in clinically aggressive sarcomas [PMID:39305899](../papers/39305899.md).
- EGFR/ErbB signaling was implicated by pathway analysis (PubChem + WikiPathways/KEGG) in chordoma PDTOs (SARC0046_2/3, SARC0053_a, SARC0049) and an osteosarcoma subgroup; chordomas showed preferential sensitivity to TAK-285 (an EGFR/ERBB2 dual kinase inhibitor), consistent with broader EGFR pathway dependency in this histology [PMID:39305899](../papers/39305899.md).
- NCI-60 CellMiner pharmacogenomics study identified EGFR-pathway genomic features associated with gefitinib sensitivity in colon cancer cell lines [PMID:22802077](../papers/22802077.md)

## Resistance mechanisms

- Clinical disease progression in sarcoma patients correlates with resistance to gefitinib in PDTO assays (p=0.048), implying that rapidly progressive sarcomas may have downregulated or bypassed EGFR dependency [PMID:39305899](../papers/39305899.md).

## Cancer types (linked)

- Sarcoma (various histologies — functional PDTO screen, progressive-disease correlation)
- [CHDM](../cancer_types/CHDM.md) — chordoma (EGFR/ErbB pathway implicated by KEGG analysis)

## Sources

- [PMID:18948947](../papers/18948947.md) — Ding et al. 2008, *Nature*. Exome-scale somatic mutation landscape of 188 LUAD tumours; mutual exclusivity of EGFR and KRAS mutations supports TKI stratification.
- [PMID:39305899](../papers/39305899.md) — Al Shihabi et al. 2024, *Cell Stem Cell*. Sarcoma PDTO functional precision-medicine screen; gefitinib resistance associated with progressive disease at follow-up.

*This page was processed by **crosslinker** on **2026-05-05**.*
- [PMID:22802077](../papers/22802077.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
