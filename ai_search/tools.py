"""Wiki navigation tools for the PydanticAI agent.

Each tool wraps a function from cbio_kb.wiki.vault and emits a ToolEvent
to the deps queue so the glass-window UI can show activity in real-time.
"""
from __future__ import annotations

import json

from pydantic_ai import RunContext

from cbio_kb.wiki.vault import (
    find_backlinks,
    find_links,
    get_outline,
    get_properties,
    list_files,
    search_context,
)

from .agent import Deps, ToolEvent, agent


def _emit(ctx: RunContext[Deps], name: str, args: dict, result) -> None:
    q = ctx.deps.tool_queue
    if q is None:
        return
    preview = json.dumps(result, default=str)[:200]
    q.put_nowait(ToolEvent(name, args, preview))


@agent.tool
async def read_page(ctx: RunContext[Deps], path: str) -> str:
    """Read the full content of a wiki page. Path is vault-relative, e.g. 'papers/25730765.md' or 'genes/EGFR.md'."""
    fpath = ctx.deps.wiki_dir / path
    if not fpath.exists():
        return f"Error: {path} not found"
    content = fpath.read_text()
    _emit(ctx, "read_page", {"path": path}, f"{len(content)} chars")
    return content


@agent.tool
async def read_section(ctx: RunContext[Deps], path: str, heading: str) -> str:
    """Read a specific section of a wiki page by heading name. Case-insensitive match."""
    fpath = ctx.deps.wiki_dir / path
    if not fpath.exists():
        return f"Error: {path} not found"
    outline = get_outline(ctx.deps.wiki_dir, path)
    lines = fpath.read_text().splitlines()
    start = None
    end = len(lines)
    target_level = None
    for i, entry in enumerate(outline):
        if entry.get("heading", "").lower() == heading.lower():
            start = entry["line"] - 1
            target_level = entry["level"]
            for later in outline[i + 1 :]:
                if later["level"] <= target_level:
                    end = later["line"] - 1
                    break
            break
    if start is None:
        avail = [e["heading"] for e in outline]
        return f"Heading '{heading}' not found. Available: {avail}"
    section = "\n".join(lines[start:end])
    _emit(ctx, "read_section", {"path": path, "heading": heading}, f"{len(section)} chars")
    return section


@agent.tool
async def get_page_metadata(ctx: RunContext[Deps], path: str) -> dict:
    """Get frontmatter metadata for a wiki page (title, genes, cancer_types, etc.)."""
    result = get_properties(ctx.deps.wiki_dir, path)
    _emit(ctx, "get_page_metadata", {"path": path}, result)
    return result


@agent.tool
async def list_pages(ctx: RunContext[Deps], folder: str) -> list[str]:
    """List all page names in a wiki section. Folder is one of: papers, genes, cancer_types, datasets, drugs, methods, themes."""
    result = list_files(ctx.deps.wiki_dir, folder)
    _emit(ctx, "list_pages", {"folder": folder}, f"{len(result)} pages")
    return result


@agent.tool
async def search(ctx: RunContext[Deps], query: str) -> list[dict]:
    """Full-text search across the wiki. Returns matching lines with surrounding context."""
    result = search_context(ctx.deps.wiki_dir, query, limit=20, context_lines=2)
    _emit(ctx, "search", {"query": query}, f"{len(result)} hits")
    return result


@agent.tool
async def follow_links(ctx: RunContext[Deps], path: str) -> list[str]:
    """Get all outgoing links from a wiki page. Useful for discovering connected pages."""
    result = find_links(ctx.deps.wiki_dir, path)
    _emit(ctx, "follow_links", {"path": path}, f"{len(result)} links")
    return result


@agent.tool
async def find_references(ctx: RunContext[Deps], entity: str) -> list[dict]:
    """Find all pages that link to a given entity. Use the file stem: 'EGFR', 'BLCA', '25730765', etc."""
    result = find_backlinks(ctx.deps.wiki_dir, entity)
    _emit(ctx, "find_references", {"entity": entity}, f"{len(result)} backlinks")
    return result
