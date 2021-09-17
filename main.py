import os
from game import Games
from handlers.input import user_input


def guess_game():
    try:
        while True:
            guess_gametype = int(input("Выберите игру 1/2/3/4, чтобы выйти закончите игру и введите любое не числовое значение в выборе игры\n"))
            if guess_gametype == 1:
                print(Games.first_game())
            elif guess_gametype == 2:
                print("Я угадал ваше число: ", Games.second_game())
            elif guess_gametype == 3:
                print(Games.third_game())
            elif guess_gametype == 4:
                print(Games.fourth_game(), " Попадания в яблочко")
    except ValueError:
        leave = input("Хотите выйти? Y/N\n").lower()
        if leave == "y":
            return
        guess_game()


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

@user_input
def login(name, password):
    if name == "admin" and password == "admin":
        guess_game()
    else:
        print("Доступ запрещен")

if __name__ == '__main__':
    try:
        login()
    except KeyboardInterrupt:
        clear_console()
        login()
