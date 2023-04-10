from tkinter import *

THEME_COLOR = "#375362"

class QuizUi:
    
    def __init__(self):
        self.window=Tk()
        self.window.title("QUIZAPP")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        self.canvas=Canvas(width=300,height=250,background="White")
        self.canvas.grid(column=0,row=1,columnspan=2)
        
        self.score=Label(text="Score:0",font=("Ariel",15,"italic"),background=THEME_COLOR,foreground="White")
        self.score.grid(column=1,row=0,padx=10,pady=10)
        self.text = self.canvas.create_text(150, 125, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "italic"))
        
        
        
        self.right=PhotoImage(file="Day-34/images/true.png")
        self.right_button=Button(image=self.right, highlightthickness=0,highlightbackground=THEME_COLOR)
        self.right_button.grid(column=0,row=2)

        self.wrong=PhotoImage(file="Day-34/images/false.png")
        self.wrong_button=Button(image=self.wrong, highlightthickness=0,background=THEME_COLOR)
        self.wrong_button.grid(column=1,row=2,pady=20)

        
        self.window.mainloop()