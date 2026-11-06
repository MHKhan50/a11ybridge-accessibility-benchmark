"""Validated aggregation of benchmark execution results."""

from collections import defaultdict
from typing import Iterable


def _parse_success(value) -> bool:
    if isinstance(value, bool):
        return value

    if isinstance(value, str):
        normalized = value.strip().lower()

        if normalized in ("true", "1", "yes"):
            return True

        if normalized in ("false", "0", "no"):
            return False

    raise ValueError(
        "Invalid success value %r; expected a boolean or supported boolean string."
        % (value,)
    )


def summarize_rows(rows: Iterable[dict]) -> dict:
    groups = defaultdict(list)
    total = 0

    for row in rows:
        if not all(key in row for key in ("task_id", "variant", "success")):
            raise KeyError(
                "Each result row must contain task_id, variant and success"
            )

        success = _parse_success(row["success"])
        groups[(row["task_id"], row["variant"])].append(success)
        total += 1

    grouped = []

    for (task_id, variant), outcomes in sorted(groups.items()):
        runs = len(outcomes)
        successes = sum(outcomes)

        grouped.append({
            "task_id": task_id,
            "variant": variant,
            "runs": runs,
            "successes": successes,
            "failures": runs - successes,
            "success_rate": successes / runs,
        })

    return {
        "total_runs": total,
        "groups": grouped,
    }
