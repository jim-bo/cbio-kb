from cbio_kb.ingest.bioc import to_markdown


def _p(stype, ptype, text, **infons):
    return {"infons": {"section_type": stype, "type": ptype, **infons}, "text": text}


def test_to_markdown_reports_article_pmid_and_sections():
    doc = {"passages": [
        _p("TITLE", "front", "MET amplification by NGS", **{"article-id_pmid": "36044468"}),
        _p("ABSTRACT", "abstract_title_1", "Purpose:"),
        _p("ABSTRACT", "abstract", "Thresholds are poorly defined."),
        _p("RESULTS", "title_1", "Copy number"),
        _p("RESULTS", "paragraph", "MET CN >= 6 was actionable."),
        _p("REF", "ref", ""),
    ]}
    pmid, md = to_markdown(doc)
    assert pmid == "36044468"
    assert md.splitlines()[0] == "# MET amplification by NGS"
    assert "## Abstract" in md and "### Purpose:" in md
    assert "## Results\n\n### Copy number\n\nMET CN >= 6 was actionable." in md
    assert "## References" not in md  # empty passages are dropped
