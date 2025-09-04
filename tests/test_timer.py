import pytest
from taskon.timer import Timer
from taskon.config import TaskConfig

class DummyRoot:
    def after(self, ms, func):
        return 1
    def after_cancel(self, timer):
        pass

def test_timer_initialization():
    config = TaskConfig()
    root = DummyRoot()
    timer = Timer(root, None, None, None, None, config)
    assert timer.remaining == 0
    assert timer.counter_seconds == config.COUNTER_SECOND
