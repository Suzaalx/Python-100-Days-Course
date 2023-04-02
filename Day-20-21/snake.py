from turtle import Turtle
X=0
MOVE_DISTANCE=20
   
positions=[(0, 0), (-20, 0), (-40, 0)]
class Snake:
    
    def __init__(self):
        self.segments=[]
        self.create_snake()
    def create_snake(self):  
        for position in positions:
            self.add_segment(position)

            
    def add_segment(self,position):
        
        snake=Turtle(shape="square")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        
        self.segments.append(snake)
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        
        
    def extend(self):
        self.add_segment(self.segments[-1].position())    
      
    
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].fd(MOVE_DISTANCE)
    
    def up(self):
        if self.segments[0].heading()!= 270:
            self.segments[0].setheading(90) 
    def down(self):
        if self.segments[0].heading()!= 90:
            self.segments[0].setheading(270)
    def right(self):
        if self.segments[0].heading()!= 180:
            self.segments[0].setheading(0)
    def left(self):
        if self.segments[0].heading()!= 0:
            self.segments[0].setheading(180)