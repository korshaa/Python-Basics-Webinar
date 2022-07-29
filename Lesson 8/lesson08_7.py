class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} {"+" if self.b > 0 else "-"} {self.b if 0 < self.b else -self.b}j'

    def __add__(self, other):
        print("Сумма комплексных чисел равна:", end=" ")
        return f'{self.a + other.a}{"+" if self.b + other.b > 0 else ""}' \
               f'{self.b + other.b}j'

    def __mul__(self, other):
        print("Произведение комплексных чисел равно: ", end=" ")
        return f'{(self.a * other.a - self.b * other.b)}{"+" if (self.a * other.b + other.a * self.b) > 0 else ""}' \
               f'{(self.a * other.b + other.a * self.b)}j'


z1 = ComplexNumber(-2, 3)
z2 = ComplexNumber(-7, 9)

print(z1)
print(z2)
print(z1 + z2)
print(z1 * z2)
print()
