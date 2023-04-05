
import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
counter=""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(counter)
    reps=0
    round.config(text="")
    title.config(text="Timer",fg=RED)
    canvas.itemconfig(timer_text, text="00:00")
    start.config(state="normal")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec= WORK_MIN*60
    break_sec=SHORT_BREAK_MIN*60
    long_break=LONG_BREAK_MIN*60
    window.attributes("-topmost",1)
    if reps%2!=0:
        count_down(work_sec)
        title.config(text="Work",fg=GREEN)
    elif reps%2==0:
        count_down(break_sec)
        title.config(text="Short break", fg=RED)
    elif reps%8==0:
        count_down(long_break)
        title.config(text="Long break",fg=RED)
    
    start.config(state="disabled")
    window.attributes('-topmost', 0) 
    
    
    
# -----------------------(--- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global counter
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f"0{str(count_sec)}"
    
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    print(count)
    if count>0:
        counter=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        session=math.floor(reps/2)
        for i in range(session):
            mark+="✓"
        round.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=PINK)


canvas=Canvas(width=210,height=230,bg=PINK, highlightthickness=0)
img=PhotoImage(file="Day-28/tomato.png")
canvas.create_image(105,115,image=img)
timer_text=canvas.create_text(105,130,text="00:00",fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1,row=1)




title=Label(text="Timer",bg=PINK , fg=RED, font=(FONT_NAME, 35, "bold"))
title.grid(column=1,row=0)

start=Button(text="Start",bg=PINK , fg=YELLOW, font=(FONT_NAME, 15, "bold"),command=start_timer)
start.grid(column=0,row=2)

round=Label(text="",bg=PINK , fg=YELLOW, font=(FONT_NAME, 20, "italic"))
round.grid(column=1,row=3)

reset=Button(text="Reset",bg=PINK , fg=YELLOW, font=(FONT_NAME, 15, "bold"),command=reset_timer)
reset.grid(column=2,row=2)

window.mainloop()