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
       self.high_score=0
       self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.point} High score: {self.high_score}",align=ALIGNMENT,font=FONT)
    
    
    def reset(self):
        if self.point>self.high_score:
            self.high_score=self.point
        self.point=0
        self.update_score()
    # def game_over(self):
        
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT,font=FONT)
    
    def points(self):
        self.point+=1
        
        self.update_score()
        
        
       
        

