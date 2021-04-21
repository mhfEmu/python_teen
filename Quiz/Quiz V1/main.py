from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # from class let's create ne object
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
quiz = QuizBrain(question_bank)
while quiz.question_left():
    quiz.next_question()

print("You've successfully completed the Quiz")
print(f"Your final score is {quiz.score}/ {quiz.question_number}")