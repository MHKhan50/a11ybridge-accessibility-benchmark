"""Browser-level checks for accessible names in synthetic fixtures."""

import pytest
from playwright.sync_api import sync_playwright

from a11ybridge.fixtures import TASKS, fixture_path


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as playwright:
        instance = playwright.chromium.launch(headless=True)
        yield instance
        instance.close()


@pytest.mark.parametrize("task", TASKS, ids=lambda task: task.task_id)
def test_baseline_has_expected_accessible_name(browser, task):
    page = browser.new_page()

    try:
        page.goto(fixture_path(task, "baseline").as_uri())

        locator = page.get_by_role(
            task.role,
            name=task.expected_name,
            exact=True,
        )

        assert locator.count() == 1
    finally:
        page.close()


@pytest.mark.parametrize("task", TASKS, ids=lambda task: task.task_id)
def test_defect_removes_expected_accessible_name(browser, task):
    page = browser.new_page()

    try:
        page.goto(fixture_path(task, "defect").as_uri())

        locator = page.get_by_role(
            task.role,
            name=task.expected_name,
            exact=True,
        )

        assert locator.count() == 0

        html = fixture_path(task, "defect").read_text(encoding="utf-8")
        assert task.expected_name in html
    finally:
        page.close()
