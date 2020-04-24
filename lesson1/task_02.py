# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print('TODO: Нет проверки корректности ввода пользователя')
print('TODO: Поэтому прошу вводить только корректные значения')

user_time = int(input("Input seconds: "))
hours = user_time // 3600

minutes = (user_time - (hours * 3600)) // 60
seconds = (user_time - (hours * 3600) - (minutes * 60)) % 60


print('Hours: ', hours)
print('Minutes: ', minutes)
print('Seconds: ', seconds)

print('{0:02d}:{1:02d}:{2:02d}'.format(hours, minutes, seconds))