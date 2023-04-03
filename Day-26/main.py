# num=[1,2,3]
# new_num=[no*2 for no in num]
# print(new_num)

# new_num=[n*2 for n in range(1,5)]
# print(new_num)


names=['sujal','khatri','boksi','dragon','aydahd','dhadh']
names2=['sujal','khatri','boksi','dragon',"hawa",'hduaidc']
result=[name for name in names if name not in names2]
print(result)