from tkinter import *

window=Tk()
window.title("Day-27")
window.minsize(500,300)

lable=Label(text="Hello how are you?" ,font=('arial',18,))
lable.grid(column=0,row=0)
def clicked():
    lable.config(text=input.get())

input=Entry(width=30)
input.grid(column=1,row=1)

button = Button(text="Click me!",command=clicked)
button.grid(row=2,column=2)

window.mainloop()

