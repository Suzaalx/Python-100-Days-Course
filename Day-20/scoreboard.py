from turtle import Turtle,Screen
import random


class Scoreboard(Turtle):
    def __init__(self):
       super().__init__() 
       self.color("white")
       self.penup()
       self.hideturtle()
       self.goto(0,280)
       self.point=0
       self.write(f"Score={self.point}",True,align="center",font=('Arial', 15, 'normal'))
       
    def points(self):
        self.point+=1
        

