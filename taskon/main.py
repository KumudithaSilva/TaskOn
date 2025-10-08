"""
Main entry point for the TaskOn application.

This module initializes the Tkinter root window, loads resources,
configures audio services, and starts the main application loop.
"""

from tkinter import Tk

from taskon.app import TaskOnApp
from taskon.messagebox import CustomInputDialog
from taskon.resources import ResourceLoader
from taskon.audio_service import PygameAudionService
from taskon.config import TaskConfig


def main():
    """
    Initialize and run the TaskOn application.
    """
    # Create the main application window and hide
    root = Tk()
    root.withdraw()

    root.title("TaskOn")
    root.geometry("250x350")
    root.config(padx=5, pady=5, bg="#fdfdfd")
    root.resizable(False, False)

    loader = ResourceLoader()

    icon_path = loader.get_resource_path("growing-seed.ico")
    root.iconbitmap(icon_path)


    images = {
        "moon": loader.load_image("clock-green.png"),
        "oak": loader.load_image("growing-seed.png"),
        "play": loader.load_image("play.png"),
        "pause": loader.load_image("pause.png"),
        "checkbox": loader.load_image("checkbox.png"),
        "work": loader.load_image("studying.png"),
        "short_break": loader.load_image("short_break.png"),
        "long_break": loader.load_image("long_break.png"),
    }

    # Initialize audio service and configuration
    audio = PygameAudionService()
    config = TaskConfig()

    # Ask for user input
    dialog = CustomInputDialog(root, prompt="Enter number of study minutes:", icon_path=icon_path)
    root.wait_window(dialog)

    value = dialog.result

    if value is not None:
        try:
            minutes = int(value)
            config.work_min = minutes

            # Show main window
            root.deiconify()

            # Start the TaskOn application
            TaskOnApp(root, images, audio, config)

            # Run the Tkinter main loop
            root.mainloop()
        except ValueError:
            raise ValueError("Invalid input. Please enter a valid number.")
    else:
        root.destroy()


if __name__ == "__main__":
    main()
