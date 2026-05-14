---
name: Papillary Thyroid Carcinoma (TCGA, Cell 2014)
studyId: thca_tcga_pub
institution: The Cancer Genome Atlas Research Network
size: 496
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
  - METHYLATION
  - PROTEIN_LEVEL
  - STRUCTURAL_VARIANT
panels: []
tags:
  - papillary-thyroid-carcinoma
  - thpa
  - tcga
  - multi-platform
  - braf-v600e
  - ras-driven
  - gene-fusion
  - whole-exome-seq
  - integrated-multiomics
processed_by: crosslinker
processed_at: 2026-05-14
---

# Papillary Thyroid Carcinoma (TCGA, Cell 2014)

## Overview

The TCGA multiplatform genomic characterization of 496 papillary thyroid carcinomas (PTCs) — the largest integrative genomic study of PTC at the time of publication. Accrued through TCGA from non-irradiated patients; focused on the most common subtype of thyroid cancer. The study aimed to define the complete landscape of oncogenic drivers, reduce the fraction of driver-negative "dark matter" cases, and propose a molecular reclassification based on BRAFV600E-like (BVL) vs. RAS-like (RL) signaling states.

## Composition

- **Cancer type:** Papillary thyroid carcinoma ([THPA](../cancer_types/THPA.md))
- **Sample count:** 496 primary PTCs + 8 metastatic tumors; 402 tumor/normal pairs with whole-exome sequencing; 390 tumors profiled across all major platforms
- **Histology breakdown:** 324 (69.4%) classical-type, 99 (21.2%) follicular-variant, 35 (7.5%) tall cell variant, 9 (2.0%) uncommon variants
- **Exclusions:** Poorly differentiated and anaplastic thyroid cancers excluded
- **Reference genome:** hg19

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md): 402 tumor/normal pairs; mean tumor depth 97.0×, normal 94.9×
- [rna-seq](../methods/rna-seq.md): transcriptome-wide expression profiling
- [mirna-seq](../methods/mirna-seq.md): microRNA expression
- [affymetrix-snp6](../methods/affymetrix-snp6.md): copy number alteration and LOH
- [450k-methylation-array](../methods/450k-methylation-array.md): Illumina 450k DNA methylation
- [rppa](../methods/rppa.md): reverse phase protein arrays for protein-level quantification

## Papers using this cohort

- [PMID:25417114](../papers/25417114.md) — TCGA Research Network, *Cell* 2014. "Integrated Genomic Characterization of Papillary Thyroid Carcinoma."

## Notable findings derived from this cohort

- Seven significantly mutated genes (q<0.1): [BRAF](../genes/BRAF.md), [NRAS](../genes/NRAS.md), [HRAS](../genes/HRAS.md), [KRAS](../genes/KRAS.md), [EIF1AX](../genes/EIF1AX.md), [PPM1D](../genes/PPM1D.md), and [CHEK2](../genes/CHEK2.md); MAPK driver mutations ([BRAF](../genes/BRAF.md) + RAS) were mutually exclusive in 74.6% of cases (Fisher's exact P=1.1×10⁻⁵) [PMID:25417114](../papers/25417114.md).
- BRAF V600E was the dominant driver in 61.7% of PTCs; RAS mutations characterized the follicular variant (12.9%); [EIF1AX](../genes/EIF1AX.md) was identified as a novel PTC driver (1.5%, q=5.3×10⁻⁸) near-mutually exclusive with MAPK drivers [PMID:25417114](../papers/25417114.md).
- Gene fusions identified in 15.3% (74/484) of cases — including [RET](../genes/RET.md) (6.8%), BRAF (2.7%), [NTRK3](../genes/NTRK3.md), [ALK](../genes/ALK.md), PAX8/PPARG, and [THADA](../genes/THADA.md) fusions — all mutually exclusive with point-mutation drivers (Fisher's exact P=4.9×10⁻⁴³) [PMID:25417114](../papers/25417114.md).
- [TERT](../genes/TERT.md) promoter mutations in 9.4% (36/384) of informative tumors; associated with older age, high MACIS recurrence risk scores, and lower thyroid differentiation score (TDS) [PMID:25417114](../papers/25417114.md).
- Fraction of PTC cases without an identified oncogenic driver reduced from ~25% (historical) to 3.5%; combining SSNVs, fusions, and SCNAs, putative drivers were identified in 397/402 (98.8%) of exome-sequenced PTCs [PMID:25417114](../papers/25417114.md).
- A 71-gene BRAFV600E-RAS Score (BRS) and a 16-gene Thyroid Differentiation Score (TDS) distinguished two fundamental PTC molecular classes with distinct MAPK/PI3K signaling profiles, epigenomic patterns, and clinical outcomes [PMID:25417114](../papers/25417114.md).

## Sources

- cBioPortal study: `thca_tcga_pub`
- Citation: TCGA, Cell 2014 [PMID:25417114](../papers/25417114.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
