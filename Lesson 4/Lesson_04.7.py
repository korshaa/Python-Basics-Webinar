def fact(n):
    f_n = 1
    for i in range(n):
        yield f_n
        f_n *= (i + 2)


for el in fact(4):
    print(el)
