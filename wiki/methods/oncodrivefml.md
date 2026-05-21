---
name: OncodriveFML
slug: oncodrivefml
kind: method
canonical_source: corpus
unverified: true
tags: [cancer-gene-discovery, functional-impact, driver-detection]
processed_by: crosslinker
processed_at: 2026-05-21
---

# OncodriveFML

## Overview

OncodriveFML is a computational method for identifying cancer driver genes by testing whether the observed somatic mutations in a gene have higher functional impact scores (e.g., from CADD or SIFT) than expected by chance, given the local sequence context and trinucleotide mutation signatures. Unlike enrichment-based methods ([MutSig](../methods/mutsig.md), [dN/dS](../methods/dndscv.md)), it leverages functional impact predictions and can detect positive selection even in genes with relatively few mutations, provided those mutations are functionally damaging.

## Used by

- Applied as one of four cancer-gene discovery tools (alongside [MutSig](../methods/mutsig.md), [LOFsigrank](../methods/lofsigrank.md), and [dN/dS](../methods/dndscv.md)) in a cutaneous squamous cell carcinoma ([CSCC](../cancer_types/CSCC.md)) meta-analysis of 88 QC-passed tumors from 10 WES/WGS studies; collectively the four tools nominated 12 cancer genes, 7 of which were called by ≥2 tools; driver candidates were additionally supplemented by [3D Hotspots](../methods/3d-hotspots.md) and [cancer hotspots](../methods/cancer-hotspots.md) overlap and focal copy-number analysis [PMID:34272401](../papers/34272401.md)
- Applied alongside MutSigCV to 122 [HCC](../cancer_types/HCC.md) biopsies ([hcc_meric_2021](../datasets/hcc_meric_2021.md)) to identify significantly mutated genes; confirmed the same 7 SMGs including newly nominated [GPAM](../genes/GPAM.md) (7/9 frameshift mutations) [PMID:35508466](../papers/35508466.md)

## Notes

- Corpus-grown slug; not listed in `schema/ontology/gene_panels.json` or any cBioPortal canonical list.
- OncodriveFML is particularly useful for detecting tumor suppressor genes with scattered inactivating mutations, and for cancer types with high TMB (e.g., UV-driven [CSCC](../cancer_types/CSCC.md)) where statistical background models must account for elevated mutation rates.
- Reference: Mularoni et al., Genome Biology 2016.

## Sources

- [PMID:34272401](../papers/34272401.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
- [PMID:35508466](../papers/35508466.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
