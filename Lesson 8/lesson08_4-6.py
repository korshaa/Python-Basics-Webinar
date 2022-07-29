class Warehouse:
    def __init__(self):
        self.dict = {}

    def add_sklad(self, of_equip):
        self.dict.setdefault(of_equip.type_e(), []).append(of_equip)

    def del_sklad(self, name):
        if self.dict[name]:
            self.dict.setdefault(name).pop(0)


class OfficeEquipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.type = self.__class__.__name__

    def type_e(self):
        return f'{self.type}'

    def __repr__(self):
        return f'Модель: {self.name}. Стоимость: {self.price}. Кол-во: {self.quantity}.'

    # def operation(self):
    #     type_name = input("Введите тип устройства: ")


class Printer(OfficeEquipment):
    def __init__(self, name, price, quantity, year):
        super().__init__(name, price, quantity)
        self.year = year


class Scanner(OfficeEquipment):
    def __init__(self, name, price, quantity, year):
        super().__init__(name, price, quantity)
        self.year = year


class Xerox(OfficeEquipment):
    def __init__(self, name, price, quantity, year):
        super().__init__(name, price, quantity)
        self.year = year


war_house = Warehouse()
printer_1 = Printer('Canon', 4000, 4, 2011)
war_house.add_sklad(printer_1)
print(war_house.dict)
