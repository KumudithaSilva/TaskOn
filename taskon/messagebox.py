import tkinter as tk

class CustomInputDialog(tk.Toplevel):
    """
    Custom input dialog that accepts an integer value.

    Args:
        parent (tk.Widget): Parent widget.
        prompt (str): Prompt text to display.
        default (str): Default value in the entry field (default "20").
        icon_path (str, optional): Path to icon file for the window.
    """

    def __init__(self, parent, prompt, default="20", icon_path=None):
        super().__init__(parent)
        self.title("TaskOn")
        self.geometry("220x100")
        self.result = None


        if icon_path:
            try:
                self.iconbitmap(icon_path)
            except Exception as e:
                print("Failed to set icon:", e)

        # Prompt label
        tk.Label(self, text=prompt).pack(pady=3)

        # Entry field
        self.entry = tk.Entry(self, width=30)
        self.entry.insert(0, default)
        self.entry.pack(pady=5, padx=10)
        self.entry.focus_set()

        # Button frame
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)

        # Button style configuration
        button_style = {
            "width": 10,
            "height": 1,
            "bg": "#4CAF50",
            "fg": "white",
            "activebackground": "#45a049",
            "activeforeground": "white",
            "bd": 0,
            "font": ("Arial", 9, "bold")
        }

        cancel_style = button_style.copy()
        cancel_style["bg"] = "#f44336"
        cancel_style["activebackground"] = "#d32f2f"

        # OK and Cancel buttons
        tk.Button(btn_frame, text="OK", command=self.on_ok, **button_style).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.on_cancel, **cancel_style).pack(side="left", padx=5)

        # Key bindings
        self.bind("<Return>", lambda event: self.on_ok())
        self.bind("<Escape>", lambda event: self.on_cancel())

    def on_ok(self):
        value = self.entry.get()
        if not value.isdigit():
            raise ValueError("Work minutes must be an integer.")
        self.result = int(value)
        self.destroy()

    def on_cancel(self):
        self.result = None
        self.destroy()
