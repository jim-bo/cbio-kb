---
name: Adenoid Cystic Carcinoma — MSKCC 2013
studyId: acyc_mskcc_2013
institution: Memorial Sloan Kettering Cancer Center (MSKCC)
size: 60
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - fish
  - copy-number-array
panels: []
tags:
  - salivary-gland-cancer
  - adenoid-cystic-carcinoma
  - ACYC
  - rare-cancers
  - exome-sequencing
processed_by: crosslinker
processed_at: 2026-05-09
---

# Adenoid Cystic Carcinoma — MSKCC 2013

## Overview

Whole-exome (n=55) or whole-genome (n=5) sequencing of 60 adenoid cystic carcinoma (ACC; [ACYC](../cancer_types/ACYC.md)) tumor/normal pairs collected at Memorial Sloan Kettering Cancer Center. At the time of publication this was the largest genomic cohort for this salivary-gland malignancy. Deposited in dbGaP under accession phs000612.v1.p1.

## Composition

- 60 ACC tumor/normal pairs: 55 whole-exome (Agilent SureSelect 51 MB) + 5 whole-genome (Illumina HiSeq 2000).
- Cancer type: [ACYC](../cancer_types/ACYC.md) (adenoid cystic carcinoma — salivary gland).
- Samples microdissected to >70% tumor purity; aligned to hg19/GRCh37 with BWA.
- Mean exome coverage 106×; mean genome coverage 37×; 92.4% of target covered at ≥10×.
- Subset of 23 samples profiled by Illumina HumanHT-12 expression arrays.
- Affymetrix SNP 6.0 arrays used for copy-number profiling (ExomeCNV + GISTIC2.0).
- MYB-NFIB translocation status determined by 3-color BAC FISH on tissue microarrays.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [whole-genome-seq](../methods/whole-genome-seq.md)
- [fish](../methods/fish.md)
- [gistic](../methods/gistic.md)
- [mutect](../methods/mutect.md)

## Papers using this cohort

- [PMID:23685749](../papers/23685749.md) — Ho et al. 2013, "The mutational landscape of adenoid cystic carcinoma," *Nature Genetics*.

## Notable findings derived from this cohort

- Remarkably low somatic mutation rate (mean 0.31 non-silent mutations/Mb; mean 22 somatic mutations per sample), comparable to neuroblastoma and hematologic malignancies [PMID:23685749](../papers/23685749.md).
- MYB-NFIB translocation detected by FISH in 57% (34/60) of cases; additional MYB-pathway lesions in 8% [PMID:23685749](../papers/23685749.md).
- Pathway-level convergence: chromatin-state regulators mutated in 35% ([SMARCA2](../genes/SMARCA2.md), [CREBBP](../genes/CREBBP.md), [KDM6A](../genes/KDM6A.md); q=4.5×10⁻³), DNA-damage response genes ([TP53](../genes/TP53.md), [UHRF1](../genes/UHRF1.md), [ATM](../genes/ATM.md), [BRCA1](../genes/BRCA1.md); q=5.6×10⁻³), PKA-pathway (RYR2/3, PTPRG/H/J/K; 27%; q=4.2×10⁻³), and FGF/IGF/PI3K axis ([PIK3CA](../genes/PIK3CA.md), [PTEN](../genes/PTEN.md), [FGFR4](../genes/FGFR4.md), [FGF16](../genes/FGF16.md), [IGFBP2](../genes/IGFBP2.md); 30%; q=2.4×10⁻²) [PMID:23685749](../papers/23685749.md).
- PI3K-altered tumors enriched for solid histology, the most aggressive ACC variant (Fisher p<1.6×10⁻³); p-AKT and p-PRAS40 IHC confirmed functional PI3K activation [PMID:23685749](../papers/23685749.md).
- KDM6A H3K27me3 demethylase activity abolished by missense mutations; some mutants showed a dominant pro-growth phenotype in cell-based assays [PMID:23685749](../papers/23685749.md).
- CHASM nominated drivers in PIK3CA, TP53, PTEN, SMARCA2, KDM6A, and CREBBP; 8 tumors lacked any CHASM driver call [PMID:23685749](../papers/23685749.md).

## Sources

- [PMID:23685749](../papers/23685749.md)
- dbGaP: phs000612.v1.p1

*This page was processed by **crosslinker** on **2026-05-09**.*
