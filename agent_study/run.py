"""Resumable runner: render pages once, then ask each local model to choose an element.

    python -m agent_study.run                     # all models, about 1.5 hours on a MacBook M4
    python -m agent_study.run --models qwen2.5:3b --limit 6
Every call is appended to agent_study/results/agent_runs.jsonl; finished calls are skipped.
"""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from typing import Callable, Dict, List, Optional

from .agent import OllamaChat, choose, score
from .pages import build_pages
from .snapshot import exact_locator_ok, numbered, snapshot_page

MODELS = ["qwen2.5:3b", "llama3.2:3b", "qwen2.5:7b", "mistral:7b", "llama3.1:8b"]
LANGS = ["en", "ru"]
OUT = Path(__file__).resolve().parent / "results"


def render_pages(out: Path) -> List[Dict[str, object]]:
    path = out / "pages.jsonl"
    if path.exists():
        return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]
    from playwright.sync_api import sync_playwright
    rows = []
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for pg in build_pages():
            snap = snapshot_page(page, pg["html"])
            rows.append({**pg, **snap, "exact_locator_ok": exact_locator_ok(page, pg["kind"], pg["target_name"])})
        browser.close()
    out.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    return rows


def run(models: List[str], out: Path = OUT, limit: Optional[int] = None,
        chat_factory: Callable[[str], Callable] = OllamaChat) -> Path:
    pages = render_pages(out)
    if limit:
        pages = pages[:limit]
    runs = out / "agent_runs.jsonl"
    done = set()
    if runs.exists():
        for l in runs.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                done.add((r["model"], r["page_id"], r["lang"]))
    todo = [(m, p, lang) for m in models for p in pages for lang in LANGS if (m, p["page_id"], lang) not in done]
    print(f"{len(done)} calls already done, {len(todo)} to go.", flush=True)
    t0 = time.time()
    with runs.open("a", encoding="utf-8") as f:
        for i, (m, p, lang) in enumerate(todo, start=1):
            try:
                res = choose(chat_factory(m), numbered(p["lines"]), p[lang])
            except Exception as exc:  # noqa: BLE001 - keep the run going; retried on the next start
                print(f"failed {m} {p['page_id']} {lang}: {exc}", flush=True)
                continue
            rec = {"model": m, "page_id": p["page_id"], "task": p["task"], "kind": p["kind"], "defect": p["defect"],
                   "layout": p["layout"], "lang": lang, "instruction": p[lang], **res,
                   "result": score(res["choice"], p["outcome"])}
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
            f.flush()
            if i % 10 == 0 or i == len(todo):
                eta = (time.time() - t0) / i * (len(todo) - i) / 3600
                print(f"{i}/{len(todo)}  {m:12s} {p['page_id'][:40]:40s} {lang} {rec['result']:8s} about {eta:.1f} h left",
                      flush=True)
    print(f"Saved {runs}")
    return runs


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", nargs="+", default=MODELS)
    ap.add_argument("--limit", type=int, default=None)
    a = ap.parse_args()
    run(a.models, limit=a.limit)


if __name__ == "__main__":
    main()
