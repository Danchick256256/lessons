from handlers.timer import timer


@timer
def guess_the_number():
    left = 0
    right = 1001
    current = (left+right) // 2
    while True:
        print('Ваше число ', current, '? (больше/меньше/равно)')
        answer = input().lower()
        #answer = input("Ваше число ", current,"? (больше/меньше/равно)\n").lower()

        if answer == 'равно':
            print('Я угадал ваше число ', current)
            break
        elif answer == 'больше':
            left = current
        elif answer == 'меньше':
            right = current
        else:
            print('Неизвестная команда')
            continue
        current = (left+right) // 2
