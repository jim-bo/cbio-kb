---
name: Pan-Cancer Analysis of Whole Genomes (PCAWG, 2020)
studyId: pancan_pcawg_2020
institution: ICGC/TCGA Pan-Cancer Analysis of Whole Genomes Consortium
size: 2658
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - rna-seq
panels: []
tags:
  - pan-cancer
  - whole-genome
  - pcawg
  - icgc
  - tcga
  - somatic-mutation
  - structural-variant
  - mutational-signatures
  - non-coding-drivers
processed_by: crosslinker
processed_at: 2026-05-16
---

# Pan-Cancer Analysis of Whole Genomes (PCAWG, 2020)

## Overview

The ICGC/TCGA Pan-Cancer Analysis of Whole Genomes (PCAWG) cohort is the canonical large-scale pan-cancer whole-genome sequencing resource, uniformly processed across a globally distributed cloud-computing infrastructure. It comprises 2,658 matched tumor–normal whole genomes (after QC from 2,834 donors) spanning 38 tumor types, uniformly aligned and variant-called through three core SNV/indel/SV pipelines (Sanger, DKFZ, Broad) plus bespoke algorithms for retrotransposition, mtDNA, and telomere length. RNA-seq is available for 1,222 donors. The study anchors 22 companion PCAWG papers covering chromothripsis, mutational signatures, evolutionary timing, transcriptomic consequences, germline determinants, and telomere maintenance. Published in *Nature* 578, 82–93 (2020) [PMID:32025007](../papers/32025007.md).

## Composition

- **2,658 white-listed donors** with matched tumor/normal WGS (2,605 primary + 173 metastases/local recurrences), drawn from 2,834 donors after QC exclusion of 176.
- **38 tumor types** including [BRCA](../cancer_types/BRCA.md), [PRAD](../cancer_types/PRAD.md), [HCC](../cancer_types/HCC.md), [PAAD](../cancer_types/PAAD.md), [PANET](../cancer_types/PANET.md), [CHRCC](../cancer_types/CHRCC.md), [GB](../cancer_types/GB.md), [LUSC](../cancer_types/LUSC.md), [LIPO](../cancer_types/LIPO.md), [MBN](../cancer_types/MBN.md), [MPN](../cancer_types/MPN.md), [THPA](../cancer_types/THPA.md), [CLLSLL](../cancer_types/CLLSLL.md), [DLBCLNOS](../cancer_types/DLBCLNOS.md), [SKCM](../cancer_types/SKCM.md), [ACRM](../cancer_types/ACRM.md), bladder, head-and-neck, esophagus, and others.
- Mean read coverage: 39× normal, bimodal 38×/60× tumor.
- RNA-seq: 1,222 donors.
- Mean age 56 (range 1–90); 55% men, 45% women.

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — 2,658 matched tumor/normal pairs; mean coverage 39× normal, bimodal 38×/60× tumor.
- [rna-seq](../methods/rna-seq.md) — 1,222 donors.
- SNV/indel calling: three-pipeline consensus (Sanger, DKFZ, [MuTect](../methods/mutect.md)).
- SV calling: [DELLY](../methods/delly.md) / [SvABA](../methods/svaba.md).
- CNA/purity-ploidy: [ABSOLUTE](../methods/absolute.md)-class tools.
- Mutational signatures: [SigProfiler](../methods/sigprofiler.md).
- Significantly mutated regions: [GISTIC2.0](../methods/gistic.md).

## Papers using this cohort

- [PMID:32025007](../papers/32025007.md) — PCAWG Consortium 2020, *Nature*: flagship marker paper; integrative analysis of 2,658 whole genomes across 38 tumor types defining the pan-cancer somatic mutation landscape, driver architecture, mutational signatures, and structural variation.

## Notable findings derived from this cohort

- 43,778,859 somatic SNVs, 2,418,247 indels, 288,416 SVs, 19,166 retrotransposition events, and 8,185 mtDNA mutations called across 2,583 white-listed donors [PMID:32025007](../papers/32025007.md).
- 91% of tumors carried ≥1 driver; mean 4.6 drivers per tumor (2.6 coding); 5.3% of tumors had no identifiable driver after technical and biological triage [PMID:32025007](../papers/32025007.md).
- 13% of driver point mutations are non-coding; 25% of tumors carry ≥1 non-coding driver, one-third of which (237/785) are [TERT](../genes/TERT.md) promoter mutations (9% of PCAWG tumors) [PMID:32025007](../papers/32025007.md).
- [TP53](../genes/TP53.md) is the most common driver (954 tumors; 77% biallelic); pan-cancer chromothripsis associated with [TP53](../genes/TP53.md) (OR=3.22, p=8.3×10⁻³⁵); chromothripsis in 22.3% (587/2,658) and chromoplexy in 17.8% (467/2,658) of samples [PMID:32025007](../papers/32025007.md).
- Germline contribution: 17% of patients carry rare germline PTVs in cancer-predisposition/DDR genes; 81% of biallelic germline+somatic inactivations affect [BRCA1](../genes/BRCA1.md), [BRCA2](../genes/BRCA2.md), or [ATM](../genes/ATM.md) [PMID:32025007](../papers/32025007.md).
- 16 hot-L1 retrotransposition source elements account for 67% (2,440/3,669) of all L1-mediated transductions; Plinian elements (rare MAF ≤2%) are far more productive than Strombolian (common) elements [PMID:32025007](../papers/32025007.md).
- Germline 22q13.1 [APOBEC3A](../genes/APOBEC3A.md)–[APOBEC3B](../genes/APOBEC3B.md) fusion deletion (rs12628403) and rs2142833 cis-eQTL modulate APOBEC mutagenesis pan-cancer; germline [MBD4](../genes/MBD4.md) PTVs cause elevated somatic CpG>T mutagenesis (p<2.5×10⁻⁶, replicated in TCGA n=8,134) [PMID:32025007](../papers/32025007.md).
- PCAWG missed [JAK2](../genes/JAK2.md) V617F in 35 MPNs due to panel-of-normals filtering — illustrates a systematic failure mode of blood-derived reference panels [PMID:32025007](../papers/32025007.md).

## Sources

- cBioPortal study: `pancan_pcawg_2020`
- PCAWG Consortium. *Nature* 578, 82–93 (2020). [PMID:32025007](../papers/32025007.md)
- ICGC Data Portal: https://dcc.icgc.org/pcawg
- AWS open data: s3://pcawg.icgc.org

*This page was processed by **crosslinker** on **2026-05-16**.*
