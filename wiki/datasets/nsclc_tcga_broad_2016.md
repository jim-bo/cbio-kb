---
name: "NSCLC Integrated Exome Cohort (Campbell et al. 2016)"
studyId: nsclc_tcga_broad_2016
institution: Broad Institute / TCGA Research Network
size: 1144
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
  - affymetrix-snp6
panels: []
tags:
  - nsclc
  - luad
  - lusc
  - lung-cancer
  - tcga
  - broad
  - mutational-signatures
  - neoantigen
  - smoking
processed_by: crosslinker
processed_at: 2026-05-14
---

# NSCLC Integrated Exome Cohort (Campbell et al. 2016)

## Overview

Integrated exome-sequencing cohort combining 660 lung adenocarcinoma (ADC) and 484 lung squamous cell carcinoma (SqCC) tumor/normal pairs (1,144 NSCLCs total), assembled from three sources: 274 previously unpublished ADC and 308 previously unpublished SqCC cases contributed directly, merged with 227 TCGA ADC cases ([luad_tcga_pub](../datasets/luad_tcga_pub.md)), 159 Imielinski/Broad ADC cases ([luad_broad](../datasets/luad_broad.md)), and 176 TCGA SqCC cases ([lusc_tcga_pub](../datasets/lusc_tcga_pub.md)). The study was designed to achieve sufficient power to identify drivers rare in each histology and to comprehensively compare molecular landscapes across [NSCLC](../cancer_types/NSCLC.md) subtypes. [PMID:27158780](../papers/27158780.md)

## Composition

- Cancer types: [LUAD](../cancer_types/LUAD.md) and [LUSC](../cancer_types/LUSC.md)
- 660 lung ADC + 484 lung SqCC tumor/normal exome pairs = 1,144 total
- RNA-seq available for 495 ADC and 476 SqCC
- SNP-array copy number on Affymetrix SNP 6.0 for all cases
- Expert pathology review performed on a 227-tumor ADC subset
- Median somatic mutation rate 8.7/Mb (ADC) and 9.7/Mb (SqCC) [PMID:27158780](../papers/27158780.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — Agilent SureSelect Human All Exon 50MB; Illumina paired-end
- [rna-seq](../methods/rna-seq.md) — 495 ADC + 476 SqCC
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — copy-number profiling
- [mutect](../methods/mutect.md) and [indelocator](../methods/indelocator.md) — variant calling
- [mutsig](../methods/mutsig.md) (MutSig2CV) — significantly mutated gene discovery
- [gistic](../methods/gistic.md) (GISTIC2.0) — recurrent somatic copy-number alteration calling
- [absolute](../methods/absolute.md) — purity and ploidy estimation
- [bayesian-nmf](../methods/bayesian-nmf.md) / [mutational-signatures](../methods/mutational-signatures.md) — six mutational signature decomposition
- [prada](../methods/prada.md) — RNA fusion calling

## Papers using this cohort

- [PMID:27158780](../papers/27158780.md) — Campbell et al. 2016, *Nature Genetics* — "Distinct patterns of somatic genome alterations in lung adenocarcinomas and squamous cell carcinomas"; primary discovery study.

## Notable findings derived from this cohort

- MutSig2CV identified 38 significantly mutated genes in lung ADC and 20 in lung SqCC (q < 0.1); only 6 genes shared between histologies ([TP53](../genes/TP53.md), [RB1](../genes/RB1.md), [ARID1A](../genes/ARID1A.md), [CDKN2A](../genes/CDKN2A.md), [PIK3CA](../genes/PIK3CA.md), [NF1](../genes/NF1.md)). [PMID:27158780](../papers/27158780.md)
- Lung SqCC molecular landscape more closely resembles [HNSC](../cancer_types/HNSC.md) and [BLCA](../cancer_types/BLCA.md) (>25% SMG overlap) than lung ADC (~12% overlap), reinforcing histological treatment distinctions. [PMID:27158780](../papers/27158780.md)
- Six mutational signatures identified: COSMIC SI4 (smoking, C>A), SI7 (UV), SI13/SI2 (APOBEC), SI15/SI6 (MMR), SI5 (clock-like); smoking SI4 distinguished never- vs ever-smokers in ADC (AUC=0.87) but not in SqCC (AUC=0.62). [PMID:27158780](../papers/27158780.md)
- Novel significantly mutated genes: [PPP3CA](../genes/PPP3CA.md) and [DOT1L](../genes/DOT1L.md) in ADC; [RASA1](../genes/RASA1.md) and [CUL3](../genes/CUL3.md) in SqCC; [KLF5](../genes/KLF5.md), [EP300](../genes/EP300.md), [CREBBP](../genes/CREBBP.md), [B2M](../genes/B2M.md) in Pan-Lung analysis. [PMID:27158780](../papers/27158780.md)
- 242 oncogene-negative lung ADCs — adding [SOS1](../genes/SOS1.md), [VAV1](../genes/VAV1.md), [RASA1](../genes/RASA1.md), [ARHGAP35](../genes/ARHGAP35.md) and novel amplification targets raised the fraction of ADC with a defined RTK/Ras/Raf driver from ~62% to 76% overall (85% in expert-reviewed subset). [PMID:27158780](../papers/27158780.md)
- Novel focal amplifications: [MIR21](../genes/MIR21.md)/[TUBD1](../genes/TUBD1.md) and [CCND3](../genes/CCND3.md) in ADC; [YES1](../genes/YES1.md) and [MIR205](../genes/MIR205.md) in SqCC; [MAPK1](../genes/MAPK1.md) in Pan-Lung. [PMID:27158780](../papers/27158780.md)
- 47% of lung ADC and 53% of lung SqCC tumors had ≥5 predicted neoepitopes, supporting broad immunotherapy applicability across both NSCLC histologies. [PMID:27158780](../papers/27158780.md)
- Neoepitope load significantly lower in never-smoker vs ever-smoker ADCs (P<0.001), but did not differ between ever-smoker ADCs and SqCCs. [PMID:27158780](../papers/27158780.md)

## Sources

- cBioPortal studyId: `nsclc_tcga_broad_2016`
- Campbell JD et al. "Distinct patterns of somatic genome alterations in lung adenocarcinomas and squamous cell carcinomas." *Nature Genetics*. 2016;48(6):607-616. [PMID:27158780](../papers/27158780.md). DOI: 10.1038/ng.3564.

*This page was processed by **crosslinker** on **2026-05-14**.*
