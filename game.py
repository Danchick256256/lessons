import random
import math


class Games:
    def first_game():
        word = input("Введите слово: ")
        result = ""
        for i in word:
            if random.randint(0, 1) == 1:
                result += i.lower()
            else:
                result += i.upper()
        return result

    def second_game():
        left = 0
        right = 1001
        current = (left + right) // 2
        while True:
            print('Ваше число ', current, '? (больше/меньше/равно)')
            answer = input().lower()
            # answer = input("Ваше число ", current,"? (больше/меньше/равно)\n").lower()

            if answer == 'равно':
                return current
                break
            elif answer == 'больше':
                left = current
            elif answer == 'меньше':
                right = current
            else:
                print('Неизвестная команда')
                continue
            current = (left + right) // 2

    def third_game():
        fib1 = fib2 = 1
        n = int(input("Введите число "))
        i = 2
        if n == 1 or n == 0:
            fib_sum = 1
        elif n < 0:
            print("Число отрицательное")
            return
        else:
            for i in range(n):
                fib_sum = fib2 + fib1
                fib1, fib2 = fib2, fib_sum
        return fib_sum

    def fourth_game():
        circle = 10 ** 2 + 10 ** 2
        sqrt = round(math.sqrt(circle))
        counter = 0
        for i in range(10):
            x, y = random.randint(0, sqrt * 2), random.randint(0, sqrt * 2)
            if x <= sqrt and y <= sqrt:
                counter += 1
        return counter
