from timer import Timer
from audio_service import IAudioService
from ui import TaskOnUI

class TaskOnApp:
    WORK_MIN = 20
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20
    WORK_REPS = 5

    def __init__(self, root, images, audio_service: IAudioService):
        self.root = root
        self.images = images
        self.audio_service = audio_service

        self.reps = 0
        self.work_reps = 0

        self.timer = Timer(root, self.on_tick, self.on_tick_alarm, self.on_tick_finish,  self.on_alarm_finish)
        self.ui = TaskOnUI(root, images, self.start, self.reset)

    def start(self):
        self.ui.clear_tick_timer()
        self.ui.clear_alarm_timer()
        if self.timer.is_tick_timer_running():
            return

        self.reps += 1
        if self.reps % 2 == 1:
            # self.timer.remaining = self.WORK_MIN * 60
            self.work_reps += 1
            self.timer.remaining = self.WORK_MIN
            self.ui.update_logo(self.images["work"])
        elif self.reps == 8:
            # self.timer.remaining = self.LONG_BREAK_MIN * 60
            self.timer.remaining = self.LONG_BREAK_MIN
            self.ui.update_logo(self.images["long_break"])
            self.ui.add_checkmark(self.images["checkbox"])
        else:
            # self.timer.remaining = self.SHORT_BREAK_MIN * 60
            self.timer.remaining = self.SHORT_BREAK_MIN
            self.ui.update_logo(self.images["short_break"])
            self.ui.add_checkmark(self.images["checkbox"])

        self.timer.start_tick()

    def end(self):
        self.ui.end_alarm_timer()
        self.reps = 0
        self.work_reps = 0

    def reset(self):
        self.reps = 0
        self.work_reps = 0
        self.ui.update_sub_logo(self.images["oak"])
        self.ui.clear_tick_timer()
        self.ui.clear_alarm_timer()
        self.ui.clear_checkmarks()
        self.timer.cancel()

    def on_tick(self, seconds):
        self.ui.update_count_down_timer(seconds)

    def on_tick_alarm(self, minutes, seconds):
        self.ui.update_alarm_timer(minutes, seconds)

    def on_tick_finish(self):
        self.audio_service.play("beep.wav")
        self.ui.clear_alarm_timer()
        self.timer.rest_tick()

    def on_alarm_finish(self):
        if self.work_reps >= self.WORK_REPS:
            self.ui.add_checkmark(self.images["checkbox"])
            self.audio_service.play("congratulations.wav")
            self.ui.update_sub_logo(self.images["oak"])
            self.end()
        else:
            self.ui.clear_alarm_timer()
            self.start()








