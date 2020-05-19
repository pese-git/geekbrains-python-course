# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

def convert(line):
    args = line.split(' ')
    return ("{0} {1}".format(args[1], args[0]), int(args[2]) - int(args[3]))


with open('task7.src.txt', 'r') as fin:
    rows = list(map(convert,[line.strip() for line in fin]))

count = 0
average_profit = 0
dictionary = {}
for name, profit in rows:
    count += 1
    average_profit += profit
    dictionary[name] = profit


data = [dictionary, {"average_profit": average_profit / count}]
print(data)

with open('task7.res.txt', 'w') as fout:
    json.dump(data, fout)