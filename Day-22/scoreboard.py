FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.score=0
        self.write("Level: ",align="left", font=FONT)
        self.update()
    
    def update(self):
       
        self.penup()
        self.goto(-160,250)
        self.write(self.score,align="left", font=FONT)
        self.score+=1
        self.clear()
        
      
        