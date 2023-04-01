from turtle import Turtle,Screen
ALIGNMENT= "center"
FONT=("courier",60,"normal")
class Score(Turtle):
    
    def __init__(self):
        super().__init__()  
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.R_score=0
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align=ALIGNMENT, font=FONT)
        self.goto(100,200)
        self.write(self.R_score,align=ALIGNMENT, font=FONT)
        
    def l_point(self):
         self.l_score+=1
         self.update_scoreboard()
    def r_point(self):
         self.R_score+=1
         self.update_scoreboard()