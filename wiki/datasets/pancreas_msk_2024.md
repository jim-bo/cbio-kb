---
name: MSK Resected PDAC KRAS-Allele Cohort (2024)
slug: pancreas_msk_2024
institution: Memorial Sloan Kettering Cancer Center
size: 1360
assays:
  - msk-impact-panel
  - cosmx-smi
tags:
  - pdac
  - kras-alleles
  - surgical-resection
  - spatial-transcriptomics
processed_by: crosslinker
processed_at: 2026-04-10
---

# MSK Resected PDAC KRAS-Allele Cohort (2024)

## Overview

Single-institution retrospective cohort of 1,360 consecutive patients with pancreatic ductal adenocarcinoma who underwent surgical resection at Memorial Sloan Kettering between April 2004 and April 2019, assembled to interrogate [KRAS](../genes/KRAS.md) allele–specific clinical outcomes and biology in [PAAD](../cancer_types/PAAD.md) [PMID:39214094](../papers/39214094.md).

## Composition

- 1,360 resected PDAC patients; 397 (29%) stage I, 963 (71%) stage II–III; [OS](../cancer_types/OS.md) of the full cohort 30.7 months (95% CI 28.0–32.8) [PMID:39214094](../papers/39214094.md).
- Tumor targeted sequencing on [MSK-IMPACT](../methods/msk-impact-panel.md) in 397 patients (103 stage I, 294 stage II–III) with no sequencing selection criteria [PMID:39214094](../papers/39214094.md).
- Bulk RNA-seq on 100 resected tumors and high-plex spatial profiling on 20 patients (14 tumors, 6 normal) using NanoString [CosMx SMI](../methods/cosmx-smi.md) tissue microarrays [PMID:39214094](../papers/39214094.md).
- 22% of the sequenced subset received neoadjuvant therapy (most commonly 5-FU–based regimens, frequently FOLFIRINOX); 82% received adjuvant therapy [PMID:39214094](../papers/39214094.md).

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — targeted tumor sequencing, used for driver-gene and KRAS-allele calls across the 397-patient sequenced subset [PMID:39214094](../papers/39214094.md).
- [CosMx SMI](../methods/cosmx-smi.md) — NanoString high-plex spatial molecular imaging on TMAs for the 20-patient spatial subcohort [PMID:39214094](../papers/39214094.md).

## Papers using this cohort

- [PMID:39214094](../papers/39214094.md) — McIntyre et al., Cancer Cell 2024. KRAS^G12R^ enrichment in early-stage PDAC with distinct clinical outcomes and NF-κB-biased transcriptional program.

## Notable findings derived from this cohort

- [KRAS](../genes/KRAS.md) altered in 90%, [TP53](../genes/TP53.md) 71%, [CDKN2A](../genes/CDKN2A.md) 24%, [SMAD4](../genes/SMAD4.md) 17%; KRAS allele distribution G12D 36.5% / G12V 32.5% / G12R 13.9% / other 8.1% / WT 9.1% [PMID:39214094](../papers/39214094.md).
- KRAS^G12R^ enriched in stage I disease (23% vs 11%), more often node-negative (47% vs 26% for G12D), and associated with improved OS and reduced distant recurrence [PMID:39214094](../papers/39214094.md).
- KRAS^G12R^ tumors carry a higher frequency of [CDKN2A](../genes/CDKN2A.md) mutations than KRAS^G12D^ (40% vs 22.1%) [PMID:39214094](../papers/39214094.md).

## Sources

- cBioPortal study: https://www.cbioportal.org/study/summary?id=pancreas_msk_2024

*This page was processed by **crosslinker** on **2026-04-10**.*
