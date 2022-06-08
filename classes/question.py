import random


class Question:
    def __init__(self) -> None:
        self.__categories = []
        self.__questions = []
        self.__right_answer = ""
        self.__answers = []

    # Getters
    def get_asnwers(self) -> list:
        self.__answers.append(self.__right_answer)
        return random.shuffle(self.__answers)

    # Properties
    answers = property(get_asnwers)

    # Private methods
    def __fill_categories(self) -> None:
        pass

    def __questions_by_category(self) -> None:
        pass

    # Public methods
    def validate_answer(self, answer: str) -> bool:
        return answer == self.__right_answer
