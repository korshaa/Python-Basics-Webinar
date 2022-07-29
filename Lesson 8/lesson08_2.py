class Division:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def div_num(self):
        if self.num_2 == 0:
            raise ZeroError(self.num_1, self.num_2)
        return f"Result: {self.num_1 / self.num_2}"


class ZeroError(Exception):

    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def __str__(self):
        return f"Division by Zero, Вы пытаетесь поделить на ноль: {self.num_1}/{self.num_2} - на ноль делить нельзя"


try:
    numbers = Division(int(input("Введите число для деления: ")), int(input("Введите второе число для деления: ")))
    print(numbers.div_num())

except ZeroError as err:
    print(err)

except ValueError as err:
    print(err, "Введите целочисленое число")
