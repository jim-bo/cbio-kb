---
name: Pediatric Pancan Tumors (MSK, Nat Commun. 2022)
studyId: mixed_kunga_msk_2022
institution: Memorial Sloan Kettering Cancer Center
size: 114
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [whole-genome-seq, rna-seq, msk-impact, cfdna-wgs]
panels: [IMPACT468, MSK-Fusion]
tags: [pediatric, pancan, sarcoma, neuroblastoma, osteosarcoma, whole-genome-sequencing, msk]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Pediatric Pancan Tumors (MSK, Nat Commun. 2022)

## Overview

Prospective clinical whole genome and transcriptome sequencing (cWGTS) cohort of 114 pediatric, adolescent, and young adult patients with solid tumors and rare cancers enrolled at MSK on protocol NCT01775072. Built to benchmark a 9-day sample-to-report end-to-end WGS pipeline and to demonstrate the added clinical value of WGS over standard panel-based testing. Released on cBioPortal as study `mixed_kunga_msk_2022`. [PMID:35585047](../papers/35585047.md)

## Composition

- **n=114** patients with solid tumors; median age 12.6 years (range 4.5 months to 43.8 years).
- Disease classes: sarcoma (n=54), neuroblastoma (n=29), osteosarcoma (n=29), CNS tumors, carcinoma (n=7), Wilms tumor, germ cell tumor, hepatoblastoma, and other rare entities.
- Of 201 nominated tumors, 58 excluded on pathology review and 29 failed the >20% tumor-purity threshold.
- Companion exploratory cohort: 7 paired fresh-frozen tumor + plasma cfDNA samples for cWGTS feasibility. [PMID:35585047](../papers/35585047.md)
- Mixed cancer types including [SARC](../cancer_types/SARC.md), [NBL](../cancer_types/NBL.md), [OS](../cancer_types/OS.md), and others.

## Assays / panels (linked)

- [Whole-genome sequencing](../methods/whole-genome-seq.md): Illumina NovaSeq 6000, PE150; median tumor depth 95× (range 67–181), normal 50× (range 32–159); fresh-frozen or OCT biopsies with matched normal buffy coat.
- [RNA-seq](../methods/rna-seq.md): whole-transcriptome on 101/114 patients.
- [MSK-IMPACT](../methods/msk-impact-panel.md) (468-gene DNA panel) and [MSK-Fusion](../methods/msk-fusion.md) (RNA fusion capture) for orthogonal validation.
- Germline analysis on a subset of 88 cancer-predisposition genes.
- cfDNA WGS (7 patients; 94–102× coverage) as proof-of-concept. [PMID:35585047](../papers/35585047.md)
- Recommended WGS depth: ≥80× effective coverage (plateaus sensitivity for SNVs, indels, and SVs by subsampling analysis).

## Papers using this cohort

- [PMID:35585047](../papers/35585047.md) — Shukla, Levine, Gundem et al., *Nat Commun* 2022: prospective cWGTS in 114 pediatric solid tumors; primary discovery and benchmarking study for this dataset.

## Notable findings derived from this cohort

- cWGTS identified at least one additional oncogenic cancer-associated variant in 54% of patients (n=62) beyond [MSK-IMPACT](../methods/msk-impact-panel.md), [MSK-Fusion](../methods/msk-fusion.md), and germline 88-gene panel testing combined; of these, 33 were directly clinically relevant (7 diagnostic, 15 prognostic, 5 therapy-informing, 5 novel oncofusions, 6 germline). [PMID:35585047](../papers/35585047.md)
- End-to-end sample-to-report turnaround of 9 days (post-optimization); 79% concordance with MSK-IMPACT somatic mutation calls; discordant calls attributed to intratumoral heterogeneity (subclonal, median VAF 8.5%). [PMID:35585047](../papers/35585047.md)
- Most incremental clinical findings came from structural variants (SVs) and genome-wide mutation signatures; only 27% would have been captured by WES + RNA-seq alone. [PMID:35585047](../papers/35585047.md)
- Chromothripsis detected in 40% of patients (most common in sarcomas 35/58); whole-genome duplication in 42/114 patients (enriched in sarcoma 24/54, neuroblastoma 11/30). [PMID:35585047](../papers/35585047.md)
- [TP53](../genes/TP53.md) SVs targeting the [TP53](../genes/TP53.md) locus were identified in 13/29 osteosarcoma patients; [TERT](../genes/TERT.md) and [ATRX](../genes/ATRX.md) rearrangements detected in neuroblastoma — illustrating the value of WGS over exome for noncoding alterations. [PMID:35585047](../papers/35585047.md)
- cfDNA WGS proof-of-concept: in patients with sufficient ctDNA (~10–83%), cfDNA genome-wide profiles recapitulated tumor mutation landscape including SNVs, amplifications, and SVs. [PMID:35585047](../papers/35585047.md)

## Sources

- cBioPortal study `mixed_kunga_msk_2022`; reference genome hg19; NCT01775072. [PMID:35585047](../papers/35585047.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
