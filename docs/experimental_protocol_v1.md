# Experimental protocol v1.0 — A11yBridge v0.1.0

## 1. Status and scope

This document specifies a reproducible software prototype experiment. It is not a preregistration, human-subjects protocol, WCAG audit method, or completed empirical study.

## 2. Research question

Within a controlled set of local HTML fixtures, do selected accessible-name/label defects change the success of browser tasks that locate elements by exact ARIA role and accessible name?

## 3. Hypothesis (mechanistic, fixture-scoped)

For each task, the baseline fixture should expose exactly one element matching the configured role and expected accessible name, allowing the action and completion marker to succeed. The corresponding defect fixture is designed to alter that accessible name or label relationship, so the exact locator should fail to resolve as intended. This is a testable implementation expectation, not a generalized scientific hypothesis.

## 4. Experimental units and conditions

The execution row is one task × variant × repetition. Tasks: button, link, textbox. Variants: baseline and defect. The default run contains six rows. Repetitions are independent executions of the same deterministic fixtures but are not independent samples of real websites or users.

## 5. Task policy

- Button: exact role `button`, name `Save report`; click; wait for `#save-status`.
- Link: exact role `link`, name `Download results`; click; wait for `#download-status`.
- Textbox: exact role `textbox`, name `Project title`; fill with a fixed test string; wait for `#title-preview`.

A run is successful only if exactly one locator matches, the action completes, and the task-specific marker becomes visible.

## 6. Execution procedure

1. Create and activate a Python virtual environment.
2. Install dependencies from `requirements.txt` and Chromium using `python -m playwright install chromium`.
3. Run tests with `python -m pytest -q`.
4. Execute `python run_experiment.py --output-dir results --repetitions 1`.
5. Preserve `raw_results.csv`, `summary.json`, and `run_metadata.json` together.
6. Record package version, machine/runtime details, and any deviations when reporting results.

## 7. Outcomes

Primary outcome: binary task execution success. Supporting diagnostics: locator count and exception details. Duration in milliseconds is exploratory and should not be interpreted as a stable latency estimate without a controlled performance protocol.

## 8. Analysis plan

Report raw counts and success rates by task and variant. For this six-row prototype, do not run inferential significance tests or claim population-level effects. With repeated executions, report denominators and raw counts; repetitions do not create external validity. A future study should add more independently authored pages, defect classes, browser engines, agent policies, preregistered hypotheses, power analysis, and appropriate clustered/statistical methods.

## 9. Threats to validity

- Construct validity: role/name locator success is a narrow proxy, not accessibility itself.
- Internal validity: hand-authored fixtures simplify the causal mechanism and omit interacting defects.
- External validity: three local examples cannot represent websites, user populations, assistive technologies, or browser diversity.
- Measurement validity: Playwright accessible-name computation may differ from actual assistive-technology interactions; elapsed time is machine-dependent.

## 10. Ethics, privacy, and safety

No human participants, external sites, or personal data are involved in the included fixtures. If future work recruits participants or collects browsing data, obtain appropriate ethics review and informed consent, minimize data, and establish retention/security controls.

## 11. Reproducibility and deviations

The fixture files and task registry are version-controlled in this package. Record dependency/browser versions and any local modifications. Do not silently modify fixtures between runs. Report failed or incomplete runs rather than dropping rows.
