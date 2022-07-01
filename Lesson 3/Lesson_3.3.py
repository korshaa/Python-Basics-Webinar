def my_func(a, b, c):
    return sum([a, b, c]) - min(a, b, c)
    # list_sum = [a, b, c] - второй вариант
    # list_sum.remove(min(list_sum))
    # print(sum(list_sum))


print(my_func(1, 2, 3))
