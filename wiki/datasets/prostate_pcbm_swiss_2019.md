---
name: Prostate Cancer Brain Metastases (Bern, Nat Commun. 2022)
studyId: prostate_pcbm_swiss_2019
institution: University of Bern / Swiss multi-institutional
size: 51
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays: [whole-exome-seq, targeted-rna-seq, immunohistochemistry]
panels: []
tags: [prostate-cancer, prad, brain-metastases, hrr, hrd, swiss, multi-region]
processed_by: crosslinker
processed_at: 2026-05-21
---

# Prostate Cancer Brain Metastases (Bern, Nat Commun. 2022)

## Overview

Multi-region whole-exome sequencing and targeted RNA-seq cohort of 51 Swiss patients with prostate cancer brain metastases (PCBM), profiled by Antonio Rodriguez-Calero, John Gallon, Salvatore Piscuoglio, and Mark Rubin at the University of Bern. Dataset generated in 2019 and released on cBioPortal as study `prostate_pcbm_swiss_2019`. Designed to characterize the genomic landscape of PCBM with a focus on homologous recombination repair (HRR) gene alterations and their implications for PARP inhibitor eligibility. [PMID:35504881](../papers/35504881.md)

## Composition

- **51 patients** with prostate adenocarcinoma brain metastases (PCBM); average age at PCBM diagnosis 71 years.
- **168 tumor regions** sequenced: 105 from PCBM (41% parenchymal, 35% dural, 24% mixed/unclear), 63 from matched primary PCa available in 20/51 patients.
- Histology: pure acinar adenocarcinoma 48/51 (94%) PCBM; 3/51 with neuroendocrine differentiation.
- Clinical exposure: 42/51 (82%) received androgen deprivation or orchiectomy; 11/42 (26%) received [abiraterone](../drugs/abiraterone.md) and/or [enzalutamide](../drugs/enzalutamide.md).
- Comparator cohorts: [prad_tcga](../datasets/prad_tcga.md) (n=495 primary PCa) and [prad_su2c_2019](../datasets/prad_su2c_2019.md) (n=411 non-brain mCRPC metastases / CRPC500). [PMID:35504881](../papers/35504881.md)
- Cancer type: [PRAD](../cancer_types/PRAD.md).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md): Agilent SureSelectXT V7 on Illumina NovaSeq6000 (2×100 bp; ~258× on-target depth); 24/51 patients without matched normal (pooled normal panel used for variant calling).
- [targeted-rna-seq](../methods/multiregion-exome-seq.md): custom Ion AmpliSeq prostate-specific RNA panel for fusion detection.
- [immunohistochemistry](../methods/immunohistochemistry.md): [ERG](../genes/ERG.md), p53, [PTEN](../genes/PTEN.md); Chromogranin-A, Synaptophysin, PSA, CK5/6, p63 in NE-suspected cases.
- Mutation signatures by SigMA; LOH assessed per-patient. [PMID:35504881](../papers/35504881.md)

## Papers using this cohort

- [PMID:35504881](../papers/35504881.md) — Rodriguez-Calero et al., *Nat Commun* 2022: genomic characterization of prostate cancer brain metastases; primary discovery study for this dataset.

## Notable findings derived from this cohort

- Elevated mutation burden in PCBM: mean 4.43 coding alterations/Mb across 168 samples (range 0.28–50.45); PCBM had significantly more SNVs (q=6.75×10⁻⁶), insertions (q=3.06×10⁻⁵), and deletions (q=9.30×10⁻³) than matched primaries, and significantly more than [prad_su2c_2019](../datasets/prad_su2c_2019.md) non-brain mCRPC (SNVs q=2.38×10⁻¹⁹). [PMID:35504881](../papers/35504881.md)
- HRD signature (COSMIC SBS3) enrichment: significantly higher in PCBM vs [prad_su2c_2019](../datasets/prad_su2c_2019.md) (q=0.041) and in PCBM primaries vs [prad_tcga](../datasets/prad_tcga.md) primaries (q=0.0003; q=0.0034 vs high-grade TCGA subset). [PMID:35504881](../papers/35504881.md)
- 10/51 (19.6%) PCBM patients met PROfound inclusion criteria with pathogenic alterations in ≥1 of 15 HRR genes; 8/51 (15.7%) had biallelic loss; 5/51 (9.8%) had pathogenic [BRCA1](../genes/BRCA1.md)/[BRCA2](../genes/BRCA2.md) alterations. [PMID:35504881](../papers/35504881.md)
- Most-mutated genes in PCBM metastases: [TP53](../genes/TP53.md) 25%, [APC](../genes/APC.md) 16%, [SPOP](../genes/SPOP.md) 16%; [AR](../genes/AR.md) coding alterations 14%, [AR](../genes/AR.md) amplifications 63%; [PTEN](../genes/PTEN.md) loss/deletion 64.71%; [TMPRSS2](../genes/TMPRSS2.md)–[ERG](../genes/ERG.md) fusions 25%. [PMID:35504881](../papers/35504881.md)
- Four hypermutators (>15 mut/Mb) identified: two MSI-H with [MSH2](../genes/MSH2.md) alterations, one with [POLD1](../genes/POLD1.md) frameshift plus [RFC4](../genes/RFC4.md) missense, one without MMR/HRR alterations. [PMID:35504881](../papers/35504881.md)
- Clonal evolution in 18/20 matched primary/metastasis cases: subclonal primary clones expanded to clonal level (CCF>0.9) in metastases; site-specific pathway enrichment for calcium signaling and FAT10/Wnt (parenchymal) vs aldosterone signaling (dural). [PMID:35504881](../papers/35504881.md)

## Sources

- cBioPortal study `prostate_pcbm_swiss_2019`; reference genome hg19. [PMID:35504881](../papers/35504881.md)

*This page was processed by **crosslinker** on **2026-05-21**.*
