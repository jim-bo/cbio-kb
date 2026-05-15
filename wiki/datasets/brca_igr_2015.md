---
name: Metastatic Breast Cancer (France/IGR, 2016)
studyId: brca_igr_2015
institution: Institut Gustave Roussy (IGR) / French SAFIR01-SAFIR02-SHIVA-MOSCATO Consortium
size: 216
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-sequencing
  - copy-number-snp-array
panels: []
tags:
  - breast-cancer
  - metastatic
  - france
  - esrr1
  - apobec
  - endocrine-resistance
processed_by: crosslinker
processed_at: 2026-05-14
---

# Metastatic Breast Cancer (France/IGR, 2016)

## Overview

The brca_igr_2015 dataset (published 2016, cBioPortal identifier brca_igr_2015) comprises whole-exome sequencing of 216 tumor-normal pairs from metastatic breast cancer (mBC) patients enrolled in four prospective French trials: SAFIR01 (NCT01414933, n=86), SAFIR02 (NCT02299999, n=80), SHIVA (NCT01771458, n=35), and MOSCATO (NCT01566019, n=15). The dataset was deposited at EGA (EGAS00001001695) and at cBioPortal. It serves as the primary discovery resource for the Lefebvre et al. 2016 study identifying metastasis-specific driver genes in breast cancer, including [ESR1](../genes/ESR1.md) and [RB1](../genes/RB1.md), and elevated APOBEC-mediated mutagenesis in HR+/HER2− metastatic disease.

## Composition

- **216 tumor-normal pairs** from metastatic breast cancer patients.
- Subtype distribution: 143 (66%) HR+/HER2−, 51 (24%) triple-negative (HR−/HER2−), 14 (6%) HER2+; 8 unclassified.
- Median patient age 54 (range 26–82); 94% had received prior chemotherapy; 84% of HR+/HER2− patients had prior endocrine therapy.
- Cancer type: [BRCA](../cancer_types/BRCA.md) (metastatic; bone metastases excluded due to DNA-extraction difficulty).
- Sample sites: visceral and soft-tissue metastases (bone excluded).

## Assays / panels (linked)

- [whole-exome sequencing](../methods/whole-exome-seq.md) — Illumina HiSeq 2500/4000 or NextSeq 500 with Agilent SureSelect All Exon V5 or Clinical Research Exome capture; mean coverage 83±18× (normal) and 122±15× (tumor).
- Mutation calling: [BWA](../methods/bwa.md)-MEM alignment → GATK base recalibration → [Mutect](../methods/mutect.md) v1.1.7 (substitutions) + Scalpel v0.5.2 (indels); annotated with snpEff/snpSift.
- Copy number: ExomeCNV + DNAcopy + [GISTIC2](../methods/gistic.md) (amp >0.3, del <−0.3 log2 ratio).
- Driver detection: [MutSig](../methods/mutsig.md), [MuSiC](../methods/genome-music.md), drGAP (FDR<0.1).
- Mutational signatures: WTSI/Sanger framework + deconstructSigs over 13 COSMIC breast cancer signatures.
- Cancer cell fraction: Sequenza tumor purity → ABSOLUTE-style framework.

## Papers using this cohort

- [PMID:28027327](../papers/28027327.md) — Lefebvre et al. 2016. WES of 216 metastatic breast cancers from four prospective French trials; identified 12 significantly mutated drivers, [ESR1](../genes/ESR1.md) and [RB1](../genes/RB1.md) as mBC-specific drivers, and 8 genes enriched in metastasis ([ESR1](../genes/ESR1.md), [FSIP2](../genes/FSIP2.md), [FRAS1](../genes/FRAS1.md), [OSBPL3](../genes/OSBPL3.md), [EDC4](../genes/EDC4.md), [PALB2](../genes/PALB2.md), [IGFN1](../genes/IGFN1.md), AGRN) conferring 2-fold higher death hazard.

## Notable findings derived from this cohort

- Twelve significantly mutated driver genes in mBC by MutSig (FDR<0.1): [TP53](../genes/TP53.md), [PIK3CA](../genes/PIK3CA.md), [GATA3](../genes/GATA3.md), [ESR1](../genes/ESR1.md), [MAP3K1](../genes/MAP3K1.md), [CDH1](../genes/CDH1.md), [AKT1](../genes/AKT1.md), [MAP2K4](../genes/MAP2K4.md), [RB1](../genes/RB1.md), [PTEN](../genes/PTEN.md), [CBFB](../genes/CBFB.md), [CDKN2A](../genes/CDKN2A.md) [PMID:28027327](../papers/28027327.md).
- [ESR1](../genes/ESR1.md) identified as a metastasis-specific driver (OR=29, 95% CI 9–155, p=1.2e-12); 22 mutations in hormone-receptor domain across 20/143 HR+/HER2− mBCs (14%), all in patients with prior endocrine therapy; 9 additional focal amplifications; combined 19% of HR+/HER2− mBC [PMID:28027327](../papers/28027327.md).
- [RB1](../genes/RB1.md) loss-of-function in 5% of HR+/HER2− mBC vs <1% in HR+/HER2− early breast cancer; implies subset with primary resistance to CDK4/6 inhibitors [PMID:28027327](../papers/28027327.md).
- [PALB2](../genes/PALB2.md) somatic mutations enriched in mBC (4%) vs early breast cancer (0.1%; FDR=0.006); candidate population for PARP inhibitor trials [PMID:28027327](../papers/28027327.md).
- [TSC1](../genes/TSC1.md)/[TSC2](../genes/TSC2.md) combined mutation rate 6.3% in HR+/HER2− mBC vs 0.7% in HR+/HER2− early breast cancer (p=0.0004); potential outlier responders to [everolimus](../drugs/everolimus.md) [PMID:28027327](../papers/28027327.md).
- APOBEC-mediated mutagenesis (signatures 2+13) nearly doubled in HR+/HER2− mBC vs primary TCGA samples (58.8% vs 31.9%, p<2e-16), linked to subclonal mutation acquisition under therapy [PMID:28027327](../papers/28027327.md).
- Eight-gene metastasis-enrichment signature (ESR1, FSIP2, AGRN, FRAS1, IGFN1, EDC4, OSBPL3, [PALB2](../genes/PALB2.md)) associated with 2-fold higher death hazard on multivariate analysis (HR=1.97, 95% CI 1.34–2.89, p=0.001) [PMID:28027327](../papers/28027327.md).

## Sources

- cBioPortal study: brca_igr_2015
- EGA accession: EGAS00001001695

*This page was processed by **crosslinker** on **2026-05-14**.*
