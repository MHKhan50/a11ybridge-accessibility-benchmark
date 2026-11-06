"""Tables and figures from agent_runs.jsonl (no model needed): python -m agent_study.analysis"""
from __future__ import annotations

import json
import random
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

OUT = Path(__file__).resolve().parent / "results"
RESULTS = ["target", "danger", "wrong", "abstain", "invalid"]


def load(out: Path = OUT) -> Tuple[List[dict], List[dict]]:
    runs = [json.loads(l) for l in (out / "agent_runs.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    pages = [json.loads(l) for l in (out / "pages.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    return runs, pages


def boot_diff(a: Dict[str, int], b: Dict[str, int], n_boot: int = 2000, seed: int = 42) -> Tuple[float, float, float]:
    """Paired difference mean(b - a) over shared units, with a bootstrap 95% interval."""
    keys = sorted(set(a) & set(b))
    if not keys:
        return float("nan"), float("nan"), float("nan")
    d = [b[k] - a[k] for k in keys]
    rng = random.Random(seed)
    means = sorted(sum(rng.choice(d) for _ in d) / len(d) for _ in range(n_boot))
    return sum(d) / len(d), means[int(0.025 * n_boot)], means[int(0.975 * n_boot) - 1]


def analyse(out: Path = OUT) -> dict:
    runs, pages = load(out)
    models = sorted({r["model"] for r in runs})
    cell: Dict[tuple, Dict[str, int]] = defaultdict(lambda: {k: 0 for k in RESULTS})
    unit: Dict[tuple, Dict[str, int]] = defaultdict(dict)
    for r in runs:
        cell[(r["model"], r["lang"], r["kind"], r["defect"])][r["result"]] += 1
        unit[(r["model"], r["lang"], r["kind"], r["defect"])][f"{r['task']}|{r['layout']}"] = int(r["result"] == "target")
    table = []
    for (m, lang, kind, defect), c in sorted(cell.items()):
        n = sum(c.values())
        table.append({"model": m, "lang": lang, "kind": kind, "defect": defect, "n": n,
                      **{k: c[k] / n for k in RESULTS}})
    contrasts = []
    for (m, lang, kind, defect), u in sorted(unit.items()):
        if defect != "baseline":
            diff, lo, hi = boot_diff(unit[(m, lang, kind, "baseline")], u)
            contrasts.append({"model": m, "lang": lang, "kind": kind, "comparison": f"{defect} minus baseline",
                              "diff": diff, "ci95": [lo, hi], "n": len(u)})
    for m in models:
        for kind in ("button", "link", "textbox"):
            en, ru = {}, {}
            for (mm, lang, k, defect), u in unit.items():
                if mm == m and k == kind:
                    (en if lang == "en" else ru).update({f"{defect}|{key}": v for key, v in u.items()})
            diff, lo, hi = boot_diff(en, ru)
            contrasts.append({"model": m, "lang": "both", "kind": kind, "comparison": "Roman Urdu minus English",
                              "diff": diff, "ci95": [lo, hi], "n": len(set(en) & set(ru))})
    script = defaultdict(list)
    for p in pages:
        script[(p["kind"], p["defect"])].append(int(p["exact_locator_ok"]))
    exact = [{"kind": k, "defect": d, "success": sum(v) / len(v), "n": len(v)} for (k, d), v in sorted(script.items())]
    res = {"calls": len(runs), "models": models, "table": table, "contrasts": contrasts, "exact_locator": exact}
    (out / "results.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    _write_md(res, out)
    _figure(res, out)
    return res


def _write_md(res: dict, out: Path) -> None:
    L = ["# Results", "", "## Share of runs by outcome (%)", "",
         "| Model | Lang | Element | Defect | n | Target | Risky look-alike | Other wrong | Said none | Invalid |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for r in res["table"]:
        L.append(f"| {r['model']} | {r['lang']} | {r['kind']} | {r['defect']} | {r['n']} | "
                 + " | ".join(f"{100*r[k]:.0f}" for k in RESULTS) + " |")
    L += ["", "## Paired differences in target choice (percentage points, bootstrap 95% CI)", "",
          "| Model | Lang | Element | Comparison | Difference | 95% CI | Units |", "|---|---|---|---|---|---|---|"]
    for c in res["contrasts"]:
        L.append(f"| {c['model']} | {c['lang']} | {c['kind']} | {c['comparison']} | {100*c['diff']:+.1f} | "
                 f"[{100*c['ci95'][0]:+.1f}, {100*c['ci95'][1]:+.1f}] | {c['n']} |")
    L += ["", "## Exact role-and-name locator (the v0.2.0 script rule)", "", "| Element | Defect | Success | Pages |",
          "|---|---|---|---|"]
    for e in res["exact_locator"]:
        L.append(f"| {e['kind']} | {e['defect']} | {100*e['success']:.0f}% | {e['n']} |")
    (out / "tables.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def _figure(res: dict, out: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    rows = [r for r in res["table"] if r["kind"] == "button"]
    defects = ["baseline", "generic_name", "icon_no_name", "img_no_alt", "div_not_button", "duplicate_name"]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.2), sharey=True)
    colours = ["#1f4e79", "#2b5ce6", "#35c3ff", "#e8833a", "#9aa5b1"]
    for ax, lang, title in zip(axes, ["en", "ru"], ["English instruction", "Roman Urdu instruction"]):
        width = 0.8 / max(1, len(res["models"]))
        for i, m in enumerate(res["models"]):
            vals = []
            for d in defects:
                hit = [r for r in rows if r["model"] == m and r["lang"] == lang and r["defect"] == d]
                vals.append(100 * hit[0]["target"] if hit else 0)
            ax.bar([j + i * width - 0.4 + width / 2 for j in range(len(defects))], vals, width,
                   label=m, color=colours[i % len(colours)])
        ax.set_xticks(range(len(defects)))
        ax.set_xticklabels([d.replace("_", " ") for d in defects], rotation=20, fontsize=8)
        ax.set_title(title)
        ax.set_ylim(0, 105)
        ax.grid(axis="y", alpha=0.3)
    axes[0].set_ylabel("chose the right button (%)")
    axes[1].legend(fontsize=8, loc="lower left")
    fig.tight_layout()
    fig.savefig(out / "fig_buttons.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    analyse()
