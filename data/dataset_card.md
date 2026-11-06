# Dataset card: A11yBridge synthetic browser-task results

## Title
A11yBridge v0.1.0 — Synthetic Role-and-Name Browser Task Benchmark

## Subtitle
Controlled HTML fixtures for measuring deterministic browser-task execution under selected accessible-name and label defects.

## Description
This package generates a small CSV dataset from six local HTML fixtures: baseline and defect variants for a button, link, and textbox. A Playwright script uses exact role-and-name locators and records whether each task completes.

## Intended uses
- Reproducing the prototype's three controlled examples.
- Teaching or demonstrating how accessible names influence role/name locator resolution.
- Developing a more comprehensive benchmark protocol.

## Out-of-scope uses
- WCAG conformance certification or legal compliance decisions.
- Estimating prevalence or severity of accessibility defects on the public web.
- Predicting real users' success, screen-reader experience, or assistive-technology behaviour.
- Comparing commercial agents or claiming general agent capability from these fixtures.

## Composition
The source fixtures are authored HTML files included in the repository. A default run emits six rows (three tasks × two variants × one repetition). Repetition count is configurable. No personal data is collected and no network access is required by the benchmark itself.

## Collection and generation
Data is generated locally by `run_experiment.py` using Playwright and Chromium. Each row contains task/variant metadata, locator count, execution success, exception details, elapsed time, and runtime metadata. See `docs/experimental_protocol_v1.md`.

## Quality checks
Unit tests check fixture presence, task registration, expected baseline strings, baseline/defect distinction, and summary aggregation. These checks validate package structure, not the construct validity of the benchmark.

## Known limitations
Only three defect/task pairs are implemented. Each defect changes a single fixture property, but the pairs are not matched on all possible browser semantics. The benchmark does not include human participants, screen readers, mobile browsers, dynamic single-page applications, multilingual names, visual layout, keyboard-only navigation, focus order, or a representative website sample. Timing is exploratory only.

## Versioning and updates
Version: 0.1.0. The CSV schema is documented in `DATA_DICTIONARY.md`. Any schema or fixture changes should increment the package version and be recorded in a changelog.

## License and citation
Software and generated example data are released under the MIT License in this prototype package. No DOI or publication is assigned. Suggested citation: Hussain, M. (2026). *A11yBridge v0.1.0: Synthetic Role-and-Name Browser Task Benchmark* (software prototype). Do not cite this as a peer-reviewed study.

## Contact and maintenance
Author/maintainer: Muzammal Hussain. Update frequency: no fixed schedule; versioned releases when the protocol or implementation changes.
