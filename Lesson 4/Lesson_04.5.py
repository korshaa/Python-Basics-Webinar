from functools import reduce
my_list = [i for i in range(1, 1001) if i % 2 == 0]
rez = reduce(lambda x, y: x*y, my_list)
print(rez)
