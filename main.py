import math
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
def timer_count_down():
    count_down(5, lambda : alarm_count_down(5 * 60))

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, on_finish=None):
    canvas.itemconfig(count_down_timer, text=count)
    if count != 0:
        windows.after(1000, count_down, count-1, on_finish)
    else:
        canvas.itemconfig(count_down_timer, text="")
        if on_finish:
            on_finish()

def alarm_count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(alarm_timer, text=f"0{count_min}:{count_sec}")
    if count > 0:
        windows.after(1000, alarm_count_down, count-1)



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
checkbox = PhotoImage(file="images/checkbox.png")


canvas = Canvas(windows, width=200, height=220, bg="white", highlightthickness=0)
canvas.place(relx=0.5, y=15, anchor="n")

canvas.create_image(100, 100, image=moon_img)
canvas.create_image(110, 100, image=oak_img)

count_down_timer = canvas.create_text(97, 100, text="", fill="white", font=(FONT_NAME, 40, "bold"))
alarm_timer = canvas.create_text(97, 200, text="", fill="black", font=(FONT_NAME, 25, "bold"))


button_frame = Frame(windows, bg="white")
button_frame.place(relx=0.46, y=300, anchor="center")


pause_button = Button(button_frame, image=pause_img, bg="white",
                      activebackground="white", borderwidth=0,
                      command=lambda: print("Pause"), highlightthickness=0)
pause_button.image = pause_img
pause_button.pack(side="left", padx=10)

play_button = Button(button_frame, image=play_img, bg="white",
                     activebackground="white", borderwidth=0,
                     command=timer_count_down, highlightthickness=0)
play_button.image = play_img
play_button.pack(side="left")


label_frame = Frame(windows, bg="white")
label_frame.place(relx=0.49, y =250, anchor="center")

image_label = Label(label_frame, image=checkbox,bg="white", highlightthickness=0)
image_label.pack(side="left")






windows.mainloop()