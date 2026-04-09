# cbio-kb

Agent-maintained knowledge base over cBioPortal publications. A Karpathy-style
LLM wiki: drop papers into `data/raw/pdfs/`, run the pipeline, and sub-agents
compile them into an interlinked Markdown wiki under `wiki/` that you browse in
Obsidian.

Two things live in this repo:

1. **`cbio-kb` CLI + package** (`src/cbio_kb/`) — deterministic tooling for
   ingesting PDFs, building a FAISS passage index, linting the wiki, and
   exporting agent session transcripts. No LLM calls.
2. **The wiki** (`wiki/`) — an Obsidian vault maintained by the sub-agents
   defined under `.claude/agents/` and `.gemini/agents/`.

## Install

```bash
uv sync                 # runtime deps only
uv sync --extra dev     # + pytest
uv sync --extra server  # + FAISS/sentence-transformers for the MCP server
```

The `cbio-kb` entry point is installed into the venv:

```bash
uv run cbio-kb --help
```

## Browse the wiki in Obsidian

```bash
git clone <this repo>
# Open Obsidian → "Open folder as vault" → select wiki/
```

The `wiki/` directory is the Obsidian vault. Schema files are reachable from
inside the vault via the symlinked `wiki/_schema/` folder. Windows users need
`git config --global core.symlinks true` before cloning.

## Pipeline (rebuild from scratch)

All artifacts land under `data/`, which is gitignored. Only `data/seed/` is
committed.

```bash
# 1. PMIDs → PMCIDs
uv run cbio-kb ingest resolve

# 2. Download PDFs from PMC
uv run cbio-kb ingest pdfs --email you@example.org

# 3. Extract text → data/raw/papers/{pmid}.md
uv run cbio-kb ingest extract

# 4. Build FAISS passage index
uv run cbio-kb index build

# 5. Search (sanity check)
uv run cbio-kb index search -q "KRAS G12C in lung cancer" --rerank
```

## Wiki maintenance (agent-driven)

See [AGENTS.md](./AGENTS.md) for the runbook. Core flow per paper:

1. `uv run cbio-kb ingest extract` to produce `data/raw/papers/{pmid}.md`.
2. Dispatch the `paper-compiler` agent → writes `wiki/papers/{pmid}.md`.
3. Dispatch `entity-page-writer` for each entity kind.
4. `uv run cbio-kb crosslink` (deterministic, no LLM).
5. `uv run cbio-kb lint` and commit.

## MCP server

```bash
uv run cbio-kb serve --host localhost --port 8123
# or
docker build -t cbio-kb . && docker run -p 8123:8123 cbio-kb
```

## Layout

```
src/cbio_kb/        Python package
  cli.py            single entry point
  ingest/           PDF → Markdown pipeline
  index/            FAISS semantic search
  ontology/         cBioPortal + OncoTree validation
  wiki/             crosslinker, linter, fts
  logs/             session transcript stitcher
  server/           MCP server
wiki/               Obsidian vault (papers, genes, cancer_types, …)
schema/             ontology + page templates (symlinked into wiki/_schema)
.claude/agents/     Claude Code agent specs
.gemini/agents/     Gemini CLI agent specs
tests/              pytest suite
data/               local artifacts (gitignored)
  seed/             committed seed CSVs
```

## License

MIT
