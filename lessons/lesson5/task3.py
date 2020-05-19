# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

employes = []
with open('task3.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        args = line.strip().split(' ')
        employes.append((args[0], args[1], int(args[2])))

print(employes)

for name, surname, salary in employes:
    if salary < 20000:
        print("{0} {1} {2}".format(name, surname, salary))

counter = 0
salaries = 0
for _, _, salary in employes:
    salaries += salary
    counter += 1

print("Срердняя зарабтная плата: {0:0.2f}".format( salaries / counter))