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


def test_replace_refetches_pdf_text_and_backs_it_up(tmp_path, monkeypatch):
    from cbio_kb.ingest import bioc

    papers, backup = tmp_path / "papers", tmp_path / "backup"
    papers.mkdir()
    (tmp_path / "map.csv").write_text("studyId,pmid,pmcid,doi\n")
    (papers / "111.md").write_text("---\npmid: 111\npmcid: PMC1\nstudy_id: s1\n"
                                   "extractor_version: 1\ntitle:\n---\n\n## Full Text\n\npdf text\n")
    (papers / "222.md").write_text("---\npmid: 222\npmcid: PMC2\nextractor_version: bioc-1\n---\n\nbioc\n")
    (papers / "333.md").write_text("---\npmid: 333\npmcid: PMC3\nextractor_version: 1\n---\n\nkept\n")
    fetched = []

    def fake_fetch(pmcid, session, retries=4):
        fetched.append(pmcid)
        if pmcid == "PMC3":
            return None
        return {"passages": [_p("TITLE", "front", "T", **{"article-id_pmid": "111"}),
                             _p("RESULTS", "paragraph", "Structured text.")]}

    monkeypatch.setattr(bioc, "fetch", fake_fetch)
    monkeypatch.setattr(bioc.time, "sleep", lambda s: None)
    bioc.run(tmp_path / "map.csv", papers, tmp_path / "pdfs", replace=True, backup_dir=backup)

    assert sorted(fetched) == ["PMC1", "PMC3"]  # the BioC paper isn't re-fetched
    new = (papers / "111.md").read_text()
    assert "extractor_version: bioc-1" in new and "study_id: s1" in new
    assert "## Results\n\nStructured text." in new
    assert "pdf text" in (backup / "111.md").read_text()
    assert (papers / "333.md").read_text().endswith("kept\n")  # no BioC: unchanged
    assert not (backup / "333.md").exists()


def test_record_without_pmid_is_accepted_only_on_matching_doi(tmp_path, monkeypatch):
    from cbio_kb.ingest import bioc

    papers = tmp_path / "papers"
    papers.mkdir()
    (tmp_path / "map.csv").write_text("studyId,pmid,pmcid,doi\n")
    for pmid, pmcid in (("111", "PMC1"), ("222", "PMC2")):
        (papers / f"{pmid}.md").write_text(f"---\npmid: {pmid}\npmcid: {pmcid}\ndoi: 10.1/X{pmid}\n"
                                           "extractor_version: 1\n---\n\nold\n")

    def fake_fetch(pmcid, session, retries=4):
        doi = "10.1/x111" if pmcid == "PMC1" else "10.1/other"
        return {"passages": [_p("TITLE", "front", "T", **{"article-id_doi": doi}),
                             _p("RESULTS", "paragraph", "New text.")]}

    monkeypatch.setattr(bioc, "fetch", fake_fetch)
    monkeypatch.setattr(bioc.time, "sleep", lambda s: None)
    bioc.run(tmp_path / "map.csv", papers, tmp_path / "pdfs", replace=True, backup_dir=tmp_path / "b")
    assert "New text." in (papers / "111.md").read_text()   # DOI matches (case-insensitive)
    assert (papers / "222.md").read_text().endswith("old\n")  # different DOI: refused
