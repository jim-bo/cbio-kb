# Token-Efficient Ingestion Patterns

This document outlines strategies for scaling the `cbio-kb` ingestion process while minimizing token consumption and maintaining high architectural quality.

## 1. Findings Manifest Pattern (Primary Optimization)

**Problem**: Passing the full text of a paper to multiple specialized sub-agents (Gene Writer, Drug Writer, etc.) creates redundant token costs.

**Solution**:
- The `paper-compiler` should output a **Structured Findings Manifest** (JSON).
- Format: `{ "entities": { "EGFR": "Found in 45% of GBM cases...", "TP53": "Altered in 78% of cases..." } }`.
- Sub-agents only receive the specific snippet relevant to their target entity.

## 2. Surgical Section Access

**Problem**: Reading entire 500+ line entity pages to perform a small append to one section.

**Solution**:
- Use `uv run cbio-kb wiki outline --path <path>` to find section boundaries.
- Use `read_file` with `start_line` and `end_line` to read only the target section.
- This reduces the context overhead for the `entity-page-writer` by an order of magnitude.

## 3. Delegation via Sub-Orchestrators

**Problem**: The main orchestrator's history compounds with every turn, making long sessions exponentially more expensive.

**Solution**:
- Create a "Vault Manager" sub-agent.
- The main orchestrator makes a single call: "Update the vault using this manifest."
- The Vault Manager handles the iterative updates. The main session history only sees one tool result instead of 15.

## 4. Entity Batching logic

**Problem**: Tool-call overhead and system prompt repetition for single-entity categories (e.g., one drug).

**Solution**:
- **Shard** high-volume categories (Genes) into alphabetical buckets (A-G, H-M, etc.) of ~20 entities.
- **Group** low-volume categories (Drugs, Datasets, Methods) into a single "Support Entities" pass.

## 5. Deferred Maintenance

**Problem**: High-cost crosslinking of dozens of files for every single paper.

**Solution**:
- Crosslink the *new* paper page immediately.
- Queue entity page crosslinking for a batch maintenance job using lower-cost models (Haiku).

## 6. Telemetry-First Workflow

**Problem**: Inability to audit costs precisely due to ephemeral environment variables.

**Solution**:
- Ensure `.gemini/settings.json` has `telemetry` enabled by default in the workspace template.
- Use persistent log files to track `input_token_count` and `output_token_count` across all sub-agents.
