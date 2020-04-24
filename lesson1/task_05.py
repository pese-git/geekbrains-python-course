# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы
# и определите прибыль фирмы в расчете на одного сотрудника.

print('TODO: Нет проверки корректности ввода пользователя')
print('TODO: Поэтому прошу вводить только корректные значения')

proceeds = float(input('Введите выручку фирмы: '))
outgoings = float(input('Введите издержки фирмы: '))

if proceeds > outgoings:
    print('выручка больше издержек')
elif proceeds < outgoings:
    print('издержки больше выручки')
else:
    print('выручка равна издержкам')

net_profit = 0
profitability = 0
if proceeds > outgoings:
    net_profit = proceeds - outgoings
    profitability = net_profit / proceeds

employees = 0
if profitability > 0:
    employees = int(input('Введите кол-во сотрудников: '))

proceeds_per_employee = 0
if employees > 0 and net_profit > 0:
    proceeds_per_employee = net_profit / employees


print('Выручка: ', proceeds)
print('Издержки: ', outgoings)
print('Чистая прибыль: ', net_profit)
print('Рентабельность: ', profitability)

if employees > 0:
    print('Кол-во сотрудников: ', employees)
    print('Выручка на одного сотрдуника: ', proceeds_per_employee)