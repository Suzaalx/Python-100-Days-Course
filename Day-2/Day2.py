print("Welcome to the tip calculator! ")
bill=input("What was the total bill? " ) 
tip=input("How much tip would you like to give? 10, 12, or 15? " )  
person = input("How many people to split the bill? " ) 
tip_decimal = int(tip)/100 +1
pay= (int(bill)/int(person)) * tip_decimal
final_pay = '{0:.2f}'.format(pay)
print(f"Each person will pay: {final_pay}")
