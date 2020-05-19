# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


from functools import reduce


def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return el_prev + el


def convert_func(el):
    str = el.strip()
    return int(str) if len(str) > 0 else 0

subjects = {}
with open('task6.src.txt', 'r') as fin:
    lines = fin.readlines()
    for line in lines:
        args = line.strip().split(':')
        name = args[0]
        clear_str = args[1].replace('(л)', '').replace('(пр)', '').replace('(лаб)', '').replace('—', '')
        counters = list(map(convert_func, clear_str.strip().split(' ')))
        subjects[args[0]] = reduce(reducer_func, counters)

print(subjects)
