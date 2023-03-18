summ=0
total=0
for number in range(1,101):
    if number%2==0:
        summ+=number
print(summ)
#Anoter way to do the same function
for num in range(2,101,2):
    total+=num
print(total)
