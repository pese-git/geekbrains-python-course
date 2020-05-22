# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from itertools import cycle
from time import sleep
from datetime import datetime


class TrafficLight:

    def __init__(self, config):
        self.__config = config
        self.__color = ''

    def show_color(self):
        print("{0} {1}".format(datetime.now().time(), self.__color))

    def get_color(self):
        return self.__color

    def run(self, counter):
        for count, el in enumerate(cycle(list(self.__config.keys()))):
            if count > counter:
                break
            self.__color = el
            self.show_color()
            sleep(self.__get_timeout(el))

    def __get_timeout(self, color):
        return self.__config[color]


if __name__ == '__main__':
    config = {
            "красный": 7,
            "желтый": 2,
            "зеленый": 4
        }
    traffic = TrafficLight(config= config)
    traffic.run(10)
