# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.


def is_unique(col, value):
    if len(col) == 0:
        return False

    count = 0
    for el in col:
        if el == value:
            count += 1

    return True if count == 1 else False


if __name__ == "__main__":
    curr_list = [10, 5, 6, 9, 4, 8, 3, 5, 10, 3, 4]
    new_list = [el for el in curr_list if is_unique(curr_list, el)]
    print("Результат: ", new_list)
