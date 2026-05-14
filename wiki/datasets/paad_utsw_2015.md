---
name: "PAAD UT Southwestern 2015 (Witkiewicz et al.)"
studyId: paad_utsw_2015
institution: "UT Southwestern Medical Center"
size: 109
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
panels: []
tags:
  - pancreatic-ductal-adenocarcinoma
  - microdissection
  - mismatch-repair
  - braf-v600e
  - myc-amplification
processed_by: crosslinker
processed_at: 2026-05-14
---

# PAAD UT Southwestern 2015 (Witkiewicz et al.)

## Overview

Microdissected whole-exome sequencing cohort of 109 surgically resected pancreatic ductal adenocarcinoma (PDA) cases from UT Southwestern Medical Center, published in *Nature Communications* 2015 (PMID:25855536). A key methodological feature was laser or manual needle microdissection of tumor epithelium prior to DNA extraction, which raised the average non-synonymous mutation count to 67/case — substantially higher than the 26/case seen in prior bulk-tissue exome studies. Raw reads deposited at NCBI SRA BioProject PRJNA278883.

## Composition

- **N = 109** surgically resected PDA cases with matched germline (normal tissue n=105, peripheral blood n=4).
- **Histological subtypes:** ductal carcinoma NOS / [PAAD](../cancer_types/PAAD.md) 86% (n=94), adenosquamous / [PAASC](../cancer_types/PAASC.md) 10% (n=11), colloid / [PAAC](../cancer_types/PAAC.md) 4% (n=4).
- **Stage:** mostly stage I (n=5) or II (n=97); stage III (n=6) or IV (n=1).
- **Median overall survival:** 21 months. Median age 66 (range 29–86); 50% male.
- **Tumor cellularity:** >50% (achieved via microdissection); tumor epithelium manually needle-dissected under dissecting microscope.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — TruSeq Exome Enrichment (FC-121-1048) or Nextera Exome Enrichment (FC-140-1003) on Illumina HiSeq 2500; mean depth 51.28× (95% CI 49.5–53.1); 21 cases re-sequenced to ~123×. Reads aligned with [bwa](../methods/bwa.md) to UCSC hg19.
- [mutect](../methods/mutect.md) — SNV calling (≥14 tumor reads, ≥8 normal reads).
- [varscan](../methods/varscan.md) — INDEL calling (≥8 reference reads, ≥3 variant reads); indels manually inspected in IGV.
- [oncotator](../methods/oncotator.md) — variant annotation (Broad Institute).
- [gistic](../methods/gistic.md) — copy-number calls (join_segment_size=4, conf=0.95; ExomeCNV + DNAcopy segmentation).
- [mutsig](../methods/mutsig.md) — MutSigCV for significantly mutated gene discovery; combined 208-case meta-cohort with Biankin et al. ICGC.
- [sanger-sequencing](../methods/sanger-sequencing.md) — validation of 248 non-silent mutations in 84 cases (92% confirmation rate, 95% CI 87.6–94.6%).
- [fish](../methods/fish.md) — Vysis LSI [MYC](../genes/MYC.md) dual-colour break-apart probe for 8q24 [MYC](../genes/MYC.md) amplification confirmation.
- [immunohistochemistry](../methods/immunohistochemistry.md) — [ARID1A](../genes/ARID1A.md), p53, pERK, p63; [ARID1A](../genes/ARID1A.md) IHC in independent 296-case cohort.
- [random-forest-classifier](../methods/random-forest-classifier.md) — unsupervised pathway-alteration subtype clustering.

## Papers using this cohort

- [PMID:25855536](../papers/25855536.md) — Witkiewicz et al., *Nature Communications* 2015: whole-exome sequencing of 109 microdissected PDA; primary discovery study for this cohort.

## Notable findings derived from this cohort

- 24 significantly mutated genes (MutSigCV); [KRAS](../genes/KRAS.md) mutated in 92%; [MYC](../genes/MYC.md) amplification at 8q24.13 uniquely associated with poor overall survival (P=0.0013) and adenosquamous histology. [PMID:25855536](../papers/25855536.md)
- [KRAS](../genes/KRAS.md) codon-61 mutations (Q61H/K/R) associated with favorable overall survival (P=0.02) and lower pERK staining versus codon-12 mutations, demonstrating allele-specific MAPK output differences. [PMID:25855536](../papers/25855536.md)
- [BRAF](../genes/BRAF.md) V600E in 3% of cases (mutually exclusive with [KRAS](../genes/KRAS.md)); patient-derived cell line PDA_014 confirmed sensitive to [vemurafenib](../drugs/vemurafenib.md). [PMID:25855536](../papers/25855536.md)
- [ARID1A](../genes/ARID1A.md) protein loss by IHC in independent 296-case cohort associated with poor overall survival (P=0.0202); ARID1A-deficient PDA cell lines vulnerable to [ARID1B](../genes/ARID1B.md) depletion (synthetic lethal). [PMID:25855536](../papers/25855536.md)
- [RBM10](../genes/RBM10.md) mutations (4%) associated with prolonged overall survival (P=0.0345) despite aggressive histological features. [PMID:25855536](../papers/25855536.md)
- High-CNV clusters (5 & 6) enriched for biallelic DNA double-strand-break repair gene loss ([ATM](../genes/ATM.md), [BRCA1](../genes/BRCA1.md), [BRCA2](../genes/BRCA2.md), Fanconi-anaemia genes); cluster 6 trended toward worst survival (HR=3.91, P=0.034). [PMID:25855536](../papers/25855536.md)

## Sources

- cBioPortal study: `paad_utsw_2015`
- NCBI SRA BioProject: PRJNA278883

*This page was processed by **crosslinker** on **2026-05-14**.*
