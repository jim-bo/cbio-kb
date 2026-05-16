---
name: MSK Upper Tract Urothelial Carcinoma PDX/PDC Panel (Kim et al. 2020)
studyId: utuc_pdx_msk_2019
institution: Memorial Sloan Kettering Cancer Center
size: 17
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - MUTATION_EXTENDED
  - COPY_NUMBER_ALTERATION
panels:
  - IMPACT300
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - UTUC
  - urothelial-carcinoma
  - PDX
  - PDC
  - patient-derived-xenograft
  - preclinical-model
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Upper Tract Urothelial Carcinoma PDX/PDC Panel (Kim et al. 2020)

## Overview

Collection of 17 patient-derived xenograft (PDX) models and 6 patient-derived cell line (PDC) models established from 34 [UTUC](../cancer_types/UTUC.md) surgical specimens at Memorial Sloan Kettering Cancer Center, all profiled by [MSK-IMPACT](../methods/msk-impact-panel.md) and benchmarked against matched patient tumors. Released on cBioPortal as utuc_pdx_msk_2019. Companion clinical cohort of 119 patient tumors released as [utuc_msk_2019](../datasets/utuc_msk_2019.md). [PMID:32332851](../papers/32332851.md)

## Composition

- 17 PDX models established from 34 surgical UTUC specimens (50% take rate); 6 PDC models from 24 tumors (25% take rate), all surviving beyond 10 passages.
- Source: predominantly radical nephroureterectomy specimens; 3 distant/nodal metastases all engrafted (100%); one endoscopic biopsy did not engraft.
- Cancer type: [UTUC](../cancer_types/UTUC.md).
- 4/17 engrafted tumors MSI-H, including three Lynch syndrome cases (germline MLH1/MSH2) and one without identifiable germline cause; TMB range 20.3–157.2 mut/Mb in MSI-H models.
- Recurrent PDX-specific genomic change: [CDKN2A](../genes/CDKN2A.md)/[CDKN2B](../genes/CDKN2B.md) deep deletions in 29% of PDX (engraftment selection pressure). [PMID:32332851](../papers/32332851.md)

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md) — multiple versions (300-, 341-, 410-, 468-gene); profiled on matched tumor–PDX pairs.
- [whole-exome-seq](../methods/whole-exome-seq.md) — UCC03 and UCC30 for linear/branched clonal evolution analysis.
- [patient-derived-xenograft](../methods/patient-derived-xenograft.md) — in vivo drug treatment models (gemcitabine/carboplatin, gemcitabine/cisplatin, [neratinib](../drugs/neratinib.md), [trastuzumab](../drugs/trastuzumab.md) deruxtecan).
- [immunohistochemistry](../methods/immunohistochemistry.md), [masson-trichrome-staining](../methods/masson-trichrome-staining.md), Picro Sirius red for histologic and ECM characterization. [PMID:32332851](../papers/32332851.md)

## Papers using this cohort

- [PMID:32332851](../papers/32332851.md) — Kim, Hu et al., establishment and genomic characterization of UTUC PDX/PDC models; pharmacologic profiling demonstrating chemosensitivity concordance with source patients and HER2-ADC (trastuzumab deruxtecan) superiority over neratinib in HER2 S310F UTUC.

## Notable findings derived from this cohort

- 72.7% concordance of known/likely oncogenic mutations across 17 tumor/PDX pairs; hypermutated UCC34 PDX dropped below 50% concordance. [PMID:32332851](../papers/32332851.md)
- PDX chemosensitivity mirrored source patients in all three tested cases: UCC03 PDX sensitive to gemcitabine/carboplatin (P=0.0177) and [gemcitabine](../drugs/gemcitabine.md) alone (P=0.0065) matching patient partial response; UCC19 PDX highly sensitive to Gem/Carbo (P<0.0001) consistent with patient durable response. [PMID:32332851](../papers/32332851.md)
- UCC17 (MSI-H) and UCC36 (MSI-H Lynch) PDX models showed minimal growth inhibition by gemcitabine/cisplatin, consistent with the 0/2 MSI-H pathologic response rate in the clinical NAC cohort. [PMID:32332851](../papers/32332851.md)
- UCC14-PDC (HER2 S310F UTUC): neratinib IC50 508.3 nM (largely refractory in vivo); trastuzumab deruxtecan (DS-8201a) strongly inhibited UCC14-PDX in vivo (P<0.0001), significantly outperforming neratinib (P<0.0001). [PMID:32332851](../papers/32332851.md)
- AID/APOBEC mutational signature (COSMIC Signatures 2+13) preserved across passages in UCC03 PDX but Signature 2 lost in UCC30 PDX, flagging potential signature drift during engraftment. [PMID:32332851](../papers/32332851.md)
- All models available as a shared community resource; genomic data released on cBioPortal. [PMID:32332851](../papers/32332851.md)

## Sources

- [PMID:32332851](../papers/32332851.md)

*This page was processed by **crosslinker** on **2026-05-16**.*
