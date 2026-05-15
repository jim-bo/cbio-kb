---
name: Unclassified Renal Cell Carcinoma — MSKCC (2016)
studyId: urcc_mskcc_2016
institution: Memorial Sloan Kettering Cancer Center
size: 62
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-targeted-seq
  - rna-seq
  - oncoscan-snp-array
  - fish
  - immunohistochemistry
panels:
  - msk-impact-panel
tags:
  - urcc
  - renal-cell-carcinoma
  - unclassified
  - non-clear-cell
  - hippo-yap
  - mtorc1
  - fh-deficiency
processed_by: crosslinker
processed_at: 2026-05-14
---

# Unclassified Renal Cell Carcinoma — MSKCC (2016)

## Overview

A single-institution prospective cohort of 62 high-grade primary renal cell carcinomas with unclassified histology (uRCC) assembled at MSKCC. All tumors were re-reviewed by three dedicated genitourinary pathologists applying WHO and ISUP consensus criteria; MiTF family translocation tumors were excluded by TFE3/TFEB IHC and FISH. The cohort represents the first in-depth integrated molecular characterization of uRCC, a heterogeneous [RCC](../cancer_types/RCC.md) subgroup comprising 4–5% of all RCC and lacking a standard-of-care therapy. [PMID:27713405](../papers/27713405.md)

## Composition

- **62** high-grade primary uRCC tumors from MSKCC. [PMID:27713405](../papers/27713405.md)
- Cancer type: unclassified renal cell carcinoma — a high-grade non-clear-cell RCC subgroup.
- Clinicopathology: 58% locally advanced (≥pT3) at nephrectomy, 32% with regional lymph-node involvement; 42% (n=26) developed metastases and 35% (n=22) died of RCC during follow-up.
- Four molecularly defined subsets: [NF2](../genes/NF2.md) loss / Hippo–YAP dysregulation (26%), mTORC1-hyperactive ([MTOR](../genes/MTOR.md)/[TSC1](../genes/TSC1.md)/[TSC2](../genes/TSC2.md)/[PTEN](../genes/PTEN.md) mutations, 21%), [FH](../genes/FH.md) deficiency (6%), and [ALK](../genes/ALK.md) translocation (2%), plus a chromatin/DNA-damage regulator group (21%). [PMID:27713405](../papers/27713405.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) 230-gene targeted sequencing (avg 348× tumor / 280× normal; matched normal in 61/62 cases). [PMID:27713405](../papers/27713405.md)
- [RNA-seq](../methods/rna-seq.md) on 7 uRCC (Illumina HiSeq 2500; [STAR](../methods/star.md) alignment; [GSEA](../methods/gsea.md) for YAP/TAZ signatures). [PMID:27713405](../papers/27713405.md)
- Affymetrix [OncoScan FFPE SNP array](../methods/oncoscan-snp-array.md) for genome-wide copy-number / LOH on 15/16 NF2-loss cases. [PMID:27713405](../papers/27713405.md)
- [FISH](../methods/fish.md): custom three-probe NF2/22q11/Cen10 assay; [ALK](../genes/ALK.md) break-apart probes for fusion confirmation. [PMID:27713405](../papers/27713405.md)
- [Immunohistochemistry](../methods/immunohistochemistry.md): [NF2](../genes/NF2.md), YAP/TAZ, p-YAP, p-S6, p-4EBP1, [FH](../genes/FH.md), 2SC, H3K36me3, INI1. [PMID:27713405](../papers/27713405.md)

## Papers using this cohort

- [PMID:27713405](../papers/27713405.md) — Chen et al., *Nat Genet* 2016: Integrated molecular characterization of 62 uRCC tumors defining four molecular subsets with distinct drivers and clinical outcomes.

## Notable findings derived from this cohort

- **29 recurrently mutated genes** identified; average 2.6 (range 0–8) somatic coding mutations per tumor. Most frequent: [NF2](../genes/NF2.md) 18%, [SETD2](../genes/SETD2.md) 18%, [BAP1](../genes/BAP1.md) 13%, [KMT2C](../genes/KMT2C.md) 10%, [MTOR](../genes/MTOR.md) 8%; only 1/62 [VHL](../genes/VHL.md) mutation — sharply contrasting with ~75% in clear-cell RCC. [PMID:27713405](../papers/27713405.md)
- **NF2-loss subset (26%):** Biallelic NF2 inactivation (mutation + 22q12 LOH) in 13/16 cases; concurrent [SETD2](../genes/SETD2.md) mutation in 44% of this subset (vs 9% in others, P=0.004); significant nuclear YAP/TAZ accumulation and depressed p-YAP; worst cancer-specific and progression-free survival by log-rank. [PMID:27713405](../papers/27713405.md)
- **mTORC1-hyperactive subset (21%):** Mutually exclusive mutations in [MTOR](../genes/MTOR.md), [TSC1](../genes/TSC1.md), [TSC2](../genes/TSC2.md), or [PTEN](../genes/PTEN.md); [MTOR](../genes/MTOR.md) L2427R recurred 3× and is functionally activating in 293T assays; 13/16 confirmed hyperactive by p-S6 / p-4EBP1 IHC; comparatively better clinical outcome. [PMID:27713405](../papers/27713405.md)
- **FH-deficient subset (6%):** All 4 cases FH IHC-negative/2SC-positive; 3 confirmed HLRCC with germline [FH](../genes/FH.md) mutations; T41 carries a somatic homozygous FH deletion — a novel non-germline mechanism. [PMID:27713405](../papers/27713405.md)
- **[TPM3](../genes/TPM3.md)–ALK fusion (2%):** T12 carries a [TPM3](../genes/TPM3.md)–[ALK](../genes/ALK.md) fusion confirmed by IMPACT and ALK break-apart FISH — only the second adult RCC case reported with this fusion. [PMID:27713405](../papers/27713405.md)
- **Functional YAP dependency:** shRNA knockdown of [YAP1](../genes/YAP1.md) in NF2-loss nccRCC cell lines reduces S- and G2/M-phase cells (P<0.001) and soft-agar colony formation. [PMID:27713405](../papers/27713405.md)

## Sources

- cBioPortal study ID: urcc_mskcc_2016
- Chen et al., *Nat Genet* 2016 — DOI: 10.1038/ng.3587

*This page was processed by **crosslinker** on **2026-05-14**.*
