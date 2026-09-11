---
name: Cancer Hotspots
slug: cancer-hotspots
kind: method
canonical_source: corpus
unverified: true
tags: [mutation-annotation, hotspot-detection, driver-discovery]
processed_by: crosslinker
processed_at: 2026-09-11
---

# Cancer Hotspots

## Overview

Cancer Hotspots is a statistical method for identifying recurrently mutated positions in cancer genomes using 2D linear protein sequence proximity. Mutations at a given amino acid position are considered a hotspot if they occur more frequently than expected by chance across a large cancer cohort. The method provides a complementary approach to 3D structural hotspot analysis (3D Hotspots) and is available as a public resource at cancerhotspots.org.

## Used by

- Applied (alongside 3D protein-structure hotspot analysis) to annotate driver mutations in 9,125 TCGA PanCanAtlas tumors across 33 cancer types, contributing to the identification of 89% of tumors carrying at least one pathway driver alteration [PMID:29625050](../papers/29625050.md).
- Chang et al. 2016 hotspot algorithm applied to a combined 2,732-breast-tumor cohort (MSK prospective + TCGA retrospective), identifying 313 significant hotspots in 72 genes; 12 novel [PIK3CA](../genes/PIK3CA.md) hotspots discovered [PMID:30205045](../papers/30205045.md)
- Cancer Hotspots used alongside OncoKB for oncogenicity annotation of somatic variants in 487 EAC/EGJ patients at MSK; copy-number purity/ploidy correction via FACETS [PMID:33795256](../papers/33795256.md)
- Applied in conjunction with four statistical gene-discovery tools ([MutSig](../methods/mutsig.md), [LOFsigrank](../methods/lofsigrank.md), [dN/dS](../methods/dndscv.md), [OncodriveFML](../methods/oncodrivefml.md)) to rescue additional driver gene candidates in a [CSCC](../cancer_types/CSCC.md) ([CSCC](../cancer_types/CSCC.md)) meta-analysis of 88 tumors; cancerhotspots.org overlap supplemented the 12 statistical nominees to reach the final 30-gene driver set [PMID:34272401](../papers/34272401.md)
- The Chang et al. cancer-hotspots method found 52 substitution hotspots across 14 genes (13 in [APC](../genes/APC.md), 8 of them novel) in 1,015 Chinese colorectal cancer patients. [PMID:35487942](../papers/35487942.md)
- The cancer-hotspots algorithm was run on 45,492 tumors across 77 cancer types, flagging 313 candidate codons (Q<0.01) later filtered to 164 new hotspots. [PMID:41895280](../papers/41895280.md)

## Notes

- Identifies hotspots based on recurrence at specific amino acid positions in the linear protein sequence.
- Complements 3D Hotspots, which uses structural proximity rather than linear position.
- Part of the TCGA PanCanAtlas driver-annotation suite alongside MutSigCV, GISTIC 2.0, OncoKB, and RESET.
- Available as a public web resource; commonly used with OncoKB for oncogenicity classification.

## Sources
- [PMID:30205045](../papers/30205045.md)
- [PMID:33795256](../papers/33795256.md)

- [PMID:34272401](../papers/34272401.md)
- [PMID:35487942](../papers/35487942.md)
- [PMID:41895280](../papers/41895280.md)

*This page was processed by **crosslinker** on **2026-09-11**.*
