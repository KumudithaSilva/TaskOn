import math
from tkinter import *
from tkinter import ttk
import pygame

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0

pygame.mixer.init()
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    pass

# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_count_down():
    global REPS
    REPS += 1

    if REPS % 2 == 1:
        count_down(5, lambda : alarm_count_down(WORK_MIN * 60))
        canvas.itemconfig(sub_logo, image=work_img)
        canvas.coords(sub_logo, 100, 100)
    elif REPS == 8:
        count_down(5, lambda : alarm_count_down(LONG_BREAK_MIN * 60))
        canvas.itemconfig(sub_logo, image=long_break_img)
        canvas.coords(sub_logo, 100, 100)
    else:
        count_down(5, lambda: alarm_count_down(SHORT_BREAK_MIN * 60))
        canvas.itemconfig(sub_logo, image=short_break_img)
        canvas.coords(sub_logo, 100, 100)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count, on_finish=None):
    canvas.itemconfig(count_down_timer, text=count)
    if count != 0:
        windows.after(1000, count_down, count-1, on_finish)
    else:
        canvas.itemconfig(count_down_timer, text="")
        pygame.mixer.music.load("audio/beep.wav")
        pygame.mixer.music.play()

        if on_finish:
            on_finish()

def alarm_count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(alarm_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        windows.after(1000, alarm_count_down, count - 1)
    else:
        if REPS < 8:
            timer_count_down()
        else:
            canvas.itemconfig(alarm_timer, text="Done 🎉")

# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("TaskOn")
windows.geometry("250x350")
windows.iconbitmap("images/growing-seed.ico")
windows.config(padx=5, pady=5, bg="#fdfdfd")
windows.resizable(False, False)


moon_img = PhotoImage(file="images/clock-green.png")
oak_img = PhotoImage(file="images/growing-seed.png")
play_img = PhotoImage(file="images/play.png")
pause_img = PhotoImage(file="images/pause.png")
checkbox = PhotoImage(file="images/checkbox.png")
work_img = PhotoImage(file="images/studying.png")
short_break_img = PhotoImage(file="images/short_break.png")
long_break_img = PhotoImage(file="images/long_break.png")


canvas = Canvas(windows, width=200, height=220, bg="#fdfdfd", highlightthickness=0)
canvas.place(relx=0.5, y=15, anchor="n")

main_logo = canvas.create_image(100, 100, image=moon_img)
sub_logo = canvas.create_image(110, 100, image=oak_img)

count_down_timer = canvas.create_text(97, 100, text="", fill="#fdfdfd", font=(FONT_NAME, 40, "bold"))
alarm_timer = canvas.create_text(97, 200, text="", fill="black", font=(FONT_NAME, 25, "bold"))


button_frame = Frame(windows, bg="#fdfdfd")
button_frame.place(relx=0.46, y=300, anchor="center")


pause_button = Button(button_frame, image=pause_img, bg="#fdfdfd",
                      activebackground="#fdfdfd", borderwidth=0,
                      command=reset_timer, highlightthickness=0)
pause_button.image = pause_img
pause_button.pack(side="left", padx=10)

play_button = Button(button_frame, image=play_img, bg="#fdfdfd",
                     activebackground="#fdfdfd", borderwidth=0,
                     command=timer_count_down, highlightthickness=0)
play_button.image = play_img
play_button.pack(side="left")


label_frame = Frame(windows, bg="#fdfdfd")
label_frame.place(relx=0.49, y =255, anchor="center")

image_label = Label(label_frame, image=checkbox,bg="#fdfdfd", highlightthickness=0)
image_label.pack(side="left")

image_label1 = Label(label_frame, image=checkbox,bg="#fdfdfd", highlightthickness=0)
image_label1.pack(side="left")

image_label2 = Label(label_frame, image=checkbox,bg="#fdfdfd", highlightthickness=0)
image_label2.pack(side="left")

image_label3 = Label(label_frame, image=checkbox,bg="#fdfdfd", highlightthickness=0)
image_label3.pack(side="left")

image_label4 = Label(label_frame, image=checkbox,bg="#fdfdfd", highlightthickness=0)
image_label4.pack(side="left")






windows.mainloop()