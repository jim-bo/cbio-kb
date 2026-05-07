---
name: Lung Adenocarcinoma (Broad, Nature Genetics 2012)
studyId: luad_broad
institution: Broad Institute
size: 183
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - mutsig
panels: []
tags:
  - LUAD
  - lung
  - Broad
  - WES
  - WGS
  - MutSig
processed_by: entity-page-writer
processed_at: 2026-05-06
---

# Lung Adenocarcinoma (Broad, Nature Genetics 2012)

## Overview

183 lung adenocarcinoma tumour-normal pairs (159 WES, 24 WGS, with 23 having both) characterised at the Broad Institute. Published in Nature Genetics 2012. The study identified 25 significantly mutated genes, confirmed EGFR/KRAS/STK11 as major drivers, and nominated novel driver genes [RBM10](../genes/RBM10.md), [U2AF1](../genes/U2AF1.md), and [ARID1A](../genes/ARID1A.md). A novel oncogenic [EGFR](../genes/EGFR.md) C-terminal in-frame deletion was also discovered. [PMID:22980975](../papers/22980975.md)

## Composition

- 183 [LUAD](../cancer_types/LUAD.md) tumour-normal pairs.
- 159 cases with WES (median 92x exome coverage, range 51–201x); 24 with WGS (median 69x tumour, 36x normal); 23 cases had both.
- Clinical composition: 27 never smokers, 17 light smokers, 118 heavy smokers, 21 unknown; stages I-IV.
- Complementary SNP array analysis for somatic copy number alterations. [PMID:22980975](../papers/22980975.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 159 tumour-normal pairs (median 92x)
- [whole-genome-seq](../methods/whole-genome-seq.md) — 24 tumour-normal pairs (median 69x tumour)
- [mutsig](../methods/mutsig.md) — significantly mutated gene analysis (InVEx/MutSig); 25 genes at q < 0.25

## Papers using this cohort

- [PMID:22980975](../papers/22980975.md) — primary characterisation study (Imielinski et al., Nature Genetics 2012)

## Notable findings derived from this cohort

- Mean exonic somatic mutation rate 12.0 mutations/Mb (median 8.1/Mb; range 0.04–117.4/Mb); smokers significantly higher than never smokers (median 9.8 vs 1.7/Mb; P = 3.0×10^-9). [PMID:22980975](../papers/22980975.md)
- 25 significantly mutated genes (q < 0.25) including known drivers [EGFR](../genes/EGFR.md), [KRAS](../genes/KRAS.md), [TP53](../genes/TP53.md), [STK11](../genes/STK11.md), [KEAP1](../genes/KEAP1.md), [NF1](../genes/NF1.md), [BRAF](../genes/BRAF.md). [PMID:22980975](../papers/22980975.md)
- [U2AF1](../genes/U2AF1.md) p.S34F hotspot mutation in 3% of cases (first report in an epithelial tumour); associated with reduced progression-free survival (P = 0.00011, log-rank). [PMID:22980975](../papers/22980975.md)
- [RBM10](../genes/RBM10.md) mutated in 7% with recurrent truncating mutations. [PMID:22980975](../papers/22980975.md)
- [ARID1A](../genes/ARID1A.md) mutated in 8% with significant accumulation of truncating mutations. [PMID:22980975](../papers/22980975.md)
- Novel oncogenic EGFR C-terminal in-frame deletion discovered. [PMID:22980975](../papers/22980975.md)

## Sources

- [PMID:22980975](../papers/22980975.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
