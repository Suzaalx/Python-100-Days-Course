from tkinter import *

window=Tk()
window.title("Mile to Km converter")
window.config(padx=25,pady=20)


def convert():
    miles=input.get()
    km_value= round(float(miles) * 1.609)
    num.config(text=km_value)

input=Entry(width=7)
input.grid(column=1,row=0)

mile=Label(text="Miles")
mile.grid(column=2,row=0)

is_equal=Label(text="is equal to" )
is_equal.grid(column=0,row=1)

num=Label(text="0" ,font=('arial',15))
num.grid(column=1,row=1)

km=Label(text="km" )
km.grid(column=2,row=1)


button = Button(text="Calculate!",command=convert)
button.grid(column=1,row=2)






window.mainloop()

