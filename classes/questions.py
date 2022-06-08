import random


class Question:
    def __init__(self) -> None:
        self.category = ""
        self.question_text = {}
        self.wrong_answers = []
        self.right_answer = ""
        

    def get_text(self) -> str:
        return self.question_text

    def get_asnwers(self) -> list:
        self.wrong_answers.append(self.right_answer)
        random.shuffle(self.wrong_answers)

        return self.wrong_answers

    text = property(get_text, None)
    answers = property(get_asnwers)
