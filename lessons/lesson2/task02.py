# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = input('Введите список значений через запятую:').split(',')
print(my_list)

size = len(my_list)
index = 0

while index < size - size % 2:
    first_value = my_list[index]
    second_value = my_list[index + 1]

    my_list[index] = second_value
    my_list[index + 1] = first_value
    index += 2

print(my_list)