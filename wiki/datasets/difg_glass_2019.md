---
name: GLASS Consortium Diffuse Glioma (2019)
studyId: difg_glass_2019
institution: GLASS Consortium (multi-institutional, 35 centers worldwide)
size: 222
reference_genome: b37
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - whole-genome-seq
  - bulk-rna-seq
panels: []
tags:
  - glioma
  - diffuse-glioma
  - IDH-mutant
  - IDH-wildtype
  - longitudinal
  - paired-samples
  - recurrence
  - hypermutation
  - clonal-evolution
  - GLASS
processed_by: crosslinker
processed_at: 2026-05-16
---

# GLASS Consortium Diffuse Glioma (2019)

## Overview

The GLASS (Glioma Longitudinal Analysis) Consortium dataset comprises temporally separated tumor samples from 222 adult patients with diffuse glioma, collected across 35 hospitals worldwide. Each patient contributed at least two time-separated tumor biopsies — an initial (diagnostic) sample and one or more recurrent samples — enabling paired longitudinal analysis of tumor evolution under therapy. Molecular subtypes follow the 2016 WHO CNS classification: IDH-mutant + 1p/19q co-deleted (IDHmut-codel, n=25), IDH-mutant without 1p/19q co-deletion (IDHmut-noncodel, n=63), and IDH wild-type (IDHwt, n=134). The dataset was assembled by re-processing TCGA-GBM ([gbm_tcga](../datasets/gbm_tcga.md)) and TCGA-LGG ([lgg_tcga](../datasets/lgg_tcga.md)) samples alongside data from 33 additional contributing centers to create a unified longitudinal resource.

## Composition

- **Total patients:** 222 (screened from 288; 66 excluded for QC)
- **Subtypes:** IDHmut-codel n=25; IDHmut-noncodel n=63; IDHwt n=134
- **Time points:** 211 initial, 234 first-recurrence, 32 second-recurrence, 11 third-recurrence, 1 fourth-recurrence samples
- **Sequencing depth:** 436 exomes (200 patients) and 165 whole genomes (78 patients); 78 samples with both; matched germline for all patients
- **RNA-seq:** 84 samples (42 pairs) used for immune deconvolution via CIBERSORT; transcriptomic subset only
- **Reference build:** b37 (human_g1k_v37_decoy)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — primary sequencing modality (n=436 exomes)
- [whole-genome-seq](../methods/whole-genome-seq.md) — subset (n=165 genomes, 78 patients)
- [bulk-rna-seq](../methods/bulk-rna-seq.md) — 84 samples for immune deconvolution
- Variant calling: [Mutect2](../methods/mutect.md) (multi- and single-sample), GATK 4 / BQSR
- Copy number: GATK ModelSegments + [TITAN](../methods/titan-cna.md) for allele-specific CN and purity/ploidy
- Clonal inference: [PyClone](../methods/pyclone.md) (CCF-based clustering); [CIBERSORT](../methods/cibersortx.md) immune deconvolution
- HLA typing: OptiType v1.3.1; neoantigen prediction: pVACseq + [netMHCpan](../methods/netmhcpan.md) v2.8
- Selection inference: dNdScv, neutralitytestr, SubClonalSelection (Bayesian)

## Papers using this cohort

- [PMID:31748746](../papers/31748746.md) — GLASS Consortium primary analysis: longitudinal somatic evolution of diffuse glioma

## Notable findings derived from this cohort

- Driver genes detected at diagnosis ([IDH1](../genes/IDH1.md), [TP53](../genes/TP53.md), [ATRX](../genes/ATRX.md), [TERT](../genes/TERT.md) promoter, chr7 gain/chr10 loss, [EGFR](../genes/EGFR.md) amplification) were almost universally retained at recurrence; few recurrence-specific alterations emerged. [PMID:31748746](../papers/31748746.md)
- Alkylating-agent-treated recurrences showed treatment-induced hypermutation at subtype-dependent rates: IDHmut-noncodel 47%, IDHmut-codel 25%, IDHwt 16% (Fisher's P=2.0e-03); hypermutation did not associate with shorter overall survival. [PMID:31748746](../papers/31748746.md)
- IDHmut-noncodel recurrences frequently acquired aneuploidy together with cell-cycle alterations ([CDKN2A](../genes/CDKN2A.md) homozygous deletion, CCND2/CDK4/CDK6 gain, [RB1](../genes/RB1.md) mutation/loss); patients with these alterations had significantly shorter survival (log-rank P<0.0001). [PMID:31748746](../papers/31748746.md)
- Subclonal selection at recurrence — observed in 64% of IDHwt tumors — was associated with shorter overall survival (adjusted Cox HR=1.53, 95% CI 1.00–2.41, P=4.8e-02). [PMID:31748746](../papers/31748746.md)
- Clonal architecture was largely stable (84% of tumors retained a dominant CCF cluster); immunoediting activity did not differ between initial and recurrent tumors, supporting the view that strongest selective pressures act early in glioma development. [PMID:31748746](../papers/31748746.md)

## Sources

- cBioPortal study: `difg_glass_2019`
- GLASS Consortium: https://www.glass-consortium.org/
- Primary publication: [PMID:31748746](../papers/31748746.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
