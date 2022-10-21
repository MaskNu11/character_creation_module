from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')


def CalculateSquareRoot(Number):
    """Вычисляет квадратный корень."""
    num = sqrt(Number)
    return num


def calc(your_number):
    if your_number <= 0:
        return
    num = CalculateSquareRoot(your_number)
    print(f"Мы вычислили квадратный корень из введённого вами числа. "
          f"Это будет: {num}")


print(message)
calc(25.5)
