class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return f'{self.cell}'

    def __add__(self, other):
        print("Сумма клеток:", end=" ")
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        print("Вычетание клеток:", end=" ")
        return Cell(self.cell - other.cell if self.cell - other.cell > 0 else "Вычитание клеток не возможно!!!")

    def __mul__(self, other):
        print("Умножение клеток:", end=" ")
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        print("Деление клеток:", end=" ")
        return Cell(int(self.cell / other.cell) if other.cell > 0 else "Деление клеток не возможно, вторая клетка равна нулю")

    def make_order(self, row):
        return "\n".join(["😀" * row for i in range(self.cell // row)]) + "\n" + "💖" * (self.cell % row)


cell_1 = Cell(12)
cell_2 = Cell(7)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)

print(cell_2.make_order(5))
