
import random
from art import logo
from replit import clear
#gives random card from the list
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)



#finds the score and gives 0 if someone get blackjack
def calculate_score(cards):
  if 10 in cards and 11 in cards:
    return 0
  if 11 in cards:
    if sum(cards)>21:
      cards.remove(11)
      cards.append(1)
  return sum(cards)


#blackjack game 
def play_game():
  print(logo)
  user_cards = []
  computer_cards = []
  game=True
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while game:
    player_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"Your cards: {user_cards}\nYour current score: {player_score}")
    print(f"   Computer's first card: {computer_cards[0]}")
    #If someone gets blackjack or the user gets above 21 the loops stops and the game is stopped.(and final score will be printed.)
    if computer_score==0 or player_score==0 or player_score>21:
      game=False
    #gives user choice if they want to draw another card or not.If they choose no then the game will end and final score will be printed,
    user_choice=input("Do you want to draw another card ('y' or 'n': ")
    if user_choice=="y":
      user_cards.append(deal_card())
    else:
      game=False
#computer gets the card until it gets blackjack or higher than 17
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
  #The final score is printed after the both the loop for computer and users choice is stopped.
  print(f"Your final hand: {user_cards}\nYour final score: {player_score}\n")
  print(f"Computer's final hand: {computer_cards}\nComputer final score: {computer_score}")
  #after printing the final score comparision is done and winner is declared.
  print(compare(computer_score,player_score))


#compares the score
def compare(computer_score,player_score):
   if player_score == computer_score:
     return "Draw 🙃"
   elif computer_score == 0:
      return "Lose, opponent has Blackjack 😱"
   elif player_score == 0:
      return "Win with a Blackjack 😎"
   elif player_score > 21:
      return "You went over. You lose 😭"
   elif computer_score > 21:
      return "Opponent went over. You win 😁"
   elif player_score > computer_score:
      return "You win 😃"
   else:
      return "You lose 😤"
  

#ask user whether they want to play the game or not
play=input("Do you want to play a game to blackjack?('y' or 'n'): ")
if play=="y":
  clear()
  play_game()
