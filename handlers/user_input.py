def user_input(func):
    def wrapper(*args, **kwargs):
        name = input("Введите имя: ")
        password = input("Введите пароль: ")
        func(name=name, password=password, *args, **kwargs)

    return wrapper