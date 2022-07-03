with open('text_5.txt', 'w+', encoding='utf-8') as my_f:
    my_f.write('7 3 345 23 321 10 15 23 94')
    my_f.seek(0)
    print(sum([int(i) for i in my_f.read().split()]))
