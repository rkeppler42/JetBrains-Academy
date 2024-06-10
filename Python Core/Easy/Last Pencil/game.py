"""
Game of pencils.
"""
import random


class Zero(Exception):
    """Raised when the number of pencils == 0"""


class WrongNameInput(Exception):
    """Raised when a wrong name is inputted in lst_game_order"""


class WrongNumberOfPencils(Exception):
    """Raised when the number of pencils taken are not 1, 2 or 3"""


class InvalidNumberOfPencils(Exception):
    """Raised when the number of pencils taken are greater than the number of pencils on the table"""


def main():
    """
    Function that will invoke all the other functions and display the game.
    :return: None
    """
    pencils = n_of_pencils()
    game_order = lst_game_order()
    print_pencils(pencils)
    gameplay(pencils, game_order)


def n_of_pencils() -> int:
    """
    Function to determine the number of pencils in the game.
    :return: int - number of pencils.
    """
    print("How many pencils would you like to use:")
    while True:
        try:
            pencils = int(input())
            if pencils == 0:
                raise Zero
            elif pencils < 0:
                raise ValueError
            break
        except ValueError:
            print("The number of pencils should be numeric")
            pass
        except Zero:
            print("The number of pencils should be positive")
            pass
    return pencils


def lst_game_order() -> list:
    """
    Function that determines the first player to play and returns a list of the order of play.
    :return: list - of the order of play, where list[0] = first_player
    """
    print("Who will be the first (John, Jack):")
    while True:
        try:
            first_player = input()
            if first_player != "John" and first_player != "Jack":
                raise WrongNameInput
            break
        except WrongNameInput:
            print("Choose between John and Jack")

    return ["John", "Jack"] if first_player == "John" else ["Jack", "John"]


def print_pencils(n):
    """
    Given an n of pencils print it n times
    :param n: int - number of pencils that should be printed
    :return: None
    """
    print("|" * n)


def gameplay(pencils, game_order):
    """
    Function that will control the gameplay of the game.
    :param pencils: int - number of pencils.
    :param game_order: lst - list of the order of the game.
    :return: None
    """
    loop = 0
    print(f"{game_order[loop % 2]}'s turn:")
    while True:
        if game_order[loop % 2] == "John":
            try:
                n_of_pen = input()
                if n_of_pen != '1' and n_of_pen != '2' and n_of_pen != '3':
                    raise WrongNumberOfPencils
                if int(n_of_pen) > pencils:
                    raise InvalidNumberOfPencils
            except WrongNumberOfPencils:
                print("Possible values: '1', '2' or '3'")
                continue
            except InvalidNumberOfPencils:
                print("Too many pencils were taken\n")
                continue
        else:
            n_of_pen = bot(pencils)
        pencils -= int(n_of_pen)
        loop += 1
        if pencils <= 0:
            print(f"{game_order[loop % 2]} won!")
            break
        print_pencils(pencils)
        print(f"{game_order[loop % 2]}'s turn:")


def bot(pencils) -> int:
    """
    Function that will control the bot.
    :param pencils: int - number of pencils that are still on the table.
    :return: int - number of pencils that the bot will take from the table.
    """
    if pencils % 4 == 1:
        random_pick = random.randint(1, 3)
        while random_pick > pencils:
            random_pick = random.randint(1, 3)
        print(random_pick)
        return random_pick
    if pencils % 4 == 3:
        print(2)
        return 2
    print(3 - pencils % 4)
    return 3 - pencils % 4


main()
