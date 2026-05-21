---
name: "Colitis-Associated Bowel Cancer — MSK 2022"
studyId: bowel_colitis_msk_2022
institution: Memorial Sloan Kettering Cancer Center
size: 174
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
  - foundationone
  - whole-exome-seq
  - rna-seq
  - hm450-methylation-array
panels:
  - msk-impact-panel
  - foundationone
tags:
  - colitis-associated-cancer
  - inflammatory-bowel-disease
  - colorectal-cancer
  - wnt-independence
  - tp53-clonality
processed_by: crosslinker
processed_at: 2026-05-21
---

# Colitis-Associated Bowel Cancer — MSK 2022

## Overview

The largest integrated clinico-genomic cohort of colitis-associated cancers (CAC) to date, assembled by Chatila et al. at Memorial Sloan Kettering and collaborating institutions. The dataset includes 174 IBD patients with bowel cancer plus 29 synchronous or isolated dysplasia specimens, profiled with targeted panel sequencing, whole-exome sequencing, RNA-seq, methylation arrays, patient-derived organoids, and xenograft models. It supports investigation of molecular evolution, field effects, and targeted therapy opportunities in [COADREAD](../cancer_types/COADREAD.md) arising in the context of inflammatory bowel disease.

## Composition

- **Patients:** 174 IBD patients with colitis-associated cancer — 144 "clinical cohort," 161 "genomic cohort" (131 full clinical + sequencing; 30 sequencing-only; 47 re-annotated from prior MSK series).
- **IBD type:** 56% ulcerative colitis, 44% Crohn's disease.
- **Cancer types:** [COAD](../cancer_types/COAD.md), [READ](../cancer_types/READ.md), [SBC](../cancer_types/SBC.md) (small bowel); overall [COADREAD](../cancer_types/COADREAD.md) framing.
- **Tumor site distribution:** 10.3% small intestine, 27.1% right colon, 29.5% left colon, 31.3% rectum, 1.8% fistula tract.
- **Stage at diagnosis:** Stage 0 (2.4%), I (16.9%), II (20.5%), III (28.3%), IV (29.5%).
- **Sequenced specimens:** 166 CAC + 9 dysplasia by targeted panel (132 [MSK-IMPACT](../methods/msk-impact-panel.md) 341–505 genes; 34 [FoundationOne](../methods/foundationone.md) 315 genes); 13 CAC + 20 dysplasia by whole-exome sequencing (150× depth).
- **Germline analysis:** MSK-IMPACT germline panel (76–88 genes) in 73 consented patients (45% of genomic cohort).
- **Sites of accrual:** MSK (n=125), Weill Cornell/NYP (n=29), Sheba Medical Center Israel (n=7).
- **Functional models:** patient-derived organoids and [PDX](../methods/patient-derived-xenograft.md) from CAC; AOM/DSS mouse model of inflammatory colorectal cancer with mouse MSK-IMPACT sequencing.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) (341–505 genes) — targeted panel NGS for somatic and germline alterations.
- [FoundationOne](../methods/foundationone.md) (315 genes) — targeted panel NGS.
- [WES](../methods/whole-exome-seq.md) — 150× depth for 33 specimens (13 CAC + 20 dysplasia) + 13 adjacent normal mucosa.
- [RNA-seq](../methods/rna-seq.md) — transcriptomic profiling (subset of patients).
- [HM450 methylation array](../methods/hm450-methylation-array.md) — global DNA methylation profiling.
- [FACETS](../methods/facets.md) — copy-number and clonality analysis.
- [OncoKB annotation](../methods/oncokb-annotation.md) — driver annotation.

## Papers using this cohort

- [PMID:36611031](../papers/36611031.md) — Chatila et al. (2023) "Integrated clinical and genomic analysis identifies driver events and molecular evolution of colitis-associated cancers," *Nature Communications*.

## Notable findings derived from this cohort

- [TP53](../genes/TP53.md) altered in 90% of CAC and ~50% of dysplasia; convergent independent [TP53](../genes/TP53.md) events confirmed across multifocal lesions; [TP53](../genes/TP53.md) not detected in adjacent normal mucosa, arguing against a TP53-driven genomic field defect. [PMID:36611031](../papers/36611031.md)
- CAC is largely Wnt-independent: Wnt alterations infrequent and enriched only in subclonal-TP53 cases (P=0.017); CAC organoids grew without exogenous Wnt; porcupine (LGK-974) and tankyrase (G007-LK) inhibitors did not suppress CAC PDX growth. [PMID:36611031](../papers/36611031.md)
- Recurrent driver landscape: [TP53](../genes/TP53.md) 90%, [KRAS](../genes/KRAS.md) 31%, [MYC](../genes/MYC.md) 20%, [APC](../genes/APC.md) 20%, [SMAD4](../genes/SMAD4.md) 13%; [PIK3CA](../genes/PIK3CA.md) and [IDH1](../genes/IDH1.md) enriched in Crohn's disease vs ulcerative colitis. [PMID:36611031](../papers/36611031.md)
- Broad copy-number alterations significantly less common in CAC than sporadic CRC (CNapp broad CNA score P=0.000016); focal CNA frequency similar; [MYC](../genes/MYC.md) focal amplifications enriched in CAC. [PMID:36611031](../papers/36611031.md)
- [IDH1](../genes/IDH1.md) R132 mutations (6 cases) showed high global methylation and suppressed PDX growth on [ivosidenib](../drugs/ivosidenib.md) treatment; [IDH1](../genes/IDH1.md) and [FGFR2](../genes/FGFR2.md) amplification/fusion represent actionable targets with FDA approvals in other IBD-associated GI cancers. [PMID:36611031](../papers/36611031.md)
- Multifocal CAC lesions develop independently: no shared genetic alterations across six synchronous lesions in one total colectomy patient; confirmed across six additional patients with multiple primaries. [PMID:36611031](../papers/36611031.md)
- Germline pathogenic alterations in 10/73 (14%) consented patients: most common [APC](../genes/APC.md) I1307K (n=3); also [PMS2](../genes/PMS2.md), [ATM](../genes/ATM.md), [RAD51B](../genes/RAD51B.md), [DICER1](../genes/DICER1.md), [FANCA](../genes/FANCA.md), [FANCC](../genes/FANCC.md). [PMID:36611031](../papers/36611031.md)

## Sources

- cBioPortal study: `bowel_colitis_msk_2022`
- DOI: [10.1038/s41467-022-35592-9](https://doi.org/10.1038/s41467-022-35592-9)

*This page was processed by **crosslinker** on **2026-05-21**.*
