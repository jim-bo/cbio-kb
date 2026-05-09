---
name: IDIBAPS Mantle Cell Lymphoma 2013 (Beà)
studyId: mcl_idibips_2013
institution: Institut d'Investigacions Biomèdiques August Pi i Sunyer (IDIBAPS), Hospital Clínic, Barcelona
size: 201
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-genome-seq
  - whole-exome-seq
  - targeted-dna-seq
  - sanger-sequencing
  - affymetrix-snp6
  - affymetrix-u133-plus2
panels: []
tags:
  - mantle-cell-lymphoma
  - clonal-evolution
  - subclonal-heterogeneity
  - chromatin-modifiers
  - notch-pathway
  - kataegis
  - sox11-expression
processed_by: crosslinker
processed_at: 2026-05-09
---

# IDIBAPS Mantle Cell Lymphoma 2013 (Beà)

## Overview

Whole-genome (n=4) and whole-exome (n=29) sequencing study of mantle cell lymphoma ([MCL](../cancer_types/MCL.md)) tumor/normal pairs plus six MCL cell lines, with targeted validation in an independent cohort of 172 MCL patients. Led by Beà, Campo, and colleagues at IDIBAPS/Hospital Clínic, Barcelona, and published in *PNAS* 2013. The study identified 25 significantly mutated genes, established [NOTCH2](../genes/NOTCH2.md) as an independent prognostic factor, described novel mutations in chromatin modifiers ([NSD2](../genes/NSD2.md), [KMT2D](../genes/KMT2D.md), [MEF2B](../genes/MEF2B.md)), and documented subclonal heterogeneity and clonal evolution at progression/relapse. The cBioPortal study identifier is `mcl_idibips_2013`. Raw sequencing data deposited under EGA accession EGAS00001000510; expression/SNP arrays under GEO GSE46969 / GSE36000.

## Composition

- **Cancer type:** [MCL](../cancer_types/MCL.md) — mantle cell lymphoma.
- **Discovery cohort:** 4 WGS + 29 WES tumor/normal pairs (primary MCL); 6 MCL cell lines (WES).
- **Validation cohort:** 172 independent MCL patients (targeted/Sanger sequencing of recurrently mutated genes).
- **Total:** ~201 MCL patients profiled across the full study (29 WES primaries + 172 validation).
- **Sequential/paired samples:** 8 cases with paired WGS/WES biopsies (simultaneous anatomical sites or diagnosis/relapse); 19 additional cases with paired targeted sequencing.
- WES median: 20 protein-coding mutations per case (range 8–47); WGS ~3,700 somatic mutations per tumor (1.2/Mb). [PMID:24145436](../papers/24145436.md)

## Assays / panels (linked)

- [whole-genome-seq](../methods/whole-genome-seq.md) — 4 tumor/normal pairs; ~3,700 somatic mutations per tumor detected.
- [whole-exome-seq](../methods/whole-exome-seq.md) — 29 tumor/normal pairs + 6 MCL cell lines.
- [targeted-dna-seq](../methods/targeted-dna-seq.md) — validation of 25 recurrently mutated genes in 172 independent MCL patients.
- [sanger-sequencing](../methods/sanger-sequencing.md) — additional mutation validation.
- [affymetrix-snp6](../methods/affymetrix-snp6.md) — copy-number / LOH profiling (Affymetrix SNP 6.0 arrays).
- [affymetrix-u133-plus2](../methods/affymetrix-u133-plus2.md) — gene-expression profiling (Affymetrix HU133+ 2.0).

## Papers using this cohort

- [PMID:24145436](../papers/24145436.md) — Beà S et al., "Landscape of somatic mutations and clonal evolution in mantle cell lymphoma", *PNAS* 2013.

## Notable findings derived from this cohort

- 25 significantly mutated genes identified by WES; all 29 primary tumors carried ≥1 mutation in this set. Mutational burden (mean 11±4 vs 25±11, P=3.4×10⁻⁵) and CNA burden (mean 2±3 vs 12±9, P=0.001) were significantly lower in 5 patients with indolent, untreated disease. [PMID:24145436](../papers/24145436.md)
- [NOTCH2](../genes/NOTCH2.md) PEST-truncating mutations in 9/172 (5.2%) MCL confer dismal prognosis (3-year [OS](../cancer_types/OS.md) 0% vs 62%, P=2.5×10⁻⁴) and are an independent OS risk factor (HR 3.5; 95% CI 1.3–9.5; P=0.017); mutually exclusive with [NOTCH1](../genes/NOTCH1.md) mutations (8/172, 4.6%). [PMID:24145436](../papers/24145436.md)
- [NSD2](../genes/NSD2.md) (WHSC1/MMSET) mutated in 13/130 (10%) MCL — first description in lymphoma; NSD2-mutated MCL transcriptionally phenocopies t(4;14) plasma-cell myeloma. [PMID:24145436](../papers/24145436.md)
- [BIRC3](../genes/BIRC3.md) inactivating mutations in 11/173 (6.4%) MCL; tightly co-occurring with 11q22.2 deletion (10/11 mutated cases, P=1.1×10⁻⁴); acquired post-treatment in 2 relapse cases. [PMID:24145436](../papers/24145436.md)
- Kataegis foci (regional hypermutation) observed in 3/4 WGS cases, clustering around the t(11;14) 11q13 breakpoint and Ig loci; stable in sequential samples — suggesting kataegis is an early, stable MCL event. [PMID:24145436](../papers/24145436.md)
- [SOX11](../genes/SOX11.md) expression partitions the mutation landscape: [ATM](../genes/ATM.md)/[NSD2](../genes/NSD2.md)/[KMT2D](../genes/KMT2D.md)/[MEF2B](../genes/MEF2B.md) mutations enriched in SOX11-positive IGHV-unmutated MCL; [CCND1](../genes/CCND1.md)/[TLR2](../genes/TLR2.md) mutations enriched in SOX11-negative IGHV-mutated MCL. [PMID:24145436](../papers/24145436.md)
- Clonal evolution documented at progression: one case gained 20 CNAs and chromothripsis on chr4/12; another showed subclone replacement after chemotherapy with loss of 11 initial mutations and new driver acquisition. [PMID:24145436](../papers/24145436.md)

## Sources

- cBioPortal study: `mcl_idibips_2013`
- [PMID:24145436](../papers/24145436.md) — primary publication
- EGA: EGAS00001000510 (sequencing); GEO: GSE46969 (SNP6.0), GSE36000 (HU133+2.0)

*This page was processed by **crosslinker** on **2026-05-09**.*
