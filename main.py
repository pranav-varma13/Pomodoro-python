from tkinter import *
import math

RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#FCF9BE"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    label.config(text="Timer")
    check_marks.config(text="")
    button_s.config(state=NORMAL)  

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break!🍵", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break!🍵", fg=RED)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)

    button_s.config(state=DISABLED)  

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)

# Start button
button_s = Button(text="Start", highlightthickness=0, command=start_timer)
button_s.grid(column=0, row=3)

# Reset button
button_r = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_r.grid(column=2, row=3)

# Checkmarks
check_marks = Label(bg=YELLOW, fg=GREEN, font=("bold"))
check_marks.grid(column=1, row=4)

window.mainloop()
