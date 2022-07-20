class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 20000, "bonus": 5000}


class Position(Worker):
    def get_full_name(self):
        print(f"Должность: {self.position}, Имя: {self.name}, Фамилия: {self.surname}")

    def get_total_income(self):
        print(f"Доход с учётом премии: {self._income.get('wage') + self._income.get('bonus')} р.")


worker_1 = Position('Иван', 'Иванов', 'Директор')
worker_1.get_full_name()
worker_1.get_total_income()
