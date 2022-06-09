from colorama import Fore
from classes.connection import Connection
from classes.question import Question


class Round:
    # Constructor
    def __init__(self) -> None:
        self.__score = 0
        self.__player = ""
        self.__n_round = 1
        self.__answers = []
        self.__question = ""
        self.__player_answer = ""
        self.__continue = True
        self.__error = ""
        self.__my_question = Question()

    # Getters
    def __get_error(self) -> str:
        return self.__error

    def __get_asnwers(self) -> list:
        return self.__answers

    def __get_question(self) -> str:
        return self.__question

    def __get_n_round(self) -> int:
        return self.__n_round

    def __get_continue(self) -> bool:
        return self.__continue

    def __get_score(self) -> int:
        return self.__score

    # Setters
    def __set_player(self, player: str) -> None:
        self.__player = player

    def __set_answer(self, answer: str) -> None:
        self.__player_answer = answer

    # Properties
    score = property(__get_score)
    error = property(__get_error)
    answers = property(__get_asnwers)
    n_round = property(__get_n_round)
    question = property(__get_question)
    player = property(fset=__set_player)
    continue_playing = property(__get_continue)
    player_answer = property(fset=__set_answer)

    # Private methods
    def validate(self) -> bool:
        if self.__player == "":
            self.__error = "Player name is empty"
            return False

        return True

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
                "INSERT INTO Player (name, score) VALUES (?, ?)", (self.__player, self.__score))

        except Exception:
            self.__error = conn.error

    # Public methods
    def play_game(self) -> None:
        try:
            if not self.validate():
                return False

            self.__my_question.n_round = self.__n_round
            self.__my_question.make_question()

            self.__question = self.__my_question.question
            self.__answers = self.__my_question.answers

            return True

        except Exception as e:
            if self.__my_question.error != "":
                self.__error = self.__my_question.error

            else:
                self.__error = e

            return False

    def check_points(self) -> None:
        try:
            if self.__player_answer == "Exit":
                self.__continue = False

                if self.__score != 0:
                    print(
                        Fore.GREEN + f"Saving score for {self.__player} which is {self.__score} points")
                    self.__upload_player_score()

                return True

            else:
                if self.__continue:
                    if not self.__my_question.validate_answer(self.__player_answer):
                        self.__score = 0
                        print(
                            Fore.RED + f"\n[!] Wrong answer! You lose all points!")
                        self.__continue = False

                    else:
                        self.__score += self.__points_per_round()
                        if 0 < self.__n_round < 5:
                            self.__continue = True
                            self.__n_round += 1

                        else:
                            self.__continue = False
                            print(
                                Fore.GREEN + f"\n[!] Congratulations {self.__player} You won the game! Your score is {self.__score}!")
                            print("Saving your score...")
                            self.__upload_player_score()

                    return True

        except Exception as e:
            if self.__my_question.error != "":
                self.__error = self.__my_question.error

            else:
                self.__error = e

            return False
