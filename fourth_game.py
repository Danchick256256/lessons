import random
import math


def shooting_range():
    random.seed()
    circle = 10**2 + 10**2
    sqrt = round(math.sqrt(circle))
    counter = 0
    for i in range(10):
        x, y = random.randint(0, sqrt*2), random.randint(0, sqrt*2)
        if x <= sqrt and y <= sqrt:
            counter += 1
    print(counter, "Попаданий в яблочко")
