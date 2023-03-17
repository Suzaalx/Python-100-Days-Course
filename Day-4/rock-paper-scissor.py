import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Welcome to the Rock-Paper-Scissor game!\nSave the world by winning this game against the computer")
game=["rock", "paper","scissors"]
#Takes user's input
player=input("Choose your weapon!(rock, paper ,or scissors)\n")
if ((player=="rock") or (player=="paper") or (player=="scissor")):
    print(f"You have chosen {player}")
    if player=="rock":
      print(rock)
    elif player=="paper":
      print(paper)
    elif player == "scissors":
      print(scissors)
    
    
    #takes computer's choice
    comp=random.randint(0,2)
    computer=game[comp]
    print(f"computer has chosen {computer}")
    if computer=="rock":
      print(rock)
    elif computer=="paper":
      print(paper)
    elif computer == "scissors":
      print(scissors)
    #runs the game
    if ((player=="rock") and (computer=="paper")):
      print("The computer wins the game")
    elif((player=="paper") and (computer=="scissors")):
      print("The computer wins")
    elif((player=="Scissors") and (computer=="rock")):
      print("The computer wins")
    elif(((player=="scissors")and (computer=="scissors")) 
         or((player=="rock")and 
        (computer=="rock")) or ((player=="paper")and 
        (computer=="paper"))):
      print("It's a Draw!!")
    else:
      print("Congratulation! You win the game")

else:
  print("Invalid choice")
