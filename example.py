from math import sqrt


message = (f'Добро пожаловать в самую лучшую программу для вычисления '
            'квадратного корня из заданного числа')


def calculate_squar_root(your_number):
    """ Вычисляет квадратный корень."""
    return sqrt(your_number: int)


def calc(your_number: int) -> int:
    """Калькулятор."""
    if your_number <= 0:
        return
    i = calculate_squar_root(your_number)
    root = 0
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          'Это будет: {i}')


print(message)
calc(25.5)
