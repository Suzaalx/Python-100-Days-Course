from turtle import Turtle,Screen
import random
ALIGNMENT= "center"
FONT=("courier",24,"normal")

class Scoreboard(Turtle):
    def __init__(self):
       super().__init__() 
       self.color("white")
       self.penup()
       self.hideturtle()
       self.goto(0,260)
       self.point=0
       self.write(f"Score: {self.point}",align=ALIGNMENT,font=FONT)
    
    def update_score(self):
         self.write(f"Score: {self.point}",align=ALIGNMENT,font=FONT)
    
    def game_over(self):
        
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT,font=FONT)
    
    def points(self):
        self.point+=1
        self.clear()
        self.update_score()
        
        
       
        

