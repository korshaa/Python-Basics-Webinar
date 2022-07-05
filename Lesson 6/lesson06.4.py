from random import choice


class Car:
    def __init__(self, speed, color, name, is_police_bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police_bool

    def go(self):
        print(f'{self.name}({self.color}), go!')

    def stop(self):
        print(f'{self.name}({self.color}), stop!')

    def turn(self):
        print(f'{self.name}({self.color}), turn {choice(["Left", "Right"])}')

    def show_speed(self):
        print(f'Speed a car {self.name}({self.color}): {self.speed} km/h')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Warning !!! {self.name}({self.color}) Exceeding the speed limit of 60 km/h')
        else:
            print(f'Speed a car {self.name}({self.color}): {self.speed} km/h')


class SportCar(Car):
    def show_speed(self):
        if self.speed > 160:
            print(f'Warning !!! {self.name}({self.color}) Exceeding the speed limit of 160 km/h')
        else:
            print(f'Speed a car {self.name}({self.color}): {self.speed} km/h')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Warning !!! {self.name}({self.color}) Exceeding the speed limit of 40 km/h')
        else:
            print(f'Speed a car {self.name}({self.color}): {self.speed} km/h')


class PoliceCar(Car):
    def show_speed(self):
        if self.is_police is True:
            print(f'No limit speed, Speed a car: {self.speed} km/h')


car_1 = Car(120, "Red", "Audi", False)
car_1.go()
car_1.turn()
car_1.stop()
car_1.show_speed()
car_2 = TownCar(70, 'Blue', "Opel", False)
car_2.go()
car_2.turn()
car_2.stop()
car_2.show_speed()
car_3 = SportCar(170, 'Orange', "Lamborgini", False)
car_3.go()
car_3.turn()
car_3.stop()
car_3.show_speed()
car_4 = WorkCar(43, 'Black', "Mercedes-Benz", False)
car_4.go()
car_4.turn()
car_4.stop()
car_4.show_speed()
car_5 = PoliceCar(43, 'Black', "BMW", True)
car_5.go()
car_5.turn()
car_5.stop()
car_5.show_speed()
