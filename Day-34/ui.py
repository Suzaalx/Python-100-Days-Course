from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizUi:
    
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title("QUIZAPP")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        self.canvas=Canvas(width=300,height=250,background="White")
        self.canvas.grid(column=0,row=1,columnspan=2)
        
        self.score=Label(text="Score:0",font=("Ariel",15,"italic"),background=THEME_COLOR,foreground="White")
        self.score.grid(column=1,row=0,padx=10,pady=10)
        self.text = self.canvas.create_text(150, 125, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "italic"))
        
        
        
        self.right=PhotoImage(file="Day-34/images/true.png")
        self.right_button=Button(image=self.right, highlightthickness=0,highlightbackground=THEME_COLOR,command=self.true)
        self.right_button.grid(column=0,row=2)

        self.wrong=PhotoImage(file="Day-34/images/false.png")
        self.wrong_button=Button(image=self.wrong, highlightthickness=0,background=THEME_COLOR,command=self.false)
        self.wrong_button.grid(column=1,row=2,pady=20)
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.text,text=q_text)
    

    def true(self):
        is_right=self.quiz.check_answer("True")
        self.feedback(is_right)

    def false(self):
        is_wrong=self.quiz.check_answer("False")
        self.feedback(is_wrong)
    
    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
            
        else:
            self.canvas.config(bg="Red")
        
        self.window.after(1000,self.get_next_question)
        
    
