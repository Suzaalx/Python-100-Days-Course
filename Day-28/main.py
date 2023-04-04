
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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    count_down(5*60)
# -------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min=math.floor(count/60)
    count_sec=count%60
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    print(count)
    if count>0:
        window.after(1000,count_down,count-1)
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

round=Label(text="✓",bg=PINK , fg=YELLOW, font=(FONT_NAME, 20, "italic"))
round.grid(column=1,row=3)

reset=Button(text="Reset",bg=PINK , fg=YELLOW, font=(FONT_NAME, 15, "bold"))
reset.grid(column=2,row=2)

window.mainloop()