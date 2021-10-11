import requests
from handlers.user_input import Handlers

url = "http://127.0.0.1:5000"


def guess_game():
    try:
        while True:
            guess_gametype = int(input("Выберите игру 1/2/3/4, чтобы выйти закончите игру и введите любое не числовое значение в выборе игры\n"))
            if guess_gametype == 1:
                first_game()
            elif guess_gametype == 2:
                second_game()
            elif guess_gametype == 3:
                third_game()
            elif guess_gametype == 4:
                fourth_game()
    except ValueError:
        leave = input("Хотите выйти? Y/N\n").lower()
        if leave == "y":
            return
        guess_game()


def auth_method(login: str,
                password: str):
    return requests.post(url=f"{url}/api/auth/login", json={"username": login, "password": password}).json()["status"]


def main():
    while True:
        auth_resp = auth_method(login=(login := input("Enter your login:\t")), password=input("Enter your password:\t"))
        if auth_resp:
            guess_game()
        else:
            print("Try again.")


@Handlers
def first_game(value):
    print(requests.post(url=f"{url}/first_game", json={"value": value}).json()["value"])


def second_game():
    while True:
        value = input("Введите значение:\t")
        print(requests.post(url=f"{url}/second_game", json={"value": value}).json()["value"])
        if requests.post(url=f"{url}/second_game", json={"value": value}).json()["status"]:
            break


@Handlers
def third_game(value):
    print(requests.post(url=f"{url}/third_game", json={"value": value}).json()["value"])


@Handlers
def fourth_game(value):
    print(requests.post(url=f"{url}/fourth_game", json={"value": value}).json()["value"])


if __name__ == '__main__':
    main()
