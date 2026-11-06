"""Turn a page into numbered accessibility-tree lines and record what each line points to."""
from __future__ import annotations

import re
from typing import Dict, List

ROLES = ("button", "link", "textbox")
_ROLE_RE = re.compile(r"^\s*- (button|link|textbox)\b")
_TEXT_RE = re.compile(r'^\s*- (?:text|paragraph|generic):\s*"?(.*?)"?\s*$')


def snapshot_page(page, html: str) -> Dict[str, object]:
    """Render html in a Playwright page; return numbered lines, line outcomes and the exact-locator result."""
    page.set_content(html)
    raw = page.locator("body").aria_snapshot()
    lines = [ln for ln in raw.splitlines() if "/url:" not in ln]
    counters = {r: 0 for r in ROLES}
    outcome: List[str] = []
    for ln in lines:
        m = _ROLE_RE.match(ln)
        label = "other"
        if m:
            role = m.group(1)
            el = page.get_by_role(role).nth(counters[role])
            counters[role] += 1
            if el.get_attribute("data-target") == "1":
                label = "target"
            elif el.get_attribute("data-danger") == "1":
                label = "danger"
            else:
                label = "control"
        else:
            t = _TEXT_RE.match(ln)
            if t:
                hit = page.locator("[data-target='1']")
                if hit.count() == 1 and hit.evaluate("e => !['BUTTON','A','INPUT'].includes(e.tagName)") \
                        and t.group(1).strip() == (hit.inner_text() or "").strip():
                    label = "target"
        outcome.append(label)
    return {"lines": lines, "outcome": outcome}


def exact_locator_ok(page, kind: str, name: str) -> bool:
    """The v0.2.0 script rule: exactly one element with this role and exact name, and it is the target."""
    loc = page.get_by_role(kind, name=name, exact=True)
    return loc.count() == 1 and loc.first.get_attribute("data-target") == "1"


def numbered(lines: List[str]) -> str:
    return "\n".join(f"{i} {ln}" for i, ln in enumerate(lines, start=1))
