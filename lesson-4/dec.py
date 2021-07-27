from time import time
__all__ = ["input_word", "timer", "user_input"]


def input_word(func):
    def wrapper(*args, **kwargs):
        word = input("Введите слово: ")
        func(String=Word, *args, **kwargs)
    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        started_at = time()
        func(*args, **kwargs)
        print('Время выполнения ', round(time() - started_at), 'сек')

    return wrapper


def user_input(func):
    def wrapper(*args, **kwargs):
        name = input("Введите имя: ")
        password = input("Введите пароль: ")
        func(name=name, password=password, *args, **kwargs)

    return wrapper
