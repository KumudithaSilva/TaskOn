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
windows.geometry("250x350")
windows.iconbitmap("images/growing-seed.ico")
windows.config(padx=5, pady=5, bg="white")
windows.resizable(False, False)


moon_img = PhotoImage(file="images/clock-green.png")
oak_img = PhotoImage(file="images/growing-seed.png")
play_img = PhotoImage(file="images/play.png")
pause_img = PhotoImage(file="images/pause.png")


canvas = Canvas(windows, width=200, height=220, bg="white", highlightthickness=0)
canvas.place(relx=0.5, y=15, anchor="n")

canvas.create_image(100, 100, image=moon_img)
canvas.create_image(110, 100, image=oak_img)

canvas.create_text(97, 205, text="00:00", fill="black", font=(FONT_NAME, 25, "bold"))


button_frame = Frame(windows, bg="white")
button_frame.place(relx=0.46, y=270, anchor="center")


pause_button = Button(button_frame, image=pause_img, bg="white",
                      activebackground="white", borderwidth=0,
                      command=lambda: print("Pause"), highlightthickness=0)
pause_button.image = pause_img
pause_button.pack(side="left", padx=10)

play_button = Button(button_frame, image=play_img, bg="white",
                     activebackground="white", borderwidth=0,
                     command=lambda: print("Play"), highlightthickness=0)
play_button.image = play_img
play_button.pack(side="left")




windows.mainloop()