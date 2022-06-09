
#!/usr/bin/env python3
# *-* coding: utf-8 *-*

import time
from os import system, name
from classes import Round
from colorama import Fore


def validate_name(name: str) -> str:
    while name == "":
        print(Fore.RED + "\nPlease enter your name!\n")
        name = input(Fore.CYAN + "[*] ")

    return name


def validate_answer(answer: str, act_round: Round) -> str:
    answers_posibilities = [str(i) for i in range(1, 6)]
    while answer not in answers_posibilities:
        answer = input(Fore.CYAN + "\nPlease enter a valid answer: ")

    if answer == "1":
        answer = act_round.answers[0]

    elif answer == "2":
        answer = act_round.answers[1]

    elif answer == "3":
        answer = act_round.answers[2]

    elif answer == "4":
        answer = act_round.answers[3]

    else:
        answer = "Exit"

    return answer


def prompt_welcome_message() -> None:
    print(Fore.GREEN + "*********************************************************")
    print(Fore.BLUE + "\n             WELCOME TO THE QUESTIONS GAME!\n")
    print(Fore.GREEN + "*********************************************************")
    print(Fore.CYAN + "\nPlease enter your name to start the game: ")
    print()
    name = input("[*] ")
    name = validate_name(name)

    return name


def clear():
    if name == 'nt':
        system('cls')

    else:
        system('clear')


def prompt_question(act_round: Round) -> None:
    time.sleep(1)
    clear()
    print(Fore.YELLOW +
          f"\nRound: {str(act_round.n_round)}           Score: {str(act_round.score)}")
    print(Fore.YELLOW + f"\n{act_round.question}\n")

    for id, answer in enumerate(act_round.answers):
        print(Fore.YELLOW + f"{id + 1}: {answer}")

    print()
    print(Fore.YELLOW + f"{id + 2}: Exit")
    answer = input(Fore.CYAN + "\nEnter the number of your answer: ")

    return answer


def main():
    try:
        name = prompt_welcome_message()
        act_round = Round()
        act_round.player = name

        while act_round.continue_playing:
            if not act_round.play_game():
                print(act_round.error)

            answer = prompt_question(act_round)
            answer = validate_answer(answer, act_round)
            act_round.player_answer = answer
            
            if not act_round.check_points():
                print(act_round.error)

    except Exception as e:
        if act_round.error != "":
            print(act_round.error)

        else:
            print(e)


if __name__ == "__main__":
    main()
