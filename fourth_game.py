import random


def shooting_range():
    random.seed()
    arr = [[random.randint(1, 10) for i in range(2)] for i in range(10)]
    counter = 0
    for i in range(10):
        if arr[i][0] == 1 or arr[i][1] == 1:
            #print(arr[i])
            counter += 1
    print(counter, "Попаданий в яблочко")