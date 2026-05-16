---
name: CWL + Docker Workflow
slug: cwl-docker-workflow
kind: method
canonical_source: corpus
unverified: true
tags: [workflow, reproducibility, containerization, pipeline]
processed_by: wiki-cli
processed_at: 2026-05-16
---

# CWL + Docker Workflow

## Overview

A workflow management approach that combines Common Workflow Language (CWL) for portable pipeline specification with Docker containers for reproducible execution environments. CWL describes tool inputs, outputs, and computational steps in a language-agnostic YAML/JSON format; Docker encapsulates software dependencies into isolated images. Together, they enable cloud-platform-independent reproducibility of bioinformatics pipelines.

## Used by

- The TCGA MC3 somatic calling pipeline was distributed as a CWL + Docker workflow at https://github.com/OpenGenomics/mc3, enabling reproducible execution of the seven-caller ensemble across DNAnexus and other cloud platforms [PMID:29596782](../papers/29596782.md)
- Common Workflow Language (CWL) and Docker-containerized pipelines described as the emerging reproducible stack for cloud-based biomedical analysis; NCI cancer-genomics cloud pilots expose >200 CWL/WDL tools for TCGA reanalysis [PMID:29902176](../papers/29902176.md)
- MSK-ACCESS bioinformatics pipeline executed using CWL (Common Workflow Language) with toil workflow engine and Docker containerization; enabled reproducible, scalable processing of 681 prospective plasma samples [PMID:34145282](../papers/34145282.md)
- Used for pipeline execution of the MSK-ACCESS bioinformatics workflow in the cf-IMPACT/ACCESS tumor-fraction-guided cfDNA triage study [PMID:34059130](../papers/34059130.md)

## Notes

- CWL workflows are portable across compliant executors (cwltool, Toil, Cromwell, etc.) and cloud platforms (AWS, GCP, Azure, DNAnexus).
- Docker container versioning is critical for reproducibility; pinning image digests (not just tags) is recommended.
- The MC3 CWL release was intended as a reference implementation to enable other groups to replicate or extend the pipeline.

## Sources

*This page was processed by **entity-page-writer** on **2026-05-15**.*
- [PMID:29902176](../papers/29902176.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:34145282](../papers/34145282.md)

*This page was processed by **wiki-cli** on **2026-05-16**.*
- [PMID:34059130](../papers/34059130.md)

*This page was processed by **entity-page-writer** on **2026-05-16**.*
