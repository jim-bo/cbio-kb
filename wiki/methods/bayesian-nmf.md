---
name: Bayesian NMF
slug: bayesian-nmf
kind: method
canonical_source: 
unverified: true
tags: [mutational-signatures, computational]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Bayesian NMF

## Overview

Bayesian non-negative matrix factorization for de novo decomposition of mutational catalogs into signatures.

## Used by

- [PMID:35927489](../papers/35927489.md) — applied as part of the CLL-map mutational signature analysis across 177 WGS samples, identifying aging, canonical AID (SBS84) enriched in clustered mutations in U-CLL, non-canonical AID (SBS85) enriched in M-CLL (p=1.6×10^-9), and SBS18 (reactive oxygen species) [PMID:35927489](../papers/35927489.md).
- Non-negative matrix factorization applied to mutation spectra of 1,144 NSCLC exomes; identified 6 mutational signatures mapping to COSMIC SI4 (smoking), SI7 (UV), SI13/SI2 (APOBEC), SI15/SI6 (MMR), and SI5 (clock-like) [PMID:27158780](../papers/27158780.md)
- Bayesian NMF used for mutation-signature discovery in the TCGA esophageal/stomach study, identifying distinct C>A (smoking) and APOBEC signatures enriched in ESCC vs. EAC [PMID:28052061](../papers/28052061.md).
- Applied to 412 BLCA SNV catalogue resolving 5 mutational signatures: APOBEC-a, APOBEC-b, C>T at CpG, POLE, and an ERCC2 signature; APOBEC-a + APOBEC-b accounted for 67% of all SNVs [PMID:28988769](../papers/28988769.md)
- Mutational signatures in 304 DLBCLs discovered via Bayesian NMF (SignatureAnalyzer framework); identified three dominant processes: aging/CpG deamination (~80%), canonical AID at RCY motifs, and AID2 at WA motifs [PMID:29713087](../papers/29713087.md)
- Applied in the high-grade UTUC WES/RNA-seq study (37 tumors) for de novo mutational signature discovery; identified dominant APOBEC (COSMIC 2, 13), defective MMR (COSMIC 6), and ERCC2-like (COSMIC 5) signatures via cosine similarity clustering against 30 COSMIC signatures [PMID:31278255](../papers/31278255.md)

## Notes

- Bayesian NMF is paired with whole-genome sequencing in the CLL cohort to support both de novo and reference-signature attribution [PMID:35927489](../papers/35927489.md).

## Sources

- [PMID:35927489](../papers/35927489.md)

*This page was processed by **crosslinker** on **2026-04-08**.*
- [PMID:27158780](../papers/27158780.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28052061](../papers/28052061.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28988769](../papers/28988769.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29713087](../papers/29713087.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:31278255](../papers/31278255.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
