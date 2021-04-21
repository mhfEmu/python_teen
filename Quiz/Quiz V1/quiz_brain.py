class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def question_left(self):
        return len(self.question_list) > self.question_number
        # if len(self.question_list) == self.question_number:
        #     return False
        # return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q,{self.question_number}: {current_question.text} (True/ False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, answers, correct_answer):
        print(f"The correct answer was {correct_answer}")
        if answers.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right \n Your current score is {self.score}/{self.question_number}")
        else:
            print(f"You got it wrong. \n Your current score is {self.score}/{self.question_number}")
        print("\n")
