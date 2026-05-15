---
name: MET500 — Michigan Oncology Sequencing Metastatic Solid Tumors 2017 (Robinson et al.)
studyId: metastatic_solid_tumors_mich_2017
institution: University of Michigan (Michigan Oncology Sequencing / Mi-Oncoseq program)
size: 500
reference_genome: GRCh37/hg19
canonical_source: cbioportal
unverified: false
assays:
  - whole-exome-seq
  - rna-seq
  - tcr-seq
panels: []
tags:
  - metastatic
  - pan-cancer
  - MET500
  - germline
  - immune
  - RNA-seq
  - fusion
processed_by: entity-page-writer
processed_at: 2026-05-15
---

# MET500 — Michigan Oncology Sequencing Metastatic Solid Tumors 2017 (Robinson et al.)

## Overview

The MET500 cohort (also referred to as `metastatic_solid_tumors_mich_2017` in cBioPortal) is a pan-cancer prospective cohort of 500 adult patients with metastatic solid tumors of diverse lineage and biopsy site, assembled under the Michigan Oncology Sequencing (Mi-Oncoseq) program. Robinson et al. performed paired tumor/normal whole-exome sequencing and poly(A)+/exome-capture transcriptomics alongside T-cell receptor β CDR3 deep sequencing to characterize the somatic, germline, fusion, and immune landscape of metastatic disease. The study established that metastatic tumors carry a higher mutation burden than matched primary cohorts, identified putative pathogenic germline variants in 12.2% of cases (75% in DNA-repair genes), and defined two transcriptional metastatic subtypes (EMT-like vs proliferative). Sequencing data are deposited in dbGaP (phs000673.v2.p1); data also accessible via the MET500 web portal (met500.path.med.umich.edu) [PMID:28783718](../papers/28783718.md).

## Composition

- **Total:** 500 adult patients (537 biopsies / 556 enrolled; 93% complete-sequencing success rate); 258 male / 242 female; 460 (92%) Caucasian; median age 59 years (range 18–86).
- **Cancer types (n=20):** Top three — 93 (18.6%) metastatic prostate ([PRAD](../cancer_types/PRAD.md)), 91 (18.2%) metastatic breast ([BRCA](../cancer_types/BRCA.md)), 42 (8.4%) soft-tissue sarcoma ([SARCNOS](../cancer_types/SARCNOS.md)); overall lineage [MIXED](../cancer_types/MIXED.md).
- **Biopsy sites (>30 organs):** 134 liver, 114 lymph node, 46 lung, 42 bone, 32 abdominal mass/ascites/pleural fluid.
- **Exome assay:** Agilent SureSelect Human All Exon v4; mean target coverage 180× tumor / 120× normal; mean tumor content 62%.
- **RNA-seq:** poly(A)+ and exome-capture on Illumina HiSeq 2000/2500 (40–50M paired reads); 868 transcriptome libraries from 496 tumors.
- **TCR-seq:** T-cell receptor β CDR3 via Adaptive Biotechnologies immunoSEQ.
- **Bioinformatics:** alignment to GRCh37/hg19 via Novoalign; SNV calling by [VarScan2](../methods/varscan.md) v2.3.2; indels by [Pindel](../methods/pindel.md); fusion calling via CODAC pipeline; RNA alignment by [STAR](../methods/star.md) to GRCh38/Gencode V23 (custom transcript reference) [PMID:28783718](../papers/28783718.md).

## Assays / panels (linked)

- [whole-exome-seq](../methods/whole-exome-seq.md)
- [rna-seq](../methods/rna-seq.md)
- [tcr-seq](../methods/tcr-seq.md)
- [varscan](../methods/varscan.md)
- [pindel](../methods/pindel.md)
- [star](../methods/star.md)
- [annovar](../methods/annovar.md)

## Papers using this cohort

- [PMID:28783718](../papers/28783718.md) — Robinson et al. 2017; inaugural description of the MET500 pan-cancer metastatic cohort (500 patients; WES + RNA-seq + TCR-seq).

## Notable findings derived from this cohort

- Mean of 119 somatic mutations per patient within targeted exome regions; mutation burden significantly elevated vs TCGA primaries for most cancer types, with the largest increase in tumor types with low primary-stage mutation burden (e.g., prostate, adrenal) [PMID:28783718](../papers/28783718.md).
- Most-altered tumor suppressors: [TP53](../genes/TP53.md) 266/500 (53.2%), [CDKN2A](../genes/CDKN2A.md) 80 (16%), [PTEN](../genes/PTEN.md) 79 (15.8%), [RB1](../genes/RB1.md) 68 (13.6%); most-altered oncogenes: [PIK3CA](../genes/PIK3CA.md) 67 (13.4%), [AR](../genes/AR.md) 63 (12.6%), [KRAS](../genes/KRAS.md) 51 (10.2%) [PMID:28783718](../papers/28783718.md).
- Presumed pathogenic germline mutations (PPGM) in 12.2% of patients (61 individuals / 18 genes); 75% in DNA-repair genes — [MUTYH](../genes/MUTYH.md) n=10 (16%), [BRCA2](../genes/BRCA2.md) n=9 (14%), [CHEK2](../genes/CHEK2.md) n=9 (14%), [BRCA1](../genes/BRCA1.md) n=5 (8%); PPGM odds significantly elevated vs ExAC controls (OR=3.00, 95% CI 2.28–3.9, P=1×10⁻¹³) [PMID:28783718](../papers/28783718.md).
- 199/496 tumors (39.8%) carried at least one putative pathogenic gene fusion; 12,027 unique fused gene pairs (mean 34/tumor); novel activating [ALK](../genes/ALK.md), [BRAF](../genes/BRAF.md), and FGFR fusions with new partners [PMID:28783718](../papers/28783718.md).
- Two transcriptional metastatic subtypes: EMT-like (inflammation signatures) and proliferative (metabolism and stress response); subtype assignments only weakly tied to biopsy site or primary tissue; metastatic samples showed significant tissue-marker dedifferentiation vs normal/primary [PMID:28783718](../papers/28783718.md).
- RNA-seq-derived MImmScore (141 ESTIMATE immune-signature genes) correlated with TCR-β CDR3 sequencing; cancer types known to be infiltrated in localized stage (kidney, lung, melanoma) remained infiltrated at metastatic sites; composite "fully active" immune classification (TIL-5 + APC-1 + Tcell-1 cluster) correlated with PD-L1, HLA, granzyme expression, and a melanoma-derived clinical-response score [PMID:28783718](../papers/28783718.md).
- Note: cBioPortal study `metastatic_solid_tumors_mich_2017` uses GRCh37/hg19 for DNA; RNA processed against GRCh38 with custom MOTR/Gencode V23 transcript reference [PMID:28783718](../papers/28783718.md).

## Sources

- Robinson DR, Wu YM, Lonigro RJ, et al. Integrative clinical genomics of metastatic cancer. *Nature.* 2017;548(7667):297-303. [PMID:28783718](../papers/28783718.md)

*This page was processed by **entity-page-writer** on **2026-05-15**.*
