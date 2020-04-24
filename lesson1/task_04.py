# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

print('TODO: Нет проверки корректности ввода пользователя')
print('TODO: Поэтому прошу вводить только корректные значения')

user_str = input('Input number: ')

if int(user_str) < 0:
    print('Error number. Please enter number > 0')
    exit(1)

big_number = 0
index = 0
count = len(user_str)

number = int(user_str)
curr_number = 0

while index < count:
    curr_number = int(user_str[index])
    print('Curr number: ', curr_number)
    if big_number < curr_number:
        big_number = curr_number

    index += 1

print('User number: ', int(user_str))
print('Big number: ', big_number)
