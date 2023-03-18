student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
a= student_scores[0]
for std in student_scores:
    if a<std:
        a=std
print(f"The highest score in the class is: {a}")
