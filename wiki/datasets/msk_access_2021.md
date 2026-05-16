---
name: MSK-ACCESS Pan-Cancer cfDNA Clinical Cohort (MSK, Nat Commun 2021)
studyId: msk_access_2021
institution: Memorial Sloan Kettering Cancer Center
size: 617
reference_genome: GRCh37
canonical_source: cbioportal
unverified: false
assays:
  - msk-access
  - msk-impact-panel
panels:
  - ACCESS129
  - IMPACT468
tags:
  - liquid-biopsy
  - cfDNA
  - ctDNA
  - pan-cancer
  - matched-normal-sequencing
  - clonal-hematopoiesis
  - umi-consensus-sequencing
  - analytical-validation
processed_by: entity-page-writer
processed_at: 2026-05-16
---

# MSK-ACCESS Pan-Cancer cfDNA Clinical Cohort (MSK, Nat Commun 2021)

## Overview

Prospective clinical cohort generated during the analytical validation and initial deployment of MSK-ACCESS, a 129-gene hybrid-capture next-generation sequencing assay for plasma cell-free DNA (cfDNA). The assay pairs ultra-deep sequencing (~20,000× raw / ~1,100× duplex consensus after UMI-based error correction) of cfDNA with matched white blood cell (WBC) sequencing to call SNVs, indels, copy-number alterations, and structural variants. After New York State Department of Health approval on 31 May 2019, the assay was used to prospectively profile 681 blood samples from 617 patients across 31 tumor types at MSKCC under IRB protocol NCT01775072. The 129 genes / 826 exons were selected so that at least one non-synonymous mutation would be captured in 84% of 25,000 previously MSK-IMPACT-sequenced solid tumors. [PMID:34145282](../papers/34145282.md)

## Composition

- 681 plasma samples from 617 unique patients (99% QC pass from 687 accessioned).
- Top tumor types: [NSCLC](../cancer_types/NSCLC.md) (n=349, 51%); [PRAD](../cancer_types/PRAD.md), [BLCA](../cancer_types/BLCA.md), [PAAD](../cancer_types/PAAD.md), and biliary cancer (collectively 28%); 31 distinct tumor types overall.
- Concordance cohort: 383/617 patients with matched MSK-IMPACT tumor tissue (520 sequenced tissues; 1,206 mutations in overlapping target regions).
- Validation cohorts: 47 healthy-donor plasma + matched WBC samples for background-error/specificity assessment; 70 cfDNA samples with 100 orthogonally validated SNVs/indels (VAF range 0.1–73%) for accuracy.
- Reference genome: GRCh37. [PMID:34145282](../papers/34145282.md)

## Assays / panels (linked)

- [MSK-ACCESS](../methods/msk-access.md) / [ACCESS129](../methods/ACCESS129.md) — 129-gene, 826-exon hybrid-capture cfDNA panel; mean raw coverage 18,264× (plasma); mean duplex consensus coverage 1,497×; error rate suppressed from 3.3×10^-4 (standard BAM) to 1.7×10^-6 (duplex).
- Matched WBC sequencing to remove germline and clonal-hematopoiesis (CH) variants.
- Tissue comparator: [MSK-IMPACT](../methods/msk-impact-panel.md) / [IMPACT468](../methods/IMPACT468.md).
- Sequencing on Illumina HiSeq 2500 or NovaSeq 6000; alignment with [BWA](../methods/bwa.md) MEM + ABRA2; [GATK](../methods/gatk.md) preprocessing; UMI-based consensus with Marianas; SNV/indel calling with [MuTect](../methods/mutect.md) and [VarDict](../methods/vardict.md); SVs with Manta; copy-number via [FACETS](../methods/facets.md)-derived method; actionability via [OncoKB](../methods/oncokb.md); workflow in CWL/toil. [PMID:34145282](../papers/34145282.md)

## Papers using this cohort

- [PMID:34145282](../papers/34145282.md) — Brannon et al., *Nat Commun* 2021: MSK-ACCESS clinical validation and prospective deployment; 73% (498/681) of samples had ≥1 alteration; 41% (278/681) carried an OncoKB level 1–3B actionable alteration; matched WBC sequencing removed >10,000 germline and CH variants; tissue-plasma concordance was 59% for mutations in overlapping regions, inversely correlated with tissue-to-blood collection interval (median ΔDOP 65 weeks). [PMID:34145282](../papers/34145282.md)

## Notable findings derived from this cohort

- 73% (498/681) of prospective samples had ≥1 detectable alteration; non-zero median 3 alterations/patient (range 1–28); 1,697 SNVs/indels in 486 samples (median VAF 1.9%). [PMID:34145282](../papers/34145282.md)
- 41% (278/681) of samples carried an OncoKB level 1–3B actionable alteration; level 1 actionable variant yields: [BLCA](../cancer_types/BLCA.md) 48%, [BRCA](../cancer_types/BRCA.md) 37%, [NSCLC](../cancer_types/NSCLC.md) 33%. [PMID:34145282](../papers/34145282.md)
- Analytical accuracy: 92% de novo sensitivity at ≥0.5% VAF (95% CI 84–96.5%); ≥99.7% specificity; PPA 94% / NPA 99.7% (genotyping). [PMID:34145282](../papers/34145282.md)
- Matched WBC sequencing removed >10,000 germline + CH variants that plasma-only calling would have missed; VAF-based germline filtering alone would have mis-removed 70 verified somatic mutations including 15 actionable. [PMID:34145282](../papers/34145282.md)
- Plasma-only 95% (1,606/1,697) SNVs/indels called de novo without prior tissue; 91 rescued by genotyping (median VAF 0.08%). [PMID:34145282](../papers/34145282.md)
- For patients without MSK-IMPACT (n=234), MSK-ACCESS detected actionable mutations in 26% (61/234). [PMID:34145282](../papers/34145282.md)
- Fragment-length analysis: confirmed tumor-derived cfDNA fragments significantly shorter than wild-type (bootstrap p<0.0001); enabled reclassification of CH variants (e.g., KRAS p.G12S at 0.44% VAF in lung adenocarcinoma reassigned to CH). [PMID:34145282](../papers/34145282.md)
- [FGFR2](../genes/FGFR2.md) mutations and fusions (predominantly FGFR2-BICC1) detected in 8/24 intrahepatic cholangiocarcinomas with detectable ctDNA; FGFR3 resistance mutations detected in FGFR3-TACC3 bladder cancers during FGFR-inhibitor treatment. [PMID:34145282](../papers/34145282.md)

## Sources

- cBioPortal study `msk_access_2021`.
- Brannon AR, et al. *Enhanced specificity of clinical high-sensitivity tumor mutation profiling in cell-free DNA via paired normal sequencing using MSK-ACCESS.* Nat Commun. 2021. [PMID:34145282](../papers/34145282.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
