from tkinter import Canvas, Frame, Button, Label


class TaskOnUI:
    """
    A class to manage and display task-related UI components using Tkinter.

    Attributes:
        root (Tk): The main application window.
        images (dict): A dictionary containing Tkinter PhotoImage objects.

    Methods:
        update_count_down_timer(secs): Updates the main countdown timer text.
        update_alarm_timer(mins, secs): Updates the alarm timer display.
        update_logo(image): Changes the sub-logo image.
        add_checkmark(checkbox_img): Adds a checkbox image label to the UI.
        clear_checkmarks(): Clears all checkbox labels from the UI.
    """

    def __init__(self, root, images, start_callback, reset_callback):
        self.root = root
        self.images = images

        # Canvas for main display
        self.canvas = Canvas(
            root,
            width=200,
            height=220,
            bg="#fdfdfd",
            highlightthickness=0
        )
        self.canvas.place(relx=0.5, y=15, anchor="n")

        # Frame for checkbox labels
        self.label_frame = Frame(root, bg="#fdfdfd")
        self.label_frame.place(relx=0.49, y=255, anchor="center")

        # Initial logo images
        self.main_logo = self.canvas.create_image(100, 100, image=images["moon"])
        self.sub_logo = self.canvas.create_image(110, 100, image=images["oak"])

        # Countdown and alarm timers
        self.count_down_timer = self.canvas.create_text(
            97, 100, text="", fill="#fdfdfd",
            font=("Courier", 40, "bold")
        )
        self.alarm_timer = self.canvas.create_text(
            97, 200, text="", fill="black",
            font=("Courier", 25, "bold")
        )

        # Frame for buttons
        button_frame = Frame(root, bg="#fdfdfd")
        button_frame.place(relx=0.46, y=300, anchor="center")

        # Play button
        self.play_button = Button(
            button_frame, image=images["play"], bg="#fdfdfd",
            activebackground="#fdfdfd", borderwidth=0,
            highlightthickness=0, command=start_callback
        )
        self.play_button.pack(side="left", padx=10)

        # Reset button
        self.reset_button = Button(
            button_frame, image=images["pause"], bg="#fdfdfd",
            activebackground="#fdfdfd", borderwidth=0,
            highlightthickness=0, command=reset_callback
        )
        self.reset_button.pack(side="left")

    def update_count_down_timer(self, secs):
        """Update the countdown timer display on the canvas."""
        self.canvas.itemconfig(self.count_down_timer, text=f"{secs}", font=("Courier", 40, "bold"))

    def update_alarm_timer(self, mins, secs):
        """Update the alarm timer display on the canvas."""
        self.canvas.itemconfig(self.alarm_timer, text=f"{mins}:{secs}", font=("Courier", 25, "bold"))

    def update_logo(self, image):
        """Update the sub-logo image."""
        self.canvas.itemconfig(self.sub_logo, image=image)
        self.canvas.coords(self.sub_logo, 100, 100)

    def update_sub_logo(self, image):
        """Update the sub-logo image."""
        self.canvas.itemconfig(self.sub_logo, image=image)
        self.canvas.coords(self.sub_logo, 110, 100)

    def add_checkmark(self, checkbox_img):
        """Add a checkbox image to the label frame."""
        Label(
            self.label_frame, image=checkbox_img,
            bg="#fdfdfd", highlightthickness=0
        ).pack(side="left")

    def end_alarm_timer(self):
        """Clear the alarm timer display."""
        self.canvas.itemconfig(self.alarm_timer, text="Congratulations 🎉", font=("Courier", 12, "bold"))

    def clear_tick_timer(self):
        """Clear the alarm timer display."""
        self.canvas.itemconfig(self.count_down_timer, text="")

    def clear_alarm_timer(self):
        """Clear the alarm timer display."""
        self.canvas.itemconfig(self.alarm_timer, text="")

    def clear_checkmarks(self):
        """Remove all checkbox images from the label frame."""
        for widget in self.label_frame.winfo_children():
            widget.destroy()

