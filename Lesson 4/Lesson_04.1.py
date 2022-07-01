from sys import argv


def salary():
    try:
        # per_hour = argv[1]
        # bet = argv[2]
        # prem = argv[3]
        per_hour, bet, prem = map(float, argv[1:])
        print(f'Зарплата - {per_hour * bet + prem} рублей')
    except ValueError:
        print("Введите данные через пробел(кол-во часов, ставка, премия)")


salary()

