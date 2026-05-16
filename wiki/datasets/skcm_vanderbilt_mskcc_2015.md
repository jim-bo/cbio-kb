---
name: Melanoma Pretreatment Biopsies — Vanderbilt / MSK (2015)
studyId: skcm_vanderbilt_mskcc_2015
institution: Memorial Sloan Kettering Cancer Center and Vanderbilt-Ingram Cancer Center
size: 66
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - targeted-capture-seq
panels:
  - msk-impact-panel
tags:
  - skcm
  - melanoma
  - braf
  - brafi-resistance
  - pretreatment
  - pten
processed_by: crosslinker
processed_at: 2026-05-16
---

# Melanoma Pretreatment Biopsies — Vanderbilt / MSK (2015)

## Overview

66 pretreatment tumors from patients with stage IV or unresectable stage III [BRAF](../genes/BRAF.md) V600E/K-mutant metastatic melanoma collected at MSKCC and Vanderbilt-Ingram Cancer Center before BRAFi-based therapy. The study was designed to identify pretreatment genomic biomarkers of response to [vemurafenib](../drugs/vemurafenib.md) and [dabrafenib](../drugs/dabrafenib.md) monotherapy or in combination with MEKi. Custom capture-based sequencing across all coding exons and selected introns of >250 cancer-associated genes (MSK-IMPACT precursor, per Wagle et al. 2012 and Cheng et al. 2015) at mean coverage 622×. Data deposited at the MSK cBioPortal for Cancer Genomics.

## Composition

- 55 patients received BRAFi monotherapy (49 vemurafenib, 5 dabrafenib, 1 vemurafenib + [cobimetinib](../drugs/cobimetinib.md)); 11 received BRAFi + MEKi combination (3 vemurafenib + cobimetinib; 8 dabrafenib + [trametinib](../drugs/trametinib.md)).
- Response endpoints: RECIST 1.1 plus composite "response grade" (excellent / intermediate / poor).
- Comparator: 151 BRAF V600E/K-mutant tumors from TCGA [SKCM](../cancer_types/SKCM.md) cohort ([skcm_tcga_pub_2015](../datasets/skcm_tcga_pub_2015.md)).
- Follow-up: median 14.6 months (cutoff March 2016).
- Cancer type: [SKCM](../cancer_types/SKCM.md) (melanoma).

## Assays / panels (linked)

- Custom capture-based DNA sequencing (>250 cancer-associated genes; MSK-IMPACT precursor, Wagle et al. 2012 / Cheng et al. 2015); mean coverage 622×
- [MuTect](../methods/mutect.md) for SNV calling
- [GATK Somatic Indel Detector](../methods/gatk-somatic-indel-detector.md) for indels
- [FACETS](../methods/facets.md) for tumor purity, ploidy, and allele-specific copy number

## Papers using this cohort

- [PMID:32913971](../papers/32913971.md) — Shi et al. 2020, JCO: pretreatment [PTEN](../genes/PTEN.md) alterations and BRAFi resistance in BRAF-mutant melanoma

## Notable findings derived from this cohort

- PTEN loss-of-function alterations enriched in poor BRAFi responders (P=.005); associated with shorter PFS (HR 3.46, 95% CI 1.79–6.71, P<.001) and [OS](../cancer_types/OS.md) (HR 3.10, 95% CI 1.59–6.05, P<.001) — [PMID:32913971](../papers/32913971.md)
- Elevated BRAF-mutant allele fraction significantly enriched in excellent responders (P<.001); [CDKN2A](../genes/CDKN2A.md) alterations (41% of patients) showed no association with response — [PMID:32913971](../papers/32913971.md)
- [KDR](../genes/KDR.md) mutations (n=4; 1 hotspot R1032Q) appeared exclusively in poor responders with significantly shorter PFS and OS — [PMID:32913971](../papers/32913971.md)
- [RB1](../genes/RB1.md) (P=.0036) and [MDM2](../genes/MDM2.md) (P=.045) alterations enriched relative to TCGA, reflecting a more aggressive clinical profile — [PMID:32913971](../papers/32913971.md)
- 0/66 RAS mutations in pretreatment tumors; MAPK-pathway escape mutations rare at baseline — [PMID:32913971](../papers/32913971.md)

## Sources

- [PMID:32913971](../papers/32913971.md)
- cBioPortal study: `skcm_vanderbilt_mskcc_2015`

*This page was processed by **crosslinker** on **2026-05-16**.*
