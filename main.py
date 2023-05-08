from tkinter import *


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
Timer = None



def resetter():
    global REPS
    Title.config(text=" Timer")
    check_mark.config(text="")
    window.after_cancel(Timer)
    canvas.itemconfig(timer_text, text="00:00")
    REPS = 0




def start_timer():
    Title.config(text="Start", fg=GREEN)
    global REPS
    REPS += 1
    if REPS == 8:
        Title.config(text="Break", fg=RED)
        count_down(2 * 60)
    elif REPS % 2 != 0:
        Title.config(text=" Work ", fg=GREEN)
        count_down(1 * 60)
    else:
        Title.config(text=" Break", fg=PINK)
        count_down(1 * 30)


def count_down(count):
    global REPS
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    count_min = count // 60
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global Timer
        Timer = window.after(1000, count_down, count - 1)
    elif 8 > REPS > 0:
        start_timer()
        new_check = ""
        for _ in range(REPS//2):
            new_check += "✔"
        check_mark.config(text=new_check)




window = Tk()
window.title("Pomodoro")
window.config(pady=40, padx=50, bg=YELLOW)
# image_file = ImageTk.PhotoImage(Image.open("tomato.png"))
# defining the window size.
Title = Label(text=" Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
Title.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Representing an image file using PhotoImage and stored
image_file = PhotoImage(file="tomato.png")
# on existing canvas adding means creating overlay by the image_file.
canvas.create_image(100, 112, image=image_file)
# displaying the canvas with all added files representing in onepiece.
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# start Button
start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

# reset Button
reset = Button(text="Reset", command=resetter)
reset.grid(column=2, row=2)

# Check Mark Label
Check_Mark = ""
check_mark = Label(text=Check_Mark, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()
