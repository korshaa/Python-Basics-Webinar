dis = int(input("Введите результат первого дня в км.: "))
result = int(input("Введите желаемый результат в км.: "))

day = 1
while dis < result:
    dis = dis+dis*10/100
    day += 1
print(f"На {day} день спортсмен достиг результата — не менее {int(dis)} км.")
