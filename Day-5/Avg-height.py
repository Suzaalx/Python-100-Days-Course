student_heights = input("Input a list of student heights ").split()
heights=0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  
  heights= heights+ student_heights[n]
average=round(heights/len(student_heights))
print(average)
