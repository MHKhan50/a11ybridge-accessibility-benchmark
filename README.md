# A11yBridge v0.1.0

**Beyond WCAG Compliance: Measuring How Accessibility Defects Affect Role-and-Name-Based Browser Task Execution**

A small, reproducible **synthetic prototype** for measuring whether selected accessible-name/label defects interfere with deterministic browser tasks that locate controls by ARIA role and accessible name.

> **Scope warning:** This is not a WCAG conformance tester, accessibility certification tool, assistive-technology simulator, or completed real-world academic study. It uses six hand-authored local HTML fixtures and three narrowly scoped task definitions. Results describe only this harness and its fixtures.

## Research question

Do selected accessibility defects cause measurable failures in browser tasks that use role-and-name-based locators, and how do the three implemented defect classes compare in this fixture set?

## Implemented task pairs

| Task | Accessible baseline | Controlled defect | Expected locator |
|---|---|---|---|
| Button | Button named “Save report” | Button name changed to “Action” | `get_by_role("button", name="Save report", exact=True)` |
| Link | Link named “Download results” | Link name changed to “Open item” | `get_by_role("link", name="Download results", exact=True)` |
| Textbox | Textbox labelled “Project title” | Label `for` no longer matches input `id` | `get_by_role("textbox", name="Project title", exact=True)` |

Each fixture includes a task-specific completion marker. The benchmark records locator count, whether the action completed, exception details, and elapsed time.

## Requirements

- Python 3.9 or later
- Playwright for Python
- Chromium installed through Playwright

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install chromium
python -m pip install -r requirements-dev.txt
python -m pytest -q
python run_experiment.py --output-dir results
```

On macOS, the commands above work in Terminal. If your environment uses `python` rather than `python3`, substitute accordingly.

## Output files

The run creates:

- `results/raw_results.csv` — one row per fixture execution.
- `results/summary.json` — aggregate counts and success rates by task and variant.
- `results/run_metadata.json` — run configuration and environment metadata.

Default design: one execution for each of three tasks × two variants (six rows). Increase repetitions with `--repetitions N`. Use `--headless false` to display Chromium while running.

## Reproducibility

The fixture HTML is stored locally in `a11ybridge/fixtures/`; no external website is contacted. Task order and fixture mapping are fixed. Timing is recorded as descriptive telemetry and is not used as a pass/fail threshold. The benchmark does not currently randomize order, model realistic user behaviour, or estimate population-level effects.

## Interpretation

A failure means that the specified exact role/name locator did not resolve to exactly one element or the intended action/completion marker did not succeed in this controlled fixture. It does **not** establish that a person using a screen reader or another assistive technology would necessarily experience the same outcome. A success does **not** prove that a page is accessible.

Use the protocol in `docs/experimental_protocol_v1.md` before extending or reporting results. The data dictionary and dataset card in `data/` describe the generated CSV and its limitations.

## Project status

v0.1.0 is a harness/prototype release. No empirical claims, statistical significance claims, novelty claims, or market-demand claims are made. Conduct a current literature review and a preregistered, broader evaluation before treating this as a research finding.

## License

MIT. See `LICENSE`.
