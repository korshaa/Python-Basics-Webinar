with open('str_file.txt', 'a+', encoding='utf-8') as my_f:
    while True:
        text_f = input('Введите данные, которые нужнно записать(для выхода ввидите пусту строку): ')
        my_f.write(f"{text_f}\n")
        if text_f == '':
            break
    my_f.seek(0)
    print(my_f.read())
