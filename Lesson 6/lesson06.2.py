class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def rez_mass(self, mass_square, thick):
        print(f'{self._length}м * {self._width}м * {mass_square}кг * {thick}см = '
              f'{self._length * self._width * mass_square * thick / 1000} т.')


tl_light = Road(20, 5000)
tl_light.rez_mass(25, 5)
