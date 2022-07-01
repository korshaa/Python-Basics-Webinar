def sum_func():
    all_sum = 0
    new_list = []
    stop = 0
    while stop != "q":
        numbers = input('Введите числа через пробел, для выхода введите "q": ')
        for i in numbers.split():
            if i.isdigit():
                new_list.append(int(i))
            elif i.isalpha():
                if i.lower() == "q":
                    stop = i.lower()
        print(f'Cумма: {sum(new_list)}.\nОбщая сумма: {all_sum + sum(new_list)}.')
    print("Приходите еще)) ")


sum_func()
