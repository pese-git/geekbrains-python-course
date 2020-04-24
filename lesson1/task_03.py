# 3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

print('TODO: Нет проверки корректности ввода пользователя')
print('TODO: Поэтому прошу вводить только корректные значения')

user_number = int(input('Input number: '))

if user_number > 9:
    print('Big number. Please enter 0..9')
    exit(0)

n = int('{0:d}'.format(user_number))
nn = int('{0:d}{1:d}'.format(user_number, user_number))
nnn = int('{0:d}{1:d}{1:d}'.format(user_number, user_number, user_number))
sum = n + nn + nnn

print('User number: ', user_number)
print('N: ', n)
print('NN: ', nn)
print('NNN: ', nnn)
print('SUM: ', sum)
