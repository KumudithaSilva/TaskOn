from taskon.timer import Timer
from taskon.audio_service import IAudioService
from taskon.ui import TaskOnUI
from taskon.config import TaskConfig
from taskon.task_manager import TaskManager


class TaskOnApp:
    """
    Main application class to manage task sessions, timers, and UI interactions.

    Attributes:
        root: Tkinter root window.
        images: Dictionary of PhotoImage objects for UI.
        audio_service: Audio service for playback.
        config: Task configuration object.
        task_manager: Manages session repetitions and type.
        timer: Countdown timer for work and break sessions.
        ui: TaskOnUI instance to update visual elements.
    """

    def __init__(self, root, images, audio_service: IAudioService, config: TaskConfig):
        """
        Initialize the TaskOn application.

        Args:
            root: Tkinter root window.
            images: Dictionary of PhotoImage objects for UI.
            audio_service: Audio service instance.
            config: Task configuration object.
        """
        self.root = root
        self.images = images
        self.audio_service = audio_service
        self.config = config

        self.reps = config.INITIAL_VALUE
        self.work_reps = config.INITIAL_VALUE

        self.task_manager = TaskManager(config)
        self.timer = Timer(
            root,
            self.on_tick,
            self.on_tick_alarm,
            self.on_tick_finish,
            self.on_alarm_finish,
            config
        )
        self.ui = TaskOnUI(root, images, self.start, self.reset)

    # --------------------------
    # Session Control Methods
    # --------------------------

    def start(self):
        """Start a new session if no tick timer is running."""
        if self.timer.is_tick_timer_running():
            return

        session_type = self.task_manager.next_session()

        if session_type == "work":
            self.timer.remaining = self.config.WORK_MIN
            self.ui.update_logo(self.images["work"])
        elif session_type == "long_break":
            self.timer.remaining = self.config.LONG_BREAK_MIN
            self.ui.update_logo(self.images["long_break"])
            self.ui.add_checkmark(self.images["checkbox"])
        else:  # short_break
            self.timer.remaining = self.config.SHORT_BREAK_MIN
            self.ui.update_logo(self.images["short_break"])
            self.ui.add_checkmark(self.images["checkbox"])

        self.timer.start_tick()

    def end(self):
        """End all sessions and reset UI."""
        self.ui.end_alarm_timer()
        self.task_manager.reset()

    def reset(self):
        """Reset app to initial state."""
        self.task_manager.reset()
        self.ui.update_sub_logo(self.images["oak"])
        self.ui.clear_tick_timer()
        self.ui.clear_alarm_timer()
        self.ui.clear_checkmarks()
        self.timer.cancel()

    # --------------------------
    # Timer Callback Methods
    # --------------------------

    def on_tick(self, seconds):
        """Update UI countdown timer on tick."""
        self.ui.update_count_down_timer(seconds)

    def on_tick_alarm(self, minutes, seconds):
        """Update UI alarm timer on tick."""
        self.ui.update_alarm_timer(minutes, seconds)

    def on_tick_finish(self):
        """Handle completion of initial tick."""
        self.audio_service.play("beep.wav")
        self.ui.clear_alarm_timer()
        self.timer.rest_tick()

    def on_alarm_finish(self):
        """Handle completion of main countdown alarm."""
        if self.task_manager.is_finished():
            self.ui.add_checkmark(self.images["checkbox"])
            self.audio_service.play("congratulations.wav")
            self.ui.update_sub_logo(self.images["oak"])
            self.end()
        else:
            self.ui.clear_alarm_timer()
            self.start()
