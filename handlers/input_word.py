def input_word(func):
    def wrapper(*args, **kwargs):
        word = input("Введите слово: ")
        func(word=word, *args, **kwargs)
    return wrapper