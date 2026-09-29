"""Split a raw paper into anchored passages for the paper index.

A raw paper (``data/raw/papers/{pmid}.md``) is either BioC text, with ``##``
sections, ``###`` subsections and blank lines between paragraphs, or PDF/web
text, where sections and paragraphs have to be inferred from line layout.
Either way it becomes a list of ``Paragraph``s under named sections, minus
reference lists, author/funding/conflict statements and PMC manuscript
boilerplate.

The kept paragraphs, joined by blank lines, form the paper's *clean text*.
Passages are runs of whole sentences within one section, and each passage's
``text`` is exactly ``clean_text[char_start:char_end]``, so the MCP server can
rebuild the clean text from the index alone and a quote that crosses passages
still matches. ``section`` + ``paragraph`` give a readable anchor such as
``§Results ¶4``.
"""
from __future__ import annotations

import re
import statistics
from dataclasses import dataclass

CHUNKER_VERSION = "sections-1"

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*\S)\s*$")

# Sections whose text is not the paper's findings. Keys are _section_key()s.
_DROP_SECTIONS = {
    "references", "reference", "bibliography", "literature cited", "references and notes",
    "auth_cont", "author contributions", "contributions",
    "comp_int", "competing interests", "conflict of interest", "conflicts of interest",
    "disclosures", "declaration of interests", "declaration of competing interest",
    "ack_fund", "acknowledgments", "acknowledgements", "acknowledgment", "acknowledgement",
    "funding", "abbr", "abbreviations", "keyword", "keywords", "footnotes",
    "supplementary material", "supplementary materials", "supplementary information",
    "supplementary data", "associated data", "data citations",
}

# Standalone lines that start a section in PDF text (compared as _section_key).
_PDF_HEADINGS = {
    "abstract", "summary", "introduction", "background", "results", "discussion",
    "conclusion", "conclusions", "methods", "materials and methods", "online methods",
    "methods summary", "patients and methods", "experimental procedures", "star methods",
    "results and discussion", "significance", "figure legends", "figures", "tables",
    "data availability", "code availability", "statement of significance",
    "translational relevance", "main",
} | _DROP_SECTIONS

# Whole lines of PDF/manuscript furniture, never paper text.
_BOILERPLATE_RES = [re.compile(p, re.IGNORECASE) for p in (
    r"^(nih|hhs)[- ]?(pa)? ?public access$",
    r"^(nih-pa |hhs )?author manuscripts?$",
    r"^europe pmc funders (group|author manuscripts?)$",
    r"author manuscript; available in pmc",
    r"^published in final edited form as:?$",
    r"^(page )?\d{1,3}( of \d{1,3})?$",
    r"^.{0,80}\bpage \d{1,3}$",
    r"^downloaded from\b",
    r"^this article is protected by copyright",
    r"^accepted article$",
)]

# Tab-separated table text longer than this is a data dump (patient-level
# rows), not a table a reader would quote.
_MAX_TABLE_CHARS = 5000

_FIGURE_START_RE = re.compile(r"^(figure|fig\.?|extended data fig(ure)?\.?)\s*\d+[.:|\s]", re.IGNORECASE)
_TABLE_START_RE = re.compile(r"^table\s*\d+[.:|\s]", re.IGNORECASE)
_TERMINAL_RE = re.compile(r"[.!?:)\]\"”]$")


@dataclass
class Paragraph:
    section: str
    text: str
    subsection: str = ""


@dataclass
class Passage:
    text: str
    section: str
    paragraph: int          # 1-based, under the passage's heading, of its first sentence
    char_start: int
    char_end: int
    subsection: str = ""

    @property
    def heading(self) -> str:
        """The most specific heading: the subsection if any, else the section."""
        return self.subsection or self.section

    @property
    def anchor(self) -> str:
        return anchor(self.heading, self.paragraph)


def anchor(section: str, paragraph: int) -> str:
    return f"§{section} ¶{paragraph}"


def _section_key(title: str) -> str:
    t = re.sub(r"^[\dIVX]+[.)]?\s+", "", title.strip())      # "2. Results", "IV Methods"
    return re.sub(r"[\s:.]+$", "", t).lower()


def strip_frontmatter(text: str) -> str:
    m = _FRONTMATTER_RE.match(text)
    return text[m.end():] if m else text


def _is_boilerplate(line: str) -> bool:
    return any(r.search(line) for r in _BOILERPLATE_RES)


def _structured(body: str) -> bool:
    """True for BioC/web text: real section headings and blank-line paragraphs."""
    headings = sum(1 for ln in body.splitlines() if ln.startswith("## ") and ln != "## Full Text")
    return headings >= 2


def _paragraphs_structured(body: str) -> list[Paragraph]:
    out: list[Paragraph] = []
    section, subsection = "Text", ""
    for block in re.split(r"\n\s*\n", body):
        lines = [ln.strip() for ln in block.strip().splitlines() if ln.strip()]
        if not lines:
            continue
        m = _HEADING_RE.match(lines[0])
        if m:
            level, title = len(m.group(1)), m.group(2)
            if level == 1:
                section, subsection = "Title", ""
                out.append(Paragraph(section, title))
            elif level == 2:
                if title != "Full Text":
                    section, subsection = title, ""
            else:
                subsection = title
            lines = lines[1:]
            if not lines:
                continue
        text = " ".join(ln for ln in lines if not _is_boilerplate(ln))
        if text:
            out.append(Paragraph(section, text, subsection))
    return out


