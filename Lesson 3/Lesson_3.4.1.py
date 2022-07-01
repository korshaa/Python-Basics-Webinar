def my_func(x, y):
    while True:
        try:
            if str(x).isdigit() and str(abs(y)).isdigit() and 0 > y:
                print(x ** y)
                break
            else:
                print("Ошибка, попробуйте еще раз, ввидите действительное "
                      "положительное число X и целое отрицательное число Y")
                break
        except TypeError:
            print("Ошибка ввода, Y - целое отрицательное число, попробуйте еще раз")
            break


my_func(2, -3)
