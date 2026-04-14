"""Token-efficient wiki vault queries — pure-Python replacement for the Obsidian CLI.

Every public function accepts a resolved ``wiki_dir: Path`` and returns a Python
object that the CLI layer serialises with ``json.dumps()``.  Paths accepted as
arguments are **vault-relative** (e.g. ``papers/39506116.md``).
"""
from __future__ import annotations

import re
import shutil
import string
import subprocess
from pathlib import Path

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_HEADING_RE = re.compile(r"^(#{1,6}) (.+)$")
_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def _parse_frontmatter(text: str) -> dict:
    """Parse YAML-ish frontmatter into a dict.

    Handles scalar ``key: value`` lines and two list forms:
    - inline ``key: [a, b, c]``
    - block::

        key:
          - a
          - b
    """
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return {}
    fm_text = m.group(1)
    result: dict = {}
    lines = fm_text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" not in line:
            i += 1
            continue
        key, _, raw = line.partition(":")
        key = key.strip()
        raw = raw.strip()
        # Inline list: key: [a, b, c]
        if raw.startswith("[") and raw.endswith("]"):
            result[key] = [
                s.strip().strip("\"'") for s in raw[1:-1].split(",") if s.strip()
            ]
            i += 1
            continue
        # Block list: next lines start with ``  - ``
        if raw == "":
            block_items: list[str] = []
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith("- "):
                block_items.append(
                    lines[j].strip().lstrip("-").strip().strip("\"'")
                )
                j += 1
            if block_items:
                result[key] = block_items
                i = j
                continue
        # Scalar
        result[key] = raw.strip("\"'") if raw else ""
        i += 1
    return result


# ---------------------------------------------------------------------------
# Public query functions
# ---------------------------------------------------------------------------


def list_files(wiki_dir: Path, folder: str) -> list[str]:
    """Return sorted list of ``.md`` file stems in *folder*."""
    target = wiki_dir / folder
    if not target.is_dir():
        return []
    return sorted(p.stem for p in target.glob("*.md"))


def get_properties(wiki_dir: Path, path: str) -> dict:
    """Return parsed frontmatter for the vault-relative *path*."""
    fpath = wiki_dir / path
    if not fpath.exists():
        return {"error": f"File not found: {path}"}
    return _parse_frontmatter(fpath.read_text())


def get_property(wiki_dir: Path, path: str, name: str) -> str | list | None:
    """Return a single frontmatter field value."""
    props = get_properties(wiki_dir, path)
    if "error" in props:
        return None
    return props.get(name)


def get_outline(wiki_dir: Path, path: str) -> list[dict]:
    """Return ``[{level, heading, line}, ...]`` with 1-indexed line numbers."""
    fpath = wiki_dir / path
    if not fpath.exists():
        return [{"error": f"File not found: {path}"}]
    result: list[dict] = []
    for lineno, line in enumerate(fpath.read_text().splitlines(), 1):
        m = _HEADING_RE.match(line)
        if m:
            result.append(
                {"level": len(m.group(1)), "heading": m.group(2), "line": lineno}
            )
    return result


def search_files(wiki_dir: Path, query: str) -> list[str]:
    """Return vault-relative paths of files whose content matches *query*."""
    rg = shutil.which("rg")
    if rg:
        proc = subprocess.run(
            [rg, "-l", "--color", "never", query, str(wiki_dir)],
            capture_output=True,
            text=True,
        )
        paths = []
        for line in proc.stdout.strip().splitlines():
            if not line:
                continue
            try:
                paths.append(str(Path(line).relative_to(wiki_dir)))
            except ValueError:
                paths.append(line)
        return sorted(paths)
    # Python fallback
    needle = query.lower()
    hits: list[str] = []
    for p in sorted(wiki_dir.rglob("*.md")):
        if needle in p.read_text().lower():
            hits.append(str(p.relative_to(wiki_dir)))
    return hits


def search_context(
    wiki_dir: Path,
    query: str,
    *,
    limit: int = 50,
    path: str | None = None,
    context_lines: int = 2,
) -> list[dict]:
    """Return matching lines with surrounding context.

    Each result: ``{file, line, text, before: [...], after: [...]}``.
    """
    search_root = wiki_dir / path if path else wiki_dir
    if path and not search_root.exists():
        return [{"error": f"File not found: {path}"}]

    results: list[dict] = []

    # Collect all .md files to search
    if search_root.is_file():
        md_files = [search_root]
    else:
        md_files = sorted(search_root.rglob("*.md"))

    pattern = re.compile(re.escape(query), re.IGNORECASE)

    for fpath in md_files:
        lines = fpath.read_text().splitlines()
        rel = str(fpath.relative_to(wiki_dir))
        for i, line in enumerate(lines):
            if pattern.search(line):
                before = lines[max(0, i - context_lines) : i]
                after = lines[i + 1 : i + 1 + context_lines]
                results.append(
                    {
                        "file": rel,
                        "line": i + 1,
                        "text": line,
                        "before": before,
                        "after": after,
                    }
                )
                if len(results) >= limit:
                    return results
    return results