def _paragraphs_pdf(body: str) -> list[Paragraph]:
    """Infer paragraphs and sections from wrapped PDF lines.

    A line ends a paragraph when it ends a sentence and falls well short of
    the paper's usual line width, or when a blank line or a heading follows.
    """
    lines = [ln.strip() for ln in body.splitlines()]
    lines = [ln for ln in lines if not ln.startswith("## Full Text")]
    widths = [len(ln) for ln in lines if len(ln) > 20]
    width = statistics.median(widths) if widths else 80
    out: list[Paragraph] = []
    section = "Front"
    cur: list[str] = []

    def flush() -> None:
        if cur:
            out.append(Paragraph(section, " ".join(cur)))
            cur.clear()

    for ln in lines:
        if not ln:
            flush()
            continue
        if _is_boilerplate(ln):
            continue
        key = _section_key(ln)
        if len(ln) <= 40 and key in _PDF_HEADINGS:
            flush()
            section = key[:1].upper() + key[1:]  # "RESULTS", "2. Results" -> "Results"
            continue
        # A reference list usually runs to the end, except for figure legends
        # and tables that PDFs put after it.
        if _section_key(section) in _DROP_SECTIONS:
            if _FIGURE_START_RE.match(ln):
                flush()
                section = "Figure legends"
            elif _TABLE_START_RE.match(ln):
                flush()
                section = "Tables"
        cur.append(ln)
        if _TERMINAL_RE.search(ln) and len(ln) < 0.75 * width:
            flush()
    flush()
    if all(p.section == "Front" for p in out):  # no headings found: not front matter
        for p in out:
            p.section = "Text"
    return out


def paragraphs(raw: str) -> list[Paragraph]:
    """The kept paragraphs of a raw paper, in order."""
    body = strip_frontmatter(raw)
    paras = _paragraphs_structured(body) if _structured(body) else _paragraphs_pdf(body)
    return [p for p in paras if _section_key(p.section) not in _DROP_SECTIONS
            and not ("\t" in p.text and len(p.text) > _MAX_TABLE_CHARS)]


def _pieces(sentence: str, limit: int) -> list[tuple[int, int]]:
    """Spans of ``sentence`` no longer than ``limit``, split at whitespace, for
    "sentences" the splitter couldn't break (tables, name lists)."""
    out: list[tuple[int, int]] = []
    a, n = 0, len(sentence)
    while a < n:
        b = n
        if n - a > limit:
            cut = sentence.rfind(" ", a + 1, a + limit + 1)
            b = cut if cut > a else a + limit
        out.append((a, b))
        a = b
        while a < n and sentence[a].isspace():
            a += 1
    return out


def passages(nlp, raw: str, target_chars: int = 900, overlap: int = 250) -> tuple[str, list[Passage]]:
    """Return (clean_text, passages) for a raw paper.

    Passages hold whole sentences, stay under one heading (the subsection if
    any, else the section), and are at most ``target_chars`` long (a longer
    sentence is split at whitespace). Each repeats the trailing sentences of
    the one before it under the same heading, up to ``overlap`` characters of
    them. Paragraphs are numbered per heading, and a heading that recurs
    continues its numbering, so every anchor is unique.

    Anchors use the most specific heading because it's the one a reader sees:
    BioC's section types are coarse, and for older Nature papers put results
    under "Introduction" or "Methods" while the subsection is the real heading.
    """
    paras = paragraphs(raw)
    clean_parts: list[str] = []
    # (start, end, heading, paragraph number under it, section, subsection) per sentence
    sents: list[tuple[int, int, str, int, str, str]] = []
    pos = 0
    para_no: dict[str, int] = {}
    docs = nlp.pipe([p.text for p in paras], batch_size=64)
    for p, doc in zip(paras, docs):
        if clean_parts:
            clean_parts.append("\n\n")
            pos += 2
        heading = p.subsection or p.section
        para_no[heading] = para_no.get(heading, 0) + 1
        for s in doc.sents:
            text = s.text
            lead = len(text) - len(text.lstrip())
            body = text.strip()
            start = pos + s.start_char + lead
            for a, b in _pieces(body, target_chars):
                sents.append((start + a, start + b, heading, para_no[heading], p.section, p.subsection))
        clean_parts.append(p.text)
        pos += len(p.text)
    clean = "".join(clean_parts)

    out: list[Passage] = []
    i = 0
    while i < len(sents):
        key = sents[i][2], sents[i][4]  # heading and section: a heading may recur elsewhere
        j = i
        while (j + 1 < len(sents) and (sents[j + 1][2], sents[j + 1][4]) == key
               and sents[j + 1][1] - sents[i][0] <= target_chars):
            j += 1
        start, end = sents[i][0], sents[j][1]
        out.append(Passage(clean[start:end], sents[i][4], sents[i][3], start, end, sents[i][5]))
        if j + 1 >= len(sents):
            break
        # Next passage: repeat this one's trailing sentences that fit in
        # ``overlap``, under the same heading, and only if the next passage still
        # reaches a new sentence (otherwise it would repeat this one forever).
        nxt = j + 1
        if (sents[nxt][2], sents[nxt][4]) == key:
            k = j
            while k > i and sents[j][1] - sents[k][0] <= overlap:
                k -= 1
            k += 1  # first sentence inside the overlap window; j + 1 if none fits
            if k <= j and sents[j + 1][1] - sents[k][0] <= target_chars:
                nxt = k
        i = nxt
    return clean, out
