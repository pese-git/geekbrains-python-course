# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def division(dividend, divisor):
    """
    Функция деления принимает два аргумента
    :param dividend: делиоме
    :param divisor: делитель
    :return: частное
    """
    return dividend / divisor


dividend = float(input("Введите делимое: "))
divisor = float(input("Введите делитель: "))

try:
    quotient = division(dividend,divisor)
    print("Результат деления: ", quotient)
except ZeroDivisionError:
    print('Делитель не может быть 0')