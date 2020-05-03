# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def calculate(arguments):
    res = 0
    for value in arguments:
        res += float(value)
    return res


print("TODO: необходимо вводить только список чисел или для выхода - q.")
print("TODO: Иначе программа упадет.")

result = 0
while True:
    str_args = input("Введите список чисел разделенных пробелами (для выхода введите с новой строки q): ")
    if str_args == "q":
        break

    args = str_args.split(' ')
    result += calculate(args)

print("Сумма: ", result)
