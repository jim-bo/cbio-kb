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
processed_by: wiki-cli
processed_at: 2026-05-16
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
- Used as part of platinum-based chemotherapy for metastatic urothelial carcinoma in UC-GENOME (n=218 patients); [ERCC2](../genes/ERCC2.md) mutations significantly associated with chemotherapy response (p=0.0134), validating this biomarker in the metastatic setting [PMID:36333289](../papers/36333289.md)
- 143 metastatic gallbladder carcinoma patients received gemcitabine/cisplatin as the predominant first-line chemotherapy regimen among 233 [GBC](../cancer_types/GBC.md) cases profiled with MSK-IMPACT at MSK (2014--2021) [PMID:36228155](../papers/36228155.md)
- Used as standard platinum-based chemotherapy in 100% of the 489 [HGSOC](../cancer_types/HGSOC.md) patients in the TCGA ovarian carcinoma study; all patients received platinum-based therapy [PMID:21720365](../papers/21720365.md)
- Referenced as part of standard chemoradiation regimens in HNSCC; the cBioPortal platform paper describes genomic data for patients treated with cisplatin-based protocols [PMID:19176454](../papers/19176454.md)
- Cisplatin (with surgery and radiation) remains the standard-of-care backbone for OSCC at the time of the Pickering 2013 OSCC genomic analysis; no new biomarkers were validated for prospective treatment selection [PMID:23619168](../papers/23619168.md)
- TCGA endometrial cancer analysis (2013) suggests ~25% of high-grade endometrioid tumors have a copy-number-high serous-like molecular phenotype and may benefit from chemotherapy regimens including cisplatin rather than adjuvant radiotherapy [PMID:23636398](../papers/23636398.md)
- In muscle-invasive bladder carcinoma (n=131 [BLCA](../cancer_types/BLCA.md)), cisplatin-based chemotherapy was the reference standard of care at the time of the TCGA analysis with a median survival of 14–15 months for recurrent/metastatic disease; no molecularly targeted agent had been approved [PMID:24476821](../papers/24476821.md)
- Cited in [HCC](../cancer_types/HCC.md) trials (CELESTIAL, SHARP supporting context) as a reference comparator chemotherapy; [sorafenib](../drugs/sorafenib.md) combinations not primary focus [PMID:24798001](../papers/24798001.md)
- Platinum-based backbone (cisplatin + [gemcitabine](../drugs/gemcitabine.md)) is the standard chemotherapy platform for R/M [NPC](../cancer_types/NPC.md); [sintilimab](../drugs/sintilimab.md) added to CCRT with cisplatin improved 36-mo EFS to 86% vs 76% (HR 0.59) [PMID:24952746](../papers/24952746.md)
- Somatic [ERCC2](../genes/ERCC2.md) mutations were found exclusively in cisplatin responders (9/25, 36%) in muscle-invasive urothelial carcinoma treated with neoadjuvant cisplatin-based chemotherapy; [ERCC2](../genes/ERCC2.md) mutation is proposed as a predictive biomarker for cisplatin sensitivity [PMID:25096233](../papers/25096233.md)
- Standard first-line therapy for advanced CCA (IHCH/EHCH/CHOL) in combination with [gemcitabine](../drugs/gemcitabine.md), with [durvalumab](../drugs/durvalumab.md) addition showing incremental benefit; BRCA1/2 mutations (~3–5% of CCA) predict platinum sensitivity [PMID:25526346](../papers/25526346.md)
- Standard front-line platinum-based chemotherapy for gastric adenocarcinoma ([STAD](../cancer_types/STAD.md)); [BRCA2](../genes/BRCA2.md) mutation (17/294 cases, 5.8%) independently predicts longer survival (pooled HR 0.37, P=0.05) and may predict platinum and PARP-inhibitor sensitivity, paralleling ovarian cancer [PMID:25583476](../papers/25583476.md)
- Referenced as a chemotherapy backbone for iCCA; [futibatinib](../drugs/futibatinib.md) is cited as synergizing with cisplatin in FGFR2-rearranged iCCA [PMID:25608663](../papers/25608663.md)
- Platinum chemotherapy; usable from second trimester in pregnant young-onset NSCLC patients; review notes TKIs and immunotherapy are contraindicated in pregnancy whereas platinum-based regimens are acceptable from T2 [PMID:27346245](../papers/27346245.md)
- In head and neck cancer, germline FANCA deletion plus somatic FANCA stopgain in one HNSC patient identified as potential cisplatin-sensitivity biomarker by MSK-IMPACT profiling (N=151 advanced tumors) [PMID:27442865](../papers/27442865.md)
- First-line platinum backbone in BEP (bleomycin+etoposide+cisplatin, 37.2%), EP (42.2%), and TIP/VIP (20%) regimens in 180 advanced GCT patients; TP53 alterations exclusive to cisplatin-resistant tumors (16.3% vs 0%; P<.001); nutlin-3 showed antiproliferative synergy with cisplatin in TP53 wild-type cisplatin-resistant GCT cell lines [PMID:27646943](../papers/27646943.md)
- Cisplatin + [gemcitabine](../drugs/gemcitabine.md) (neoadjuvant/first-line) administered in the WashU urothelial carcinoma WES cohort (n=32 patients, 72 tumors); post-chemotherapy tumors showed clonal enrichment of [L1CAM](../genes/L1CAM.md) and integrin-signaling missense mutations, an APOBEC3A-dominant mutational signature, and selective elimination of [ATM](../genes/ATM.md)/[RB1](../genes/RB1.md)/[FANCC](../genes/FANCC.md)-altered clones (73.3% pre- vs 37.9% post-chemotherapy, p=0.05); cisplatin specifically drove a C>A mutational signature consistent with its known adduct-forming mechanism [PMID:27749842](../papers/27749842.md)
- Used in combination with etoposide (cisplatin/etoposide) as first-line chemotherapy in SCLC PDX models; 10/10 PDXs were sensitive to 6–8 cycles with 65–95% tumor growth inhibition; concurrent EZH2 inhibitor (EPZ011989) enhanced disease control and prevented SLFN11 suppression in SLFN11-high models [PMID:28196596](../papers/28196596.md).
- Adjuvant cisplatin/[carboplatin](../drugs/carboplatin.md) plus [vinorelbine](../drugs/vinorelbine.md) was the standard adjuvant chemotherapy backbone in the TRACERx NSCLC ctDNA study (NCT01888601, n=24 longitudinal patients). ctDNA clearance after adjuvant therapy correlated with sustained remission (CRUK0013, 688 days relapse-free), while rising ctDNA SNV burden during adjuvant therapy identified resistance in real time in patients who all recurred within 1 year. [PMID:28445469](../papers/28445469.md)
- Luminal-papillary MIBC (35% of TCGA bladder cohort, FGFR3-enriched) shows preliminary low likelihood of response to cisplatin-based neoadjuvant chemotherapy, while basal-squamous MIBC is proposed as appropriate for cisplatin-based regimens; etoposide-cisplatin is proposed for the neuronal subtype [PMID:28988769](../papers/28988769.md)
- In 295 metastatic EGC patients (MSK-IMPACT), HRD/LST scores did not predict PFS on first-line platinum-based chemotherapy (HR=0.99, P=0.947); MSI-H patients had significantly shorter PFS on cytotoxic therapy (4.8 vs 6.9 months, HR=0.4, P=0.027) [PMID:29122777](../papers/29122777.md)
- Pietzak et al. compared cisplatin-based neoadjuvant chemotherapy (NAC) outcomes in 288 MIBC patients: pathologic response 26% in secondary MIBC vs 45% in primary MIBC (OR=0.4, p=0.02); NAC was associated with worse CSS in secondary MIBC (p=0.002), and enrichment of [ERCC2](../genes/ERCC2.md) missense mutations in primary MIBC (12% vs 1.3%, p=0.004) provides a genomic explanation for differential cisplatin sensitivity [PMID:30290956](../papers/30290956.md).
- In a 3D cell culture review, cisplatin co-culture of ovarian cancer cell lines with fibroblasts in liquid-overlay spheroids increased cisplatin susceptibility, demonstrating stromal modulation of drug response; anchored-droplet microfluidic chips delivered IC50 measurements for cisplatin + etoposide combinations on Ewing sarcoma (A673) spheroids consistent with 96-well plates, with etoposide-first sequencing showing greater synergy [PMID:30643250](../papers/30643250.md).
- MSI-H UTUC PDX models (UCC17 MSI-H, UCC36 MSI-H Lynch) showed minimal gemcitabine/cisplatin inhibition (p=0.07) in contrast to MSS tumors; in a 20-patient NAC cohort, 0/2 MSI-H UTUC patients achieved pathologic response vs 10/17 MSS (59%), suggesting MSI status should redirect patients toward immunotherapy rather than cytotoxic NAC [PMID:32332851](../papers/32332851.md)
- Platinum agent used as part of first-line trastuzumab + pembrolizumab + fluoropyrimidine/platinum chemotherapy in NCT02954536; 37 HER2-positive metastatic esophagogastric cancer patients achieved 91% ORR and 27.2-month median OS [PMID:32437664](../papers/32437664.md).

