from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password generator")
window.config(padx=20,pady=20)

canvas=Canvas(width=200,height=200)
img=PhotoImage(file="Day-29/logo.png")
canvas.create_image(100,100,image=img)
canvas.pack()


window.mainloop()