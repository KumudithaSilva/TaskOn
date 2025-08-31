from timer import Timer
from audio_service import IAudioService
from ui import TaskOnUI

class TaskOnApp:
    WORK_MIN = 2
    SHORT_BREAK_MIN = 1
    LONG_BREAK_MIN = 3

    def __init__(self, root, images, audio_service: IAudioService):
        self.root = root
        self.images = images
        self.audio_service = audio_service

        self.reps = 0
        self.timer = Timer(root, self.on_tick, self.on_finish)
        self.ui = TaskOnUI(root, images, self.start, self.reset)

    def start(self):
        if self.timer.is_running():
            return
        self.timer.start_tick()

    def reset(self):
        pass

    def on_tick(self, seconds):
        self.ui.update_count_down_timer(seconds)

    def on_finish(self):
        pass





