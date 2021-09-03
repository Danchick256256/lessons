from handlers.user_input import user_input
from first_game import change_case
from second_game import guess_the_number
from third_game import fib
from fourth_game import shooting_range


def guess_game():
    try:
        while True:
            guess_gametype = int(input("Выберите игру 1/2/3/4, чтобы выйти закончите игру и введите любое не числовое значение в выборе игры\n"))
            if guess_gametype == 1:
                change_case()
            elif guess_gametype == 2:
                guess_the_number()
            elif guess_gametype == 3:
                fib()
            elif guess_gametype == 4:
                shooting_range()
    except ValueError:
        leave = input("Хотите выйти? Y/N\n").lower()
        if leave == "y":
            return
        guess_game()


@user_input
def login(name, password):
    if name == "admin" and password == "admin":
        guess_game()
    else:
        print("Доступ запрещен")


login()
