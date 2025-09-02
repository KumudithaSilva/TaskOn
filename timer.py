import math
from logger import logger

COUNTER_SECOND = 5
INITIAL_REMINDER = 0

class Timer:
    """Handles countdown logic without UI specifics."""

    def __init__(self, root, on_tick, on_tick_alarm, on_tick_finish,  on_alarm_finish):
        """
        Initialize the Timer.

        Args:
            root: Tkinter root or any object with `after` method.
            on_tick: Callback for each tick of main countdown.
             Signature: on_tick(minutes, seconds)
             on_alarm_finish: Call after main alarm over
        """
        self.root = root

        self.counter_seconds = COUNTER_SECOND
        self.remaining = INITIAL_REMINDER

        self.on_tick = on_tick
        self.on_tick_alarm = on_tick_alarm
        self.on_alarm_finish = on_alarm_finish
        self.on_tick_finish = on_tick_finish

        self.tick_timer = None
        self.timer = None

    def start_timer(self, seconds):
        """Start main countdown timer."""
        self.remaining = seconds
        logger.info(f"[START] Main Timer For {seconds}s Start")
        self._count_down_timer()

    def start_tick(self):
        """Start simple second-based countdown timer."""
        logger.info(f"[START] Ticking Timer Start")
        self._count_down_tick()

    def _count_down_tick(self):
        """Internal method: simple countdown in seconds."""
        count_min = math.floor(self.counter_seconds/ 60)
        count_sec = self.counter_seconds % 60

        if self.counter_seconds > 0:
            logger.info(f"[TICK] {count_min:02d}.{count_sec:02d} Remaining")
            if self.on_tick:
                self.on_tick(self.counter_seconds)

            self.counter_seconds -= 1
            # Schedule next tick after 1 second
            self.tick_timer = self.root.after(1000, self._count_down_tick)
        else:
            logger.info("[DONE] Initial Tick Finished \n")
            self.tick_timer = None

            if self.on_tick:
                self.on_tick("")

            if self.on_tick_finish:
                self.on_tick_finish()

            self.start_timer(self.remaining)


    def _count_down_timer(self):
        """Internal method: main countdown in minutes and seconds."""
        count_min = math.floor(self.remaining/ 60)
        count_sec = self.remaining % 60

        logger.info(f"[TIMER] {count_min:02d}:{count_sec:02d} Remaining")

        if self.on_tick_alarm:
            if count_sec < 10:
                count_sec = f"0{count_sec}"
            if count_min < 10:
                count_min = f"0{count_min}"
            self.on_tick_alarm(count_min, count_sec)

        if self.remaining > 0:
            self.remaining -= 1
            # Schedule next tick after 1 second
            self.timer = self.root.after(1000, self._count_down_timer)
        else:
            logger.info("[DONE] Main Timer Finished!")
            self.timer = None

            if self.on_alarm_finish:
                self.on_alarm_finish()

    def cancel(self):
        """Cancel the running timers safely."""

        def safe_cancel(timer_id):
            if timer_id:
                try:
                    self.root.after_cancel(timer_id)
                except ValueError:
                    # Already expired or invalid
                    pass

        safe_cancel(self.tick_timer)
        safe_cancel(self.timer)

        self.tick_timer = None
        self.timer = None
        self.counter_seconds = COUNTER_SECOND
        logger.info("[CANCEL] All Timer Cancelled")

    def is_tick_timer_running(self):
        """Return True if tick_timer is active."""
        return self.tick_timer is not None

    def is_timer_running(self):
        """Return True if timer is active."""
        return self.timer is not None

    def rest_tick(self):
        """Reset the initial tick duration before starting."""
        self.counter_seconds = COUNTER_SECOND

    def rest_alarm(self):
        """Reset the timer duration before starting."""
        self.remaining = INITIAL_REMINDER

