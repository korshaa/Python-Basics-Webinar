with open('text_4.txt', 'r', encoding='utf-8') as my_f, \
        open('text_4.1.txt', 'w', encoding='utf-8') as my_f1:
    dic_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    new_list = [i.split() for i in my_f]
    for i in new_list:
        for n in range(len(i)):
            if i[n] in dic_num.keys():
                i[n] = dic_num.get(i[n])

        my_f1.write(f'{" ".join(i)}\n')
