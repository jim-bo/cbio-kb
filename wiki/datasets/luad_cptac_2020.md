---
name: CPTAC Lung Adenocarcinoma Proteogenomic Dataset (2020)
studyId: luad_cptac_2020
institution: Clinical Proteomic Tumor Analysis Consortium (CPTAC)
size: 110
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - rna-seq
  - mirna-seq
  - epic-methylation-array
  - tmt-proteomics
  - tmt-phosphoproteomics
panels: []
tags:
  - proteogenomics
  - cptac
  - lung-adenocarcinoma
  - never-smokers
  - phosphoproteomics
  - multi-omics
  - kinase-fusions
processed_by: crosslinker
processed_at: 2026-05-16
---

# CPTAC Lung Adenocarcinoma Proteogenomic Dataset (2020)

## Overview

The luad_cptac_2020 cohort is a comprehensive multi-omics resource from the Clinical Proteomic Tumor Analysis Consortium characterizing 110 treatment-naïve [LUAD](../cancer_types/LUAD.md) tumors and 101 matched normal adjacent tissues (NATs). The dataset integrates whole-exome and whole-genome sequencing, RNA-seq, miRNA-seq, EPIC methylation arrays, and deep-scale TMT-based proteomics, phosphoproteomics, and acetylproteomics. Deliberate enrichment for never-smokers and non-Western populations relative to TCGA distinguishes this cohort. Multi-omics NMF clustering identified four subgroups anchored on driver mutations and geography, and phosphoproteomics revealed therapeutic vulnerabilities downstream of [EGFR](../genes/EGFR.md), [KRAS](../genes/KRAS.md), and [EML4](../genes/EML4.md)-[ALK](../genes/ALK.md). Raw proteomics are at the CPTAC data portal (S056); genomics via GDC (dbGaP phs001287.v5.p4). [PMID:32649874](../papers/32649874.md)

## Composition

- **110 treatment-naïve [LUAD](../cancer_types/LUAD.md) tumors** and **101 paired normal adjacent tissues (NATs)**; complete multi-omics data for 101 tumors and 96 NATs.
- 111 participants (73 males, 38 females; age range 35–81); 13 tissue source sites across 8 countries.
- Enriched for never-smokers and non-Western (Vietnamese, Chinese) populations relative to TCGA [LUAD](../cancer_types/LUAD.md).
- Driver landscape: [EGFR](../genes/EGFR.md) mutations enriched in cluster C4 (female, Chinese); [KRAS](../genes/KRAS.md) mutations in C1–C3; [STK11](../genes/STK11.md) mutations enriched in C3 (Vietnamese patients). [PMID:32649874](../papers/32649874.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — ~150× coverage; somatic SNV and indel calling. [PMID:32649874](../papers/32649874.md)
- [whole-genome-seq](../methods/whole-genome-seq.md) — ~15× coverage; structural variant and fusion calling. [PMID:32649874](../papers/32649874.md)
- [rna-seq](../methods/rna-seq.md) — transcript expression quantification. [PMID:32649874](../papers/32649874.md)
- [mirna-seq](../methods/mirna-seq.md) — miRNA expression. [PMID:32649874](../papers/32649874.md)
- [epic-methylation-array](../methods/epic-methylation-array.md) — genome-wide DNA methylation. [PMID:32649874](../papers/32649874.md)
- [tmt-proteomics](../methods/tmt-proteomics.md) and [tmt-phosphoproteomics](../methods/tmt-phosphoproteomics.md) — TMT isobaric labeling; deep-scale protein and phosphosite quantification. [PMID:32649874](../papers/32649874.md)

## Papers using this cohort

- [PMID:32649874](../papers/32649874.md) — Gillette et al. (2020), *Cell*: Proteogenomic Characterization Reveals Therapeutic Vulnerabilities in Lung Adenocarcinoma.

## Notable findings derived from this cohort

- Multi-omics NMF clustering yielded four LUAD subgroups (C1–C4) that recapitulate and refine mRNA subtypes; C3 enriched for Vietnamese patients and [STK11](../genes/STK11.md) mutation; C4 enriched for [EGFR](../genes/EGFR.md) mutations, female sex, and Chinese nationality. [PMID:32649874](../papers/32649874.md)
- [PTPN11](../genes/PTPN11.md)/Shp2 Y62 phosphorylation was a consistent outlier in [EGFR](../genes/EGFR.md)-mutant tumors and Y546/Y584 in [ALK](../genes/ALK.md)-fusion tumors, without concordant RNA/protein changes — first such report in treatment-naïve primary LUAD; Shp2 inhibition nominated as a therapeutic strategy. [PMID:32649874](../papers/32649874.md)
- [SOS1](../genes/SOS1.md) S1161 phosphorylation was an extreme outlier in [KRAS](../genes/KRAS.md)-mutant tumors, nominatig [SOS1](../genes/SOS1.md) inhibition as a KRAS-specific therapeutic strategy. [PMID:32649874](../papers/32649874.md)
- [STK11](../genes/STK11.md)-mutant tumors showed the most dramatic immune downregulation; neutrophil-degranulation proteins (16 measured, including CAMP, [LTF](../genes/LTF.md), MPO, MMP8/9) were coherently overexpressed without corresponding RNA enrichment — granule-storage mechanism; deep-learning model predicted [STK11](../genes/STK11.md) mutation from histopathology with 94% slide-level accuracy. [PMID:32649874](../papers/32649874.md)
- Seven in-frame [ALK](../genes/ALK.md) kinase fusions detected, including novel HMBOX1-ALK and ANKRD36B-ALK partners; [ALK](../genes/ALK.md) Y1507 phosphorylation was specific to fusion-positive samples and validated by IHC. [PMID:32649874](../papers/32649874.md)
- [KEAP1](../genes/KEAP1.md) G511V BTB-domain missense mutation preserved [KEAP1](../genes/KEAP1.md) protein but produced high [NFE2L2](../genes/NFE2L2.md) S215/S433 phosphorylation, suggesting binding disruption rather than KEAP1 degradation as the resistance mechanism. [PMID:32649874](../papers/32649874.md)
- 289 proteins upregulated (log2 FC >2, FDR <0.01, ≥90% of pairs) in tumor vs. NAT; [GREM1](../genes/GREM1.md) (log2 FC >5) and OCIAD2 (log2 FC >4) highlighted as candidate poor-prognosis markers. [PMID:32649874](../papers/32649874.md)

## Sources

- cBioPortal study: `luad_cptac_2020`
- CPTAC data portal: S056
- dbGaP: phs001287.v5.p4
- DOI: [10.1016/j.cell.2020.06.013](https://doi.org/10.1016/j.cell.2020.06.013)

*This page was processed by **crosslinker** on **2026-05-16**.*
