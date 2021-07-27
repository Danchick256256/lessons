from dec import *
import random


@timer
@input_word
def change_case(word):
    result = ""
    for i in word:
        r_case = random.randint(0, 1)
        if (r_case == 1):
            rs_Word = i.lower()
        else:
            rs_Word = i.upper()

        result += rs_Word

    print(result)
