"""Entity-anchor extraction for the graph-1-hop retrieval leg.

Builds a gazetteer at startup from ``wiki/{genes,cancer_types,datasets,
drugs,methods}/*.md`` — file stems plus any ``aliases`` from frontmatter —
and exposes :func:`extract_anchors` to find which of those entities a
free-form user query mentions.

The output feeds the graph retriever in :mod:`ai_search.hybrid`: each
matched anchor's wiki page is the entry point for a 1-hop expansion via
``cbio_kb.wiki.vault.find_backlinks``.
"""
from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path

from cbio_kb.wiki import vault

_WIKI_DIR_DEFAULT = Path(os.environ.get(
    "CBIO_WIKI_DIR",
    Path(__file__).resolve().parent.parent / "wiki",
))

_ENTITY_KINDS = ("genes", "cancer_types", "datasets", "drugs", "methods")

# Many HUGO symbols and aliases collide with ordinary English words
# (REST, MET, MAX, SET, CAN→PPP3CA, CAT, …). Left in the gazetteer they fire
# on non-genomic prose ("the rest of the set we met") and pollute the graph
# leg with spurious 1-hop expansions. We drop any term whose lowercase form is
# a common word — those genes are still reachable via the dense and BM25 legs,
# so recall is unharmed while precision improves. Curated toward short tokens,
# since long entity names effectively never collide.
_COMMON_WORDS = frozenset({
    "a", "about", "above", "after", "again", "all", "also", "an", "and", "any",
    "are", "as", "at", "back", "be", "been", "before", "being", "below",
    "best", "both", "but", "by", "call", "came", "can", "case", "cat", "cell",
    "clock", "come", "could", "cut", "damage", "data", "day", "did", "do",
    "does", "down", "each", "end", "even", "ever", "face", "fact", "far",
    "fast", "fat", "few", "find", "first", "for", "form", "from", "front",
    "full", "gap", "get", "give", "go", "good", "got", "had", "hand", "has",
    "have", "he", "her", "here", "hers", "high", "him", "his", "hit", "home",
    "how", "i", "if", "impact", "in", "info", "into", "is", "it", "its",
    "just", "keep", "kind", "knock", "know", "large", "last", "led", "less",
    "let", "level", "like", "line", "link", "list", "long", "look", "lot",
    "low", "made", "main", "make", "many", "mark", "max", "may", "me", "mean",
    "met", "might", "min", "minor", "more", "most", "much", "must", "my",
    "name", "near", "need", "new", "next", "no", "non", "nor", "not", "now",
    "of", "off", "old", "on", "once", "one", "only", "or", "other", "our",
    "out", "over", "own", "pair", "part", "past", "per", "plus", "point",
    "rate", "rest", "right", "rim", "role", "run", "said", "same", "see",
    "set", "she", "should", "show", "side", "site", "size", "so", "some",
    "soon", "spread", "stage", "star", "step", "still", "such", "sum", "sure",
    "tag", "take", "tank", "than", "that", "the", "their", "them", "then",
    "there", "these", "they", "this", "those", "time", "to", "too", "top",
    "two", "type", "up", "us", "use", "used", "very", "was", "way", "we",
    "well", "went", "were", "what", "when", "where", "which", "while", "who",
    "why", "will", "with", "work", "would", "yes", "yet", "you", "your",
})


@dataclass(frozen=True)
class Anchor:
    """A matched entity mention."""

    stem: str            # canonical file stem, e.g. "EGFR"
    kind: str            # one of _ENTITY_KINDS
    path: str            # vault-relative, e.g. "genes/EGFR.md"
    matched_text: str    # the literal substring from the query that matched


@dataclass
class Gazetteer:
    """Compiled term-to-Anchor map plus the alternation regex used to scan."""

    # lowercase term → list of canonical anchors (a term can be ambiguous
    # across kinds; we keep all of them and let the consumer rank).
    terms: dict[str, list[Anchor]]
    pattern: re.Pattern[str] | None

    def match(self, query: str) -> list[Anchor]:
        if not self.pattern or not query:
            return []
        seen: set[tuple[str, str]] = set()
        anchors: list[Anchor] = []
        for m in self.pattern.finditer(query):
            term = m.group(0).lower()
            for a in self.terms.get(term, ()):
                key = (a.kind, a.stem)
                if key in seen:
                    continue
                seen.add(key)
                anchors.append(Anchor(
                    stem=a.stem, kind=a.kind, path=a.path,
                    matched_text=m.group(0),
                ))
        return anchors


_GAZETTEER: Gazetteer | None = None


def _collect_terms(wiki_dir: Path) -> dict[str, list[Anchor]]:
    terms: dict[str, list[Anchor]] = {}
    for kind in _ENTITY_KINDS:
        folder = wiki_dir / kind
        if not folder.is_dir():
            continue
        for fpath in folder.glob("*.md"):
            stem = fpath.stem
            anchor = Anchor(
                stem=stem, kind=kind, path=f"{kind}/{stem}.md", matched_text="",
            )
            if stem.lower() not in _COMMON_WORDS:
                terms.setdefault(stem.lower(), []).append(anchor)
            # Pick up aliases from frontmatter (genes especially carry these).
            try:
                fm = vault._parse_frontmatter(fpath.read_text())
            except OSError:
                continue
            aliases = fm.get("aliases", []) or []
            if isinstance(aliases, str):
                aliases = [aliases]
            for alias in aliases:
                alias = alias.strip()
                if not alias or alias.lower() in _COMMON_WORDS:
                    continue
                terms.setdefault(alias.lower(), []).append(anchor)
    return terms


def _build_pattern(terms: dict[str, list[Anchor]]) -> re.Pattern[str] | None:
    if not terms:
        return None
    # Sort by length descending so longer phrases win over their prefixes
    # (regex alternation is leftmost — within a position the first
    # matching alternative wins).
    sorted_terms = sorted(terms.keys(), key=len, reverse=True)
    # Skip 1-char terms (would produce noise like "a", "b").
    parts = [re.escape(t) for t in sorted_terms if len(t) > 1]
    if not parts:
        return None
    return re.compile(r"\b(?:" + "|".join(parts) + r")\b", re.IGNORECASE)


def build_gazetteer(wiki_dir: Path | None = None) -> Gazetteer:
    """Build and cache the gazetteer. Idempotent — second call returns the cache."""
    global _GAZETTEER
    wd = wiki_dir or _WIKI_DIR_DEFAULT
    terms = _collect_terms(wd)
    gaz = Gazetteer(terms=terms, pattern=_build_pattern(terms))
    _GAZETTEER = gaz
    return gaz


def get_gazetteer(wiki_dir: Path | None = None) -> Gazetteer:
    if _GAZETTEER is None:
        return build_gazetteer(wiki_dir)
    return _GAZETTEER


def extract_anchors(query: str, wiki_dir: Path | None = None) -> list[Anchor]:
    """Return all entity anchors the query mentions, dedup'd by (kind, stem)."""
    return get_gazetteer(wiki_dir).match(query)
