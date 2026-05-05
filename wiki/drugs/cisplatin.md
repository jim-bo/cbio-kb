---
name: cisplatin
targets:
  - DNA
drug_class: platinum-based chemotherapy / radiosensitizer
canonical_source: corpus
unverified: true
tags:
  - radiosensitizer
  - chemoradiation
  - hnscc
  - standard-of-care
processed_by: crosslinker
processed_at: 2026-05-04
---

# cisplatin

## Overview

Cisplatin is a platinum-based alkylating agent that forms intrastrand and interstrand DNA crosslinks, inducing replication fork stalling and double-strand break (DSB) accumulation. It is one of the oldest and most widely used radiosensitizers: platinum adducts inhibit nucleotide-excision repair (NER), impairing the cell's ability to resolve the DNA damage compounded by ionizing radiation. Cisplatin is part of definitive concurrent chemoradiation (CRT) regimens in head and neck squamous cell carcinoma (HNSCC), cervical cancer, and other epithelial malignancies, and remains the reference arm against which novel radiosensitizers and immunotherapy combinations are benchmarked.

## Evidence in the corpus

- The ROBIN GenRad HNSCC trial (NCT03521570, part 2) at Cleveland Clinic / Emory compared re-irradiation + cisplatin versus re-irradiation + immune checkpoint inhibitor (PD-1 inhibitor) in recurrent or second-primary HNSCC; this trial is described as completed at the time of the white paper. In that cohort, a 1.5-fold increase in PD1+Ki67+[CD4](../genes/CD4.md)+ T cells from baseline to week 2–4 correlated with shorter progression-free survival under re-irradiation + PD-1 blockade — findings that were interpreted in contrast to the cisplatin reference arm. [PMID:41941260](../papers/41941260.md)
- The paper also references the Javelin HN100 chemoradiation ± [avelumab](../drugs/avelumab.md) expansion cohort (a cisplatin-backbone CRT trial) in the GenRad HNSCC context; analysis of that cohort identified intratumoral bacteria as a major source of therapy resistance in HNSCC, implicating the tumor microbiome as a resistance axis for CRT. [PMID:41941260](../papers/41941260.md)
- Cisplatin-based CRT is used as background context for the METEOR center's cervical cancer cohort, where CRT was found to remodel the TME with myeloid-cell infiltration and upregulation of the TP53/MDM2 axis in tumor cells, without significant upregulation of PD-L1/PD-1. [PMID:41941260](../papers/41941260.md)
- In the UCLA sarcoma PDTO biobank ([sarcoma_ucla_2024](../datasets/sarcoma_ucla_2024.md)), cisplatin was a component of the MAP neoadjuvant regimen (methotrexate/doxorubicin/cisplatin) tested in three treatment-naïve [osteosarcoma](../cancer_types/OS.md) biopsies. Organoid residual viability after MAP correlated with post-resection necrosis and clinical outcome: two specimens with ~50–57% residual viability had 99% and 95% necrosis respectively (no recurrence at 1,400–1,500 days), while one specimen with 73% residual viability had only 60% necrosis and relapsed within 200 days. [PMID:39305899](../papers/39305899.md)
- Cisplatin is also listed as a component of the >400-compound sarcoma PDTO screen and appears among the NCCN-listed standard-of-care regimens for osteosarcoma identified in the functional screen. [PMID:39305899](../papers/39305899.md)
- In the phase 3 CALGB 90601 (NCT00942331) first-line metastatic urothelial carcinoma trial (gemcitabine/cisplatin ± [bevacizumab](../drugs/bevacizumab.md)), pretreatment cfDNA from 201 patients was assessed for DDR alterations and prognostic genomic features. Oncogenic DDR alterations including [ERCC2](../genes/ERCC2.md) were not significantly associated with response to cisplatin-based chemotherapy (DDR+ response 50% vs DDR− 41%, p=0.4), primarily due to insufficient power ([ERCC2](../genes/ERCC2.md) only 4.5%). Higher ctDNA VAF was independently associated with shorter [OS](../cancer_types/OS.md) on cisplatin-based therapy (HR 2.51, 95% CI 1.26–5.00; p=0.009). [PMID:40256659](../papers/40256659.md)
- In the MSK PDAC cohort ([pdac_msk_2024](../datasets/pdac_msk_2024.md), n=1,480 with curated treatment data), FOLFIRINOX ([oxaliplatin](../drugs/oxaliplatin.md), not cisplatin) and gemcitabine/nab-paclitaxel were the dominant first-line regimens (38% and 37% respectively); cisplatin is mentioned as a historical reference in PDAC chemotherapy background. [PMID:39753968](../papers/39753968.md)
- In preclinical HER2+ xenograft models, cisplatin was used as a comparator in cell viability assays; T-DM1 was more potent than cisplatin (and [paclitaxel](../drugs/paclitaxel.md), [trastuzumab](../drugs/trastuzumab.md), [lapatinib](../drugs/lapatinib.md), [erlotinib](../drugs/erlotinib.md)) in HER2+ OE19 esophageal cancer cells, with T-DM1 IC50 <1 nM vs >100 nM in HER2− lines [PMID:27698471](../papers/27698471.md).
- Cohort-metadata context only: in the MD Anderson HNSCC imaging archive (n=215), 127 patients (59%) received concurrent chemotherapy, of whom 98% received platinum-based regimens (effectively cisplatin). No efficacy or biomarker claim is made; this citation records treatment-arm composition. [PMID:30179230](../papers/30179230.md)

