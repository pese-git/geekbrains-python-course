# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce


def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev + el

numbers = []
while True:
    number = input('Введите целое число (q - выход): ')
    if number == 'q':
        break
    numbers.append(number)

with open('task5.src.txt', 'w') as fout:
        print(' '.join(numbers), file=fout)

sum = 0
with open('task5.src.txt', 'r') as fin:
    line = fin.readline()
    numbers = list(map(lambda x: int(x), line.strip().split(' ')))
    sum = reduce(reducer_func, numbers)


print("Сумма: ", sum)