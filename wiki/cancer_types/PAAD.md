---
name: Pancreatic Adenocarcinoma
oncotree_code: PAAD
parent: PANCREAS
tags: [pancreas, kras-driven]
processed_by: paper-compiler
processed_at: 2026-04-09
---

# Pancreatic Adenocarcinoma (PAAD)

## Overview

OncoTree code for pancreatic adenocarcinoma. In the corpus, PAAD is characterized by near-universal [KRAS](../genes/KRAS.md) mutation with allele-specific biology, recurrent [TP53](../genes/TP53.md) / [CDKN2A](../genes/CDKN2A.md) / [SMAD4](../genes/SMAD4.md) co-alterations, and clinical behavior strongly shaped by stage at resection.

## Cohorts in the corpus

- [msk_chord_2024](../datasets/msk_chord_2024.md) — 3,109 pancreatic cancer patients at MSK in the MSK-CHORD clinicogenomic harmonized real-world dataset [PMID:39506116](../papers/39506116.md).
- [pancreas_msk_2024](../datasets/pancreas_msk_2024.md) — 1,360 consecutive resected PDAC patients at MSK (2004–2019), with [MSK-IMPACT](../methods/msk-impact-panel.md) targeted sequencing on 397, bulk RNA-seq on 100, and [CosMx SMI](../methods/cosmx-smi.md) spatial profiling on 20 [PMID:39214094](../papers/39214094.md).

## Recurrent alterations

- Included in pan-cancer MSK-IMPACT pathway and metastasis analyses [PMID:39506116](../papers/39506116.md).
- Canonical driver frequencies in the resected MSK cohort (n=397 sequenced): [KRAS](../genes/KRAS.md) 90%, [TP53](../genes/TP53.md) 71%, [CDKN2A](../genes/CDKN2A.md) 24%, [SMAD4](../genes/SMAD4.md) 17%; no significant difference in these frequencies between early- and late-stage disease after multiple-testing correction [PMID:39214094](../papers/39214094.md).
- KRAS allele distribution: G12D 36.5%, G12V 32.5%, G12R 13.9%, other KRAS 8.1%, KRAS wildtype 9.1% [PMID:39214094](../papers/39214094.md).
- KRAS^G12R^ tumors carry a higher proportion of CDKN2A mutations than KRAS^G12D^ (40% vs 22.1%, p=0.046) [PMID:39214094](../papers/39214094.md).

## Subtypes

- KRAS^G12R^-mutant PDAC is a distinct clinical subset: enriched in stage I disease (23% vs 11% in stage II–III, p=0.022), more often node-negative (47% vs 26% for KRAS^G12D^, p=0.019), with improved OS and decreased distant recurrence compared to KRAS^G12D^; also associated with family history of pancreatic cancer (16.4% vs 4.2%, p=0.003) [PMID:39214094](../papers/39214094.md).
- Transcriptional programs diverge by KRAS allele: KRAS^G12D^ tumors show enhanced KRAS signaling and EMT; KRAS^G12R^ tumors show increased TNF/NF-κB signaling by both bulk RNA-seq and [CosMx SMI](../methods/cosmx-smi.md) spatial profiling [PMID:39214094](../papers/39214094.md).

## Therapeutic landscape

- NLP-augmented integrated survival-prediction models outperformed stage- or genomics-only models [PMID:39506116](../papers/39506116.md).
- KRAS^G12R^ resected PDAC was enriched among patients who received neoadjuvant [fluorouracil](../drugs/fluorouracil.md)-based chemotherapy (most frequently FOLFIRINOX with [irinotecan](../drugs/irinotecan.md) and [oxaliplatin](../drugs/oxaliplatin.md)), consistent with higher response likelihood rather than borderline-resectable selection [PMID:39214094](../papers/39214094.md).
- Allele-specific transcriptional divergence (NF-κB vs KRAS/EMT) suggests divergent actionable dependencies across KRAS-mutant PDAC rather than a single pan-KRAS strategy [PMID:39214094](../papers/39214094.md).

## Sources

- [PMID:39506116](../papers/39506116.md)
- [PMID:39214094](../papers/39214094.md)

*This page was processed by **paper-compiler** on **2026-04-09**.*
