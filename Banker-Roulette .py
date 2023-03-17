# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
list=len(names)
number=random.randint(0,list-1)
print(f"{names[number]} is going to buy the meal today!")
