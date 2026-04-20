"""Wiki navigation tools for the PydanticAI agent.

Each tool wraps a function from cbio_kb.wiki.vault and emits a ToolEvent
to the deps queue so the glass-window UI can show activity in real-time.
"""
from __future__ import annotations

import json
import time

from pydantic_ai import RunContext

from cbio_kb.wiki.vault import (
    find_backlinks,
    find_links,
    get_outline,
    get_properties,
    list_files,
)

from .agent import Deps, ToolEvent, agent


def _serialize_result(result) -> str:
    """Return the string form the model will actually see for *result*.

    PydanticAI passes string tool results through verbatim and JSON-
    encodes anything else. Matching that here keeps our char/token
    counts honest — they reflect the real context footprint.
    """
    if isinstance(result, str):
        return result
    return json.dumps(result, default=str)


def _now(ctx: RunContext[Deps]) -> float:
    """Seconds since the turn started, or 0.0 if no baseline recorded."""
    t0 = ctx.deps.turn_start_monotonic
    return time.monotonic() - t0 if t0 is not None else 0.0


def _emit(
    ctx: RunContext[Deps],
    name: str,
    args: dict,
    result,
    *,
    summary: str | None = None,
    result_paths: list[str] | None = None,
    t_start: float = 0.0,
) -> None:
    """Push a ToolEvent describing this tool call onto the deps queue.

    ``result`` must be the actual value the tool is about to return —
    char and token counts are computed from its serialized form so
    they reflect the true context footprint. The preview always shows
    the first chunk of the real serialized payload so the UI can
    reveal exactly what flowed into the model's context. ``summary``
    is an optional short label (e.g. ``"21 pages"``) shown alongside
    the preview as a compact header badge.
    """
    q = ctx.deps.tool_queue
    if q is None:
        return
    serialized = _serialize_result(result)
    chars = len(serialized)
    # Rough token estimate — Anthropic/OpenAI average ~4 chars per token
    # for English text. Good enough for a "glass window" indicator.
    tokens = max(1, chars // 4) if chars else 0
    preview = serialized[:500]
    t_end = _now(ctx)
    q.put_nowait(ToolEvent(
        name, args, preview, chars, tokens, summary,
        result_paths=list(result_paths) if result_paths else [],
        t_start=t_start,
        t_end=t_end,
    ))


@agent.tool
async def read_page(ctx: RunContext[Deps], path: str) -> str:
    """Read the full content of a wiki page. Path is vault-relative, e.g. 'papers/25730765.md' or 'genes/EGFR.md'."""
    t_start = _now(ctx)
    fpath = ctx.deps.wiki_dir / path
    if not fpath.exists():
        err = f"Error: {path} not found"
        _emit(ctx, "read_page", {"path": path}, err, t_start=t_start)
        return err
    content = fpath.read_text()
    _emit(ctx, "read_page", {"path": path}, content, result_paths=[path], t_start=t_start)
    return content


@agent.tool
async def read_section(ctx: RunContext[Deps], path: str, heading: str) -> str:
    """Read a specific section of a wiki page by heading name. Case-insensitive match."""
    t_start = _now(ctx)
    fpath = ctx.deps.wiki_dir / path
    if not fpath.exists():
        err = f"Error: {path} not found"
        _emit(ctx, "read_section", {"path": path, "heading": heading}, err, t_start=t_start)
        return err
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
        msg = f"Heading '{heading}' not found. Available: {avail}"
        _emit(ctx, "read_section", {"path": path, "heading": heading}, msg, t_start=t_start)
        return msg
    section = "\n".join(lines[start:end])
    _emit(ctx, "read_section", {"path": path, "heading": heading}, section, result_paths=[path], t_start=t_start)
    return section


@agent.tool
async def get_page_metadata(ctx: RunContext[Deps], path: str) -> dict:
    """Get frontmatter metadata for a wiki page (title, genes, cancer_types, etc.)."""
    t_start = _now(ctx)
    result = get_properties(ctx.deps.wiki_dir, path)
    _emit(ctx, "get_page_metadata", {"path": path}, result, result_paths=[path], t_start=t_start)
    return result


@agent.tool
async def list_pages(ctx: RunContext[Deps], folder: str) -> list[str]:
    """List all page names in a wiki section. Folder is one of: papers, genes, cancer_types, datasets, drugs, methods, themes."""
    t_start = _now(ctx)
    result = list_files(ctx.deps.wiki_dir, folder)
    _emit(
        ctx, "list_pages", {"folder": folder}, result,
        summary=f"{len(result)} pages",
        t_start=t_start,
    )
    return result


@agent.tool
async def follow_links(ctx: RunContext[Deps], path: str) -> list[str]:
    """Get all outgoing links from a wiki page. Useful for discovering connected pages."""
    t_start = _now(ctx)
    result = find_links(ctx.deps.wiki_dir, path)
    _emit(
        ctx, "follow_links", {"path": path}, result,
        summary=f"{len(result)} links",
        result_paths=list(result),
        t_start=t_start,
    )
    return result


@agent.tool
async def find_references(ctx: RunContext[Deps], entity: str) -> list[dict]:
    """Find all pages that link to a given entity. Use the file stem: 'EGFR', 'BLCA', '25730765', etc."""
    t_start = _now(ctx)
    result = find_backlinks(ctx.deps.wiki_dir, entity)
    _emit(
        ctx, "find_references", {"entity": entity}, result,
        summary=f"{len(result)} backlinks",
        result_paths=list(dict.fromkeys(h["source"] for h in result if isinstance(h, dict) and "source" in h)),
        t_start=t_start,
    )
    return result
