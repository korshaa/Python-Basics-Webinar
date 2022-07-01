rev = int(input("Введите значение выручки: "))
out = int(input("Введите значение издержек: "))
result = rev - out

if result < 0:
    print(f"Фирма отработала в убыток, результат: {result}")
elif result == 0:
    print("Фирма отработала в ноль!")
else:
    profit = rev/out * 100
    print(f"Поздравляем фирма отработала в плюс, прибыль составила: {result}")
    print(f"Рентабельность: {profit}%")
    staff = int(input("Введите кол-во сотрудников: "))
    print(f"Прибыль фирмы в расчёте на одного сотрудника: {rev/staff} ")
