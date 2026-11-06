"""Playwright execution engine for local synthetic fixtures."""

import csv
import json
import platform
import sys
import time
import uuid

from datetime import datetime, timezone
from importlib.metadata import version as package_version
from pathlib import Path
from typing import List

from playwright.sync_api import sync_playwright

from .fixtures import TASKS, VARIANTS, fixture_path
from .metrics import summarize_rows


CSV_FIELDS = [
    "run_id",
    "task_id",
    "variant",
    "role",
    "expected_name",
    "expected_success",
    "success",
    "outcome_match",
    "failure_stage",
    "locator_count",
    "exception_type",
    "exception_message",
    "navigation_duration_ms",
    "locator_lookup_duration_ms",
    "action_completion_duration_ms",
    "total_duration_ms",
    "cleanup_exception_type",
    "cleanup_exception_message",
    "python_version",
    "platform",
]


def _new_result(task, variant: str) -> dict:
    return {
        "run_id": str(uuid.uuid4()),
        "task_id": task.task_id,
        "variant": variant,
        "role": task.role,
        "expected_name": task.expected_name,
        "expected_success": variant == "baseline",
        "success": False,
        "outcome_match": None,
        "failure_stage": "",
        "locator_count": None,
        "exception_type": "",
        "exception_message": "",
        "navigation_duration_ms": None,
        "locator_lookup_duration_ms": None,
        "action_completion_duration_ms": None,
        "total_duration_ms": None,
        "cleanup_exception_type": "",
        "cleanup_exception_message": "",
        "python_version": platform.python_version(),
        "platform": platform.platform(),
    }


def _record_exception(result: dict, exc: Exception, stage: str) -> None:
    result["failure_stage"] = stage
    result["exception_type"] = type(exc).__name__
    result["exception_message"] = str(exc).replace("\n", " ")[:500]


def _evaluate_outcome(result: dict) -> None:
    stage = result["failure_stage"]

    # Infrastructure failures cannot be scored as accessibility outcomes.
    if stage in ("fixture_resolution", "navigation", "page_creation"):
        result["outcome_match"] = None
        return

    if result["variant"] == "baseline":
        result["outcome_match"] = result["success"]
        return

    # A defect is correctly detected only when the expected locator
    # does not resolve to exactly one element.
    result["outcome_match"] = (
        not result["success"]
        and stage == "locator_lookup"
        and result["locator_count"] != 1
    )


def execute_fixture(page, task, variant: str) -> dict:
    result = _new_result(task, variant)
    total_started = time.perf_counter()
    stage = "fixture_resolution"

    try:
        path = fixture_path(task, variant)

        stage = "navigation"
        navigation_started = time.perf_counter()
        try:
            page.goto(path.as_uri())
        finally:
            result["navigation_duration_ms"] = round(
                (time.perf_counter() - navigation_started) * 1000, 3
            )

        stage = "locator_lookup"
        lookup_started = time.perf_counter()
        try:
            locator = page.get_by_role(
                task.role,
                name=task.expected_name,
                exact=True,
            )
            result["locator_count"] = locator.count()
        finally:
            result["locator_lookup_duration_ms"] = round(
                (time.perf_counter() - lookup_started) * 1000, 3
            )

        if result["locator_count"] != 1:
            raise AssertionError(
                "Expected exactly one matching role/name locator; found %s"
                % result["locator_count"]
            )

        stage = "action_completion"
        action_started = time.perf_counter()

        try:
            if task.action == "click":
                locator.click()
            elif task.action == "fill":
                locator.fill("A11yBridge test project")
            else:
                raise ValueError("Unsupported action: " + task.action)

            page.locator(task.completion_selector).wait_for(
                state="visible",
                timeout=1500,
            )
            result["success"] = True
        finally:
            result["action_completion_duration_ms"] = round(
                (time.perf_counter() - action_started) * 1000, 3
            )

    except Exception as exc:
        _record_exception(result, exc, stage)

    finally:
        result["total_duration_ms"] = round(
            (time.perf_counter() - total_started) * 1000, 3
        )
        _evaluate_outcome(result)

    return result


def _record_page_creation_failure(task, variant: str, exc: Exception) -> dict:
    result = _new_result(task, variant)
    _record_exception(result, exc, "page_creation")
    _evaluate_outcome(result)
    return result


def run_benchmark(
    output_dir: Path,
    repetitions: int = 1,
    headless: bool = True,
) -> dict:
    if repetitions < 1:
        raise ValueError("repetitions must be >= 1")

    output_dir.mkdir(parents=True, exist_ok=True)
    rows: List[dict] = []

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=headless)

        try:
            browser_version = browser.version

            for _ in range(repetitions):
                for task in TASKS:
                    for variant in VARIANTS:
                        try:
                            page = browser.new_page()
                        except Exception as exc:
                            rows.append(
                                _record_page_creation_failure(task, variant, exc)
                            )
                            continue

                        try:
                            result = execute_fixture(page, task, variant)
                        finally:
                            try:
                                page.close()
                            except Exception as exc:
                                result["cleanup_exception_type"] = type(exc).__name__
                                result["cleanup_exception_message"] = (
                                    str(exc).replace("\n", " ")[:500]
                                )

                        rows.append(result)

        finally:
            browser.close()

    with (output_dir / "raw_results.csv").open(
        "w", newline="", encoding="utf-8"
    ) as handle:
        writer = csv.DictWriter(handle, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    summary = summarize_rows(rows)
    summary.update({
        "benchmark": "A11yBridge",
        "version": "0.2.0",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": "synthetic local fixtures; prototype only",
    })

    (output_dir / "summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )

    metadata = {
        "benchmark": "A11yBridge",
        "version": "0.2.0",
        "repetitions": repetitions,
        "tasks": [task.task_id for task in TASKS],
        "variants": list(VARIANTS),
        "headless": headless,
        "browser_engine": "Chromium",
        "browser_version": browser_version,
        "playwright_version": package_version("playwright"),
        "python_version": sys.version,
        "platform": platform.platform(),
        "fixture_source": "package-local HTML files; no network access",
        "timing_definitions": {
            "navigation_duration_ms": "Time spent navigating to the local fixture",
            "locator_lookup_duration_ms": "Time spent locating and counting the expected role/name match",
            "action_completion_duration_ms": "Time spent performing the action and waiting for its completion marker; not applicable when the locator does not match",
            "total_duration_ms": "Elapsed time from before fixture resolution/navigation through task completion or failure; excludes browser launch and page cleanup",
        },
        "outcome_definitions": {
            "expected_success": "True for baseline fixtures and False for defect fixtures",
            "success": "Whether the configured locator, action and completion marker all succeeded",
            "outcome_match": "Whether the observed task outcome matches the expected fixture outcome; null for infrastructure failures",
            "failure_stage": "Execution stage where a task failure occurred; blank when no task failure occurred",
        },
    }

    (output_dir / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n",
        encoding="utf-8",
    )

    return summary
