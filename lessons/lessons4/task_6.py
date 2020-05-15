# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle

if __name__ == "__main__":
    start_num = int(input('Введите стартовое число: '))
    iter_count = int(input('Введите кол-во итераций: '))

    for i, el in enumerate(count(start_num)):
        if iter_count - 1 < i:
            break
        print("Value: ", el)

    iter_count = int(input('Введите кол-во итераций: '))


    for i, el in enumerate(cycle(['лево', 'верх', 'право', 'низ'])):
        if iter_count - 1 < i:
            break
        print("Value: ", el)