def find_backlinks(wiki_dir: Path, file_stem: str) -> list[dict]:
    """Find pages containing links to *file_stem* (resolved by stem, like a wikilink).

    Returns ``[{source, line, text}, ...]``.
    """
    # Match both relative links (../genes/EGFR.md) and wikilinks ([[EGFR]])
    link_pat = re.compile(
        rf"(?:\]\([^)]*/{re.escape(file_stem)}\.md\))"
        rf"|(?:\[\[{re.escape(file_stem)}\]\])"
    )
    results: list[dict] = []
    for fpath in sorted(wiki_dir.rglob("*.md")):
        if fpath.stem == file_stem:
            continue  # skip self
        lines = fpath.read_text().splitlines()
        rel = str(fpath.relative_to(wiki_dir))
        for i, line in enumerate(lines):
            if link_pat.search(line):
                results.append({"source": rel, "line": i + 1, "text": line})
    return results


def find_links(wiki_dir: Path, path: str) -> list[str]:
    """Return all outgoing markdown link hrefs from *path*."""
    fpath = wiki_dir / path
    if not fpath.exists():
        return []
    return _LINK_RE.findall(fpath.read_text())


def find_by_tag(wiki_dir: Path, tag: str) -> list[str]:
    """Return vault-relative paths of pages whose frontmatter ``tags`` includes *tag*."""
    results: list[str] = []
    for fpath in sorted(wiki_dir.rglob("*.md")):
        fm = _parse_frontmatter(fpath.read_text())
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",")]
        if tag in tags:
            results.append(str(fpath.relative_to(wiki_dir)))
    return results


def find_unresolved(wiki_dir: Path) -> list[dict]:
    """Find broken intra-wiki links.

    Returns ``[{source, target, href}, ...]``.
    """
    all_pages = {
        p.relative_to(wiki_dir).as_posix(): p for p in wiki_dir.rglob("*.md")
    }
    results: list[dict] = []
    for rel, fpath in sorted(all_pages.items()):
        text = fpath.read_text()
        for href in _LINK_RE.findall(text):
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = (fpath.parent / href).resolve()
            try:
                target_rel = target.relative_to(wiki_dir.resolve()).as_posix()
            except ValueError:
                continue
            if target_rel not in all_pages and not target.exists():
                results.append({"source": rel, "target": target_rel, "href": href})
    return results


def find_orphans(wiki_dir: Path) -> list[str]:
    """Find pages not referenced from ``index.md`` or a Quarto listing.

    Returns vault-relative paths.
    """
    index = wiki_dir / "index.md"
    if not index.exists():
        return []
    index_text = index.read_text()
    # Sections with Quarto auto-listing
    listed_sections: set[str] = set()
    for qmd in wiki_dir.glob("*/index.qmd"):
        qtext = qmd.read_text()
        if re.search(r"contents:\s*\"?\*\.md\"?", qtext):
            listed_sections.add(qmd.parent.name)
    orphans: list[str] = []
    for fpath in sorted(wiki_dir.rglob("*.md")):
        rel = fpath.relative_to(wiki_dir).as_posix()
        if rel == "index.md":
            continue
        section = rel.split("/", 1)[0]
        if section in listed_sections:
            continue
        stem = fpath.stem
        if stem not in index_text and rel not in index_text:
            orphans.append(rel)
    return orphans


def find_deadends(wiki_dir: Path) -> list[str]:
    """Find pages with no outgoing intra-wiki links.

    Returns vault-relative paths.
    """
    deadends: list[str] = []
    for fpath in sorted(wiki_dir.rglob("*.md")):
        text = fpath.read_text()
        has_wiki_link = False
        for href in _LINK_RE.findall(text):
            if not href.startswith(("http://", "https://", "#", "mailto:")):
                has_wiki_link = True
                break
        if not has_wiki_link:
            deadends.append(str(fpath.relative_to(wiki_dir)))
    return deadends


def reload() -> dict:
    """No-op compatibility shim — the filesystem is always fresh."""
    return {"ok": True}


# ---------------------------------------------------------------------------
# Index generation
# ---------------------------------------------------------------------------

_SECTIONS = ["papers", "genes", "cancer_types", "datasets", "drugs", "methods", "themes"]


