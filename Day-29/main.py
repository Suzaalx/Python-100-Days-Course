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
canvas.grid(column=1,row=0)
#label grids
web=Label(text="Website:")
web.grid(column=0,row=1)

email=Label(text="Email/Username:")
email.grid(column=0,row=2)

password=Label(text="Password:")
password.grid(column=0,row=3)

#Entry grids. 
#sticky="EW" makes the widget stick to the edges so that the layout looks better.
web_name=Entry(width=35)
web_name.grid(column=1,row=1,columnspan=2, sticky="EW")

user_name=Entry(width=35)
user_name.grid(column=1,row=2,columnspan=2, sticky="EW")

pass_name=Entry(width=21)
pass_name.grid(column=1,row=3, sticky="EW")


#button grids
generate_button= Button(text="Generate Password")
generate_button.grid(column=2,row=3, sticky="EW")

button=Button(text="Add",width=36)
button.grid(column=1,row=4,columnspan=2, sticky="EW")



window.mainloop()