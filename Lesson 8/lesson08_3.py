class OnlyINT(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"OnlyINT, {self.number} - не являеться числом!!! ВВОДИТЕ ТОЛЬКО ЧИСЛА!!!"


class IntList:
    @staticmethod
    def new_list():
        new_list = []
        stop = 0
        while stop != "q":
            numbers = input('Введите числа через пробел, для выхода введите "q": ')
            for i in numbers.split():
                if not i.isdigit():
                    try:
                        if i.lower() == "q":
                            stop = i.lower()
                        else:
                            raise OnlyINT(i)
                    except OnlyINT as err:
                        print(err)
                else:
                    new_list.append(int(i))
        print(f'Результат: {new_list}')
        print("Приходите еще)) ")


user_list = IntList()
user_list.new_list()
