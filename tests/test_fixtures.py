from a11ybridge.fixtures import TASKS, VARIANTS, fixture_path, get_task


def test_all_registered_fixtures_exist():
    assert len(TASKS) == 3
    assert set(VARIANTS) == {"baseline", "defect"}
    for task in TASKS:
        for variant in VARIANTS:
            assert fixture_path(task, variant).is_file()


def test_unknown_task_rejected():
    try:
        get_task("not_a_task")
    except ValueError as exc:
        assert "Unknown task_id" in str(exc)
    else:
        raise AssertionError("Unknown task should raise ValueError")
