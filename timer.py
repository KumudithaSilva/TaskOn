import math

COUNTER_SECOND = 5

class Timer:
    """Handles countdown logic without UI specifics."""

    def __init__(self, root, timer_seconds, on_tick=None):
        """
        Initialize the Timer.

        Args:
            root: Tkinter root or any object with `after` method.
            timer_seconds: Countdown in mm:ss format (total seconds).
            on_tick: Callback for each tick of timer_seconds countdown.
        """
        self.root = root
        self.counter_seconds = COUNTER_SECOND
        self.timer_seconds = timer_seconds
        self.on_tick = on_tick
        self.timer = None

    def start_tick(self):
        """Start simple second-based countdown."""
        self._count_down_tick()

    def start_timer(self):
        """Start mm:ss style countdown."""
        self._count_down_timer()

    def _count_down_tick(self):
        """Internal method: simple countdown in seconds."""
        if self.counter_seconds > 0:
            print(self.counter_seconds)  # Print current second
            self.counter_seconds -= 1
            # Schedule next tick after 1 second
            self.root.after(1000, self._count_down_tick)
        else:
            print("Initial 5-second countdown finished!")
            # if self.on_finish:
                # Trigger finish callback
            self.start_timer()

    def _count_down_timer(self):
        """Internal method: countdown in minutes and seconds."""
        count_min = math.floor(self.timer_seconds / 60)
        count_sec = self.timer_seconds % 60

        if self.timer_seconds > 0:
            print(count_min, count_sec)
            self.timer_seconds -= 1
            # Schedule next tick after 1 second
            self.timer = self.root.after(1000, self._count_down_timer)
        else:
            print("State Over")
            if self.on_tick:
                # Trigger tick callback at the end
                self.on_tick()

    def cancel(self):
        """Cancel the running timer."""
        if self.timer:
            self.root.after_cancel(self.timer)
            self.timer = None

    def is_running(self):
        """Return True if timer is active."""
        return self.timer is not None
