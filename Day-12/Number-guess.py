from art import logo
import random
print(logo)
print("Welcome to the number guessing game!!")
print("I'm thinking between a number between 1 and 100.")
number=random.randint(1,101)
print(f"The number is {number}")
level=input("Set the difficulty level for the game.\nType 'hard' or 'easy':\n")
if level=="easy":
  chance=10
elif level=="hard":
  chance=5

while chance!=0:
  print(f"You have {chance} attempts remaining to guess the answer")
  guess=int(input("Enter your guess: "))
  if chance>1:
    if guess>number:
      print("The number is too high!")
      print("Guess again.")
    elif guess<number:
      print("The number is too low!")
      print("Guess again.")
    elif guess==number:
      print(f"You got it!\nThe number is {number}")
      chance=0
  if chance>0:
    print("You have run out of guesses!")
  chance-=1
