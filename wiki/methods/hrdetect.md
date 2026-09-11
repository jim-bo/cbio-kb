---
name: HRDetect
slug: hrdetect
kind: MUTATION_EXTENDED
canonical_source: corpus
unverified: true
tags: [homologous-recombination, mutational-signatures, wgs, brca-deficiency]
processed_by: wiki-cli
processed_at: 2026-09-10
---

# HRDetect

## Overview

HRDetect is a machine-learning classifier that combines six mutational-signature features (SBS3, SBS8, deletions at microhomology, SV signatures, indel enrichment, and large deletions) to assign a probability of homologous-recombination deficiency (HRD) to a tumour. A score >0.7 is typically used as the HRD-positive threshold.

## Used by

- Applied in the Sherlock-Lung WGS study of 232 never-smoker lung cancers (LCINS); approximately 16% of tumours (n=37) scored >0.7 (HRD-positive), concentrated in the forte and mezzo-forte SCNA subtypes (P=1.4e-3 vs piano) [PMID:34493867](../papers/34493867.md)
- Used (with COSMIC v3.1 signatures) to call homologous-recombination deficiency in whole-genome-sequenced CDH1-wild-type invasive lobular carcinomas [PMID:38347189](../papers/38347189.md).

## Notes

- Originally validated in breast cancer (BRCA1/2-deficient tumours); applicability in lung cancer underscores its cross-tumour-type utility.
- In the Sherlock-Lung cohort, biallelic [ATM](../genes/ATM.md) loss was confirmed in one HRDetect-positive tumour; monoallelic loss of HRD-associated genes was found in 42% of all 232 tumours.
- HRD-positive tumours in the LCINS cohort are candidates for PARP inhibitor therapy.

## Sources

- [PMID:38347189](../papers/38347189.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
