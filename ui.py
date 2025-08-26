from tkinter import Canvas, Frame, Button, Label

class TaskOnUI:
    def __init__(self, root, images):
        self.root = root
        self.images = images

        # Canvas
        self.canvas = Canvas(root, width=200, height=220, bg="#fdfdfd", highlightthickness=0)
        self.canvas.place(relx=0.5, y=15, anchor="n")

        # Checkbox Label Frame
        self.label_frame = Frame(root, bg="#fdfdfd")
        self.label_frame.place(relx=0.49, y=255, anchor="center")

        # Initial Logos
        self.main_logo = self.canvas.create_image(100, 100, image=images["moon"])
        self.sub_logo = self.canvas.create_image(110, 100, image=images["oak"])

        # Text
        self.count_down_timer = self.canvas.create_text(97, 100, text="", fill="#fdfdfd", font=("Courier", 40, "bold"))
        self.alarm_timer = self.canvas.create_text(97, 200, text="", fill="black", font=("Courier", 25, "bold"))

        # Button Frame
        button_frame = Frame(root, bg="#fdfdfd")
        button_frame.place(relx=0.46, y=300, anchor="center")

        # Play button
        self.play_button = Button(button_frame, image=images["play"], bg="#fdfdfd",
                                  activebackground="#fdfdfd", borderwidth=0,highlightthickness=0)
        self.play_button.pack(side="left", padx=10)

        # Reset button
        self.reset_button = Button(button_frame, image=images["pause"], bg="#fdfdfd",
                                   activebackground="#fdfdfd", borderwidth=0, highlightthickness=0)
        self.reset_button.pack(side="left")

    # Update count down timer
    def update_count_down_timer(self, secs):
        self.canvas.itemconfig(self.count_down_timer, text=f"{secs}")

    # Update alarm timer
    def update_alarm_timer(self, mins, secs):
        self.canvas.itemconfig(self.alarm_timer, text=f"{mins}:{secs}")

    # Update Sub Logs
    def update_logo(self, image):
        self.canvas.itemconfig(self.sub_logo, image=image)
        self.canvas.coords(self.sub_logo, 100, 100)

    # Add checkbox label
    def add_checkmark(self, checkbox_img):
        Label(self.label_frame, image=checkbox_img, bg="#fdfdfd", highlightthickness=0).pack(side="left")

    #  Clear all checkbox labels
    def clear_checkmarks(self):
        for widget in self.label_frame.winfo_children():
            widget.destroy()

