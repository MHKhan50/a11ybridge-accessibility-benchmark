"""Fixture registry for the controlled synthetic task pairs."""
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures"


@dataclass(frozen=True)
class TaskSpec:
    task_id: str
    role: str
    expected_name: str
    action: str
    fixture_basename: str
    completion_selector: str


TASKS: Tuple[TaskSpec, ...] = (
    TaskSpec("button_name", "button", "Save report", "click", "button", "#save-status"),
    TaskSpec("link_name", "link", "Download results", "click", "link", "#download-status"),
    TaskSpec("textbox_name", "textbox", "Project title", "fill", "textbox", "#title-preview"),
)

VARIANTS = ("baseline", "defect")


def fixture_path(task: TaskSpec, variant: str) -> Path:
    if variant not in VARIANTS:
        raise ValueError("variant must be one of: baseline, defect")
    return FIXTURE_DIR / (task.fixture_basename + "_" + variant + ".html")


def get_task(task_id: str) -> TaskSpec:
    for task in TASKS:
        if task.task_id == task_id:
            return task
    raise ValueError("Unknown task_id: " + task_id)
