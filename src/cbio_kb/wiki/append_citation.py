"""Deterministic append-citation for entity pages.

Short-circuits the entity-page-writer agent for the common case: appending a
single finding bullet + Sources entry to an existing page. Returns structured
JSON so the caller (agent or orchestrator) can decide whether to fall back to
the LLM path.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

from cbio_kb.wiki.vault import _FRONTMATTER_RE, _HEADING_RE, _parse_frontmatter

# Default target section per entity kind
_DEFAULT_SECTIONS: dict[str, str] = {
    "gene": "Alterations observed in the corpus",
    "cancer_type": "Recurrent alterations",
    "dataset": "Notable findings derived from this cohort",
    "drug": "Evidence in the corpus",
    "method": "Used by",
}

# Folder mapping
_KIND_FOLDER: dict[str, str] = {
    "gene": "genes",
    "cancer_type": "cancer_types",
    "dataset": "datasets",
    "drug": "drugs",
    "method": "methods",
}


def _find_section_range(
    lines: list[str], heading: str
) -> tuple[int, int] | None:
    """Return (start_line_idx, end_line_idx) for the given H2 heading.

    start is the line index of the heading; end is the line index of the next
    heading of equal or higher level (or EOF).
    """
    start = None
    for i, line in enumerate(lines):
        m = _HEADING_RE.match(line)
        if m:
            level = len(m.group(1))
            title = m.group(2).strip()
            if start is not None and level <= 2:
                return (start, i)
            if level == 2 and title == heading:
                start = i
    if start is not None:
        return (start, len(lines))
    return None


def _update_frontmatter(text: str, pmid: str, today: str) -> str:
    """Update processed_at, processed_by, and citing_pmids in frontmatter."""
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return text

    fm_text = m.group(1)
    fm_lines = fm_text.splitlines()

    updated_processed_at = False
    updated_processed_by = False
    for i, line in enumerate(fm_lines):
        if line.startswith("processed_at:"):
            fm_lines[i] = f"processed_at: {today}"
            updated_processed_at = True
        elif line.startswith("processed_by:"):
            fm_lines[i] = "processed_by: wiki-cli"
            updated_processed_by = True

    if not updated_processed_at:
        fm_lines.append(f"processed_at: {today}")
    if not updated_processed_by:
        fm_lines.append("processed_by: wiki-cli")

    new_fm = "\n".join(fm_lines)
    return text[: m.start(1)] + new_fm + text[m.end(1) :]


def _update_footer(text: str, today: str) -> str:
    """Rewrite the trailing provenance footer."""
    footer_re = re.compile(
        r"\n\*This page was processed by \*\*[^*]+\*\* on \*\*[^*]+\*\*\.\*\s*$"
    )
    new_footer = f"\n*This page was processed by **wiki-cli** on **{today}**.*\n"
    if footer_re.search(text):
        return footer_re.sub(new_footer, text)
    return text.rstrip("\n") + "\n" + new_footer


def run(
    wiki_dir: Path,
    kind: str,
    entity_id: str,
    pmid: str,
    bullet: str,
    section: str | None = None,
) -> dict:
    """Append a citation bullet to an existing entity page.

    Returns a dict with keys: path, action, section, reason (optional).
    Raises SystemExit(1) on unrecoverable errors (missing page, missing section).
    """
    folder = _KIND_FOLDER.get(kind)
    if not folder:
        return {"error": f"Unknown kind: {kind}", "exit_code": 1}

    target_section = section or _DEFAULT_SECTIONS[kind]
    page_path = wiki_dir / folder / f"{entity_id}.md"

    if not page_path.exists():
        return {
            "path": str(page_path.relative_to(wiki_dir)),
            "action": "error",
            "reason": "page_not_found",
            "exit_code": 1,
        }

    text = page_path.read_text()
    lines = text.splitlines()

    # Idempotency: check if PMID already present
    pmid_pattern = f"PMID:{pmid}"
    if pmid_pattern in text:
        return {
            "path": str(page_path.relative_to(wiki_dir)),
            "action": "skipped",
            "reason": "pmid_present",
            "exit_code": 0,
        }

    # Find target section
    section_range = _find_section_range(lines, target_section)
    if section_range is None:
        return {
            "path": str(page_path.relative_to(wiki_dir)),
            "action": "error",
            "reason": f"section_not_found: {target_section}",
            "exit_code": 1,
        }

    # Insert bullet at the end of the target section (before next heading)
    insert_idx = section_range[1]
    # Walk backwards from end to skip blank lines
    while insert_idx > section_range[0] + 1 and lines[insert_idx - 1].strip() == "":
        insert_idx -= 1

    lines.insert(insert_idx, f"- {bullet}")

    # Find or create Sources section and append PMID
    sources_range = _find_section_range(lines, "Sources")
    source_entry = f"- [PMID:{pmid}](../papers/{pmid}.md)"

    if sources_range:
        # Insert before end of Sources section
        src_insert = sources_range[1]
        while src_insert > sources_range[0] + 1 and lines[src_insert - 1].strip() == "":
            src_insert -= 1
        lines.insert(src_insert, source_entry)
    else:
        # Append Sources section at end (before footer)
        lines.append("")
        lines.append("## Sources")
        lines.append("")
        lines.append(source_entry)

    today = date.today().isoformat()
    new_text = "\n".join(lines) + "\n"
    new_text = _update_frontmatter(new_text, pmid, today)
    new_text = _update_footer(new_text, today)

    page_path.write_text(new_text)

    return {
        "path": str(page_path.relative_to(wiki_dir)),
        "action": "appended",
        "section": target_section,
        "exit_code": 0,
    }


def cli_main(args) -> int:
    """CLI entry point."""
    wiki_dir = Path(args.wiki_dir)
    result = run(
        wiki_dir=wiki_dir,
        kind=args.kind,
        entity_id=args.id,
        pmid=args.pmid,
        bullet=args.bullet,
        section=args.section,
    )
    exit_code = result.pop("exit_code", 0)
    print(json.dumps(result, indent=2))
    return exit_code