## Resistance mechanisms

- Intratumoral bacteria in HNSCC identified as a source of resistance to cisplatin-containing chemoradiation in the Javelin HN100 expansion cohort analysis (GenRad). [PMID:41941260](../papers/41941260.md)

## Cancer types (linked)

- [HNSC](../cancer_types/HNSC.md) — head and neck squamous cell carcinoma; standard concurrent CRT agent; GenRad comparator arm.
- [CESC](../cancer_types/CESC.md) — cervical cancer; concurrent CRT backbone in the METEOR cohort.
- [ESCA](../cancer_types/ESCA.md), [STAD](../cancer_types/STAD.md) — HER2+ esophageal/gastric cancer; preclinical comparator context.
- [BLCA](../cancer_types/BLCA.md) — metastatic urothelial carcinoma; CALGB 90601 backbone cisplatin-based chemotherapy; DDR alteration predictive value not confirmed (underpowered).
- [OS](../cancer_types/OS.md) — osteosarcoma; MAP regimen component; organoid viability correlated with post-resection necrosis.

## Sources

- [PMID:41941260](../papers/41941260.md) — Gregucci et al. 2026, *Clin Cancer Res*. ROBIN white paper; cisplatin discussed as radiosensitizer reference and CRT backbone in GenRad HNSCC and METEOR cervical cohorts.
- [PMID:27698471](../papers/27698471.md)
- [PMID:30179230](../papers/30179230.md) — Grossberg et al. 2018, *Sci Data*. MD Anderson HNSCC imaging archive; cisplatin referenced as concurrent chemotherapy in 98% of the 127 chemo-treated patients (cohort-metadata only, no efficacy or biomarker claim).
- [PMID:39305899](../papers/39305899.md) — Al Shihabi et al. (Cell Stem Cell 2024). UCLA sarcoma PDTO biobank; MAP (methotrexate/doxorubicin/cisplatin) organoid viability correlated with post-resection necrosis in osteosarcoma.
- [PMID:39753968](../papers/39753968.md) — Varghese, Perry et al. (2024). MSK PDAC cohort; cisplatin referenced in chemotherapy background context.
- [PMID:40256659](../papers/40256659.md) — Guercio et al. (2025). CALGB 90601 cfDNA study; cisplatin-based chemotherapy backbone; DDR predictive value null (underpowered); VAF and TERT/PIK3CA/ERBB2 as prognostic markers.

*This page was processed by **crosslinker** on **2026-05-04**.*
