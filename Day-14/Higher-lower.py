#takes a random dictionary from the data and then removes that particular data so that it doesn't repeat.(Takes place in line 56,57)
def person():
  num=random.choice(data)
  data.remove(num)
  #print(num)
  return num


#Compares the follower of the two random personality/page.(Takes place in line 59)
def compare(opt1,opt2):
  if opt1['follower_count'] > opt2['follower_count']:
    return "a"
  else:
    return "b"
#The game is ran and user is asked which one has highest follower,
def round(opt1,opt2):
  loop=True
  correct=0
  #looped(The game is played) until user gives incorrect answer.
  while loop:
    print(f"\nCompare A: {opt1['name']}, a {opt1['description']}, from {opt1['country']}.")
    print(vs)
    print(f"\nAgainst B: {opt2['name']}, a {opt2['description']}, from {opt2['country']}.")
    answer=input("\nWho has more follower? (Type 'A' or 'B'): ").lower()
    #If user gives correct answer they get one point then the correct option becomes option A and then new random option B is taken.
    if answer==compare(opt1,opt2):
      clear()
      correct+=1
      print(f"\nYou're right. Current score: {correct}")
      if answer=="b":
        opt1=opt2
      opt2=person()
      #The game ends if they have incorrect answer.
    else:
      clear()
      print(f"\nIt's Incorrect.You scored {correct} points")
      loop=False
   
from art import logo
from game_data import data
import random
from art import vs
from replit import clear


play=True
while play:
  print(logo)
  #Two random personalities from the data is taken and removed.
  opt1=person()
  opt2=person()
  
  round(opt1,opt2)
  if input("\nDo you want to play again?\nType 'y or 'n': ").lower()=='y':
    clear()
  else:
    clear()
    print("Thank you for playing the game.")
    play=False
