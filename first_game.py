from handlers.timer import timer
from handlers.input_word import input_word
import random


@timer
@input_word
def change_case(word):
    result = ""
    for i in word:
        r_case = random.randint(0, 1)
        if (r_case == 1):
            r_word = i.lower()
            continue
        r_word = i.upper()

        result += r_word

    print(result)