## Resistance mechanisms

- Intratumoral bacteria in HNSCC identified as a source of resistance to cisplatin-containing chemoradiation in the Javelin HN100 expansion cohort analysis (GenRad). [PMID:41941260](../papers/41941260.md)

## Cancer types (linked)

- [HNSC](../cancer_types/HNSC.md) — head and neck squamous cell carcinoma; standard concurrent CRT agent; GenRad comparator arm.
- [CESC](../cancer_types/CESC.md) — cervical cancer; concurrent CRT backbone in the METEOR cohort.
- [ESCA](../cancer_types/ESCA.md), [STAD](../cancer_types/STAD.md) — HER2+ esophageal/gastric cancer; preclinical comparator context.
- [BLCA](../cancer_types/BLCA.md) — metastatic urothelial carcinoma; CALGB 90601 backbone cisplatin-based chemotherapy; DDR alteration predictive value not confirmed (underpowered). WashU WES cohort (n=32): cisplatin + [gemcitabine](../drugs/gemcitabine.md) reshapes clonal architecture and drives APOBEC mutagenesis.
- [OS](../cancer_types/OS.md) — osteosarcoma; MAP regimen component; organoid viability correlated with post-resection necrosis.
- [NSCLC](../cancer_types/NSCLC.md) — adjuvant cisplatin/carboplatin + vinorelbine backbone in TRACERx; ctDNA monitoring detected resistance and clearance in real time.

