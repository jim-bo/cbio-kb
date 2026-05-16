---
name: Cancer Cell Line Encyclopedia Next-Generation Characterization (Broad, 2019)
studyId: ccle_broad_2019
institution: Broad Institute
size: 1072
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - rrbs-methylation
  - mirna-profiling
  - histone-mass-spec
  - rppa
panels: []
tags:
  - cell-line
  - pan-cancer
  - multi-omic
  - pharmacogenomics
  - ccle
  - dependency-screen
processed_by: wiki-cli
processed_at: 2026-05-16
---

# Cancer Cell Line Encyclopedia Next-Generation Characterization (Broad, 2019)

## Overview

The 2019 CCLE next-generation characterization study (Ghandi et al., *Nature* 2019, [PMID:31068700](../papers/31068700.md)) [expands](../methods/expands.md) the original Cancer Cell Line Encyclopedia by layering seven additional molecular modalities onto a backbone of 1,072 human cancer cell lines spanning multiple lineages and ethnicities. Whole-exome sequencing (326 lines), whole-genome sequencing (329 lines), deep RNA-seq (1,019 lines), reduced-representation bisulfite sequencing (RRBS; 843 lines covering 17,182 promoter regions), Nanostring miRNA profiling of 734 miRNAs (954 lines), global histone H3 mass-spectrometry profiling for 42 marks (897 lines), and RPPA quantification of 213 antibodies (899 lines) are integrated with Project Achilles / DRIVE functional perturbation data to reveal novel synthetic lethalities, splicing biomarkers of drug sensitivity, and phospho-protein predictors of RTK-inhibitor response.

The companion cell-line resource providing mutation, copy-number, and expression data for this panel is [cellline_ccle_broad](../datasets/cellline_ccle_broad.md).

## Composition

- **1,072 cancer cell lines** from multiple tumor lineages including [AML](../cancer_types/AML.md), [CML](../cancer_types/CML.md), [SKCM](../cancer_types/SKCM.md) melanoma, and others (pan-cancer [MIXED](../cancer_types/MIXED.md) panel).
- Profiling coverage varies by assay: 326 (WES), 329 (WGS), 1,019 (RNA-seq), 843 (RRBS), 897 (histone mass-spec), 899 (RPPA), 954 (miRNA).
- Overlapping Sanger GDSC panel: 667 lines with matched somatic variant data for concordance benchmarking.
- Companion metabolomic dataset: 225 metabolites across 928 lines (reported in parallel work).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — 326 lines
- [whole-genome-seq](../methods/whole-genome-seq.md) — 329 lines
- [rna-seq](../methods/rna-seq.md) — 1,019 lines
- [rrbs](../methods/rrbs.md) — 843 lines; 17,182 promoter regions
- [mirna-seq](../methods/mirna-seq.md) — 954 lines (Nanostring 734 miRNAs)
- [rppa](../methods/rppa.md) — 899 lines, 213 antibodies
- [shrna-rnai-screen](../methods/shrna-rnai-screen.md) — integrated from Project Achilles and DRIVE dependency screens

## Papers using this cohort

- [PMID:31068700](../papers/31068700.md) — Ghandi et al. 2019, *Nature*: next-generation multi-omic characterization that defines this dataset.
- [PMID:31978347](../papers/31978347.md) — Nusinow et al. 2020, *Cell*: quantitative TMT proteomics of 375 CCLE lines revealing MSI proteome buffering and complex-level synthetic-lethality associations.

## Notable findings derived from this cohort

- Multi-omic profiling of 1,072 cancer cell lines integrating WES/WGS/RNA-seq/RPPA/RRBS/miRNA/histone mass-spec with functional perturbation screens revealed paralogue synthetic lethalities (RPP25/RPP25L, LDHA/LDHB), [MDM4](../genes/MDM4.md) exon-6 inclusion as a biomarker for MDM2-inhibitor sensitivity, and phospho-SHP2 (pY542) as a ponatinib-sensitivity marker in AML/CML [PMID:31068700](../papers/31068700.md).
- [TERT](../genes/TERT.md) promoter mutations were detected in 16.7% (84/503) of surveyed cell lines — the most common non-coding somatic alteration in the panel [PMID:31068700](../papers/31068700.md).
- 3–10% of lines showed substantial somatic-variant divergence between CCLE and GDSC passages (genetic drift), and 3/667 overlapping lines (0.4%) had mismatching germline calls indicating mislabelling [PMID:31068700](../papers/31068700.md).
- [EP300](../genes/EP300.md) and [CREBBP](../genes/CREBBP.md) truncating mutations distal to the HAT domain define a novel H3K18/H3K27 hyperacetylation cluster — nominated as the first cancer-associated gain-of-function alterations of p300/CBP [PMID:31068700](../papers/31068700.md).
- Used as the proteomics-extended CCLE resource: 375 cell lines profiled by TMT 10-plex proteomics (>12,000 proteins), with MSI-specific proteome analysis revealing co-downregulation of mismatch repair, SKI, and RQC surveillance complexes — results linked to WRN synthetic lethality [PMID:31978347](../papers/31978347.md)
- 20 bladder cell lines profiled for DNA methylation and expression (GDSC data); validated the 14,209-probe EpiC methylation signature — cell lines clustered by FGFR3 alteration vs SWI/SNF gene mutation status; SWI/SNF-mutant cluster showed higher interferon-γ stimulation signature (P=0.022) [PMID:33397444](../papers/33397444.md)
- Used as a bulk RNA-seq benchmarking cohort (n=1,019 cell lines) to validate OncoMark hallmark predictions — K-S statistics >0.69 separating cancer from normal across all ten hallmarks (p≈0) [PMID:35121966](../papers/35121966.md)

## Sources

- cBioPortal study: `ccle_broad_2019`
- Ghandi et al. *Nature* 2019. [PMID:31068700](../papers/31068700.md)
- Nusinow et al. *Cell* 2020. [PMID:31978347](../papers/31978347.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
- [PMID:33397444](../papers/33397444.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:35121966](../papers/35121966.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
