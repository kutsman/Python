class Cell:
    def __init__(self, cell_number):
        self.length = None
        self.cell_number = cell_number

    def __str__(self):
        return f"Клетка с ячейками: {self.cell_number}"

    def __add__(self, other):
        return f"Результат сложения клеток равен клетке с ячейками: {self.cell_number + other.cell_number}"

    def __sub__(self, other):
        if self.cell_number > other.cell_number:
            return f"Остаток от вычитания клеток равен клетке с ячейками: {self.cell_number - other.cell_number}"
        return f"!!! Вычитание не возможно клетка первая клетка меньше второй"

    def __mul__(self, other):
        return f"Результат перемножения клеток равен клетке с ячейками: {self.cell_number * other.cell_number}"

    def __truediv__(self, other):
        if other.cell_number != 0:
            return f"Результат деления клеток равен клетке с ячейками: {round(self.cell_number / other.cell_number)}"
        return f"!!! Деление клетки на клетку без ячеек не возможно"

    def make_order(self, length):
        self.length = length
        cell_str = ['*' * length] * (self.cell_number // self.length)
        cell_str_1 = ['*' * (self.cell_number % self.length)]
        if self.cell_number % self.length != 0:
            return '\n'.join((cell_str + cell_str_1))
        return '\n'.join((cell_str))

cell_1 = Cell(15)
print(cell_1)
cell_2 = Cell(22)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(f"Визуализация клетки с ячейками {cell_2.cell_number}:\n{cell_2.make_order(9)}")
