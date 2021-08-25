from handlers.timer import timer
from handlers.input_word import input_word
import random


@timer
@input_word
def change_case(word):
    result = ""
    for i in word:
        if random.randint(0, 1) == 1:
            result += i.lower()
        else:
            result += i.upper()

    print(result)
