from turtle import Turtle,Screen
import random
ALIGNMENT= "center"
FONT=("courier",24,"normal")
file= "D:\\SAT\\Python-100-Days-Course\\Day-20-21\\data.txt"
class Scoreboard(Turtle):
    def __init__(self):
       super().__init__() 
       self.color("white")
       self.penup()
       self.hideturtle()
       self.goto(0,260)
       self.point=0
       with open(file) as data:
           self.high_score=int(data.read())
       self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.point} High score: {self.high_score}",align=ALIGNMENT,font=FONT)
    
    
    def reset(self):
        if self.point>self.high_score:
            self.high_score=self.point
            with open(file ,mode="w") as data:
                data.write(f"{self.high_score}")
                
        self.point=0
        self.update_score()
    # def game_over(self):
        
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT,font=FONT)
    
    def points(self):
        self.point+=1
        
        self.update_score()
        
        
       
        

