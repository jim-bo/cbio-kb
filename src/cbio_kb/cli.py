"""Single console entry point: `cbio-kb <subcommand>`.

Only deterministic subcommands live here. LLM-shaped work (compile, query,
crosslink agent, theme synthesis) is performed by agents under
.claude/agents/ or .gemini/agents/, orchestrated interactively — not by this CLI.
"""
from __future__ import annotations

import argparse
from pathlib import Path


def _cmd_ingest_extract(args: argparse.Namespace) -> int:
    from cbio_kb.ingest import extract

    return extract.run(
        pdf_dir=Path(args.pdf_dir),
        out_dir=Path(args.out_dir),
        mapping_csv=Path(args.mapping),
        limit=args.limit,
    )


def _cmd_ingest_resolve(args: argparse.Namespace) -> int:
    from cbio_kb.ingest import pmid2pmcid

    return pmid2pmcid.main([])


def _cmd_ingest_pdfs(args: argparse.Namespace) -> int:
    from cbio_kb.ingest import pmc_downloader

    return pmc_downloader.main([
        "--in", args.mapping,
        "--out-dir", args.out_dir,
        "--email", args.email,
    ])


def _cmd_index_build(args: argparse.Namespace) -> int:
    from cbio_kb.index import semsearch

    return semsearch.main([
        "index",
        "--pdf-dir", args.pdf_dir,
        "--index-dir", args.index_dir,
    ])


def _cmd_index_search(args: argparse.Namespace) -> int:
    from cbio_kb.index import semsearch

    argv = [
        "search",
        "--index-dir", args.index_dir,
        "-q", args.query,
        "--top-k", str(args.top_k),
    ]
    if args.rerank:
        argv.append("--rerank")
    return semsearch.main(argv)


def _cmd_index_build_papers(args: argparse.Namespace) -> int:
    from cbio_kb.index import papers

    return papers.main([
        "build",
        "--papers-dir", args.papers_dir,
        "--pmid-list", args.pmid_list,
        "--index-dir", args.index_dir,
        "--chunk-chars", str(args.chunk_chars),
        "--overlap", str(args.overlap),
        "--batch-size", str(args.batch_size),
    ])


def _cmd_ontology_sync(args: argparse.Namespace) -> int:
    from cbio_kb.ontology import sync

    return sync.run(out_dir=Path(args.out_dir))


def _cmd_ontology_lookup(args: argparse.Namespace) -> int:
    from cbio_kb.ontology import lookup

    return lookup.run_lookup(ontology_dir=Path(args.ontology_dir), query=args.query)


