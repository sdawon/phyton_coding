from models.enums import TaskScope, TaskStatus, WaitStatus


def test_task_status_values() -> None:
    assert len(TaskStatus) == 6
    assert TaskStatus.INBOX.value == "INBOX"
    assert TaskStatus.COMPLETED.value == "COMPLETED"


def test_task_scope_values() -> None:
    assert len(TaskScope) == 4
    assert TaskScope.PROJECT.value == "PROJECT"
    assert TaskScope.PERSONAL.value == "PERSONAL"


def test_wait_status_values() -> None:
    assert len(WaitStatus) == 3
    assert WaitStatus.WAITING.value == "WAITING"
    assert WaitStatus.RECEIVED.value == "RECEIVED"
