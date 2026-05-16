---
name: RB1 cfDNA Custom Capture Panel
slug: rb1-cfdna-custom-capture-panel
kind: method
canonical_source: corpus
unverified: true
tags:
  - liquid-biopsy
  - ctdna
  - targeted-sequencing
  - panel
  - retinoblastoma
  - hybrid-capture
processed_by: crosslinker
processed_at: 2026-05-16
---

# RB1 cfDNA Custom Capture Panel

## Overview

A custom hybrid-capture targeted sequencing panel developed at Memorial Sloan Kettering Cancer Center specifically for plasma cell-free DNA (cfDNA) analysis in retinoblastoma. The panel tiles all 27 exons of [RB1](../genes/RB1.md) along with heterozygous-SNP regions used for allele-specific copy-number estimation. It is sequenced on Illumina HiSeq 2×100 bp paired-end chemistry and achieves average unique coverage of approximately 1530×, providing the depth needed to detect somatic RB1 mutations at low variant allele frequencies (VAF 0.7%–12.6% in the primary cohort). This panel addresses the clinical problem that intraocular biopsy is contraindicated in retinoblastoma and ophthalmic artery chemosurgery has reduced enucleation rates, eliminating most tumor tissue from molecular workups.

## Used by

- Applied to matched plasma and buffy-coat cfDNA from 10 pediatric patients with advanced unilateral retinoblastoma who underwent primary enucleation at MSKCC; cfDNA yields 5.5–27.4 ng (mean 17.3 ng); tumor-guided genotyping via [Waltz 2.0](../methods/waltz.md) recovered 10/13 somatic RB1 mutations in 8/10 patients (median VAF 4.9%); tumor-blind de novo calling via [VarDict](../methods/vardict.md) recovered 7/13 mutations in 6/10 patients [PMID:32633890](../papers/32633890.md)

## Notes

- Designed exclusively for RB1 exon coverage; does not provide genome-wide or multi-gene panel coverage. Authors flag incorporation of copy-number analysis to capture the ~1% of retinoblastomas driven by [MYCN](../genes/MYCN.md) amplification (RB1-wildtype) as a future extension.
- No unique molecular identifiers (UMIs) in the current version; authors flag UMI integration as the primary sensitivity improvement pathway.
- Used in conjunction with [MSK-IMPACT](../methods/msk-impact-panel.md) tumor sequencing and the [rbl_cfdna_msk_2020](../datasets/rbl_cfdna_msk_2020.md) cBioPortal dataset.
- Five samples with leftover library were run as technical replicates; Waltz VAF concordance showed Pearson r²=0.993.

## Sources

- [PMID:32633890](../papers/32633890.md) — Plasma cfDNA somatic RB1 mutation detection in pediatric retinoblastoma; custom hybrid-capture panel used for plasma/buffy-coat sequencing.

*This page was processed by **crosslinker** on **2026-05-16**.*
