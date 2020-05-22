# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print("Поехали")

    def stop(self):
        print("Остановились")

    def turn(self, direction):
        print("Поворот: ", direction)

    def show_speed(self):
        print("Скорость: ", self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышена скорость: ", self.speed)
        else:
            print("Скорость: ", self.speed)

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышена скорость: ", self.speed)
        else:
            print("Скорость: ", self.speed)

class PoliceCar(Car):
    pass

if __name__ == '__main__':
    cars = [
        TownCar(
            name= "Автобус",
            color="белый",
            speed=80,
            is_police=False
        ),
        WorkCar(
            name="Хлебовоз",
            color="белый",
            speed=77,
            is_police=False
        ),
        SportCar(
            name="Ферари",
            color="красный",
            speed=177,
            is_police=False
        ),
        SportCar(
            name="Полиция",
            color="черный",
            speed=199,
            is_police=True
        )
    ]

    for car in cars:
        print("Название: ", car.name)
        print("Цвет: ", car.color)
        print("Скорость: ", car.speed)
        print("Полиция: ", car.is_police)


        car.go()
        car.turn("на лево")
        car.show_speed()
        car.turn("прямо")
        car.stop()
