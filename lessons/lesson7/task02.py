# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from enum import Enum
from abc import ABC, abstractmethod

class ClothesType(Enum):
    COAT = 1
    SUIT = 2

class Clothes(ABC):
    def __init__(self, name, clothes_type):
        self.name = name
        self.clothes_type = clothes_type

    @abstractmethod
    def calculate(self):
        pass

class Coat(Clothes):
    def __init__(self, name, v=None):
        Clothes.__init__(self, name=name, clothes_type=ClothesType.COAT)
        self.v = v

    @property
    def calculate(self):
        return self.v / 6.5 + 0.5

    def __str__(self):
        return 'Coat(name="{0}", v={1})'.format(self.name, self.v)

class Suit(Clothes):
    def __init__(self, name, h=None):
        Clothes.__init__(self, name=name, clothes_type=ClothesType.SUIT)
        self.h = h

    @property
    def calculate(self):
        return 2 * self.h + 0.3

    def __str__(self):
        return 'Suit(name="{0}", h={1})'.format(self.name, self.h)

if __name__ == '__main__':
    coat = Coat(name="Winter", v=33)
    suit = Suit(name="BOSS", h=172)

    print("Пальто: ", coat, ' ', coat.calculate)
    print("Костюм: ", suit, ' ', suit.calculate)