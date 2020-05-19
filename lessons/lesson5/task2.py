# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('task2.txt', 'r') as f:
    lines = f.readlines()
    print('Строки: ', lines)
    print('Кол-во строк: ', len(lines))
    for line in lines:
        words = line.split(' ')
        print('Строка: ', line.strip())
        print('Кол-во слов в строке: ', len(words))
