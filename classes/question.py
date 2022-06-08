import random


class Question:
    def __init__(self) -> None:
        self.__n_round = 0
        self.__answers = []
        self.__category = ""
        self.__question = ""
        self.__questions = []
        self.__categories = []
        self.__right_answer = ""
        self.__error = ""

    # Getters
    def get_asnwers(self) -> list:
        self.__answers.append(self.__right_answer)
        return random.shuffle(self.__answers)

    def get_error(self) -> str:
        return self.__error

    # Setters
    def set_n_round(self, n_round: int) -> None:
        self.__n_round = n_round

    # Properties
    answers = property(get_asnwers)
    n_round = property(fset=set_n_round)
    error = property(get_error)

    # Private methods
    def __validate(self) -> bool:
        if self.__n_round <= 0 or self.__n_round > 5:
            self.__error = "Invalid round number"
            return False

    def __fill_categories(self) -> None:
        pass

    def __actual_category(self) -> None:
        if self.__n_round == 1:
            self.__category = self.__categories[0]

        elif self.__n_round == 2:
            self.__category = self.__categories[1]

        elif self.__n_round == 3:
            self.__category = self.__categories[2]

        elif self.__n_round == 4:
            self.__category = self.__categories[3]

        elif self.__n_round == 5:
            self.__category = self.__categories[4]

    def __questions_by_category(self) -> None:
        pass

    def __answers_by_question(self) -> None:
        pass

    # Public methods
    def make_question(self) -> None:
        try:
            if not self.__validate():
                raise ValueError(self.__error)

            self.__fill_categories()
            self.__actual_category()
            self.__questions_by_category()

            self.question = random.choice(self.__questions)

            self.__answers_by_question()

        except Exception as e:
            self.__error = e

    def validate_answer(self, answer: str) -> bool:
        return answer == self.__right_answer
