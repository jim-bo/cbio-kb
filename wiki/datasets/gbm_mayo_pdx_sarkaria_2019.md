---
name: Mayo Clinic GBM Patient-Derived Xenograft Panel (Sarkaria 2019)
studyId: gbm_mayo_pdx_sarkaria_2019
institution: Mayo Clinic
size: 96
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - bulk-rna-seq
  - methylation-array
  - sanger-sequencing
  - fish
  - immunohistochemistry
panels: []
tags:
  - glioblastoma
  - GBM
  - PDX
  - patient-derived-xenograft
  - preclinical
  - EGFR
  - PDGFRA
  - temozolomide
  - MGMT
  - tumor-resource
processed_by: crosslinker
processed_at: 2026-05-16
---

# Mayo Clinic GBM Patient-Derived Xenograft Panel (Sarkaria 2019)

## Overview

The Mayo Clinic Brain Tumor PDX National Resource, established by the Sarkaria laboratory, comprises 96 glioblastoma patient-derived xenograft (PDX) lines derived from 261 glioma patients surgically resected at Mayo Clinic between 2000 and 2017 (overall engraftment rate 36%). The panel predominantly captures IDH-wildtype [GBM](../cancer_types/GBM.md) (n=93) and is openly available to the research community. Comprehensive molecular profiling (WES, RNA-seq, genome-wide methylation) demonstrates that the panel recapitulates canonical GBM driver frequencies comparable to TCGA-GBM ([gbm_tcga](../datasets/gbm_tcga.md)), with the notable exception that [PDGFRA](../genes/PDGFRA.md) amplification is absent. The panel has been used for 1×1×1 preclinical trial designs and MGMT-stratified drug-response studies.

## Composition

- **PDX lines:** 96 (from 261 patients; engraftment rate 36%; grade IV: 47%)
- **Histology of viable PDX:** GBM IDH-wildtype n=93; GBM IDH-mutant n=2; diffuse midline glioma H3 K27M-mutant ([DMG](../cancer_types/DMG.md)) n=1
- **Primary vs recurrent tumor origin:** primary n=60, recurrent n=34
- **Cancer type:** predominantly [GBM](../cancer_types/GBM.md) (IDH-wildtype); one [DMG](../cancer_types/DMG.md)
- **Sequencing coverage:** WES n=83 (SureSelect / TGen Strexome V2); RNA-seq n=68; methylation EPIC array n=76
- **Matched patient–PDX pairs:** WES on 24 matched patient–PDX pairs; germline WES on 55 patients

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — n=83 PDX (SureSelect / TGen Strexome V2; mouse reads removed with Xenome)
- [bulk-rna-seq](../methods/bulk-rna-seq.md) — n=68 PDX (TruSeq libraries); expression subtype classification
- [epic-methylation-array](../methods/epic-methylation-array.md) — n=76 PDX (Illumina MethylationEPIC at MD Anderson); methylation class assignment
- [sanger-sequencing](../methods/sanger-sequencing.md) — IDH1/2 and [TERT](../genes/TERT.md) promoter status
- [qmsp](../methods/qmsp.md) — [MGMT](../genes/MGMT.md) promoter methylation (n=78 PDX)
- [fish](../methods/fish.md) — [EGFR](../genes/EGFR.md), [MDM2](../genes/MDM2.md), N-MYC, PDGFRA copy number validation
- [immunohistochemistry](../methods/immunohistochemistry.md) — [GFAP](../genes/GFAP.md), Ki67, EGFR, PDGFRA protein expression
- [str-profiling](../methods/str-profiling.md) — tissue provenance verification

## Papers using this cohort

- [PMID:31852831](../papers/31852831.md) — Vaubel et al. 2019, comprehensive molecular characterization of the Mayo GBM PDX National Resource panel

## Notable findings derived from this cohort

- The PDX driver landscape mirrors TCGA-GBM: TERT promoter mutation 86%, [CDKN2A](../genes/CDKN2A.md) homozygous deletion 70%, [PTEN](../genes/PTEN.md) alteration 48%, [TP53](../genes/TP53.md) mutation 36%, [NF1](../genes/NF1.md) alteration 17%, [RB1](../genes/RB1.md) loss/mutation 16%, [BRAF](../genes/BRAF.md) alteration 4%. [PMID:31852831](../papers/31852831.md)
- EGFR is the dominant RTK alteration: 45% of PDX with high-level amplification (n=35), 14 SNVs across 12 lines, 16 exon-deletion variants including EGFRvIII (n=11). EGFR amplification was preserved in 100% of 24 matched patient–PDX pairs. [PMID:31852831](../papers/31852831.md)
- PDGFRA amplification is completely absent from the panel (0/83 WES-profiled PDX) despite ~15% expected frequency in IDH-wildtype GBM; engraftment-associated clonal selection (demonstrated in GBM159 by FISH) is the leading explanation. [PMID:31852831](../papers/31852831.md)
- MGMT promoter methylation was strongly associated with [temozolomide](../drugs/temozolomide.md) and concurrent RT/TMZ benefit but not radiation alone, directly mirroring the human clinical phenotype (Spearman ρ=0.53 patient–PDX survival correlation). [PMID:31852831](../papers/31852831.md)
- Targetable fusions identified: [FGFR3](../genes/FGFR3.md)–[TACC3](../genes/TACC3.md) (3 lines), [PTPRZ1](../genes/PTPRZ1.md)–[MET](../genes/MET.md) and [CHTOP](../genes/CHTOP.md)–[NTRK1](../genes/NTRK1.md) fusions (3 lines), plus two novel FGFR3 fusions (FGFR3–[TRIM54](../genes/TRIM54.md), FGFR3–[CALCOCO1](../genes/CALCOCO1.md)). [PMID:31852831](../papers/31852831.md)
- Engraftment was restricted to WHO grade IV; zero of 59 grade II–III glioma samples established viable PDX. [PMID:31852831](../papers/31852831.md)

## Sources

- cBioPortal study: `gbm_mayo_pdx_sarkaria_2019`
- Mayo PDX National Resource: https://www.mayo.edu/research/labs/sarkaria/pages/brain-tumor-pdx-national-resource
- Primary publication: [PMID:31852831](../papers/31852831.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
