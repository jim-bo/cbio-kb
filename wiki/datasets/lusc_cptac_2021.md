---
name: CPTAC Lung Squamous Cell Carcinoma (Cell 2021)
studyId: lusc_cptac_2021
institution: Clinical Proteomic Tumor Analysis Consortium (CPTAC)
size: 108
reference_genome: GRCh38
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
  - PROTEIN_LEVEL
  - PHOSPHOPROTEIN
panels: []
tags:
  - lung
  - LUSC
  - proteogenomics
  - CPTAC
  - multi-omic
processed_by: crosslinker
processed_at: 2026-05-16
---

# CPTAC Lung Squamous Cell Carcinoma (Cell 2021)

## Overview

Deep proteogenomic characterization of 108 treatment-naive primary lung squamous cell carcinomas (LSCC) and 99 paired normal adjacent tissues (NATs), collected prospectively by 13 tissue source sites in 7 countries between May 2016 and August 2018. Performed by the Clinical Proteomic Tumor Analysis Consortium (CPTAC) and published in Cell 2021. Available on cBioPortal as `lusc_cptac_2021`; processed data at LinkedOmics; raw data at PDC (PDC000232/233/234/237) and GDC (dbGaP phs001287.v10.p5). [PMID:34358469](../papers/34358469.md)

## Composition

- 108 treatment-naive primary [LUSC](../cancer_types/LUSC.md) tumors + 99 paired NATs; age range 40–88; 90 male / 18 female (5 of 113 originally enrolled excluded after pathology review).
- Median clinical follow-up 2.5 years.
- Nine data modalities integrated: whole-exome sequencing ([whole-exome-seq](../methods/whole-exome-seq.md)), whole-genome sequencing ([whole-genome-seq](../methods/whole-genome-seq.md)), RNA-seq ([rna-seq](../methods/rna-seq.md)), miRNA-seq ([mirna-seq](../methods/mirna-seq.md)), EPIC methylation arrays ([epic-methylation-array](../methods/epic-methylation-array.md)), TMT11-based global proteomics ([tmt-proteomics](../methods/tmt-proteomics.md)), phosphoproteomics ([tmt-phosphoproteomics](../methods/tmt-phosphoproteomics.md)), acetylproteomics, and ubiquitylproteomics. Reference genome GRCh38/hg38. [PMID:34358469](../papers/34358469.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — somatic mutations, small indels, copy-number alteration backbone.
- [whole-genome-seq](../methods/whole-genome-seq.md) — structural variants, TMB, mutational signatures.
- [rna-seq](../methods/rna-seq.md) — gene expression.
- [tmt-proteomics](../methods/tmt-proteomics.md) — TMT11 global proteome.
- [tmt-phosphoproteomics](../methods/tmt-phosphoproteomics.md) — phosphoproteome.
- [epic-methylation-array](../methods/epic-methylation-array.md) — DNA methylation.
- [nmf-clustering](../methods/nmf-clustering.md) — multi-omic subtyping into five NMF subtypes.
- [xcell](../methods/xcell.md) and [estimate](../methods/estimate.md) — immune deconvolution.
- [gistic](../methods/gistic.md) — focal copy-number alteration calling.
- [clumps](../methods/clumps.md) — 3D clustering of post-translational modification sites.

## Papers using this cohort

- [PMID:34358469](../papers/34358469.md) — CPTAC proteogenomic characterization of LSCC; NMF-based multi-omic subtyping; implicated [NSD3](../genes/NSD3.md) rather than [FGFR1](../genes/FGFR1.md) as the 8p11.23 amplicon driver; identified [BIRC5](../genes/BIRC5.md) as a target in ΔNp63-low tumors. [PMID:34358469](../papers/34358469.md)

## Notable findings derived from this cohort

- Five multi-omic NMF subtypes defined: Basal-Inclusive (B-I), EMT-Enriched (EMT-E), Classical, Inflamed-Secretory (I-S), and Proliferative-Primitive (P-P). "Mixed" cluster-membership samples had significantly worse survival and were enriched for [SOX2](../genes/SOX2.md) amplifications (p=0.0038). [PMID:34358469](../papers/34358469.md)
- [NSD3](../genes/NSD3.md), not [FGFR1](../genes/FGFR1.md), implicated as the likely driver of the recurrent 8p11.23 amplicon based on proteomic data; consistent with failure of FGFR1-targeted therapy in LSCC. [PMID:34358469](../papers/34358469.md)
- Universal CDK4/6-pathway dysregulation: every sample showed loss of at least one of [CDKN2A](../genes/CDKN2A.md) or [RB1](../genes/RB1.md) function; [CCND1](../genes/CCND1.md) amplification correlated with higher mean Rb protein and phospho-Rb but with broad overlap. [PMID:34358469](../papers/34358469.md)
- [PDGFRB](../genes/PDGFRB.md) and [ROR2](../genes/ROR2.md) phosphorylation markedly elevated in the EMT-E subtype, implicating non-canonical Wnt signaling as a targetable pathway. [PMID:34358469](../papers/34358469.md)
- [EGFR](../genes/EGFR.md) protein significantly upregulated in [LUSC](../cancer_types/LUSC.md) but [EGFR](../genes/EGFR.md) amplification did not correlate with EGFR pathway activity; ligand mRNA abundance proposed as a better predictor of response to ligand-blocking inhibitors. [PMID:34358469](../papers/34358469.md)
- ΔNp63-low LSCC subset overexpresses survivin ([BIRC5](../genes/BIRC5.md)); TP63-low LSCC cell lines significantly more sensitive to the survivin inhibitor YM-155. [PMID:34358469](../papers/34358469.md)
- NRF2 pathway activation extends beyond mutation: CDK5-mediated [NFE2L2](../genes/NFE2L2.md) S433 phosphorylation proposed as an alternative non-mutational mechanism in the Classical subtype. [KEAP1](../genes/KEAP1.md) mutations did NOT reduce KEAP1 protein in LSCC (unlike [LUAD](../cancer_types/LUAD.md)). [PMID:34358469](../papers/34358469.md)

## Sources

- cBioPortal study: `lusc_cptac_2021` (canonical, verified).
- Raw data: PDC (PDC000232/233/234/237); GDC (dbGaP phs001287.v10.p5); TCIA.
- Processed data: LinkedOmics.
- Primary publication: [PMID:34358469](../papers/34358469.md).

*This page was processed by **crosslinker** on **2026-05-16**.*