def _cmd_lint(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import lint

    return lint.run(wiki_dir=Path(args.wiki_dir), allow_orphans=args.allow_orphans)


def _cmd_search(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import search

    return search.run(wiki_dir=Path(args.wiki_dir), query=args.query)


def _cmd_crosslink(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import crosslink

    return crosslink.run(
        Path(args.wiki_dir),
        [Path(p) for p in args.paths] if args.paths else None,
        dry_run=args.dry_run,
        update_provenance=args.update_provenance,
    )


def _cmd_logs_export(args: argparse.Namespace) -> int:
    from cbio_kb.logs import export

    sid = export._latest_session() if args.latest else args.session
    export.export(sid, Path(args.out), truncate=args.truncate)
    return 0


def _cmd_serve(args: argparse.Namespace) -> int:
    from cbio_kb.server import mcp

    return mcp.main(["--host", args.host, "--port", str(args.port)])


# ---- wiki vault queries ---------------------------------------------------

def _json_print(obj) -> int:
    import json
    print(json.dumps(obj, indent=2, ensure_ascii=False))
    return 0


def _cmd_wiki_files(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.list_files(Path(args.wiki_dir), args.folder))


def _cmd_wiki_properties(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.get_properties(Path(args.wiki_dir), args.path))


def _cmd_wiki_property(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.get_property(Path(args.wiki_dir), args.path, args.name))


def _cmd_wiki_outline(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.get_outline(Path(args.wiki_dir), args.path))


def _cmd_wiki_search(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.search_files(Path(args.wiki_dir), args.query))


def _cmd_wiki_search_context(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(
        vault.search_context(
            Path(args.wiki_dir), args.query,
            limit=args.limit, path=args.path,
        )
    )


def _cmd_wiki_backlinks(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.find_backlinks(Path(args.wiki_dir), args.file))


def _cmd_wiki_links(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.find_links(Path(args.wiki_dir), args.path))


def _cmd_wiki_tag(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.find_by_tag(Path(args.wiki_dir), args.name))


def _cmd_wiki_unresolved(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.find_unresolved(Path(args.wiki_dir)))


def _cmd_wiki_orphans(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.find_orphans(Path(args.wiki_dir)))


def _cmd_wiki_deadends(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.find_deadends(Path(args.wiki_dir)))


def _cmd_wiki_reload(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault
    return _json_print(vault.reload())


def _cmd_wiki_build_index(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import vault

    wiki_dir = Path(args.wiki_dir)
    template = Path(args.template)
    if not template.exists():
        print(f"[!] template not found: {template}")
        return 1
    rendered = vault.build_index(wiki_dir, template)
    if args.dry_run:
        print(rendered)
    else:
        (wiki_dir / "index.md").write_text(rendered)
        print(f"[build-index] wrote {wiki_dir / 'index.md'}")
    return 0


def _cmd_wiki_build_graph(args: argparse.Namespace) -> int:
    import json
    from cbio_kb.wiki import vault

    wiki_dir = Path(args.wiki_dir)
    graph = vault.build_graph(wiki_dir)
    if args.dry_run:
        print(json.dumps(graph, indent=2))
        return 0
    out_path = wiki_dir / "graph.json"
    out_path.write_text(json.dumps(graph, indent=2) + "\n")
    n_nodes = 1 + len(graph["sections"]) + len(graph["nodes"])
    print(
        f"[build-graph] wrote {out_path} "
        f"({n_nodes} nodes, {len(graph['tree_edges'])} tree edges, "
        f"{len(graph['cross_edges'])} cross edges)"
    )
    return 0


def _cmd_wiki_reprocess_frontmatter(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import reprocess

    sections = args.sections.split(",") if args.sections else None
    return reprocess.run_patch(
        Path(args.wiki_dir),
        Path(args.template_dir),
        sections=sections,
        dry_run=args.dry_run,
    )


def _cmd_wiki_reprocess_extract(args: argparse.Namespace) -> int:
    from cbio_kb.wiki import reprocess

    return reprocess.run_extract(
        Path(args.wiki_dir),
        Path(args.raw_dir),
        Path(args.template_dir),
        emit_prompts=args.prompts,
    )


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="cbio-kb", description="cbio-kb CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    ingest = sub.add_parser("ingest", help="Fetch and normalize raw papers")
    ingest_sub = ingest.add_subparsers(dest="subcmd", required=True)

    ext = ingest_sub.add_parser("extract", help="PDFs -> raw/papers/*.md")
    ext.add_argument("--pdf-dir", default="data/raw/pdfs")
    ext.add_argument("--out-dir", default="data/raw/papers")
    ext.add_argument("--mapping", default="data/pmid_to_pmcid.csv")
    ext.add_argument("--limit", type=int, default=None)
    ext.set_defaults(func=_cmd_ingest_extract)

    res = ingest_sub.add_parser("resolve", help="PMIDs -> PMCIDs (NCBI)")
    res.set_defaults(func=_cmd_ingest_resolve)

    pdfs = ingest_sub.add_parser("pdfs", help="Download PDFs from PMC")
    pdfs.add_argument("--mapping", default="data/pmid_to_pmcid.csv")
    pdfs.add_argument("--out-dir", default="data/raw/pdfs")
    pdfs.add_argument("--email", required=True)
    pdfs.set_defaults(func=_cmd_ingest_pdfs)

    idx = sub.add_parser("index", help="FAISS passage index")
    idx_sub = idx.add_subparsers(dest="subcmd", required=True)
    idx_b = idx_sub.add_parser("build")
    idx_b.add_argument("--pdf-dir", default="data/raw/pdfs")
    idx_b.add_argument("--index-dir", default="data/index_dir")
    idx_b.set_defaults(func=_cmd_index_build)
    idx_s = idx_sub.add_parser("search")
    idx_s.add_argument("--index-dir", default="data/index_dir")
    idx_s.add_argument("-q", "--query", required=True)
    idx_s.add_argument("--top-k", type=int, default=5)
    idx_s.add_argument("--rerank", action="store_true")
    idx_s.set_defaults(func=_cmd_index_search)
    idx_bp = idx_sub.add_parser(
        "build-papers",
        help="Index raw paper markdowns for the RAG-vs-agentic experiment",
    )
    idx_bp.add_argument("--papers-dir", default="data/raw/papers")
    idx_bp.add_argument("--pmid-list", default="eval/corpus_pmids.txt")
    idx_bp.add_argument("--index-dir", default="data/paper_index")
    idx_bp.add_argument("--chunk-chars", type=int, default=900)
    idx_bp.add_argument("--overlap", type=int, default=120)
    idx_bp.add_argument("--batch-size", type=int, default=100)
    idx_bp.set_defaults(func=_cmd_index_build_papers)

    ont = sub.add_parser("ontology", help="Canonical ontology management")
    ont_sub = ont.add_subparsers(dest="subcmd", required=True)
    ont_s = ont_sub.add_parser("sync", help="Pull canonical lists from cBioPortal + OncoTree")
    ont_s.add_argument("--out-dir", default="schema/ontology")
    ont_s.set_defaults(func=_cmd_ontology_sync)
    ont_l = ont_sub.add_parser("lookup", help="Validate a term against canonical IDs")
    ont_l.add_argument("query")
    ont_l.add_argument("--ontology-dir", default="schema/ontology")
    ont_l.set_defaults(func=_cmd_ontology_lookup)

    lnt = sub.add_parser("lint", help="Validate wiki structure")
    lnt.add_argument("--wiki-dir", default="wiki")
    lnt.add_argument(
        "--allow-orphans",
        action="store_true",
        help="Downgrade 'not in index.md' errors to warnings (Quarto listing pages are the canonical index)",
    )
    lnt.set_defaults(func=_cmd_lint)

    srch = sub.add_parser("search", help="Ripgrep-backed FTS over wiki/")
    srch.add_argument("query")
    srch.add_argument("--wiki-dir", default="wiki")
    srch.set_defaults(func=_cmd_search)

    xl = sub.add_parser("crosslink", help="Deterministic crosslinker (no LLM)")
    xl.add_argument("--wiki-dir", default="wiki")
    xl.add_argument("--paths", nargs="*")
    xl.add_argument("--dry-run", action="store_true")
    xl.add_argument("--update-provenance", action="store_true",
                     help="Update processed_by/processed_at and footer")
    xl.set_defaults(func=_cmd_crosslink)

    logs = sub.add_parser("logs", help="Session transcript tools")
    logs_sub = logs.add_subparsers(dest="subcmd", required=True)
    logs_e = logs_sub.add_parser("export", help="Stitch main + subagent JSONLs into a Markdown transcript")
    g = logs_e.add_mutually_exclusive_group(required=True)
    g.add_argument("--session", help="session UUID")
    g.add_argument("--latest", action="store_true")
    logs_e.add_argument("--out", required=True)
    logs_e.add_argument("--truncate", type=int, default=2000)
    logs_e.set_defaults(func=_cmd_logs_export)

    srv = sub.add_parser("serve", help="Start MCP server")
    srv.add_argument("--host", default="localhost")
    srv.add_argument("--port", type=int, default=8123)
    srv.set_defaults(func=_cmd_serve)

    # ---- wiki vault queries -----------------------------------------------
    wiki = sub.add_parser("wiki", help="Token-efficient wiki vault queries (JSON)")
    wiki_sub = wiki.add_subparsers(dest="subcmd", required=True)
    wiki.add_argument("--wiki-dir", default="wiki")

    w_files = wiki_sub.add_parser("files", help="List .md stems in a folder")
    w_files.add_argument("--folder", required=True)
    w_files.set_defaults(func=_cmd_wiki_files)

    w_props = wiki_sub.add_parser("properties", help="Frontmatter as JSON")
    w_props.add_argument("--path", required=True)
    w_props.set_defaults(func=_cmd_wiki_properties)

    w_prop = wiki_sub.add_parser("property", help="Single frontmatter field")
    w_prop.add_argument("--path", required=True)
    w_prop.add_argument("--name", required=True)
    w_prop.set_defaults(func=_cmd_wiki_property)

    w_outline = wiki_sub.add_parser("outline", help="Heading map with line numbers")
    w_outline.add_argument("--path", required=True)
    w_outline.set_defaults(func=_cmd_wiki_outline)

    w_search = wiki_sub.add_parser("search", help="File paths matching query")
    w_search.add_argument("--query", required=True)
    w_search.set_defaults(func=_cmd_wiki_search)

    w_ctx = wiki_sub.add_parser("search-context", help="Matching lines with context")
    w_ctx.add_argument("--query", required=True)
    w_ctx.add_argument("--limit", type=int, default=50)
    w_ctx.add_argument("--path", default=None)
    w_ctx.set_defaults(func=_cmd_wiki_search_context)

    w_bl = wiki_sub.add_parser("backlinks", help="Pages linking to a file stem")
    w_bl.add_argument("--file", required=True)
    w_bl.set_defaults(func=_cmd_wiki_backlinks)

    w_links = wiki_sub.add_parser("links", help="Outgoing links from a page")
    w_links.add_argument("--path", required=True)
    w_links.set_defaults(func=_cmd_wiki_links)

    w_tag = wiki_sub.add_parser("tag", help="Pages with a frontmatter tag")
    w_tag.add_argument("--name", required=True)
    w_tag.set_defaults(func=_cmd_wiki_tag)

    w_unres = wiki_sub.add_parser("unresolved", help="Broken intra-wiki links")
    w_unres.set_defaults(func=_cmd_wiki_unresolved)

    w_orph = wiki_sub.add_parser("orphans", help="Pages not in index.md")
    w_orph.set_defaults(func=_cmd_wiki_orphans)

    w_dead = wiki_sub.add_parser("deadends", help="Pages with no outgoing links")
    w_dead.set_defaults(func=_cmd_wiki_deadends)

    w_reload = wiki_sub.add_parser("reload", help="No-op (filesystem is always fresh)")
    w_reload.set_defaults(func=_cmd_wiki_reload)

    w_bindex = wiki_sub.add_parser("build-index", help="Regenerate wiki/index.md from template")
    w_bindex.add_argument("--template", default="schema/templates/index.md")
    w_bindex.add_argument("--dry-run", action="store_true",
                          help="Print rendered index to stdout instead of writing")
    w_bindex.set_defaults(func=_cmd_wiki_build_index)

    w_bgraph = wiki_sub.add_parser(
        "build-graph",
        help="Regenerate wiki/graph.json (hierarchy + cross-link adjacency)",
    )
    w_bgraph.add_argument(
        "--dry-run",
        action="store_true",
        help="Print rendered graph JSON to stdout instead of writing",
    )
    w_bgraph.set_defaults(func=_cmd_wiki_build_graph)

    w_repatch = wiki_sub.add_parser("reprocess-frontmatter",
                                     help="Tier 1: patch frontmatter to match templates (deterministic)")
    w_repatch.add_argument("--template-dir", default="schema/templates")
    w_repatch.add_argument("--sections", default=None,
                            help="Comma-separated sections to process (default: all)")
    w_repatch.add_argument("--dry-run", action="store_true")
    w_repatch.set_defaults(func=_cmd_wiki_reprocess_frontmatter)

    w_reextract = wiki_sub.add_parser("reprocess-extract",
                                       help="Tier 2: find papers needing delta extraction")
    w_reextract.add_argument("--template-dir", default="schema/templates")
    w_reextract.add_argument("--raw-dir", default="data/raw/papers")
    w_reextract.add_argument("--prompts", action="store_true",
                              help="Emit agent prompts instead of JSON manifest")
    w_reextract.set_defaults(func=_cmd_wiki_reprocess_extract)

    return p


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
