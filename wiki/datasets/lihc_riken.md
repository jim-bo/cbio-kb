---
name: RIKEN HCC Genomics (lihc_riken)
studyId: lihc_riken
institution: RIKEN (and synthesized external studies including Sung et al. Nat Genet 2012; Chen et al. Nature 2024)
size: 494
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - MRNA_EXPRESSION
panels: []
tags:
  - HCC
  - hepatocellular carcinoma
  - HBV
  - TERT
  - WGS
processed_by: wiki-cli
processed_at: 2026-05-16
---

# RIKEN HCC Genomics (lihc_riken)

## Overview

The lihc_riken entry represents genomic studies of hepatocellular carcinoma ([HCC](../cancer_types/HCC.md)) associated with RIKEN, synthesizing findings from multiple HBV-related HCC genomic surveys including deep WGS of 494 HCCs (Chen et al., Nature 2024). The primary paper in this corpus (PMID:22634756) is a narrative review synthesizing HBV integration patterns, copy-number alterations, and transcriptomic data from cell line and animal models alongside large WGS cohorts.

## Composition

- Cancer type: [HCC](../cancer_types/HCC.md)
- Primary focus: HBV-related HCC; WGS, RNA-seq, and spatial transcriptomics applied across referenced cohorts
- Up to 494 HCCs with deep WGS in referenced studies
- Key referenced methods: WGS, RNA-seq, spatial transcriptomics, droplet digital PCR (ddPCR)

## Assays / panels (linked)

- [Whole-genome sequencing](../methods/whole-genome-seq.md)
- [RNA sequencing](../methods/rna-seq.md)
- [Spatial transcriptomics](../methods/spatial-transcriptomics.md)

## Papers using this cohort

- [PMID:22634756](../papers/22634756.md)

## Notable findings derived from this cohort

- HBV DNA integration occurs in ~90% of HBV-related HCCs; recurrent hotspots include [TERT](../genes/TERT.md) promoter (23.7%), [KMT2D](../genes/KMT2D.md) (11.8%), and [CCNE1](../genes/CCNE1.md) (5%) [PMID:22634756](../papers/22634756.md)
- HBV-TERT integration can cyclize into extrachromosomal circular DNA (ecDNA) found in 27.3% of liver cancer samples, harboring 76 oncogenes including [MYC](../genes/MYC.md) [PMID:22634756](../papers/22634756.md)
- TERT promoter mutations, [CTNNB1](../genes/CTNNB1.md), and [TP53](../genes/TP53.md) are top recurrent somatic alterations in HCC with Wnt and mTOR as key therapeutic pathways [PMID:22634756](../papers/22634756.md)
- Nucleos(t)ide analogues reduced HBV DNA integration frequency from median 1.01x10^9 to 4.84x10^7 after 10 years (n=28) [PMID:22634756](../papers/22634756.md)
- Served as a reference HCC cohort (RIKEN-LIHC) in the pan-Asia cHCC-ICC integrative genomic study; contributed to the pan-liver-cancer transcriptomic clustering (n=367) identifying P1–P4 clusters and to comparative mutational-landscape benchmarks for TP53 and TERT promoter frequencies [PMID:31130341](../papers/31130341.md)

## Sources

- [PMID:22634756](../papers/22634756.md)

*This page was processed by **entity-page-writer** on **2026-05-06**.*
- [PMID:31130341](../papers/31130341.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
