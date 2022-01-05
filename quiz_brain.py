class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def still_has_question(self):
        still_next_question = True if self.question_number < len(self.questions_list) else False
        return still_next_question

    def check_answer(self, user_answer, right_answer):
        return user_answer.lower() == right_answer

    def next_question(self):
        actual_question = self.questions_list[self.question_number].text
        right_answer = self.questions_list[self.question_number].answer.lower()
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {actual_question} (True / False): ").lower()
        if self.check_answer(user_answer, right_answer):
            self.score += 1
            print("You got it right")
        else:
            print("That is wrong")
        print(f"The correct answer is {right_answer}")
        print(f"Your current score {self.score}/{self.question_number}")
        print("\n")


