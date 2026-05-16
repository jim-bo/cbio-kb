---
name: Droplet Digital PCR (ddPCR)
slug: droplet-digital-pcr
kind: method
canonical_source: corpus
unverified: true
tags:
  - pcr
  - digital-pcr
  - validation
  - subclonal
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Droplet Digital PCR (ddPCR)

## Overview

Droplet digital PCR (ddPCR) is an [absolute](../methods/absolute.md) quantification method that partitions a PCR reaction into thousands of nanoliter droplets, each serving as an independent reaction. Positive and negative droplets are counted after endpoint PCR amplification, enabling highly sensitive detection and quantification of rare variants without the need for a standard curve. In cancer genomics it is used primarily for validation of low-frequency somatic mutations identified by next-generation sequencing and for quantification of subclonal variant allele frequencies.

## Used by

- Applied to validate subclonal/heterogeneity findings from whole-exome sequencing in grade II glioma paired initial/recurrent tumor cohort (n=23), confirming variant allele frequencies at low clonal abundance [PMID:24336570](../papers/24336570.md)
- Used in 5/5 tested [COADREAD](../cancer_types/COADREAD.md) cases to confirm frameshifted splice product from the recurrent APC intronic splice-acceptor mutation chr5:112151184 A>G in MSS CRC [PMID:29316426](../papers/29316426.md)
- ddPCR on a QX200 system used to validate selected variants from a multi-site breast cancer autopsy case; confirmed mutual exclusivity of ESR1 Y537 and ERBB2 driver mutations across metastatic sites at ~0.03% sensitivity [PMID:30205045](../papers/30205045.md)
- Used for orthogonal validation of PIK3CA hotspot mutations (H1047R/L/Y, E545K, E542K, C420R, N345K) across 90 plasma specimens in the breast_alpelisib_2020 ctDNA cohort [PMID:32864625](../papers/32864625.md)

## Notes

- Sensitivity typically reaches 0.01–0.1% variant allele frequency, well below standard WES detection thresholds (~5–10%).
- Used as an orthogonal validation method for mutations present at low allele frequencies in intratumoral heterogeneity studies.
- Unverified corpus-grown slug; not a cBioPortal gene panel identifier.

## Sources

*This page was processed by **crosslinker** on **2026-05-09**.*
- [PMID:29316426](../papers/29316426.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:30205045](../papers/30205045.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:32864625](../papers/32864625.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
