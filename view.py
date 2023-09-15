import menu
import json


def input_choice():
    while True:
        number = input(menu.input_choice)
        if number.isdigit() and 0 < int(number) < 7:
            return int(number)
        else:
            print(menu.wrong_choice)


def main_menu():
    print(menu.menu)
    return input_choice()


