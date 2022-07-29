class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return "Дата: "

    @classmethod
    def date_int(cls, obj):
        return [int(i) for i in obj.date.split('-')]

    @staticmethod
    def val_date(obj):

        if 1 <= Date.date_int(obj)[0] <= 31:
            if 1 <= Date.date_int(obj)[1] <= 12:
                if 999 < Date.date_int(obj)[2]:
                    return "Дата введена верно"
                else:
                    return "Невеный формат даты, вводить год нужно в формате YYYY"
            else:
                return "Невеный формат даты, в календаре 12 месяцев"
        else:
            return "Невеный формат даты, в календаре 31 день"


try:
    d = Date(input("Введите дату в фармате DD-MM-YYYY: "))
    print(f"День: {Date.date_int(d)[0]} Месяц: {Date.date_int(d)[1]} Год: {Date.date_int(d)[2]}")
    print((d.val_date(d)))

except ValueError as err:
    print(err, "Необходимый формат вводв 'DD-MM-YYYY'")
