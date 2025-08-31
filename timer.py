import math

COUNTER_SECOND = 5

class Timer:
    """Handles countdown logic without UI specifics."""

    def __init__(self, root, on_tick, on_finish):
        """
        Initialize the Timer.

        Args:
            root: Tkinter root or any object with `after` method.
            on_tick: Callback for each tick of main countdown.
             Signature: on_tick(minutes, seconds)
            on_finish: Callback when main countdown finishes.
        """
        self.root = root
        self.counter_seconds = COUNTER_SECOND
        self.on_tick = on_tick
        self.on_finish = on_finish
        self.timer = None
        self.remaining = 0

    def start_timer(self, seconds):
        """Start main countdown timer."""
        self.remaining = seconds
        print(f"[START] Main timer for {seconds} seconds")
        self._count_down_timer()

    def start_tick(self):
        """Start simple second-based countdown timer."""
        self._count_down_tick()

    def _count_down_tick(self, first_call=False):
        """Internal method: simple countdown in seconds."""
        if self.counter_seconds > 0:
            print(self.counter_seconds)
            if self.on_tick:
                self.on_tick(self.counter_seconds)

            self.counter_seconds -= 1
            # Schedule next tick after 1 second
            self.timer = self.root.after(1000, self._count_down_tick)
        else:
            print("Initial tick finished \n")

            if self.on_tick:
                self.on_tick("")

            self.start_timer(self.remaining)

    def _count_down_timer(self):
        """Internal method: main countdown in minutes and seconds."""
        count_min = math.floor(self.remaining/ 60)
        count_sec = self.remaining % 60

        print(f"[TIMER] {count_min:02d}:{count_sec:02d} remaining")

        if self.remaining > 0:
            self.remaining -= 1
            # Schedule next tick after 1 second
            self.timer = self.root.after(1000, self._count_down_timer)
        else:
            print("[DONE] Main timer finished!")
            if self.on_finish:
                # Trigger tick callback at the end
                self.on_finish()

    def cancel(self):
        """Cancel the running timer."""
        if self.timer:
            print("[CANCEL] Timer cancelled")
            self.root.after_cancel(self.timer)
            self.timer = None

    def is_running(self):
        """Return True if timer is active."""
        return self.timer is not None

