class Handlers:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        return self.function(self, *args, **kwargs, value=input("Введите значение: "))