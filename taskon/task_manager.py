from taskon.config import TaskConfig


class TaskManager:
    """
    Track session repetitions and determine the type of the next session.

    Attributes:
        config: Configuration object containing session settings.
        reps: Total session repetitions completed.
        work_reps: Number of work sessions completed.
        work_reps_goal: Target number of work sessions to complete.
    """

    def __init__(self, config: TaskConfig):
        """
        Initialize the TaskManager.

        Args:
            config: Configuration object with session parameters.
        """
        self.config = config
        self.reps = config.INITIAL_VALUE
        self.work_reps = config.INITIAL_VALUE
        self.work_reps_goal = config.WORK_REPS

    # --------------------------
    # Session Management Methods
    # --------------------------

    def next_session(self):
        """
        Determine the next session type and update counters.

        Returns:
            str: Type of next session ('work', 'short_break', 'long_break').
        """
        self.reps += 1
        if self.reps % 2 == 1:
            self.work_reps += 1
            return "work"
        elif self.reps == 8:
            return "long_break"
        else:
            return "short_break"

    def is_finished(self):
        """
        Check if all work sessions are completed.

        Returns:
            bool: True if work session goal reached, False otherwise.
        """
        return self.work_reps >= self.work_reps_goal

    def reset(self):
        """Reset all counters to initial values."""
        self.reps = self.config.INITIAL_VALUE
        self.work_reps = self.config.INITIAL_VALUE
