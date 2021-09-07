from time  import time


def timer(func):
    def wrapper(*args, **kwargs):
        started_at = time()
        func(*args, **kwargs)
        print('Время выполнения ', round(time() - started_at), 'сек')

    return wrapper