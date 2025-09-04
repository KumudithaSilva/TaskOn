from taskon.task_manager import TaskManager
from taskon.config import TaskConfig


def test_next_session_logic():
    config = TaskConfig(work_reps=4)
    manager = TaskManager(config)

    assert manager.next_session() == "work"
    assert manager.next_session() == "short_break"
    assert manager.next_session() == "work"
