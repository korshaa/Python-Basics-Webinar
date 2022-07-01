my_str = input('Ввидите строку из нескольких слов, разделённых пробелами.:  ')
my_str = my_str.split()
for i, v in enumerate(my_str, 1):
    if len(v) > 10:
        print(f"{i}) {v[:10]}")
    else:
        print(f"{i}) {v}")
