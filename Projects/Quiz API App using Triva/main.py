from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface




# ! Unescape character Website
# https://www.freeformatter.com/html-escape.html#before-output

# !  CharacterEntities
# https://www.w3schools.com/html/html_entities.asp

#! Get Data from this website easily
# https://opentdb.com/api_config.php


# ! Get data from the Trivia Data base API
response=requests.get(url="https://opentdb.com/api.php?amount=20&category=9&difficulty=medium&type=boolean")
response.raise_for_status()
question_data=response.json()["results"]
# print(question_data)

question_bank = []
for question in question_data:
    # print(question)
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)      

# App UI

quiz = QuizBrain(question_bank)
quiz_app=QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
