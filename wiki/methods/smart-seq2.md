---
name: Smart-Seq2
slug: smart-seq2
kind: method
canonical_source: corpus
unverified: true
tags: [single-cell, transcriptomics, sequencing, full-length]
processed_by: entity-page-writer
processed_at: 2026-04-15
---

# Smart-Seq2

## Overview

Smart-Seq2 is a plate-based, full-length single-cell (or single-nucleus) RNA sequencing protocol that uses template-switching reverse transcription with locking oligonucleotides to capture transcripts from 5' to 3'. Unlike droplet-based UMI methods, Smart-Seq2 provides high-depth, full-length coverage per cell, enabling detection of splice isoforms and improving coverage of lowly expressed genes, at the cost of lower cell throughput.

## Used by

- [PMID:27806376](../papers/27806376.md) — plate-based Smart-Seq2 scRNA-seq applied to 4,347 FACS-sorted live single cells (calcein AM+/TO-PRO-3−) from 6 untreated IDH-mutant 1p/19q co-deleted oligodendrogliomas; 96 cells from MGH60 were also profiled in parallel with a UMI-based protocol with concordant results, validating Smart-Seq2 accuracy in the tumor context [PMID:27806376](../papers/27806376.md).
- [PMID:34493726](../papers/34493726.md) — Smart-Seq2 nuc-Seq applied to 11 neuroblastoma tumors (4,224 nuclei; average 709,676 reads/nucleus), 3 postnatal human adrenal glands (1,536 nuclei; ~485,000 reads/nucleus), and 5 mouse adrenal glands (1,920 cells; ~670,000 reads/cell); the full-length protocol supported identification of a novel NTRK2+/CLDN11+ cholinergic progenitor population absent from mouse adrenal gland [PMID:34493726](../papers/34493726.md).

## Notes

- Smart-Seq2 depth is higher than droplet methods per cell but total cell numbers are modest; rare subpopulations could be missed compared with 10x Chromium-scale datasets [PMID:34493726](../papers/34493726.md).
- Full-length coverage enables detection of allele-specific expression and splice variants that UMI-based 3'-end protocols cannot resolve [PMID:27806376](../papers/27806376.md).
- Corpus-grown slug; not present in canonical ontology.

## Sources

- [PMID:27806376](../papers/27806376.md)
- [PMID:34493726](../papers/34493726.md)

*This page was processed by **entity-page-writer** on **2026-04-15**.*
