# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import argparse


def calculate_salary(hours, rate, bonus):
    return hours * rate + bonus


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-hours", type=int, help="Выработка в часах")
    parser.add_argument("-rate", type=int, help="Ставка за час")
    parser.add_argument("-bonus", type=int, help="Премия")

    args = parser.parse_args()
    salary = calculate_salary(hours=args.hours, rate=args.rate, bonus=args.bonus)
    print("Зарплата: ", salary)
