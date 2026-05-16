---
name: MSK Upper Tract Urothelial Carcinoma Clinical Cohort (Kim et al. 2020)
studyId: utuc_msk_2019
institution: Memorial Sloan Kettering Cancer Center
size: 119
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
panels:
  - IMPACT300
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - UTUC
  - urothelial-carcinoma
  - upper-tract
  - MSK-IMPACT
  - RNA-seq
  - Lynch-syndrome
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Upper Tract Urothelial Carcinoma Clinical Cohort (Kim et al. 2020)

## Overview

Integrated genomic and transcriptomic characterization of 119 upper tract urothelial carcinoma ([UTUC](../cancer_types/UTUC.md)) patient tumors from Memorial Sloan Kettering Cancer Center (37 prospective + 82 retrospective from Sfakianos 2015 / Audenet et al.). All 119 were sequenced by [MSK-IMPACT](../methods/msk-impact-panel.md); 80 had additional [rna-seq](../methods/rna-seq.md) for molecular subtype classification. Released on cBioPortal as utuc_msk_2019. RNA-seq data deposited at GEO GSE134292. Companion PDX/PDC cohort released as [utuc_pdx_msk_2019](../datasets/utuc_pdx_msk_2019.md). [PMID:32332851](../papers/32332851.md)

## Composition

- 119 UTUC patients; 118 nephroureterectomies and 1 metastasectomy.
- Cancer types: [UTUC](../cancer_types/UTUC.md), with comparative reference to [BLCA](../cancer_types/BLCA.md).
- Molecular subtypes (n=80 RNA-seq): 70/80 (87.5%) luminal, 10/80 (12.5%) basal by BASE47 classifier; 66/80 (82.5%) luminal–papillary by consensus MIBC classifier.
- 39.3% of all somatic mutations identified were variants of unknown functional significance. [PMID:32332851](../papers/32332851.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — four panel versions: 300-gene, [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md).
- [rna-seq](../methods/rna-seq.md) — 80 of 119 tumors; BASE47 and consensus MIBC subtype classification.
- [whole-exome-seq](../methods/whole-exome-seq.md) — UCC03 and UCC30 (within PDX cohort).
- [immunohistochemistry](../methods/immunohistochemistry.md) for MMR proteins ([MLH1](../genes/MLH1.md), [MSH2](../genes/MSH2.md), [MSH6](../genes/MSH6.md), [PMS2](../genes/PMS2.md)). [PMID:32332851](../papers/32332851.md)

## Papers using this cohort

- [PMID:32332851](../papers/32332851.md) — Kim, Hu et al., genomic and transcriptomic characterization of 119 UTUC tumors and establishment of 17 PDX / 6 PDC models; HER2-mutant UTUC sensitivity to ADC ([trastuzumab](../drugs/trastuzumab.md) deruxtecan) over kinase inhibitor ([neratinib](../drugs/neratinib.md)) demonstrated.

## Notable findings derived from this cohort

- Recurrent actionable drivers: [FGFR3](../genes/FGFR3.md) 47–48%, [KDM6A](../genes/KDM6A.md) 38%, [KMT2D](../genes/KMT2D.md) 26%, [TERT](../genes/TERT.md) 26%, [TP53](../genes/TP53.md) 25%, [STAG2](../genes/STAG2.md) 22%, [ARID1A](../genes/ARID1A.md) 20%, [CREBBP](../genes/CREBBP.md) 20%, [HRAS](../genes/HRAS.md) 15%, [PIK3CA](../genes/PIK3CA.md) 14–16%, [TSC1](../genes/TSC1.md) 14%, [ERBB2](../genes/ERBB2.md) 8–9%, [KRAS](../genes/KRAS.md) 8%. [PMID:32332851](../papers/32332851.md)
- [FGFR3](../genes/FGFR3.md) mutations occurred only in the luminal subtype; R248C hotspot enriched in Lynch-related UTUC (present in 3/4 MSI-H PDX pairs). [PMID:32332851](../papers/32332851.md)
- Oncogenic [ERBB2](../genes/ERBB2.md) mutations in 8–9% of UTUC and 10.3% of bladder UC in a 44,183-patient MSK cohort; [ERBB2](../genes/ERBB2.md) amplification 4.4% of UTUC and 6.2% of bladder UC. [PMID:32332851](../papers/32332851.md)
- In 20 UTUC patients receiving neoadjuvant chemotherapy before nephroureterectomy, pathologic response (≤pT1N0) occurred in 10/17 MSS (59%) but 0/2 MSI-H patients, supporting redirection of MSI-H UTUC toward immunotherapy rather than cytotoxic NAC. [PMID:32332851](../papers/32332851.md)
- Basal/squamous consensus subtype correlated with PDX engraftment (P=0.04); cell-cycle/DNA-replication pathways enriched in engrafters; ECM-receptor/focal-adhesion pathways enriched in non-engrafters. [PMID:32332851](../papers/32332851.md)

## Sources

- [PMID:32332851](../papers/32332851.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
