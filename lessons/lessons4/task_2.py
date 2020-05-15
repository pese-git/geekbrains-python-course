# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.

def my_compare(col, index, value):
    if len(col) == 0 or index < 1:
        return False

    if value < col[index - 1]:
        return False

    return True


if __name__ == "__main__":
    curr_list = [10, 5, 6, 9, 4, 8, 3]
    new_list = [el for num, el in enumerate(curr_list) if my_compare(curr_list, num, el)]
    print("Результат: ", new_list)
