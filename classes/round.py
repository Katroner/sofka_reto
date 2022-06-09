from question import Question
from connection import Connection


class Round:
    # Constructor
    def __init__(self) -> None:
        self.__score = 0
        self.__player = ""
        self.__n_round = 0
        self.__answers = []
        self.__question = ""
        self.__answer = ""
        self.__continue = True

    # Getters

    # Setters
    def __set_player(self, player: str) -> None:
        self.__player = player

    def __set_answer(self, answer: str) -> None:
        self.__answer = answer

    # Properties
    player = property(fset=__set_player)
    answer = property(fset=__set_answer)

    # Private methods
    def __validate(self) -> bool:
        if self.__asnwer == "":
            self.__error = "Invalid answer"
            return False

    def __points_per_round(self) -> int:
        if self.__n_round == 1:
            return 10

        elif self.__n_round == 2:
            return 20

        elif self.__n_round == 3:
            return 30

        elif self.__n_round == 4:
            return 40

        elif self.__n_round == 5:
            return 50
        
    def __upload_player_score(self) -> None:
        try:
            conn = Connection()

            conn.upload_insert(
                "INSERT INTO Player (name, score) VALUE(?, ?)", (self.__player, self.__score))

        except Exception:
            self.__error = conn.error

    # Public methods
    def play_game(self) -> None:
        try:
            question = Question()
            question.n_round = self.__n_round
            question.make_question()

            self.__question = question.question
            self.__answers = question.answers

            if not self.__validate():
                raise Exception(self.__error)

            if not question.validate_answer(self.__answer):
                self.__score = 0
                self.__continue = False

            else:
                self.__score += self.__points_per_round()
                if self.__n_round > 0 or self.__n_round < 5:
                    self.__continue = True
                    self.__n_round += 1
                
                else:
                    self.__continue = False
                    self.__upload_player_score()

        except Exception:
            self.__error = question.error
