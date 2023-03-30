#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
total=[]
password=""
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
print(type(nr_letters))
  #generate random letters
for i in range(0,nr_letters):
  lett=random.randint(0,len(letters)-1)
  total.append(letters[lett])
  #generate random symbols
for i in range(0,nr_symbols):
  sym=random.randint(0,len(symbols)-1)
  total.append(symbols[sym])
  #generate random number
for i in range(0,nr_numbers):
  num=random.randint(0,len(numbers)-1)
  total.append(numbers[num])
#final password generation
for i in range(0,len(total)):
  order=random.randint(0,len(total)-1)
  password+=total[order]
print(f"Your password id: {password}")
