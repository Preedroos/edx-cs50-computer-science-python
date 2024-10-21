import pytest
from todo import add_task, delete_task, complete_task, view_tasks


def test_add_task():
    tasks = []
    result = add_task("New Task", tasks)
    assert len(result) == 1
    assert result[0]['task'] == "New Task"
    assert result[0]['completed'] is False


def test_complete_task():
    tasks = [{'task': 'Task 1', 'completed': False}]
    result = complete_task(1, tasks)
    assert result[0]['completed'] is True


def test_delete_task():
    tasks = [{'task': 'Task 1', 'completed': False}]
    result = delete_task(1, tasks)
    assert len(result) == 0


def test_view_tasks():
    tasks = [{'task': 'Task 1', 'completed': False}]
    result = view_tasks(tasks)
    assert isinstance(result, list)
    assert len(result) == 1

    empty_result = view_tasks([])
    assert empty_result == 'No tasks available.'
