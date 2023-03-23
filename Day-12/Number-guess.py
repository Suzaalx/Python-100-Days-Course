#user gets choice to choose the difficulty
def set_difficulty():
  level=input("Set the difficulty level for the game.\nType 'hard' or 'easy':\n")
  if level=="easy":
    return 10
  elif level=="hard":
    return 5

#gives user choice to guess the number.User gets either 10 ra 5 choice based on the difficulty level they choose.And prints out the result.
def turns():
  chance=set_difficulty()
  #This loop runs unless the user have no guesses left or if they guessed the correct number
  while chance!=0:
    print(f"\nYou have {chance} attempts remaining to guess the answer\n")
    guess=int(input("Enter your guess: "))
    if chance>1:
      if guess>number:
        print("\nThe number is too high!\n")
        print("\nGuess again.")
      elif guess<number:
        print("\nThe number is too low!")
        print("\nGuess again.")
      elif guess==number:
        print(f"\nYou got it!\nThe number is {number}")
        chance=0
    if chance==1:
      print("\nYou have run out of guesses!")
    chance-=1
   
from art import logo
import random
from replit import clear

#The game runs and user are able to decide whether they want to play another game or not.
play_game=True
while play_game==True:
  print(logo)
  print("Welcome to the number guessing game!!\n")
  print("I'm thinking between a number between 1 and 100.\n")
  number=random.randint(1,100)
  #print(f"The number is {number}\n")
  turns()
  if input("\nDo you want to play again?(Type 'y' or 'n': ")=="n":
    play_game=False
  else:
    clear()
