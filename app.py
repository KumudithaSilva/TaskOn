from timer import Timer
from audio_service import IAudioService
from ui import TaskOnUI

class TaskOnApp:
    WORK_MIN = 1
    SHORT_BREAK_MIN = 1
    LONG_BREAK_MIN = 1

    def __init__(self, root, images, audio_service: IAudioService):
        self.root = root
        self.images = images
        self.audio_service = audio_service

        self.reps = 0
        self.timer = Timer(root, self.on_tick, self.on_tick_alarm, self.on_finish)
        self.ui = TaskOnUI(root, images, self.start, self.reset)

    def start(self):
        if self.timer.is_running():
            return
        self.timer.start_tick()

        self.reps += 1
        if self.reps % 2 == 1:
            self.timer.remaining = self.WORK_MIN * 60
        elif self.reps == 8:
            self.timer.remaining = self.LONG_BREAK_MIN * 60
        else:
            self.timer.remaining = self.SHORT_BREAK_MIN * 60


    def reset(self):
        pass

    def on_tick(self, seconds):
        self.ui.update_count_down_timer(seconds)

    def on_tick_alarm(self, minutes, seconds):
        self.ui.update_alarm_timer(minutes, seconds)

    def on_finish(self):
        self.audio_service.play("beep.wav")