def _build_entity_list(wiki_dir: Path, section: str) -> str:
    """Build a compact inline list of links to every page in a section.

    Papers get bullet-list format (PMID + title).  All other sections use a
    flowing ``·``-separated paragraph that renders nicely in Obsidian/Quarto
    and is still machine-parseable.
    """
    folder = wiki_dir / section
    if not folder.is_dir():
        return ""
    pages = sorted(
        (p for p in folder.glob("*.md") if p.name != "index.md"),
        key=lambda p: p.stem,
    )
    if not pages:
        return ""
    if section == "papers":
        lines: list[str] = []
        for p in pages:
            rel = f"{section}/{p.name}"
            fm = _parse_frontmatter(p.read_text())
            title = fm.get("title", p.stem)
            if isinstance(title, list):
                title = title[0] if title else p.stem
            lines.append(f"- [{p.stem}]({rel}) — {title}")
        return "\n".join(lines)
    # Compact inline format for entity sections
    links = [f"[{p.stem}]({section}/{p.name})" for p in pages]
    return " · ".join(links)


_SECTION_LABELS = {
    "papers": "Papers",
    "genes": "Genes",
    "cancer_types": "Cancer types",
    "datasets": "Datasets",
    "drugs": "Drugs",
    "methods": "Methods",
    "themes": "Themes",
}


def _section_label(slug: str) -> str:
    return _SECTION_LABELS.get(slug, slug.replace("_", " ").title())


def build_graph(wiki_dir: Path) -> dict:
    """Build a hierarchical graph manifest of the wiki.

    Returns a JSON-serialisable dict shaped as::

        {
          "root":     {"id": "index", "label": "Index"},
          "sections": [{"id": "papers", "label": "Papers", "count": 21}, ...],
          "nodes":    [{"id": "papers/12345.md", "section": "papers",
                        "label": "12345", "title": "..."}, ...],
          "tree_edges":  [{"from": "index", "to": "papers"},
                          {"from": "papers", "to": "papers/12345.md"}, ...],
          "cross_edges": [{"from": "papers/12345.md", "to": "genes/EGFR.md"}, ...]
        }

    Node ids for entity pages are vault-relative paths so they match
    ``tool_use.args.path`` from the chat agent exactly.
    """
    sections_meta: list[dict] = []
    nodes: list[dict] = []
    tree_edges: list[dict] = []
    cross_edges: list[dict] = []
    known_ids: set[str] = set()

    root_id = "index"
    for section in _SECTIONS:
        folder = wiki_dir / section
        tree_edges.append({"from": root_id, "to": section})
        if not folder.is_dir():
            sections_meta.append(
                {"id": section, "label": _section_label(section), "count": 0}
            )
            continue
        pages = sorted(
            (p for p in folder.glob("*.md") if p.name != "index.md"),
            key=lambda p: p.stem,
        )
        sections_meta.append(
            {"id": section, "label": _section_label(section), "count": len(pages)}
        )
        for p in pages:
            rel = f"{section}/{p.name}"
            known_ids.add(rel)
            fm = _parse_frontmatter(p.read_text())
            title = (
                fm.get("title")
                or fm.get("name")
                or fm.get("symbol")
                or p.stem
            )
            if isinstance(title, list):
                title = title[0] if title else p.stem
            nodes.append(
                {
                    "id": rel,
                    "section": section,
                    "label": p.stem,
                    "title": str(title),
                }
            )
            tree_edges.append({"from": section, "to": rel})

    seen: set[tuple[str, str]] = set()
    wiki_root = wiki_dir.resolve()
    for src in sorted(known_ids):
        src_path = wiki_dir / src
        text = src_path.read_text()
        for href in _LINK_RE.findall(text):
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = (src_path.parent / href).resolve()
            try:
                target_rel = target.relative_to(wiki_root).as_posix()
            except ValueError:
                continue
            if target_rel == src or target_rel not in known_ids:
                continue
            key = (src, target_rel)
            if key in seen:
                continue
            seen.add(key)
            cross_edges.append({"from": src, "to": target_rel})

    return {
        "root": {"id": root_id, "label": "Index"},
        "sections": sections_meta,
        "nodes": nodes,
        "tree_edges": tree_edges,
        "cross_edges": cross_edges,
    }


def build_index(wiki_dir: Path, template_path: Path) -> str:
    """Render ``wiki/index.md`` from a template with section counts and entity lists.

    Placeholders use ``string.Template`` syntax:

    - ``${papers_count}``, ``${genes_count}``, etc. — integer counts
    - ``${papers_list}``, ``${genes_list}``, etc. — markdown link lists
    """
    subs: dict[str, str] = {}
    for section in _SECTIONS:
        folder = wiki_dir / section
        if folder.is_dir():
            pages = [p for p in folder.glob("*.md") if p.name != "index.md"]
            subs[f"{section}_count"] = str(len(pages))
        else:
            subs[f"{section}_count"] = "0"
        subs[f"{section}_list"] = _build_entity_list(wiki_dir, section)

    tmpl = string.Template(template_path.read_text())
    return tmpl.safe_substitute(subs)
