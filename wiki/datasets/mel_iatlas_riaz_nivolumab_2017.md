---
name: CA209-038 Melanoma Nivolumab (Riaz et al. 2017)
studyId: mel_iatlas_riaz_nivolumab_2017
institution: Memorial Sloan Kettering Cancer Center
size: 68
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
  - tcr-seq
  - immunohistochemistry
panels: []
tags:
  - melanoma
  - anti-pd1
  - nivolumab
  - immunotherapy
  - immunoediting
  - tumor-mutation-burden
  - paired-biopsy
  - clonal-evolution
processed_by: crosslinker
processed_at: 2026-05-15
---

# CA209-038 Melanoma Nivolumab (Riaz et al. 2017)

## Overview

Riaz et al. profiled paired pre- and on-therapy biopsies from 68 advanced [melanoma](../cancer_types/SKCM.md) patients enrolled on the prospective CA209-038 trial (NCT01621490) of [nivolumab](../drugs/nivolumab.md) (3 mg/kg q2w). Patients were stratified into ipilimumab-progressed (Ipi-P, n=35) and ipilimumab-naive (Ipi-N, n=33) cohorts. Combining whole-exome sequencing, RNA-seq, and TCR beta-chain sequencing on biopsies obtained pre-treatment and at cycle 1 day 29, the study establishes the genomic basis of tumor immunoediting on PD-1 blockade and characterizes the divergent response dynamics by prior immunotherapy exposure. Published in *Cell* (2017). The dataset is the genomic backbone of the iAtlas resource.

## Composition

- **68 advanced melanoma patients** with paired biopsies — 35 previously progressed on [ipilimumab](../drugs/ipilimumab.md) (Ipi-P), 33 ipilimumab-naive (Ipi-N).
- Median age 55 (range 22–89); stage distribution 1 M0 / 13 M1a / 10 M1b / 36 M1c / 8 unknown.
- Response rates (RECIST v1.1): Ipi-N 21% CR/PR, Ipi-P 22% CR/PR.
- Biopsies from the same anatomic site — pre-therapy (1–7 days before first dose) and on-therapy (cycle 1 day 29, between days 23–29).
- Cancer type: [Skin Cutaneous Melanoma (SKCM)](../cancer_types/SKCM.md).
- 85 patients accrued on the trial; 68 had sufficient material for genomic analysis.

## Assays / panels (linked)

- [whole-exome sequencing](../methods/whole-exome-seq.md) — Agilent SureSelect All Exon V2 with HiSeq 2000/2500, mean depth 168×; somatic variant calling by intersection of [MuTect](../methods/mutect.md) 1.1.4, SomaticSniper, [VarScan](../methods/varscan.md) 2.3.7, and [Strelka](../methods/strelka.md) 1.0.13 (n=68 pre-therapy; n=41 paired pre/on)
- [RNA-seq](../methods/rna-seq.md) — aligned with [STAR](../methods/star.md) on hg19, DESeq2-normalized FPKM, immune deconvolution by [CIBERSORT](../methods/cibersortx.md) (n=45 baseline; n=26 paired with WES)
- [TCR beta-chain sequencing](../methods/tcr-seq.md) — tumor DNA via Adaptive Biotechnologies immunoSEQ (n=34 paired pre/on)
- [FISH](../methods/fish.md) / [IHC](../methods/immunohistochemistry.md) — PD-L1 (clone 28-8), CD3, [CD4](../genes/CD4.md), CD8, [FOXP3](../genes/FOXP3.md)
- [FACETS](../methods/facets.md) v0.5.0 — allele-specific copy number; [GISTIC](../methods/gistic.md) for recurrent SCNAs; [PyClone](../methods/pyclone.md) v0.13.0 — cancer cell fraction
- [NetMHCpan](../methods/netmhcpan.md) v4.0 — neoantigen prediction (9-mer sliding windows, rank < 2%)
- [GSEA](../methods/gsea.md) — pathway analysis

## Papers using this cohort

- [PMID:29033130](../papers/29033130.md) — Riaz et al., *Cell* (2017): Tumor and Microenvironment Evolution during Immunotherapy with Nivolumab.

## Notable findings derived from this cohort

- **Pre-therapy tumor mutation burden (TMB) and clonal mutation load predict overall survival** in ipilimumab-naive (Ipi-N) but not ipilimumab-progressed (Ipi-P) melanoma patients. Median cohort mutation load 183 (range 1–7360). [PMID:29033130](../papers/29033130.md)
- **Mutation and neoantigen load drop markedly on-therapy in responders** (n=41 paired WES): mean 19% of pre-therapy variants retained in CR/PR vs 101% in PD (p=5.87e–5); consistent with active immunoediting. [PMID:29033130](../papers/29033130.md)
- **Net genomic contraction** (variants undergoing mutational contraction minus persistence) predicts response and [OS](../cancer_types/OS.md) better than raw TMB change. [PMID:29033130](../papers/29033130.md)
- **Selective depletion of antigenic mutations on-therapy:** neoantigen-to-non-antigenic mutation ratio dropped in CR/PR vs PD (p=0.03); number of expanded T-cell clones scales linearly with neoantigens becoming undetectable in responders (p=0.03). [PMID:29033130](../papers/29033130.md)
- **Focal [CDKN2A](../genes/CDKN2A.md) loss emerged on-therapy in 4 PD patients**; 3/4 had co-occurring chromosome-9p deletions encompassing the IFN gene cluster, suggesting acquired immune evasion. [PMID:29033130](../papers/29033130.md)
- **Immune checkpoint genes upregulated on-therapy** in all patients regardless of response: [PDCD1](../genes/PDCD1.md), [CD274](../genes/CD274.md), [CTLA4](../genes/CTLA4.md), [LAG3](../genes/LAG3.md), [TNFRSF9](../genes/TNFRSF9.md), [ICOS](../genes/ICOS.md); additionally [TNFRSF4](../genes/TNFRSF4.md), [TIGIT](../genes/TIGIT.md), [HAVCR2](../genes/HAVCR2.md), [VSIR](../genes/VSIR.md) selectively upregulated in responders. [PMID:29033130](../papers/29033130.md)
- **Diverging TCR-diversity dynamics by prior-therapy status:** on-therapy CDR3 richness change associated with benefit in Ipi-P (p=0.016); evenness change associated with benefit in Ipi-N (p=0.036). [PMID:29033130](../papers/29033130.md)
- **Cytolytic activity** ([GZMA](../genes/GZMA.md)/[PRF1](../genes/PRF1.md) geometric mean) on-therapy associated with benefit in both Ipi-N (p=0.005) and Ipi-P (p=0.043) patients. [PMID:29033130](../papers/29033130.md)
- **Pre-existing immunity distinguishes responders:** 189 DEGs between CR/PR vs PD pre-therapy; all Ipi-P responders showed a "hot tumor" phenotype pre-therapy. [PMID:29033130](../papers/29033130.md)
- TCGA mutational subtypes ([BRAF](../genes/BRAF.md), RAS, [NF1](../genes/NF1.md), triple-WT) did not stratify response to [nivolumab](../drugs/nivolumab.md). [PMID:29033130](../papers/29033130.md)

## Sources

- cBioPortal study ID: mel_iatlas_riaz_nivolumab_2017
- Trial: NCT01621490 (CA209-038)
- iAtlas resource (TCIA immunotherapy cohorts portal)

*This page was processed by **crosslinker** on **2026-05-15**.*
