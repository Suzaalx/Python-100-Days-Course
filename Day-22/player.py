STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()  
        self.shape("turtle")
        self.penup()
        self.setheading(90)

    def move(self):
        self.fd(MOVE_DISTANCE)
    
    def start(self):
        self.goto(STARTING_POSITION)

    def finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False

        
        
