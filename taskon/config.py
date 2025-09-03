class TaskConfig:
    """
    Configuration for task session durations and repetitions.

    Attributes:
        WORK_MIN: Work session duration in minutes.
        SHORT_BREAK_MIN: Short break duration in minutes.
        LONG_BREAK_MIN: Long break duration in minutes.
        WORK_REPS: Number of work sessions before ending.
        COUNTER_SECOND: Initial tick timer duration in seconds.
        INITIAL_VALUE: Initial value for counters and timers.
    """

    def __init__(self, work_min=20, short_break_min=5, long_break_min=20,
                 work_reps=5, counter_second=5, initial_value=0):
        """
        Initialize TaskConfig with optional custom durations and repetitions.

        Args:
            work_min: Duration of a work session in minutes.
            short_break_min: Duration of a short break in minutes.
            long_break_min: Duration of a long break in minutes.
            work_reps: Number of work sessions before ending.
            counter_second: Duration of initial tick timer in seconds.
            initial_value: Initial value for counters and timers.
        """
        self.WORK_MIN = work_min
        self.SHORT_BREAK_MIN = short_break_min
        self.LONG_BREAK_MIN = long_break_min
        self.WORK_REPS = work_reps
        self.COUNTER_SECOND = counter_second
        self.INITIAL_VALUE = initial_value
