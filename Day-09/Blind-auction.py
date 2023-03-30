from replit import clear
from art import logo
print(logo)
data={}
continue_loop=True
def winner(data):
  highest_bid=0
  for key in data:
    value=data[key]
    if value>highest_bid:
      highest_bid=value
      winner=key
  print(f"The winner of the bid is {winner} with ${highest_bid} bid.")

while continue_loop:
  name=input("Enter your name: ")
  bid=int(input("Enter your bid price:$ "))
  data[name]=bid
  other_people=input("Are there other people?(Enter YES or NO):")
  if other_people=="NO":
    continue_loop=False
    print(data)
    clear()
    winner(data)
    
  else:
    clear()
