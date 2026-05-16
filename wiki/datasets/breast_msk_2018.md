---
name: MSK Metastatic Breast Cancer IMPACT Cohort (2018)
studyId: breast_msk_2018
institution: Memorial Sloan Kettering Cancer Center
size: 1756
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - targeted-dna-seq
  - whole-exome-seq
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - breast-cancer
  - BRCA
  - metastatic
  - endocrine-resistance
  - msk-impact
  - hormone-receptor-positive
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Metastatic Breast Cancer IMPACT Cohort (2018)

## Overview

A prospective single-institution cohort of 1,918 breast tumors from 1,756 patients sequenced at Memorial Sloan Kettering Cancer Center between April 2014 and March 2017 using the MSK-IMPACT targeted sequencing panel. The dataset is enriched for hormone-receptor-positive (HR+) disease (1,501 of 1,918 samples) and metastatic specimens (52% of tumors from metastatic sites). It was assembled to characterize the genomic landscape of endocrine-resistant advanced breast cancer and identify mechanisms of resistance beyond [ESR1](../genes/ESR1.md) mutation. The dataset is publicly available via cBioPortal. [PMID:30205045](../papers/30205045.md)

## Composition

- **1,756 unique patients**, 1,918 tumor specimens sequenced prospectively (April 2014 – March 2017). [PMID:30205045](../papers/30205045.md)
- **Cancer types:** [BRCA](../cancer_types/BRCA.md), [IDC](../cancer_types/IDC.md), [ILC](../cancer_types/ILC.md) (invasive ductal carcinoma, invasive lobular carcinoma, and mixed IDC/ILC). [PMID:30205045](../papers/30205045.md)
- **HR+ subgroup:** 1,501/1,918 samples; 692 collected after prior endocrine-therapy exposure and 809 endocrine-therapy-naïve. [PMID:30205045](../papers/30205045.md)
- **52% metastatic specimens** (1,000/1,918); 52% collected after systemic-therapy exposure; median 3 prior systemic regimens in the metastatic setting (range 1–15). [PMID:30205045](../papers/30205045.md)
- **MSK-IMPACT panels:** [IMPACT341](../methods/IMPACT341.md) (n=432), [IMPACT410](../methods/IMPACT410.md) (n=968), [IMPACT468](../methods/IMPACT468.md) (n=518); mean coverage 771-fold. [PMID:30205045](../papers/30205045.md)
- **Supplemental WES:** 30 patients with matched treatment-naïve primary and post-progression tumors sequenced by WES (median 358-fold) and MSK-IMPACT; 44 additional patients with MSK-IMPACT matched pairs only (74 total matched pairs). One research autopsy: 10 metastatic tissues by WES (median 296-fold). [PMID:30205045](../papers/30205045.md)
- **Reference genome:** GRCh37
- **IRB:** NCT01775072 (return of results to patients and physicians allowed).

## Assays / panels (linked)

- [msk-impact-panel](../methods/msk-impact-panel.md) — primary sequencing platform
- [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md)
- [whole-exome-seq](../methods/whole-exome-seq.md) — 74 matched pairs plus 10-site research autopsy
- [facets](../methods/facets.md) — allele-specific copy-number and tumor purity inference
- [droplet-digital-pcr](../methods/droplet-digital-pcr.md) — variant confirmation in autopsy case
- [cancer-hotspots](../methods/cancer-hotspots.md) — applied to combined 2,732-tumor cohort (this cohort + retrospective primaries including TCGA)

## Papers using this cohort

- [PMID:30205045](../papers/30205045.md) — Razavi et al. 2018, "The Genomic Landscape of Endocrine-Resistant Advanced Breast Cancers," *Cancer Cell*

## Notable findings derived from this cohort

- **[PIK3CA](../genes/PIK3CA.md) hotspots:** 313 statistically significant hotspot mutations in 72 genes across the combined 2,732-tumor analysis; [PIK3CA](../genes/PIK3CA.md) alone had 35 hotspots in 36.4% of tumors, including 12 newly identified hotspots. [PMID:30205045](../papers/30205045.md)
- **Endocrine-therapy enrichment of MAPK alterations:** [ERBB2](../genes/ERBB2.md) activating mutations and [NF1](../genes/NF1.md) loss-of-function mutations were more than twice as frequent after endocrine therapy vs. before (p=3×10⁻⁵ and p=4×10⁻⁴, respectively). [PMID:30205045](../papers/30205045.md)
- **ESR1 mutations:** [ESR1](../genes/ESR1.md) ligand-binding-domain mutations in 18% of post-endocrine-therapy HR+HER2− tumors; mutually exclusive with MAPK-pathway and transcription-factor lesions (p<0.0001). [PMID:30205045](../papers/30205045.md)
- **Resistance taxonomy:** four classes — ESR1-mutant, MAPK-pathway-altered ([ERBB2](../genes/ERBB2.md), [NF1](../genes/NF1.md), [EGFR](../genes/EGFR.md), [KRAS](../genes/KRAS.md), [HRAS](../genes/HRAS.md), [BRAF](../genes/BRAF.md), [MAP2K1](../genes/MAP2K1.md)), ER-transcriptional-machinery-altered ([MYC](../genes/MYC.md), [CTCF](../genes/CTCF.md), [FOXA1](../genes/FOXA1.md), [TBX3](../genes/TBX3.md)), and pan-wild-type — collectively affected 22% of all 692 post-endocrine-therapy tumors. [PMID:30205045](../papers/30205045.md)
- **Survival impact:** MAPK-pathway lesions predicted shorter PFS on aromatase inhibitors (median 3.5 vs. 15.2 months; p=1.4×10⁻⁹); transcription-factor lesions median PFS 6.4 months (p=1.3×10⁻⁶). [PMID:30205045](../papers/30205045.md)
- **Convergent resistance at autopsy:** a single HR+ patient harbored independent [ERBB2](../genes/ERBB2.md) driver mutations (S310, L755, D769) across five spatially distinct lesions and [ESR1](../genes/ESR1.md) Y537 at a sixth — confirmed mutually exclusive by ddPCR. [PMID:30205045](../papers/30205045.md)
- **32 genes enriched in metastases** (q<0.05) vs. primaries; 29/32 arose in HR+HER2− disease; included [TP53](../genes/TP53.md), [ARID1A](../genes/ARID1A.md), [ARID2](../genes/ARID2.md), [CREBBP](../genes/CREBBP.md), [ERBB2](../genes/ERBB2.md), and [NF1](../genes/NF1.md). [PMID:30205045](../papers/30205045.md)

## Sources

- cBioPortal study ID: `breast_msk_2018`
- NCT01775072
- [PMID:30205045](../papers/30205045.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
