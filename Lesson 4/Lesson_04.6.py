from itertools import cycle, count

for num in count(3):
    if num > 10:
        break
    else:
        print(num)


my_list = ['Строка 1', 'Строка 2', 'Строка 3', 'Строка 4', 'Строка 5']
for i, n in enumerate(cycle(my_list)):
    if i >= len(my_list):
        break
    else:
        print(n)

next_pri = cycle(my_list)
print(next(next_pri))
print(next(next_pri))
print(next(next_pri))
print(next(next_pri))
print(next(next_pri))
