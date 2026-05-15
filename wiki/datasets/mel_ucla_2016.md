---
name: "Melanoma UCLA Anti-PD-1 Cohort (Hugo et al. 2016)"
studyId: mel_ucla_2016
institution: University of California Los Angeles (UCLA)
size: 38
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
panels: []
tags:
  - melanoma
  - anti-pd-1
  - immunotherapy
  - pembrolizumab
  - nivolumab
  - ipres
  - tumor-mutational-burden
  - brca2
processed_by: crosslinker
processed_at: 2026-05-14
---

# Melanoma UCLA Anti-PD-1 Cohort (Hugo et al. 2016)

## Overview

Prospective cohort of 38 metastatic cutaneous melanoma patients treated with anti-PD-1 antibodies ([pembrolizumab](../drugs/pembrolizumab.md) or [nivolumab](../drugs/nivolumab.md)) at UCLA. Pretreatment biopsies were collected and profiled by whole-exome sequencing (all 38) and RNA-seq (28-tumor subset). The cohort was the primary discovery set for the Innate anti-PD-1 Resistance (IPRES) transcriptomic signature. Transcriptome data are deposited as GEO accession GSE78220. [PMID:26997480](../papers/26997480.md)

## Composition

- Cancer type: [SKCM](../cancer_types/SKCM.md) (metastatic cutaneous melanoma)
- 38 patients: 21 responders and 17 non-responders (irRECIST criteria; mixed-response cases excluded)
- 14 of 38 patients had prior MAPK-inhibitor therapy
- Specimens: 32 pretreatment tumors, 2 pretreatment tumor-derived cultures, 3 early on-treatment non-responding tumors, 1 early on-treatment responding tumor; all with patient-matched normals
- Assay: Illumina HiSeq 2000, 2×100 bp; median exome coverage 140×; RNA-seq on 28-tumor subset with sufficient RNA quality [PMID:26997480](../papers/26997480.md)

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md) — all 38 tumors
- [rna-seq](../methods/rna-seq.md) — 28-tumor subset
- Variant annotation: [Oncotator](../methods/oncotator.md)
- Copy-number: intersection of Sequenza and [VarScan2](../methods/varscan.md)
- Gene set enrichment: [GSVA](../methods/gsva.md) and [GSEA](../methods/gsea.md) using MSigDB C2/C6/C7

## Papers using this cohort

- [PMID:26997480](../papers/26997480.md) — Hugo et al. 2016, *Cell* — "Genomic and Transcriptomic Features of Response to Anti-PD-1 Therapy in Metastatic Melanoma"; primary discovery study for this cohort.

## Notable findings derived from this cohort

- Mutational load (median 495 vs 281 non-synonymous SNVs in responders vs non-responders) trended higher in responders but was not significantly predictive (Mann-Whitney P=0.30); high mutational load was prognostic for longer overall survival. [PMID:26997480](../papers/26997480.md)
- [BRCA2](../genes/BRCA2.md) loss-of-function nsSNVs enriched in responders: 28% (6/21) vs 6% (1/17) non-responders (Fisher P=0.002, OR=6.2 vs 6% melanoma background rate in 469-tumor cohort); BRCA2-mutant tumors had significantly higher overall mutational loads. [PMID:26997480](../papers/26997480.md)
- IPRES (Innate anti-PD-1 Resistance) co-enrichment of 26 transcriptomic signatures covering mesenchymal transition, ECM remodeling, angiogenesis, hypoxia, and wound healing defined a non-responder subset (9/13 non-responders vs 1/15 responders; OR=4.6, P=0.013). [PMID:26997480](../papers/26997480.md)
- No recurrent copy-number alterations exclusive to either responder group. [PMID:26997480](../papers/26997480.md)
- Key IPRES mesenchymal-transition transcripts up-regulated in non-responders: [AXL](../genes/AXL.md), [ROR2](../genes/ROR2.md), [WNT5A](../genes/WNT5A.md), [LOXL2](../genes/LOXL2.md), [TWIST2](../genes/TWIST2.md), [TAGLN](../genes/TAGLN.md), [FAP](../genes/FAP.md); immunosuppressive cytokines [IL10](../genes/IL10.md), [VEGFA](../genes/VEGFA.md), [VEGFC](../genes/VEGFC.md); monocyte chemoattractants [CCL2](../genes/CCL2.md), [CCL7](../genes/CCL7.md), [CCL8](../genes/CCL8.md), [CCL13](../genes/CCL13.md). [PMID:26997480](../papers/26997480.md)
- IPRES program detected across multiple TCGA cancer types ([PAAD](../cancer_types/PAAD.md), [LUAD](../cancer_types/LUAD.md), [COAD](../cancer_types/COAD.md), ccRCC) and was enriched in metastatic vs primary [SKCM](../cancer_types/SKCM.md) (90/282 metastatic vs 6/69 primary in [skcm_tcga_pub_2015](../datasets/skcm_tcga_pub_2015.md); P=3.9e-5, OR=0.2). [PMID:26997480](../papers/26997480.md)
- IPRES was NOT enriched in non-responders to anti-CTLA-4 in the [skcm_dfci_2015](../datasets/skcm_dfci_2015.md) cohort, indicating mechanistic distinction between anti-PD-1 and anti-CTLA-4 innate resistance. [PMID:26997480](../papers/26997480.md)

## Sources

- cBioPortal studyId: `mel_ucla_2016`
- GEO accession: GSE78220 (transcriptome data)
- Hugo W et al. "Genomic and Transcriptomic Features of Response to Anti-PD-1 Therapy in Metastatic Melanoma." *Cell*. 2016;165(1):35-44. [PMID:26997480](../papers/26997480.md). DOI: 10.1016/j.cell.2016.02.065.

*This page was processed by **crosslinker** on **2026-05-14**.*
