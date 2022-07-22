from abc import ABC, abstractmethod

cloth = []


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return self.param + other.param

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        consumption = round(self.param / 6.5 + 0.5, 0)
        cloth.append(consumption)
        return consumption


class Suit(Clothes):
    @property
    def consumption(self):
        consumption = round((self.param * 2 + 0.3) / 100, 2)
        cloth.append(consumption)
        return consumption


# class Coat(Clothes):
#     @property
#     def consumption(self):
#         return round(self.param / 6.5 + 0.5, 2)


# class Suit(Clothes):
#     @property
#     def consumption(self):
#         return round((self.param * 2 + 0.3) / 100, 2)


# print(person_1.consumption)
# print(person_2.consumption)
# print(person_3.consumption)
# print(person_1.consumption + person_2.consumption + person_3.consumption)

person_1 = Coat(42).consumption
person_2 = Suit(170).consumption
person_3 = Coat(52).consumption
# print(person_1 + person_2 + person_3)
print(f"Общий расход ткани: {sum(cloth)} м.")