## Sources

- [PMID:41941260](../papers/41941260.md) — Gregucci et al. 2026, *Clin Cancer Res*. ROBIN white paper; cisplatin discussed as radiosensitizer reference and CRT backbone in GenRad HNSCC and METEOR cervical cohorts.
- [PMID:27698471](../papers/27698471.md)
- [PMID:30179230](../papers/30179230.md) — Grossberg et al. 2018, *Sci Data*. MD Anderson HNSCC imaging archive; cisplatin referenced as concurrent chemotherapy in 98% of the 127 chemo-treated patients (cohort-metadata only, no efficacy or biomarker claim).
- [PMID:39305899](../papers/39305899.md) — Al Shihabi et al. (Cell Stem Cell 2024). UCLA sarcoma PDTO biobank; MAP (methotrexate/doxorubicin/cisplatin) organoid viability correlated with post-resection necrosis in osteosarcoma.
- [PMID:39753968](../papers/39753968.md) — Varghese, Perry et al. (2024). MSK PDAC cohort; cisplatin referenced in chemotherapy background context.
- [PMID:40256659](../papers/40256659.md) — Guercio et al. (2025). CALGB 90601 cfDNA study; cisplatin-based chemotherapy backbone; DDR predictive value null (underpowered); VAF and TERT/PIK3CA/ERBB2 as prognostic markers.

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36333289](../papers/36333289.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:36228155](../papers/36228155.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:21720365](../papers/21720365.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:19176454](../papers/19176454.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23619168](../papers/23619168.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:23636398](../papers/23636398.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24476821](../papers/24476821.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24798001](../papers/24798001.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:24952746](../papers/24952746.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25096233](../papers/25096233.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25526346](../papers/25526346.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25583476](../papers/25583476.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:25608663](../papers/25608663.md)

*This page was processed by **crosslinker** on **2026-05-14**.*
- [PMID:27346245](../papers/27346245.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:27442865](../papers/27442865.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:27646943](../papers/27646943.md)
- [PMID:27749842](../papers/27749842.md) — Faltas et al. 2016, *Nature Genetics*. WES of 72 UC tumors (32 patients); cisplatin + gemcitabine clonal evolution study; APOBEC3A enrichment and L1CAM/integrin clonal enrichment post-chemotherapy.

- [PMID:28445469](../papers/28445469.md) — Abbosh et al. 2017, *Nature*. TRACERx NSCLC ctDNA study; cisplatin/carboplatin + vinorelbine adjuvant chemotherapy; ctDNA clearance vs. resistance detected in real time.

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:28196596](../papers/28196596.md)

*This page was processed by **wiki-cli** on **2026-05-14**.*
- [PMID:28988769](../papers/28988769.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:29122777](../papers/29122777.md)

*This page was processed by **wiki-cli** on **2026-05-15**.*
- [PMID:30290956](../papers/30290956.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:30643250](../papers/30643250.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:32332851](../papers/32332851.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
- [PMID:32437664](../papers/32437664.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
