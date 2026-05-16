---
name: MSK Clonal Hematopoiesis in Cancer Patients (2020)
studyId: msk_ch_2020
institution: Memorial Sloan Kettering Cancer Center
size: 24146
reference_genome: hg19
canonical_source: cbioportal
unverified: false
assays:
  - msk-impact-panel
panels:
  - IMPACT341
  - IMPACT410
  - IMPACT468
tags:
  - clonal-hematopoiesis
  - chip
  - tmn
  - therapy-related
  - solid-tumor
  - cross-sectional
processed_by: crosslinker
processed_at: 2026-05-16
---

# MSK Clonal Hematopoiesis in Cancer Patients (2020)

## Overview

Cross-sectional cohort of 24,146 cancer patients with matched tumor and blood MSK-IMPACT sequencing on protocol NCT01775072 (prior to July 1, 2018), representing 56 primary tumor types. Clonal hematopoiesis (CH) was defined as a blood-only variant at VAF ≥2% with ≥10 supporting reads. The dataset also includes a treatment-annotated subcohort (n=10,138), a serial-sampling subcohort (n=525; median interval 23 months), a CH-to-therapy-related myeloid neoplasm (tMN) transition cohort (n=35 paired pre/post-tMN samples), and a pooled tMN risk cohort (n=9,437). Reference genome hg19. Data released on cBioPortal as `msk_ch_2020`.

## Composition

- Cross-sectional cohort: 24,146 cancer patients (56 tumor types); 7,216 (30%) harbored ≥1 CH mutation.
- Treatment-annotated subcohort: 10,138 patients; 5,978 (59%) with prior cancer therapy, 4,160 (41%) treatment-naive.
- Serial-sampling cohort: 525 patients with ≥2 blood draws (median 23 months interval); 95% CH mutations stable between draws.
- CH→tMN cohort: 35 paired pre-tMN and tMN samples (median interval 24 months, range 5–90).
- Pooled tMN risk cohort: 9,437 therapy-exposed cancer patients (MSK + collaborating institutions); 75 developed tMN.
- AML/MDS risk reference: Abelson PMC (n=969) + Young WSU (n=103) healthy-individual panels.

## Assays / panels (linked)

- [MSK-IMPACT](../methods/msk-impact-panel.md): [IMPACT341](../methods/IMPACT341.md), [IMPACT410](../methods/IMPACT410.md), [IMPACT468](../methods/IMPACT468.md); median blood coverage 497×, tumor 790×
- Serial CH testing: 163-gene myeloid capture panel (median depth 665×)
- Alignment: [BWA](../methods/bwa.md) 0.7.5a → ABRA 0.92 → [GATK](../methods/gatk.md) 3.3-0
- SNV calling: [MuTect](../methods/mutect.md) + [VarDict](../methods/vardict.md) (retained if called by both)
- Annotation: [VEP](../methods/vep.md) v86 and [OncoKB](../methods/oncokb.md)
- Selection inference: [dNdScv](../methods/dndscv.md); absolute-risk modeling: [iCARE](../methods/icare.md)

## Papers using this cohort

- [PMID:33106634](../papers/33106634.md) — Bolton et al. 2020, Nat Genet: "Cancer therapy shapes the fitness landscape of clonal hematopoiesis"

## Notable findings derived from this cohort

- 7,216/24,146 patients (30%) harbored ≥1 CH mutation (VAF ≥2%); most frequent genes were [DNMT3A](../genes/DNMT3A.md), [TET2](../genes/TET2.md), and [ASXL1](../genes/ASXL1.md) — [PMID:33106634](../papers/33106634.md)
- DDR-gene CH ([TP53](../genes/TP53.md), [PPM1D](../genes/PPM1D.md), [CHEK2](../genes/CHEK2.md)) strongly therapy-associated; PPM1D (OR=4.3, q<10⁻⁶) most enriched in ovarian (13%) and endometrial (7%) cancer patients — [PMID:33106634](../papers/33106634.md)
- Carboplatin most strongly associated with CH (OR=1.4, p=0.001); external-beam radiation (OR=1.4, p<10⁻⁶); targeted therapy and immunotherapy showed no significant CH association — [PMID:33106634](../papers/33106634.md)
- CH VAF >2% increased tMN risk HR=6.9 (p<10⁻⁶); TP53 and spliceosome genes ([SRSF2](../genes/SRSF2.md), [U2AF1](../genes/U2AF1.md), [SF3B1](../genes/SF3B1.md)) had strongest gene-specific tMN hazard ratios — [PMID:33106634](../papers/33106634.md)
- In 34 patients with paired DDR-CH and non-DDR-CH clones, DDR clones outgrew non-DDR under cytotoxic/radiation therapy but were outcompeted by DNMT3A-class clones in untreated patients — [PMID:33106634](../papers/33106634.md)
- 59% of CH→tMN paired samples showed ≥1 leukemia-defining mutation already present at the CH timepoint; 40% of tMN cases carried TP53 mutations, 10/14 detectable at CH stage — [PMID:33106634](../papers/33106634.md)

## Sources

- [PMID:33106634](../papers/33106634.md)
- cBioPortal study: `msk_ch_2020`
- Clinical trial: NCT01775072

*This page was processed by **crosslinker** on **2026-05-16**.*
