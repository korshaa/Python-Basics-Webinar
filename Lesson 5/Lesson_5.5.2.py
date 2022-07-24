# Через input
with open('text_5.txt', 'w+', encoding='utf-8') as my_f:
    try:
        my_f.write(input("Введите числа цифры пробел: "))
        my_f.seek(0)
        print(sum([int(i) for i in my_f.read().split()]))
    except ValueError:
        print("введен неверный формат")
