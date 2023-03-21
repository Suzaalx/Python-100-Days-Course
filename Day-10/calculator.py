from art import logo
from replit import clear
#add
def add(n1,n2):
  return n1+n2
#subtract
def subtract(n1,n2):
  return n1-n2
#multiply
def multiply(n1,n2):
  return n1*n2
#divide
def divide(n1,n2):
  return n1/n2
operators={
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}
def calculation():
  continue_loop=True
  print(logo)
  n1=float(input("Enter the first number:"))
  while continue_loop==True:
    for key in operators:
      print(key)
    operand=input("Enter the operand: ")
    n2=float(input("Enter the another number: "))
    function=operators[operand]
    clear()
    print(logo)
    print(f"{n1} {operand} {n2} : {function(n1,n2)}")
    if input(f"If you want to continue calculating with {function(n1,n2)} ,Type 'y' else type 'n' to stop.")=="y":
      n1=function(n1,n2)
    else:
      clear()
      continue_loop=False
      calculation()

calculation()
