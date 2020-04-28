# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [True, 1, 'hello', 3.4, {1,2,3}, {'name': 'jek', 'age': 11}, [100, 200, 300]]
print(my_list)

for value in my_list:
    message = ''
    curr_type = type(value)
    if curr_type is bool:
        message = 'Булево значение'
    elif curr_type is int:
        message = 'Целое значение'
    elif curr_type is str:
        message = 'Строковое значение'
    elif curr_type is float:
        message = 'Дробное значение'
    elif curr_type is set:
        message = 'Перчисление'
    elif curr_type is dict:
        message = 'Словарь'
    elif curr_type is list:
        message = 'Список'
    print(value, ' - ', message)