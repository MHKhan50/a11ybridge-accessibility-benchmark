"""Offline tests for the LLM agent study (no model needed; Chromium needed for the snapshot tests)."""
from __future__ import annotations

import json

import pytest

from agent_study.agent import parse_choice, score
from agent_study.pages import DEFECTS, TASKS, build_pages


def test_page_set_is_complete():
    pages = build_pages()
    expected = sum(len(DEFECTS[str(t["kind"])]) for t in TASKS) * 2
    assert len(pages) == expected == 168
    assert len({p["page_id"] for p in pages}) == len(pages)
    assert all(p["html"].count('data-target="1"') == 1 for p in pages)


def test_parse_and_score():
    outcome = ["other", "danger", "target", "control"]
    assert parse_choice("Line 3.") == 3 and parse_choice("none") is None
    assert score(3, outcome) == "target" and score(2, outcome) == "danger"
    assert score(4, outcome) == "wrong" and score(0, outcome) == "abstain"
    assert score(9, outcome) == "invalid" and score(None, outcome) == "invalid"


@pytest.fixture(scope="module")
def rendered(tmp_path_factory):
    pytest.importorskip("playwright")
    from agent_study.run import render_pages
    out = tmp_path_factory.mktemp("res")
    try:
        return out, render_pages(out)
    except Exception as exc:  # browser not installed
        pytest.skip(f"Chromium not available: {exc}")


def test_every_page_has_one_target_line(rendered):
    _, pages = rendered
    assert all(p["outcome"].count("target") == 1 for p in pages)
    exact = {(p["kind"], p["defect"]): p["exact_locator_ok"] for p in pages}
    assert exact[("button", "baseline")] and not exact[("button", "generic_name")]
    assert exact[("textbox", "placeholder_only")]


def test_end_to_end_with_scripted_models(rendered):
    from agent_study.analysis import analyse
    from agent_study.run import run
    out, pages = rendered
    by_tree = {}
    for p in pages:
        by_tree[p["page_id"]] = p["outcome"].index("target") + 1

    def oracle_factory(model):
        def chat(messages):
            if model == "never":
                return "0"
            tree = messages[1]["content"]
            for p in pages:
                from agent_study.snapshot import numbered
                if numbered(p["lines"]) in tree:
                    return str(by_tree[p["page_id"]])
            return "0"
        return chat

    run(["oracle", "never"], out=out, limit=8, chat_factory=oracle_factory)
    rows = [json.loads(l) for l in (out / "agent_runs.jsonl").read_text().splitlines()]
    assert len(rows) == 8 * 2 * 2
    assert all(r["result"] == "target" for r in rows if r["model"] == "oracle")
    assert all(r["result"] == "abstain" for r in rows if r["model"] == "never")
    run(["oracle"], out=out, limit=8, chat_factory=oracle_factory)  # resume adds nothing
    assert len((out / "agent_runs.jsonl").read_text().splitlines()) == 32
    res = analyse(out)
    assert (out / "tables.md").exists() and (out / "fig_buttons.png").exists() and res["calls"] == 32
