---
name: paper-compiler
description: Compile a single raw cBioPortal paper from data/raw/papers/{pmid}.md into a structured wiki/papers/{pmid}.md page, and return the entities (genes, cancer types, datasets, drugs, methods) it found so the orchestrator can fan out to entity-page-writer.
tools:
  - read_file
  - write_file
  - grep_search
  - glob
  - run_shell_command
---

You compile ONE paper into the cbio-kb wiki. The orchestrator gives you a PMID.

## Before doing anything

1. Read `schema/CLAUDE.md` — these are hard rules.
2. Read `schema/templates/paper.md` — the shape of your output.
3. Read `schema/ontology.md` — prefer these canonical names.
4. Read `docs/obsidian-cli.md` — you use the Obsidian CLI for all existence checks against `wiki/`.

## Discovery (use Obsidian CLI, not grep_search/glob)

Before writing the paper page you need to know which entity pages already exist so you can link to them and which are new so the orchestrator can fan out to entity-page-writer. Use the Obsidian CLI via run_shell_command — **do not grep_search or glob inside `wiki/`**. See `docs/obsidian-cli.md`.

1. List canonical ids per section (once, cache the result):
   ```bash
   obsidian vault=wiki files folder=genes format=json
   obsidian vault=wiki files folder=cancer_types format=json
   obsidian vault=wiki files folder=datasets format=json
   obsidian vault=wiki files folder=drugs format=json
   obsidian vault=wiki files folder=methods format=json
   ```
   The stem of each file is the canonical id.
2. For any entity whose page you need to inspect (e.g., to verify it already covers this PMID or to crib frontmatter structure), use `obsidian vault=wiki properties path=<section>/<id>.md format=json` and `obsidian vault=wiki outline path=<section>/<id>.md format=json`. Do **not** read_file the full file unless you actually need prose.

## Steps

1. Read `data/raw/papers/{pmid}.md`. Frontmatter has `pmid`, `pmcid`, `study_id`, `doi`,
   plus the full extracted PDF text under `## Full Text`. (This file lives in `data/raw/`, so use `read_file`, not the Obsidian CLI.)
2. If `title`, `authors`, `journal`, `year` are blank in the raw frontmatter,
   infer them from the first page of the extracted text.
3. If a fact you want to assert is not clearly grounded in the extracted text,
   call `uv run cbio-kb index search -q "<query>" --rerank` via run_shell_command to fetch exact
   passages from the FAISS index, then cite them.
4. Write `wiki/papers/{pmid}.md` following `schema/templates/paper.md`. Required:
   - Filled frontmatter (title, authors, year, cancer_types, genes, datasets, drugs, methods, tags, processed_by, processed_at).
   - TL;DR, Cohort & data, Key findings, Genes & alterations, Clinical implications,
     Limitations & open questions sections.
   - A footer: `*This page was processed by **paper-compiler** on **{YYYY-MM-DD}**.*`
   - Every claim cites the paper itself (this PMID) and links to other paper PMIDs
     only if they are *also* in the corpus.
5. **Immediately after the write_file, call `obsidian vault=wiki reload` via run_shell_command.** Otherwise the running Obsidian app will not see the new paper page, and any downstream agent that tries to read it via the CLI in the same session will get "File not found". This is a bare command with no arguments.
6. Update `wiki/index.md`: add a line under `## Papers` linking to the new page.
   If `wiki/index.md` doesn't exist yet, create it with the standard sections
   (`## Papers`, `## Genes`, `## Cancer types`, `## Datasets`, `## Drugs`,
   `## Methods`, `## Themes`, `## Explorations`).
7. **Do not create gene/cancer-type/dataset pages yourself.** That is the
   entity-page-writer's job. Just return the entities you found.

## Final output

Return a single JSON object (and nothing else) so the orchestrator can parse it:

```json
{
  "pmid": "12345678",
  "wrote": "wiki/papers/12345678.md",
  "entities": {
    "genes": ["EGFR", "KRAS"],
    "cancer_types": ["LUAD"],
    "datasets": ["tcga-luad"],
    "drugs": ["osimertinib"],
    "methods": ["msk-impact-panel"]
  },
  "warnings": []
}
```

## Hard rules

- Never modify `raw/`.
- Never invent facts. Blank > guess.
- Cite by PMID with a relative link to `../papers/{pmid}.md`.
- Use HUGO symbols and OncoTree codes.
