---
name: Chromosome Arm Aneuploidy Score
slug: chromosome-arm-aneuploidy-score
kind: method
canonical_source: corpus
unverified: true
tags: [aneuploidy, copy-number, pan-cancer, score]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Chromosome Arm Aneuploidy Score

## Overview

A quantitative per-sample metric that counts the number of chromosome arms showing broad somatic copy-number alteration (gain or loss) relative to the sample's euploid level. The score ranges from 0 to 39 (summing altered p and q arms of non-acrocentric autosomes plus q arms of chromosomes 13–15, 21, and 22). Arm-level calls are derived from ABSOLUTE-segmented copy number using a Gaussian mixture model with BIC-based cluster selection (2–9 clusters); arms where the mean SCNA spans ≥80% of arm length are called "altered," ≤20% are called "normal," and intermediates are left uncalled.

## Used by

- Defined and applied to 10,522 TCGA pan-cancer tumors across 33 cancer types; score correlates almost perfectly with fraction of genome altered (Spearman ρ = 0.975); reveals [TP53](../genes/TP53.md) mutation as the only positive outlier in a pan-cancer multivariable linear model; shows cancer-type-specific clustering by arm-level pattern (squamous cluster: chr_3p loss + chr_3q gain) [PMID:29622463](../papers/29622463.md)
- Arm-level CNAs in 2,069 MSK-IMPACT-profiled prostate cancer patients were called with ASCETS; chr8q gain was enriched in Black men (49%) vs White men (37%, adjusted difference +11 pp, 95% CI 4–18) and was independently prognostic for survival [PMID:34667026](../papers/34667026.md)

## Notes

- The score is intentionally restricted to broad arm-level events and excludes focal SCNAs, departing from some other aneuploidy definitions in the literature.
- Score values range from 0 ([THCA](../cancer_types/THCA.md) mean 0.87) to ~18.7 ([TGCT](../cancer_types/TGCT.md) mean).
- Derived from Affymetrix SNP 6.0 + ABSOLUTE data; applying to other platforms requires re-derivation.
- Tetraploid samples (18 cases) are assigned score 0 as a conservative choice.

## Sources

*This page was processed by **crosslinker** on **2026-05-15**.*
- [PMID:34667026](../papers/34667026.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
