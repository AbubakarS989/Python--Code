from data import question_data
from Questions_model import questions
from quiz_brain import brain

question_bank=[]

for question in question_data: 
    question_text=question["text"]
    question_ans=question["answer"]
    new_qs=questions(question_text,question_ans)
    # print(question_ans)
    # print(question_text)
    question_bank.append(new_qs)
    quiz=brain(question_bank)
run = 0
while quiz.still_have_qs():  # Use the quiz object to check if there are still questions
    quiz.next_question()
    run += 1
    if run == len(question_bank):
        print("You have completed the quiz!")
        print(f"Your final score is: {quiz.score}/{len(question_bank)}")
        break




