# Idea: Package cbio-kb as a Claude Code Plugin

Expose the 6 subagents + wiki workflow as an installable plugin so others can run the same loop on their own knowledge bases.

## How Claude Code plugins work

- A plugin is a directory with `.claude-plugin/plugin.json` (manifest) plus optional subdirs:
  - `commands/` — slash commands
  - `agents/` — subagent `.md` files (with YAML frontmatter declaring tools)
  - `skills/` — skill `.md` files (auto-invoke when description matches context)
  - `hooks/` — event-triggered shell hooks
  - `.mcp.json` — MCP server configs
- Distributed via git URL (`/plugin install <repo>`) or a marketplace registry. No centralized package manager yet beyond the [official registry](https://github.com/anthropics/claude-plugins-official).
- Always-on once installed for the session — no per-project enable step.
- Plugins **cannot** bundle executables. Any CLI dependency must be installed separately.

Docs: https://code.claude.com/docs/en/plugins

## Proposed layout

```
cbio-kb-plugin/
├── .claude-plugin/plugin.json
├── agents/              # copies of .claude/agents/*.md (paper-compiler, entity-page-writer,
│                        #   crosslinker, wiki-linter, wiki-querier, theme-synthesizer)
├── commands/
│   ├── cbio-init.md     # scaffolds wiki/, schema/templates/, data/raw/
│   ├── cbio-add-paper.md
│   └── cbio-add-batch.md
├── skills/
│   └── cbio-kb.md       # high-level trigger: "this repo manages a paper-based KB"
└── README.md            # install steps incl. `uv tool install cbio-kb`
```

## Gotchas to design around

1. **CLI not bundled.** `cbio-kb` ships separately via `uv tool install`. README must call this out; plugin agents/commands assume it's on PATH.
2. **No directory scaffolding from plugins.** The opinionated `wiki/` + `schema/templates/` + `data/raw/` layout has to be created by a `/cbio-init` slash command (or a `cbio-kb init` subcommand the slash command wraps).
3. **Skill auto-invocation needs a sharp description.** The top-level `skills/cbio-kb.md` description determines when Claude reaches for this workflow vs. ignoring it.
4. **Agent frontmatter must list tools explicitly.** Already true in `.claude/agents/` — copy as-is.
5. **Gemini parity drifts.** Today `.claude/agents/` and `.gemini/agents/` are kept in sync manually. A plugin only covers the Claude side; if Gemini CLI users matter, that's a second distribution channel.

## Open questions

- Does `cbio-kb init` belong in the existing Python package, or should the plugin's slash command emit the scaffolding inline?
- Templates in `schema/templates/` — ship inside the plugin (`commands/cbio-init.md` writes them) or have `cbio-kb init` pull them from the installed package's data files? Latter is cleaner for updates.
- Index/graph builds (`build-index`, `build-graph`) — wire as a `Stop` hook so they run automatically after a paper is added? Or keep manual per current workflow?
