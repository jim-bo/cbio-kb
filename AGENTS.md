# cbio-kb Agents

This repository uses specialized sub-agents to maintain the knowledge base. To ensure compatibility with both Claude and Gemini CLI, agents are defined in two parallel directories.

## Agent Directories

- **`.claude/agents/`**: Definitions for Claude Code (YAML frontmatter with `Read`, `Edit`, `Bash` etc.).
- **`.gemini/agents/`**: Definitions for Gemini CLI (YAML frontmatter with `read_file`, `replace`, `run_shell_command` etc.).

## Synchronization Strategy

The **Markdown body** (System Prompt) of the agents should be kept identical. Only the YAML frontmatter differs in its `tools` definitions.

| Claude Tool | Gemini CLI Tool |
| :--- | :--- |
| `Read` | `read_file` |
| `Write` | `write_file` |
| `Edit` | `replace` |
| `Grep` | `grep_search` |
| `Glob` | `glob` |
| `Bash` | `run_shell_command` |

### How to update an agent

1.  Modify the instructions in the `.claude/agents/{name}.md` file.
2.  Copy the updated Markdown body to the matching `.gemini/agents/{name}.md` file.
3.  Ensure the `tools` list in the Gemini file uses the names in the table above.

## Tool Execution

All Python-based CLI tools (`cbio-kb`) must be executed using `uv run`. 

Example:
`uv run cbio-kb ontology lookup "KRAS"`

## Wiki CLI (token-efficient wiki access)

When the target lives in `wiki/`, prefer `uv run cbio-kb wiki <cmd>` over `Read` / `Grep` / `Glob`. It returns structured JSON and costs a fraction of the tokens. Full command reference: `uv run cbio-kb wiki --help`.

High-value substitutions:

| Task | Old | New |
| :-- | :-- | :-- |
| Paper structure | `Read wiki/papers/{pmid}.md` | `uv run cbio-kb wiki outline --path papers/{pmid}.md` |
| Frontmatter only | Read + parse | `uv run cbio-kb wiki properties --path papers/{pmid}.md` |
| Entity mentions with context | `Grep -C 3 EGFR wiki/` | `uv run cbio-kb wiki search-context --query EGFR --limit 20` |
| Pages citing an entity | `Grep '\[\[EGFR\]\]' wiki/` | `uv run cbio-kb wiki backlinks --file EGFR` |
| Unresolved / orphan lint checks | custom walk | `uv run cbio-kb wiki unresolved` / `orphans` / `deadends` |

Rules:
- Only for `wiki/` content — `data/raw/`, `schema/`, `.claude/`, and code still use Read / Grep / Glob.
- CLI is **read-only**. All edits still go through `Edit` / `Write` so diffs land in git.
- Paths are vault-relative (`papers/39506116.md`, not `wiki/papers/39506116.md`).
- **Narrow Reads for merge-append.** The `Edit` tool requires a prior `Read` on the same file. For large entity pages, use `uv run cbio-kb wiki outline --path …` to find the section line, then `Read offset=<line> limit=<slice_size>` for just that section — not a full-file Read.

## Available Agents

- **`paper-compiler`**: Ingests raw papers into the wiki.
- **`entity-page-writer`**: Creates/updates gene, cancer type, and drug pages.
- **`crosslinker`**: Rewrites entity mentions as internal wiki links.
- **`wiki-linter`**: Audits the wiki for structural issues.
- **`wiki-querier`**: Answers questions using the wiki and FAISS index.
- **`theme-synthesizer`**: Identifies cross-cutting research themes.

## Workflows

The **main loop** (Claude Code or Gemini CLI) is the orchestrator. Sub-agents are dispatched for discrete tasks; the orchestrator owns cross-cutting state (notably `wiki/index.md`).

### Adding one paper

1. Drop the PDF into `data/raw/pdfs/`.
2. `uv run cbio-kb ingest extract` — idempotent; writes `data/raw/papers/{pmid}.md`.
3. Dispatch **paper-compiler** with the PMID. It writes `wiki/papers/{pmid}.md` and returns the entity lists (genes, cancer_types, datasets, drugs, methods).
4. For each entity kind with new/touched entries, dispatch **entity-page-writer** once with the entity→[PMID] mapping.
5. Dispatch **crosslinker** over the new paper page plus any entity pages touched in step 4.
6. `uv run cbio-kb wiki build-index` — deterministic, regenerates `wiki/index.md` from `schema/templates/index.md`.
7. `uv run cbio-kb lint --wiki-dir wiki` and fix any structural errors.
8. Commit.

### Adding a batch of N papers

1. Drop PDFs into `data/raw/pdfs/`; run `ingest extract` once.
2. Dispatch **paper-compiler** in parallel waves of ~5 PMIDs. On 529 overloads, retry failed PMIDs sequentially — do not abandon the wave.
3. Collect all returned entity lists and invert to `{entity_kind: {entity: [pmids...]}}` with a Python one-liner.
4. Fan out **entity-page-writer** once per kind. Shard `genes` into alphabetical buckets of ~20 to keep prompts tight.
5. Single **crosslinker** pass over the new papers + all touched entity pages (pin to `haiku`).
6. `uv run cbio-kb wiki build-index` — deterministic, regenerates `wiki/index.md` from template.
7. `cbio-kb lint`; optionally `cbio-kb ontology sync` if new studies/panels appeared.
8. Commit per wave, not per paper.

### Reprocessing after ontology or template changes

Not every change requires a full recompilation. Three tiers:

| Tier | What changed | Command | Cost |
|---|---|---|---|
| **1 — Frontmatter** | New/renamed fields in a template | `uv run cbio-kb wiki reprocess-frontmatter [--sections papers,genes] [--dry-run]` | Zero (deterministic Python) |
| **2 — Delta extraction** | Expanded ontology (e.g. added `drugs` field) | `uv run cbio-kb wiki reprocess-extract [--prompts]` | Low (sonnet, targeted) |
| **3 — Full recompile** | Template structure or extraction quality overhaul | Re-dispatch `paper-compiler` per paper | High (opus, full) |

**Tier 1** adds missing frontmatter keys, removes stale ones, and reorders to match the template. Run `--dry-run` first.

**Tier 2** scans paper pages for empty entity-list fields that raw text could fill. Without `--prompts`, emits a JSON manifest. With `--prompts`, emits ready-to-dispatch agent prompts for delta extraction (one per paper, sonnet-level, frontmatter-only edits).

**Tier 3** is a full re-dispatch of paper-compiler. Only needed when the template structure or extraction approach fundamentally changes.

### Rules of thumb

- **Model pinning**: `crosslinker` and `wiki-linter` → `haiku` (mechanical). `paper-compiler`, `theme-synthesizer`, and `wiki-querier` → `opus` (reasoning). `entity-page-writer` → `sonnet` (bounded extraction).
- **Index generation**: no agent edits `wiki/index.md`. Run `uv run cbio-kb wiki build-index` once at the end — it reads `schema/templates/index.md` and fills section counts + entity links from disk.
- **Rerun semantics**: `paper-compiler` overwrites `wiki/papers/{pmid}.md` via Write (idempotent rerun OK); `entity-page-writer` merges via Edit (append-only, idempotent by PMID dedup).
- **Ontology discipline**: never invent a HUGO symbol, OncoTree code, or cBioPortal `studyId`. Unverified terms go to `schema/ontology/_observed.md`, not into canonical pages as if they were official.
- **Provenance**: every entity page must carry `processed_by` / `processed_at` frontmatter and an italicized footer naming the agent that last touched it.
