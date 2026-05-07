---
name: lapatinib
targets: [EGFR, ERBB2]
drug_class: dual EGFR/HER2 tyrosine kinase inhibitor
canonical_source: corpus
unverified: true
tags: [targeted-therapy, tki, egfr, her2]
processed_by: wiki-cli
processed_at: 2026-05-06
---

# lapatinib

## Overview

Lapatinib (Tykerb) is an oral small-molecule reversible inhibitor of both [EGFR](../genes/EGFR.md) and [ERBB2](../genes/ERBB2.md) (HER2) tyrosine kinase domains. It is FDA-approved for HER2-positive metastatic breast cancer in combination with [capecitabine](../drugs/capecitabine.md) and for HER2+ metastatic/locally advanced breast cancer in combination with letrozole. It blocks downstream MAPK and PI3K/AKT signaling from both receptors.

## Evidence in the corpus

- In HER2+ OE19 (esophageal) and HER2+ NCI-N87 (gastric) cancer cell viability assays, lapatinib was used as a dual EGFR/HER2 TKI comparator; T-DM1 was more potent than lapatinib at sub-nanomolar concentrations in HER2+ cells, demonstrating that cytotoxic payload delivery via ADC surpasses receptor signal inhibition in this context [PMID:27698471](../papers/27698471.md).
- Lapatinib represents the ErbB signal-inhibition strategy that the paper argues is suboptimal due to bypass-pathway resistance (downstream signaling via alternate ErbB members, PI3K/RAS pathways), which the ADC approach circumvents [PMID:27698471](../papers/27698471.md).
- Included in the CCLE pharmacogenomic screen across 947 cancer cell lines; sensitivity correlated with genomic features via elastic-net regression [PMID:22460905](../papers/22460905.md)
- NCI-60 CellMiner pharmacogenomics analysis linked EGFR/ERBB2 pathway activity to lapatinib sensitivity across cancer cell lines including colon [PMID:22802077](../papers/22802077.md)

## Resistance mechanisms

- Bypass-pathway activation (via alternate [EGFR](../genes/EGFR.md)/[ERBB2](../genes/ERBB2.md)/ErbB3/ErbB4 signaling) is cited as a general limitation of EGFR/HER2 signal-inhibition strategies including lapatinib, motivating ADC-based approaches [PMID:27698471](../papers/27698471.md).

## Cancer types (linked)

- [ESCA](../cancer_types/ESCA.md)
- [STAD](../cancer_types/STAD.md)

## Sources

- [PMID:27698471](../papers/27698471.md)

*This page was processed by **crosslinker** on **2026-05-04**.*
- [PMID:22460905](../papers/22460905.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
- [PMID:22802077](../papers/22802077.md)

*This page was processed by **wiki-cli** on **2026-05-06**.*
