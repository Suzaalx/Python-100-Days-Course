from data import question_data
from question_model  import Question
from quiz_brain import Quiz
question_bank=[]      

for i in question_data:
   new_question= Question(i['question'],i['correct_answer'])
   question_bank.append(new_question)
   

quiz=Quiz(question_bank)
while quiz.has_questions():
    quiz.next_question()
print("You have completed the quiz.")

print(f"Your final score was: {quiz.score}/{len(question_bank)}")