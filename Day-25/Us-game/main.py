from turtle import Turtle, Screen
import pandas
from tkinter import messagebox
guess=0
loop= True
guessed=[]
#reading the data
data=pandas.read_csv("Day-25/Us-game/50_states.csv")
states=data.to_dict()
state_list=data["state"].to_list()
state_x=data["x"].to_list()
state_y=data["y"].to_list()
print(state_x)


#state name writer function in their respective co-ordinate
class State_name(Turtle):
    def __init__(self,answer,x,y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x,y)
        self.write(answer)
            
#screen
screen=Screen()
img=Turtle()
screen.title("U.S States Game")
image="Day-25/Us-game/blank_states_img.gif"
screen.addshape(image)
img.shape(image)

#the loop whicch continues until user guesses all the state.Note: There is no pentalty for wrong guess but it will give prompts based on user's choice to let them know whether it is  correct guess or not.
while loop:
    answer=screen.textinput(title=f"Guess the state  {guess}/{len(state_list)}",prompt="What's another state name?").title()
    print(answer)
    if answer in state_list and guess<len(state_list) and answer not in guessed:
        num=state_list.index(answer)
        x=state_x[num]
        y=state_y[num]
        state_name=State_name(answer,x,y)
        guess+=1
        guessed.append(answer)
    elif answer=="Exit":
        break
    elif guess==len(state_list):
        loop=False
    elif answer=="":
        messagebox.showinfo("No input!","Enter a state")
    elif answer in guessed:
        messagebox.showinfo(title="Incorrect guess", message=f"{answer} already guessed")
    else:
        messagebox.showinfo(title="Incorrect guess", message=f"{answer} not on the map")
# print(guessed)
print(state_list)

# creates a new csv with states which user couldn't guess
not_guessed=[state for state in state_list if state not in guessed]

print(not_guessed)
df=pandas.DataFrame(not_guessed)
df.to_csv("Day-25/Us-game/learn.csv")


screen.exitonclick()