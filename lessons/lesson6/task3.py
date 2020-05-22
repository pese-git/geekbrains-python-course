# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class IncomeBuilder:
    def __init__(self):
        self._income = {"wage": 0.0, "bonus": 0.0}

    def wage(self, value):
        self._income['wage'] = value
        return self

    def bonus(self, value):
        self._income['bonus'] = value
        return self

    def build(self):
        return self._income


class Worker:
    def __init__(self, name, surname, position, income=None):
        if income is None:
            income = {"wage": 0.0, "bonus": 0.0}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

    def show_income(self):
        print(self._income)


class Position(Worker):
    def get_full_name(self):
        return "{0} {1}".format(self.name, self.surname)

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    workers = [
        Position(
            name="Владимир",
            surname="Путин",
            position="Президент РФ",
            income=IncomeBuilder()
                .wage(125000)
                .bonus(3500)
                .build()
        ),
        Position(
            name="Владимир",
            surname="Зеленский",
            position="Президент Украины",
            income=IncomeBuilder()
                .wage(100000)
                .bonus(1500)
                .build()
        ),
        Position(
            name="Александр",
            surname="Лукашенко",
            position="Президент РБ",
            income=IncomeBuilder()
                .wage(105000)
                .bonus(2500)
                .build()
        )
    ]
    for worker in workers:
        print("Полное имя: ", worker.get_full_name())
        print("Зарплата: ", worker.get_total_income())
