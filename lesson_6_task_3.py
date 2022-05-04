class Worker:

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Полный доход сотрудника: {sum(self._income.values())}")


worker_1 = Position('Clark', 'Kent', 'DCs heroes', {'wage': 9000, 'bonus': 500})
worker_1.get_full_name()
worker_1.get_total_income()
