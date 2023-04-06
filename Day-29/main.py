from tkinter import *
from tkinter import messagebox
from random import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter=[choice(letters) for _ in range(randint(8, 10))]
    password_symbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]
    password_list= password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pass_name.insert(0,password)
    # print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if web_name.get()!="" and pass_name.get()!="":
        is_ok=messagebox.askokcancel(title="Website", message=f"These are the details entered: \n Email: {user_name.get()}\nPassword: {pass_name.get()}\nIs it okay to save?")
        
        if is_ok:
            f=open("Day-29/password.txt","a")
            f.write(f"{web_name.get()}  |  {user_name.get()}  |  {pass_name.get()}\n")
            web_name.delete(0, END)
            pass_name.delete(0, END)
    else:
        messagebox.showinfo(title="Error",message="Don't leave any field empty.")


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password generator")
window.config(padx=60,pady=40)

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
web_name.focus()


user_name=Entry(width=35)
user_name.grid(column=1,row=2,columnspan=2, sticky="EW")
user_name.insert(0,"sujalxetry00@gmail.com")

pass_name=Entry(width=21)
pass_name.grid(column=1,row=3, sticky="EW")


#button grids
generate_button= Button(text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3, sticky="EW")

button=Button(text="Add",width=36,command=save)
button.grid(column=1,row=4,columnspan=2, sticky="EW")



window.mainloop()