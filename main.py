from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []


for i in question_data:
    question = Question(i['question'], i['correct_answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"You final score was: {quiz.score}/{quiz.question_number}")


