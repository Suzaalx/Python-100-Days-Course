from tkinter import *
from tkinter import messagebox
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
color="#94c3ab"
try:
    words=pandas.read_csv("Day-31/data/to_learn.csv")
except FileNotFoundError:
    original_words=pandas.read_csv("Day-31/data/french_words.csv")
    item={row.French:row.English for (index,row) in original_words.iterrows()}
    data=original_words.to_dict(orient="records")
except ValueError or IndexError:
    
    play_again=messagebox.askokcancel(title="There is no words left.",message="Do you want to play again?")
    if play_again:
        original_words=pandas.read_csv("Day-31/data/french_words.csv")
        item={row.French:row.English for (index,row) in original_words.iterrows()}
        data=original_words.to_dict(orient="records")
else:
    item={row.French:row.English for (index,row) in words.iterrows()}
    data=words.to_dict(orient="records")

current_card={}

def new_word():
    global timer
    global current_card
    window.after_cancel(timer)
    current_card=random.choice(data)
    print(current_card)
    print(current_card["French"])
    word.config(text=current_card['French'],background="white",foreground="Black")
    title.config(text="French",background="white",foreground="Black")
    canvas.itemconfig(img,image=front_bg)
    timer=window.after(3000,func=answer)
    
def answer():
    french=word.cget('text')
    print(item[french])
    canvas.itemconfig(img,image=back_bg)
    title.config(background=color,text="English",foreground="White")
    word.config(background=color,text=item[french],foreground="White")
    
def is_known():
    data.remove(current_card)
    new_data=pandas.DataFrame(data)
    new_data.to_csv("Day-31/data/to_learn.csv",index=False)
    new_word()
    
    
window=Tk()

window.title("Flash card")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

timer=window.after(3000,func=answer)


canvas=Canvas(width=800,height=526,background=BACKGROUND_COLOR,highlightthickness=0)
front_bg=PhotoImage(file="Day-31/images/card_front.png")
back_bg=PhotoImage(file="Day-31/images/card_back.png")
img=canvas.create_image(400,263,image=front_bg)
canvas.grid(column=0,row=0,columnspan=2)

right=PhotoImage(file="Day-31/images/right.png")
right_button=Button(image=right, highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=is_known)
right_button.grid(column=1,row=1)

wrong=PhotoImage(file="Day-31/images/wrong.png")
wrong_button=Button(image=wrong, highlightthickness=0,highlightbackground=BACKGROUND_COLOR,command=new_word)
wrong_button.grid(column=0,row=1)

title=Label(text="Title",font=("Ariel",40,"italic"),background="#ffffff")
title.place(x=400,y=150,anchor=CENTER)

word=Label(text="Word",font=("Ariel",60,"bold"),background="#ffffff")
word.place(x=400,y=263,anchor=CENTER)

new_word()

window.mainloop()