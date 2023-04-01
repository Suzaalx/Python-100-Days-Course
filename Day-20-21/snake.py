from turtle import Turtle
X=0
MOVE_DISTANCE=20
# segments=[]
# for i in range(3):
#     snake=Turtle(shape="square")
#     snake.color("white")
#     snake.penup()
#     snake.goto(x=-x,y=0)
#     x+=20
#     segments.append(snake)
    
# for seg_num in range(len(segments)-1, 0, -1):
#         new_x=segments[seg_num-1].xcor()
#         new_y=segments[seg_num-1].ycor()
#         segments[seg_num].goto(new_x,new_y)
    
#     segments[0].fd(20)   
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