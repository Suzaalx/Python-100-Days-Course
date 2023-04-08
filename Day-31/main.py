from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"


window=Tk()

window.title("Flash card")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
bg=PhotoImage(file="Day-31/images/card_front.png")
canvas.create_image(400,263,image=bg)
canvas.grid(column=0,row=0,columnspan=2)

right=PhotoImage(file="Day-31/images/right.png")
right_button=Button(image=right, highlightthickness=0,highlightbackground=BACKGROUND_COLOR)
right_button.grid(column=1,row=1)

wrong=PhotoImage(file="Day-31/images/wrong.png")
wrong_button=Button(image=wrong, highlightthickness=0,highlightbackground=BACKGROUND_COLOR)
wrong_button.grid(column=0,row=1)
window.mainloop()