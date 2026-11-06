import pytest

from a11ybridge.metrics import summarize_rows


def test_summarize_boolean_and_csv_string_values():
    rows = [
        {"task_id": "button_name", "variant": "baseline", "success": True},
        {"task_id": "button_name", "variant": "baseline", "success": "False"},
        {"task_id": "link_name", "variant": "defect", "success": False},
    ]

    result = summarize_rows(rows)

    assert result["total_runs"] == 3
    assert result["groups"] == [
        {
            "task_id": "button_name",
            "variant": "baseline",
            "runs": 2,
            "successes": 1,
            "failures": 1,
            "success_rate": 0.5,
        },
        {
            "task_id": "link_name",
            "variant": "defect",
            "runs": 1,
            "successes": 0,
            "failures": 1,
            "success_rate": 0.0,
        },
    ]


def test_empty_input_returns_empty_summary():
    assert summarize_rows([]) == {"total_runs": 0, "groups": []}


@pytest.mark.parametrize("value", ["", "unknown", "2", None, 1, [], {}])
def test_invalid_success_values_are_rejected(value):
    rows = [
        {"task_id": "button_name", "variant": "baseline", "success": value}
    ]

    with pytest.raises(ValueError, match="Invalid success value"):
        summarize_rows(rows)


def test_missing_required_field_is_rejected():
    rows = [{"task_id": "button_name", "variant": "baseline"}]

    with pytest.raises(KeyError, match="task_id, variant and success"):
        summarize_rows(rows)


def test_supported_string_boolean_values():
    rows = [
        {"task_id": "button_name", "variant": "baseline", "success": " YES "},
        {"task_id": "button_name", "variant": "baseline", "success": "no"},
        {"task_id": "button_name", "variant": "baseline", "success": "1"},
        {"task_id": "button_name", "variant": "baseline", "success": "0"},
    ]

    group = summarize_rows(rows)["groups"][0]

    assert group["runs"] == 4
    assert group["successes"] == 2
    assert group["failures"] == 2
    assert group["success_rate"] == 0.5
