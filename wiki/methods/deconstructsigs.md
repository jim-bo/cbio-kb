---
name: deconstructSigs
slug: deconstructsigs
kind: method
canonical_source: corpus
unverified: true
tags:
  - mutational-signatures
  - signature-deconvolution
  - somatic-mutation
  - cosmic
processed_by: wiki-cli
processed_at: 2026-09-10
---

# deconstructSigs

## Overview

deconstructSigs is an R package for decomposing the mutational spectrum of a tumor sample into a weighted mixture of known COSMIC mutational signatures. Given the trinucleotide-context mutation counts for a sample, it solves for the linear combination of reference signatures (e.g., COSMIC v2 or v3) that best fits the observed profile. It is commonly applied to targeted-panel or whole-exome sequencing data to assign dominant mutational processes (aging, APOBEC, HRD, tobacco, etc.) to individual samples, although it requires a minimum number of mutations for reliable decomposition (typically ≥50 SNVs for targeted panels, ≥40 for WES as applied in Pareja et al. 2020).

## Used by

- [brca_pareja_msk_2020](../datasets/brca_pareja_msk_2020.md) — mutational signature decomposition in synchronous [DCIS](../cancer_types/DCIS.md) and IDC-NST [PMID:32220886](../papers/32220886.md)
- Applied to identify APOBEC mutational signatures (SBS2, SBS13) in 3 of 4 patients with acquired [PTEN](../genes/PTEN.md) mutations in a phase I/II [alpelisib](../drugs/alpelisib.md) + AI trial in HR+ [MBC](../cancer_types/MBC.md) [PMID:32864625](../papers/32864625.md)
- Applied to compute mutational signature decomposition in 38 [MBC](../cancer_types/MBC.md) WES samples; 60% displayed dominant COSMIC signatures 3/8 (HRD-associated), 34% signatures 1/5 (aging); used alongside [SigMA](../methods/sigma-mutational-signatures.md) for cross-validation [PMID:33863915](../papers/33863915.md)
- Used in [prostate_pcbm_swiss_2019](../datasets/prostate_pcbm_swiss_2019.md) to decompose mutational signatures in 168 prostate cancer brain metastasis samples, identifying enrichment of SBS3 (HRD), SBS1, SBS5, SBS16, and SBS44 (MMR-deficiency) signatures [PMID:35504881](../papers/35504881.md)
- deconstructSigs applied with COSMIC v3.1 reference to decompose mutational signatures in 184 MSI-H/MMR-D endometrial cancers; aging-related signature 1 dominated germline/somatic cases while MMR-D signatures 6/15/20/26 dominated MLH1-promoter-hypermethylated cases [PMID:35849120](../papers/35849120.md)
- Used to derive COSMIC mutational signatures as part of the genomic pipeline in a breast cancer proteogenomic cohort [PMID:36001024](../papers/36001024.md)
- Used with COSMIC v3.2 signatures to characterize mutational processes in pediatric solid-tumor PDX models [PMID:37990009](../papers/37990009.md)

## Notes

- Applied in Pareja et al. (2020) to samples with ≥40 SNVs; aging signatures 1/5 dominated in 63% of synchronous [DCIS](../cancer_types/DCIS.md) and 58% of IDC-NSTs; HRD-related signature 3 dominated in 21%/26%; APOBEC signatures 2/13 dominated in 16%/16%.
- Distinct from [mutational-signatures](../methods/mutational-signatures.md) (umbrella analysis concept) and [SigProfiler](../methods/sigprofiler.md) / [SignatureAnalyzer](../methods/signatureanalyzer.md) (alternative decomposition tools).
- No cBioPortal gene-panel or molecular-profile canonical ID; slug is corpus-derived.

## Sources

- Used for COSMIC signature decomposition (aging signatures 1/5, HRD signature 3, APOBEC signatures 2/13) in [DCIS](../cancer_types/DCIS.md) and IDC-NST samples with ≥40 SNVs [PMID:32220886](../papers/32220886.md)
- [PMID:32864625](../papers/32864625.md)

- [PMID:33863915](../papers/33863915.md)
- [PMID:35504881](../papers/35504881.md)
- [PMID:35849120](../papers/35849120.md)
- [PMID:36001024](../papers/36001024.md)
- [PMID:37990009](../papers/37990009.md)

*This page was processed by **wiki-cli** on **2026-09-10**.*
