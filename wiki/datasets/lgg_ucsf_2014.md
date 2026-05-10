---
name: UCSF Recurrent Glioma Cohort (2014)
studyId: lgg_ucsf_2014
institution: University of California, San Francisco (UCSF) / BC Cancer Agency / University of Tokyo
size: 23
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
  - droplet-digital-pcr
panels: []
tags:
  - low-grade-glioma
  - glioma-recurrence
  - clonal-evolution
  - hypermutation
  - temozolomide-mutagenesis
  - mismatch-repair
  - paired-tumor-normal
processed_by: crosslinker
processed_at: 2026-05-09
---

# UCSF Recurrent Glioma Cohort (2014)

## Overview

The lgg_ucsf_2014 cohort is a paired initial-and-recurrent tumor exome sequencing study of 23 patients with grade II astrocytic gliomas (predominantly astrocytic and diffuse histology), assembled at UCSF in collaboration with BC Cancer Agency and the University of Tokyo. The primary scientific question was how the mutational landscape evolves from initial low-grade glioma to recurrence — and what role adjuvant [temozolomide](../drugs/temozolomide.md) (TMZ) therapy plays in that evolution. Recurrences were resected up to 11 years after the initial tumor. Data were deposited in the European Genome-phenome Archive (EGAS00001000579) and, for patients 24–29, in the Japanese Genotype-phenotype Archive (JGAS00000000004).

## Composition

- **23 patients** with paired initial and recurrent grade II astrocytomas; recurrences spanned histological grades II–IV (including grade IV [GBM](../cancer_types/GBM.md)).
- Cancer types: [ASTR](../cancer_types/ASTR.md), [DIFG](../cancer_types/DIFG.md), [GBM](../cancer_types/GBM.md).
- 10 of 23 patients received adjuvant [temozolomide](../drugs/temozolomide.md); the remainder received surveillance, radiation alone, or radiation + TMZ.
- Average 33 somatic coding mutations identified per initial tumor; average 125× exome coverage enabling detection down to ~10% variant allele frequency.

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — tumor and matched-normal pairs at mean 125× coverage.
- [rna-seq](../methods/rna-seq.md) — transcriptome sequencing used to validate aberrant splicing events.
- [droplet-digital-pcr](../methods/droplet-digital-pcr.md) — subclonal/heterogeneity validation of select mutations.

## Papers using this cohort

- [PMID:24336570](../papers/24336570.md) — Johnson, Mazor et al., *Science* (2014): Mutational Analysis Reveals the Origin and Therapy-driven Evolution of Recurrent Glioma.

## Notable findings derived from this cohort

- In **43% of cases**, at least half of the mutations present in the initial tumor — including driver mutations in [TP53](../genes/TP53.md), [ATRX](../genes/ATRX.md), [SMARCA4](../genes/SMARCA4.md), and [BRAF](../genes/BRAF.md) — were undetected at recurrence, indicating recurrent tumors frequently arise from cells that diverged early in clonal evolution. [PMID:24336570](../papers/24336570.md)
- [IDH1](../genes/IDH1.md) R132H was the only mutation shared in every patient pair, reinforcing [IDH1](../genes/IDH1.md) as the initiating event in low-grade glioma. [PMID:24336570](../papers/24336570.md)
- **6 of 10 TMZ-treated patients** developed hypermutated recurrent tumors bearing a TMZ-signature mutational spectrum; all 6 progressed to GBM and acquired TMZ-signature driver mutations in the RB and AKT–mTOR pathways (including [RB1](../genes/RB1.md), [CDKN2A](../genes/CDKN2A.md), [PIK3CA](../genes/PIK3CA.md), [PTEN](../genes/PTEN.md), [MTOR](../genes/MTOR.md)). [PMID:24336570](../papers/24336570.md)
- Mismatch-repair gene [MSH6](../genes/MSH6.md) was recurrently mutated in TMZ-treated hypermutators, consistent with TMZ-induced mismatch-repair deficiency driving hypermutation. [PMID:24336570](../papers/24336570.md)

## Sources

- EGA accession: EGAS00001000579
- JGAS accession: JGAS00000000004 (patients 24–29)
- cBioPortal study ID: lgg_ucsf_2014

*This page was processed by **crosslinker** on **2026-05-09**.*
