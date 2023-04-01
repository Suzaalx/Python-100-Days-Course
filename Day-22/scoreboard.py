FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1
        self.goto(-280,250)
        self.score()
    def score(self):
        self.clear()
        self.write(f"Level: {self.level}",align="left", font=FONT)
    def update(self):
        self.level += 1
        self.score()
    
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
       

        
      
        