import random
from connection import Connection


class Question:
    # Constructor
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
    def __get_question(self) -> str:
        return self.__question
    
    def __get_asnwers(self) -> list:
        return random.shuffle(self.__answers)

    def __get_error(self) -> str:
        return self.__error

    # Setters
    def __set_n_round(self, n_round: int) -> None:
        self.__n_round = n_round

    # Properties
    question = property(__get_question)
    answers = property(__get_asnwers)
    n_round = property(fset=__set_n_round)
    error = property(__get_error)

    # Private methods
    def __validate(self) -> bool:
        if self.__n_round > 0 or self.__n_round <= 5:
            self.__error = "Invalid round number"
            return False

    def __fill_categories(self) -> None:
        try:
            conn = Connection()
            self.__categories = conn.select("SELECT * FROM Categories;")

        except Exception:
            self.__error = conn.error

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
        try:
            conn = Connection()
            self.__questions = conn.select(
                "SELECT question FROM Questions WHERE idCategory = ?;", (self.__category[0],))

            self.__categories = [category[0] for category in self.__categories]

        except Exception:
            self.__error = conn.error

    def __answers_by_question(self) -> None:
        # * TODO: Get answers from database 
        pass

    # Public methods
    def make_question(self) -> None:
        try:
            if not self.__validate():
                raise ValueError(self.__error)

            self.__fill_categories()
            self.__actual_category()
            self.__questions_by_category()
            self.__questions = [question[0] for question in self.__questions]

            self.__question = random.choice(self.__questions)

            # self.__answers_by_question()

        except Exception as e:
            self.__error = e

    def validate_answer(self, answer: str) -> bool:
        return answer == self.__right_answer
