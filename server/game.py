import random
import math
from flask import jsonify, request


class FirstGame:
    @app.route('/first_game', methods=['POST'])
    def first_game(self):
        self.user_data = request.get_json()
        self.value = self.user_data["value"]
        result = ""
        for i in self.value:
            if random.randint(0, 1) == 1:
                result += i.lower()
            else:
                result += i.upper()
        return jsonify(value=result)


class SecondGame:
    @app.route('/second_game', methods=['POST'])
    def second_game(self):
        self.user_data = request.get_json()
        self.value = self.user_data["value"]
        counter = 0
        left = 0
        right = self.value // 2
        current = (left + right) // 2
        while True:
            print('Ваше число ', current, '? (больше/меньше/равно)')
            answer = input().lower()
            if answer == 'равно':
                counter += 1
                return jsonify(value=current, counter=counter)
                break
            elif answer == 'больше':
                left = current
                counter += 1
            elif answer == 'меньше':
                right = current
                counter += 1
            else:
                return ('Неизвестная команда')
                continue
            current = (left + right) // 2


class ThirdGame:
    def third_game(self, value):
        self.value = int(value)
        fib1 = fib2 = 1
        i = 2
        if self.value == 1 or self.value == 0:
            fib_sum = 1
        elif self.value < 0:
            return ("Число отрицательное")
        else:
            for i in range(self.value):
                fib_sum = fib2 + fib1
                fib1, fib2 = fib2, fib_sum
        print(fib_sum)
        return fib_sum


class FourthGame:
    def fourth_game():
        circle = 10 ** 2 + 10 ** 2
        sqrt = round(math.sqrt(circle))
        counter = 0
        for i in range(10):
            x, y = random.randint(0, sqrt * 2), random.randint(0, sqrt * 2)
            score = (x + y) * 2
            if x <= sqrt and y <= sqrt:
                counter += 1
        return counter, score


class Games:
    def first_game():
        return FirstGame.first_game()


    def second_game():
        current, counter = SecondGame.second_game()
        return f"{current}, Мне потребовалось {counter} попыток/ка/ки"


    def third_game():
       return ThirdGame.third_game()


    def fourth_game():
        counter, score = FourthGame.fourth_game()
        return f"{counter} Попадания в яблочко, Ваш счет {score}"
