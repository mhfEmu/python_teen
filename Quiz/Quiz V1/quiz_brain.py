class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def question_left(self):
        return len(self.question_list) > self.question_number
        # if len(self.question_list) == self.question_number:
        #     return False
        # return True

    def next_question(self):
        current_question = self.question_list[self.question_number]

        while self.question_left():
            self.question_number += 1
            input(f"Q,{self.question_number}: {current_question.text} (True/ False): ")
