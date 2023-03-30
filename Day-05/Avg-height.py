student_heights = input("Input a list of student heights ").split()
total_height=0
num=0
for heights in student_heights:
  
  num=num+1
  total_height+= int(heights)
average=round(total_height/num)
print(average)

