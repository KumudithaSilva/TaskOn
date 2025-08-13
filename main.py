from tkinter import *
from tkinter import ttk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("TaskOn")
windows.geometry("300x400")
windows.config(padx=30, pady=20)
windows.resizable(False, False)

canvas = Canvas(windows, width=210, height=220)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(105, 110, image=tomato_img)
canvas.create_text(110, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.pack(expand=True)

# style = ttk.Style()
# style.configure("TLabel", font=("Segoe UI", 14))
# style.configure("TEntry", padding=5)
# style.configure("TButton", font=("Segoe UI", 14), padding=6)



windows.mainloop()