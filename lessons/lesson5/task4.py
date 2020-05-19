# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

number_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

rows = []
with open('task4.txt', 'r') as fin:
    lines = fin.readlines()
    for line in lines:
        args = line.strip().split('—')
        rows.append((args[0].strip(), args[1].strip()))

with open('task4.res.txt', 'w') as fout:
    for key, value in rows:
        print("{0} — {1}".format(number_dict[key], value), file=fout)


