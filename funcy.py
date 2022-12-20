# function - y=2^x + ln(-5x)
import math

def sub_func_1(x: [int, float]) -> [int, float]:
    """
    Подфункция №1.
    f1 = 2 ^ x
    Args:
        x:   Любое число.
    Returns:
        2 ^ x
    """
    return math.pow(2, x)

def sub_func_2(x: [int, float]) -> [int, float]:
    """
    Подфункция №2.
    f2 = ln(-5x)
    Args:
        x:   Отрицательное число.
    Returns:
        ln(-5x)
    """
    return math.log(-5 * x)

# y = f1 + f2
def main_func(x: [int, float]) -> [int, float]:
    """
    Главная функция.
    y = f1 + f2
    Args:
        x:   Отрицательное число.
    Returns:
        f1 + f2
    """
    return sub_func_1(x) + sub_func_2(x)
