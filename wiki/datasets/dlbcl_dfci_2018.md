---
name: DFCI / Broad DLBCL WES Cohort (Chapuy et al. 2018)
studyId: dlbcl_dfci_2018
institution: Dana-Farber Cancer Institute / Brigham and Women's Hospital / Broad Institute
size: 304
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
  - STRUCTURAL_VARIANT
  - MRNA_EXPRESSION
panels: []
tags:
  - dlbcl
  - diffuse-large-b-cell-lymphoma
  - whole-exome-seq
  - structural-variants
  - genetic-subtypes
  - r-chop
  - nmf-clustering
  - dbgap
  - geo
processed_by: crosslinker
processed_at: 2026-05-16
---

# DFCI / Broad DLBCL WES Cohort (Chapuy et al. 2018)

## Overview

Whole-exome sequencing cohort of 304 primary diffuse large B-cell lymphomas ([DLBCLNOS](../cancer_types/DLBCLNOS.md)) assembled at Dana-Farber Cancer Institute, Brigham and Women's Hospital, Mayo Clinic/University of Iowa, the RICOVER-60 trial (Germany), and the University of Göttingen. WES included a spiked-in structural variant (SV) bait set enabling targeted SV capture in 296/304 samples. 85% of patients (259/304) received R-CHOP-like therapy with long-term follow-up (median 78.5 months). The study defined five coordinate genetic subtypes (C1–C5) of DLBCL by NMF consensus clustering on 158 driver alterations. Raw WES deposited in dbGaP phs000450.v1.p1; Affymetrix expression data in GEO GSE98588.

## Composition

- **n = 304** newly diagnosed primary DLBCLs (passed QC from 351 collected); 85% (259/304) received R-CHOP-like therapy.
- Sources: 129 RICOVER-60 trial samples, 103 DFCI/Brigham & Women's, 67 Mayo Clinic/University of Iowa SPORE, 5 University of Göttingen.
- 44% (135/304) had patient-matched normals; 56% (168/304) were FFPE-derived (tumor-only calling with Panel-of-Normals and ExAC filtering).
- Cancer type: [DLBCLNOS](../cancer_types/DLBCLNOS.md); includes rare extranodal cases with [PCNSL](../cancer_types/PCNSL.md) or primary testicular lymphoma ([TT](../cancer_types/TT.md)) involvement that cluster in genetic subtype C5.
- Median tumor WES coverage 87.6× (range 39–206.8×); SV bait capture mean depth 221.4×.

## Assays / panels (linked)

- [Whole-exome sequencing](../methods/whole-exome-seq.md): Agilent SureSelect Human All Exon v2.0 + spiked-in SV bait set.
- Reads aligned with [BWA](../methods/bwa.md) to GRCh37 (hg19) via Broad's Picard/Firehose pipeline.
- Somatic mutations called with [MuTect](../methods/mutect.md) and Indelocator; annotated with [Oncotator](../methods/oncotator.md).
- Significantly mutated genes by [MutSig2CV](../methods/mutsig.md) (q ≤ 0.1); spatial clustering by [CLUMPS](../methods/clumps.md).
- SCNAs by [GISTIC2.0](../methods/gistic.md); purity/ploidy by [ABSOLUTE](../methods/absolute.md).
- SVs by four-algorithm consensus: BreaKmer, Lumpy, dRanger, SvABA.
- Affymetrix U133plus2 expression arrays (GEO GSE98588) for transcriptional COO classification.

## Papers using this cohort

- [PMID:29713087](../papers/29713087.md) — Chapuy et al. 2018, Nature Medicine — "Molecular subtypes of diffuse large B cell lymphoma are associated with distinct pathogenic mechanisms and outcomes."

## Notable findings derived from this cohort

- 98 candidate cancer genes (CCGs) identified (MutSig2CV q<0.1), including 40 previously undescribed DLBCL drivers; 7 additional CCGs captured only by CLUMPS 3D protein-structure clustering [PMID:29713087](../papers/29713087.md).
- SVs detected in 64% (189/296) of tumors; most frequently rearranged genes: [IGH](../genes/IGH.md) (40%), [BCL2](../genes/BCL2.md) (21%), [BCL6](../genes/BCL6.md) (19%), [MYC](../genes/MYC.md) (8%), [CD274](../genes/CD274.md)/PD-L1 + PDCD1LG2/PD-L2 (5% combined) [PMID:29713087](../papers/29713087.md).
- Five coordinate genetic subtypes defined by NMF: C1 (ABC, marginal-zone-like, BCL6-SV, favorable); C2 (COO-independent, biallelic [TP53](../genes/TP53.md) inactivation, genomic instability); C3 (GCB, BCL2-SV/[EZH2](../genes/EZH2.md)/[PTEN](../genes/PTEN.md), unfavorable); C4 (GCB, histone/BCR mutations, favorable); C5 (ABC, [MYD88](../genes/MYD88.md)^L265P^/[CD79B](../genes/CD79B.md)/18q-BCL2, unfavorable) [PMID:29713087](../papers/29713087.md).
- Genetic signatures predicted PFS and [OS](../cancer_types/OS.md) independently of the International Prognostic Index (IPI); C5 HR=2.01 for low-risk IPI reference; combined high-risk IPI + C5 features HR≈6.91 [PMID:29713087](../papers/29713087.md).
- 74% of DLBCLs carried at least one genetic basis of immune escape (MHC class I, [B2M](../genes/B2M.md), [CD70](../genes/CD70.md), [CD58](../genes/CD58.md), CD274/PD-L1, [PDCD1LG2](../genes/PDCD1LG2.md), [CIITA](../genes/CIITA.md) alterations) [PMID:29713087](../papers/29713087.md).

## Sources

- Chapuy B et al. "Molecular subtypes of diffuse large B cell lymphoma are associated with distinct pathogenic mechanisms and outcomes." Nature Medicine. 2018;24(5):679-690. [PMID:29713087](../papers/29713087.md). DOI: 10.1038/s41591-018-0016-8.
- dbGaP accession: phs000450.v1.p1 (WES data).
- GEO accession: GSE98588 (Affymetrix U133plus2 expression data).

*This page was processed by **crosslinker** on **2026-05-16**.*
