from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()   
        self.color("white")
        self.shape("circle")
        self.penup()
        self.y_move=10
        self.x_move=10
        self.move_speed=0.1
        
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
        

    def bounce_y(self):
        self.y_move*=-1
        
        
    def bounce_xl(self):
        self.x_move = (abs(self.x_move))
        self.move_speed*=0.9
    def bounce_xr(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed*=0.9
    def bounce(self):
        self.x_move*=-1
        
    
    def new(self):
        self.goto(0,0)
        self.bounce()
        self.move_speed=0.1
