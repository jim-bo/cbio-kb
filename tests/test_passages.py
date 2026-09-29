import re
from types import SimpleNamespace

from cbio_kb.index.passages import paragraphs, passages


class FakeNLP:
    """Sentence splitter with spaCy's pipe()/sents/start_char shape."""

    def pipe(self, texts, batch_size=64):
        for t in texts:
            yield SimpleNamespace(sents=[SimpleNamespace(text=m.group(), start_char=m.start())
                                         for m in re.finditer(r"[^.!?]+[.!?]*\s*", t)])


BIOC = """---
pmid: 1
extractor_version: bioc-1
---

## Full Text

# A study of KRAS

## Abstract

KRAS is mutated. It matters.

## Results

### Mutations

KRAS mutations correlate with smoker status (P=0.021). EGFR is exclusive.

A second paragraph here.

## References

Smith J. A paper. Nature 2008.

## Comp_Int

The authors declare no conflicts.
"""

PDF = """---
pmid: 2
extractor_version: 1
---

## Full Text

NIH Public Access
Author Manuscript
Nature. Author manuscript; available in PMC 2009 June 10.
Somatic mutations affect key pathways in lung adenocarcinoma
Abstract
Determining the genetic basis of cancer requires comprehensive analyses of large collections of
tumours. We report here the sequencing of genes in lung adenocarcinomas.
Results
KRAS mutations correlate with smoker status (P=0.021) and this line is as long as the others.
Ding et al. Page 5
The mutations were validated by an independent method in all of these tumour samples here.
Short last line.
References
1. Weir BA, et al. Characterizing the cancer genome in lung adenocarcinoma. Nature 2007.
Figure 1. Mutated genes in lung adenocarcinoma across the whole cohort of tumours studied.
"""


def test_bioc_sections_paragraphs_and_dropped_sections():
    paras = paragraphs(BIOC)
    assert [(p.section, p.subsection) for p in paras] == [
        ("Title", ""), ("Abstract", ""), ("Results", "Mutations"), ("Results", "Mutations")]
    text = " ".join(p.text for p in paras)
    assert "Smith J" not in text and "conflicts" not in text


def test_pdf_boilerplate_headings_and_reference_list_dropped():
    paras = paragraphs(PDF)
    sections = [p.section for p in paras]
    assert sections[0] == "Front" and "Abstract" in sections and "Results" in sections
    text = "\n".join(p.text for p in paras)
    assert "Public Access" not in text and "available in PMC" not in text and "Page 5" not in text
    assert "Weir BA" not in text
    # figure legend after the references is kept, as its own section
    assert paras[-1].section == "Figure legends" and paras[-1].text.startswith("Figure 1.")
    # wrapped lines join into one paragraph; the short sentence-final line ends it
    results = [p.text for p in paras if p.section == "Results"]
    assert len(results) == 1 and results[0].endswith("Short last line.")


def test_passages_are_exact_slices_with_anchors():
    clean, ps = passages(FakeNLP(), BIOC, target_chars=80, overlap=0)
    assert ps and all(clean[p.char_start:p.char_end] == p.text for p in ps)
    kras = next(p for p in ps if "smoker status" in p.text)
    assert kras.anchor == "§Mutations ¶1" and kras.section == "Results"
    assert next(p for p in ps if "second paragraph" in p.text).anchor == "§Mutations ¶2"
    # no passage spans two sections
    assert not any("It matters." in p.text and "KRAS mutations" in p.text for p in ps)


def test_overlap_repeats_whole_sentences_and_always_progresses():
    raw = "## Full Text\n\n## Results\n\n" + " ".join(f"Sentence number {i} is here." for i in range(40)) \
        + "\n\n## Discussion\n\nDone.\n"
    clean, ps = passages(FakeNLP(), raw, target_chars=120, overlap=60)
    assert all(clean[p.char_start:p.char_end] == p.text for p in ps)
    starts = [p.char_start for p in ps]
    assert starts == sorted(set(starts))  # strictly increasing: no infinite repeat
    assert any(a.char_end > b.char_start for a, b in zip(ps, ps[1:]) if a.section == b.section)
    assert all(p.text.startswith("Sentence") or p.text == "Done." for p in ps)
    assert ps[-1].section == "Discussion"


def test_long_sentence_is_split_at_word_boundaries():
    raw = "## Full Text\n\n## Results\n\n" + "word " * 100 + "end. Short one.\n\n## Discussion\n\nX.\n"
    clean, ps = passages(FakeNLP(), raw, target_chars=50, overlap=40)
    assert all(len(p.text) <= 50 and not p.text.startswith(" ") for p in ps)
    assert all(clean[p.char_start:p.char_end] == p.text for p in ps)
    assert any("end." in p.text for p in ps) and ps[-2].text.endswith("Short one.")


def test_long_unsplittable_text_is_capped_and_data_tables_dropped():
    names = ", ".join(f"Person {i}" for i in range(300))  # no sentence breaks
    dump = "\t".join(f"TCGA-{i}" for i in range(2000))
    raw = f"## Full Text\n\n## Appendix\n\n{names}\n\n## Tables\n\n{dump}\n\nTable 1. Small.\n"
    clean, ps = passages(FakeNLP(), raw, target_chars=200, overlap=0)
    assert max(len(p.text) for p in ps) <= 200
    assert all(clean[p.char_start:p.char_end] == p.text for p in ps)
    assert "TCGA-5" not in clean and "Table 1. Small." in clean
    assert " ".join(p.text for p in ps if p.section == "Appendix") == names


def test_pdf_heading_names_are_normalized():
    raw = "## Full Text\n\nTitle line\nPATIENTS AND METHODS\nSome text here.\n2. Results\nMore text.\n"
    assert [p.section for p in paragraphs(raw)] == ["Front", "Patients and methods", "Results"]


def test_anchor_uses_subsection_and_passages_break_at_headings():
    # BioC types a Nature letter's results as INTRO; the subsection is the real heading.
    raw = ("## Full Text\n\n## Introduction\n\nLung cancer is common.\n\n"
           "### Somatic alterations\n\nKRAS (32%, n =74) was mutated.\n\n"
           "### Pathways\n\nRTK/RAS/RAF was altered in 76%.\n\n"
           "## Methods\n\n### Pathways\n\nWe tested pathways.\n")
    clean, ps = passages(FakeNLP(), raw, target_chars=900, overlap=0)
    assert [(p.anchor, p.section) for p in ps] == [
        ("§Introduction ¶1", "Introduction"), ("§Somatic alterations ¶1", "Introduction"),
        ("§Pathways ¶1", "Introduction"), ("§Pathways ¶2", "Methods")]  # recurring heading continues
