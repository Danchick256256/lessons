from dec import timer


@timer
def fib():
    fib1 = 1
    fib2 = 1
    n = input("Введите число ")
    n = int(n)
    i = 2
    if n == 1 or n == 0:
        fib_sum = 1
    elif n < 0:
        print("Неправильное число")
        return
    else:
        for i in range(n):
            fib_sum = fib2 + fib1
            fib1 = fib2
            fib2 = fib_sum
    print(fib_sum)
