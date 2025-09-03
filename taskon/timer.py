import math
from taskon.logger import logger
from taskon.config import TaskConfig


class Timer:
    """
    Handles countdown logic without UI specifics.

    Attributes:
        root: Tkinter root or any object with `after` method.
        config: Timer configuration object.
        counter_seconds: Seconds for initial tick countdown.
        remaining: Seconds for main countdown timer.
        on_tick: Callback for each tick of main countdown.
        on_tick_alarm: Callback for each tick of main alarm.
        on_tick_finish: Callback when tick timer finishes.
        on_alarm_finish: Callback when main timer finishes.
        tick_timer: Internal reference to the tick timer.
        timer: Internal reference to the main countdown timer.
    """

    def __init__(self, root, on_tick, on_tick_alarm, on_tick_finish,
                 on_alarm_finish, config: TaskConfig):
        """
        Initialize the Timer.

        Args:
            root: Tkinter root or any object with `after` method.
            on_tick: Callback for each tick of main countdown.
            on_tick_alarm: Callback for each tick of alarm countdown.
            on_tick_finish: Callback when tick timer finishes.
            on_alarm_finish: Callback when main alarm finishes.
            config: Timer configuration object.
        """
        self.root = root
        self.config = config
        self.counter_seconds = config.COUNTER_SECOND
        self.remaining = config.INITIAL_VALUE

        self.on_tick = on_tick
        self.on_tick_alarm = on_tick_alarm
        self.on_alarm_finish = on_alarm_finish
        self.on_tick_finish = on_tick_finish

        self.tick_timer = None
        self.timer = None

    # --------------------------
    # Timer Start / Tick Methods
    # --------------------------

    def start_timer(self, seconds):
        """Start main countdown timer."""
        self.remaining = seconds
        logger.info(f"[START] Main Timer For {seconds}s Start")
        self._count_down_timer()

    def start_tick(self):
        """Start simple second-based countdown timer."""
        logger.info("[START] Ticking Timer Start")
        self._count_down_tick()

    def _count_down_tick(self):
        """Internal method: simple countdown in seconds."""
        count_min = math.floor(self.counter_seconds / 60)
        count_sec = self.counter_seconds % 60

        if self.counter_seconds > 0:
            logger.info(f"[TICK] {count_min:02d}.{count_sec:02d} Remaining")
            if self.on_tick:
                self.on_tick(self.counter_seconds)

            self.counter_seconds -= 1
            self.tick_timer = self.root.after(1000, self._count_down_tick)
        else:
            logger.info("[DONE] Initial Tick Finished\n")
            self.tick_timer = None

            if self.on_tick:
                self.on_tick("")

            if self.on_tick_finish:
                self.on_tick_finish()

            self.start_timer(self.remaining)

    def _count_down_timer(self):
        """Internal method: main countdown in minutes and seconds."""
        count_min = math.floor(self.remaining / 60)
        count_sec = self.remaining % 60

        logger.info(f"[TIMER] {count_min:02d}:{count_sec:02d} Remaining")

        if self.on_tick_alarm:
            self.on_tick_alarm(f"{count_min:02}", f"{count_sec:02}")

        if self.remaining > 0:
            self.remaining -= 1
            self.timer = self.root.after(1000, self._count_down_timer)
        else:
            logger.info("[DONE] Main Timer Finished!")
            self.timer = None

            if self.on_alarm_finish:
                self.on_alarm_finish()

    # --------------------------
    # Timer Control / Cancel
    # --------------------------

    def cancel(self):
        """Cancel all timers and reset durations."""
        if self.tick_timer:
            self.root.after_cancel(self.tick_timer)
        if self.timer:
            self.root.after_cancel(self.timer)

        self.tick_timer = None
        self.timer = None
        self.counter_seconds = self.config.COUNTER_SECOND
        logger.info("[CANCEL] All Timer Cancelled")

    def rest_tick(self):
        """Reset the initial tick duration before starting."""
        self.counter_seconds = self.config.COUNTER_SECOND

    def rest_alarm(self):
        """Reset the main timer duration before starting."""
        self.remaining = self.config.INITIAL_VALUE

    # --------------------------
    # Timer State Queries
    # --------------------------

    def is_tick_timer_running(self):
        """Return True if tick_timer is active."""
        return self.tick_timer is not None

    def is_timer_running(self):
        """Return True if main timer is active."""
        return self.timer is not None
